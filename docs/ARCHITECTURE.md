# ARCHITECTURE — как устроен UPG внутри

UPG — это большой системный промпт, который ведёт LLM через фиксированный пайплайн генерации визуальных промптов с гарантированными проверками на каждом шаге.

Этот документ — разбор архитектуры для тех, кто хочет понять, как эта штука устроена. Читается за ~30 минут. Актуально для **v10** (текущая стабильная версия).

<details>
<summary><b>📑 Содержание</b></summary>

1. [Четыре принципа](#1-четыре-принципа)
2. [Высокоуровневая картина](#2-высокоуровневая-картина)
3. [ZONE A — parse, safety, enrich](#3-zone-a--parse-safety-enrich)
4. [ZONE B — spectrum generation](#4-zone-b--spectrum-generation)
5. [ZONE C — craft, validate, output](#5-zone-c--craft-validate-output)
6. [Подсистемы](#6-подсистемы)
7. [MODE 1 / 2 / 3](#7-mode-1--2--3)
8. [Где что читать дальше](#8-где-что-читать-дальше)

</details>

---

## 1. Четыре принципа

**1.1. Zero tolerance на клише.** Запрещённые прилагательные, существительные и финальные паттерны собраны в BAN REGISTRY и проверяются валидационным слоем на выходе. Всё, что просочилось в виде `soft light`, `elegant composition`, `sense of wonder` — ловится на L8, промпт идёт в rewrite, не в output.

**1.2. Измеримость вместо оценок.** Drift между оригинальной темой и финальным слотом измеряется численно через EIS (Emotional Intensity Score, 0–100). "Drift ≤ 20 по EIS" — это число с допуском, а не субъективная оценка.

**1.3. Propagation locks.** Если Phase 1.3 заменила "Mickey Mouse" на "cartoon mouse with round ears in retro style", то в Phase 2, 4, 5 и 6 разрешён только `replacement`. Original термин не может всплыть в Slot 4, потому что "художник запамятовал". Propagation проверяется в Phase 2.6 Gate 4, Phase 4.3, Phase 5, Phase 6.2.

**1.4. Executable over poetic.** Красивая, но нерендерящаяся метафора ("acoustic emptiness made chromatic") переписывается на визуализируемый эквивалент (свет, форма, текстура, жест, среда). Абстрактные темы идут через маршрут Abstract → Physical, а не попытку передать абстракцию напрямую.

---

## 2. Высокоуровневая картина

```
┌─────────────────────────────────────────────────────────────┐
│                         INPUTS                              │
│    THEME · GOAL · PLATFORM · MODE · CONSTRAINTS · CONCISE?  │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│  ZONE A — Phases 1–3                                        │
│  Parse · Safety · Route · Enrich · AUTO-GOAL                │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│  ZONE B — Phase 4                                           │
│  Spectrum: Seeds · Slots · Lenses · Entry Angles            │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│  ZONE C — Phases 5–6                                        │
│  Craft (prose) · Validate (L1–L9.2) · Output                │
└─────────────────────┬───────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                       OUTPUT                                │
│              1 / 3 / 5 промптов (по TRACK)                  │
└─────────────────────────────────────────────────────────────┘
```

Деление на зоны появилось в **v7.2**. До v7.2 фазы шли линейным списком; зонирование дало логические точки возврата при ошибке и сделало возможным CONCISE_MODE (сжатый вывод без промежуточной диагностики).

---

## 3. ZONE A — parse, safety, enrich

### 3.1 Phase 1.1 — Raw Input Extraction

Парсер вытаскивает поля дословно, без перефразирования:
- `THEME_RAW` — exact verbatim
- `GOAL` (опц., если пусто → AUTO-GOAL в Phase 3)
- `CONTEXT`, `CONSTRAINTS`, `PLATFORM` — опц.

Никакой интерпретации. Если пользователь написал `eco-packaging`, в `THEME_RAW` лежит ровно `eco-packaging`, а не `sustainable packaging solutions for the modern consumer`.

### 3.2 Phase 1.2 — Theme Width + INTENT_SIGNAL + ABSTRACT-HARD

**THEME_WIDTH** (v5.4):
- `NARROW` — один конкретный объект/сцена ("красные кроссовки под дождём").
- `MODERATE` — одна концепция с нюансами ("утренний кофейный ритуал", "тревога").
- `BROAD` — умбрелла ("eco-packaging", "любовь", "AI").

Ширина диктует, что разрешено добавить в ENRICHED THEME. Для BROAD — только структурные добавки (environment type, time of day, mood register), никаких сужений типа `luxury` или `molded fiber`. Все специализации выносятся в `SPECIALIZED VARIANTS` как параллельные ветки.

**INTENT_SIGNAL** (v5.4):
- `LITERAL` ("visualize X", "photo of X") — приоритет точности
- `EXPANSIVE` ("creative take on X", "imagine X") — творческая свобода
- `COMPLEXITY` ("5 prompts", "full spectrum") — явный запрос сложности
- `DEFAULT` — LITERAL для BROAD, EXPANSIVE для NARROW

**ABSTRACT-HARD flag** (v6.0): тема BROAD и без физических якорей → активируется. Примеры: "пустота без пустоты", "смысл жизни", "чистое сознание". ABSTRACT-HARD меняет маршрут в Phase 2.4 (включает Pattern 3C — abstract → physical anchor routing).

### 3.3 Phase 1.3 — Safety Transform

Четыре категории, проверяются последовательно (могут срабатывать параллельно):

| Категория | Триггер | Действие |
|---|---|---|
| **Identity** | реальные люди, бренды, копирайт-персонажи | REDIRECT → archetype/generic |
| **Explicit** | сексуальный контент | Module C |
| **Violence** | графика насилия, glorification | Module V |
| **Hate** | hate speech, дегуманизация | REFUSE (явный intent) / REDIRECT (ambiguous) |

Результат фазы — `safety_transform` map:

```yaml
safety_transform:
  - original: "Mickey Mouse"
    replacement: "cartoon mouse with round ears in retro style"
    category: Copyright
```

**HARD RULE:** после Phase 1.3 оригинальные термины из `original` не могут появиться ни в одном downstream-выходе. Propagation lock проверяется на Phase 2.6 Gate 4, Phase 4.3, Phase 5, Phase 6.2, L1 validation.

### 3.4 Phase 1.4 — Context Classification

- `COMMERCIAL` — product, packaging, бренд, fashion, архитектура
- `ARTISTIC` — fine art, абстракт, сюрреализм
- `SCIENTIFIC` — процесс, механизм, биология
- `PERSONAL` — портрет, путешествия, еда, спорт
- `EDITORIAL` — журналистика, документалистика, social commentary

Hybrid: `HYBRID: COMMERCIAL + EDITORIAL`. Context диктует регистр AUTO-GOAL в Phase 3 (для COMMERCIAL нельзя стартовать с "sublime" или "tragic" — только "precise", "confident", "trustworthy").

### 3.5 Phase 1.5 — Module Activation

| Модуль | Триггер |
|---|---|
| **A — Layout & Text** | poster / banner / cover / CTA / copy space / headline |
| **B — Package Essence** | packaging / bottle / jar / box / pouch / vessel / label |
| **C — REDIRECT-EXPLICIT** | safety issued REDIRECT-EXPLICIT |
| **D — Narrative** | MODE = 2 |
| **V — REDIRECT-VIOLENCE** | safety issued REDIRECT-VIOLENCE |

### 3.6 Phase 1.6 — Complexity Routing

Только objective signals, без субъективной оценки:

| Signal | SIMPLE | STANDARD | COMPLEX |
|---|---|---|---|
| Theme length | ≤5 слов | 6–15 | >15 |
| Context certainty | single clear | clear primary | dual/unclear |
| Abstractness | только физ. объекты | mix | чисто концептуальный |
| Modules active | 0 | ≤1 | 2+ or Module A |

**DEFAULT OVERRIDE:** routing дефолтит в COMPLEX (5 промптов), если нет явных сигналов за SIMPLE/STANDARD.

**TRACK → Slots:**
- SIMPLE → 1 prompt (S1)
- STANDARD → 3 prompts (S1, S3, S5)
- COMPLEX → 5 prompts (S1–S5)

**Seed → Slot mapping:**
- SIMPLE: 1 seed → S1
- STANDARD: 2 seeds → S3 (SEED 1), S5 (SEED 3)
- COMPLEX: 3 seeds → S3 (SEED 1), S4 (SEED 2), S5 (SEED 3)

### 3.7 Phase 2 — Theme Enrichment

Enrichment проходит в рамках, заданных THEME_WIDTH и INTENT_SIGNAL. Семь паттернов (v5.4):

| Pattern | Когда | Формула |
|---|---|---|
| 1 | любой контекст, vague | [sensory adj] + [specific subject] + [environment] + [implied tension] |
| 2A | COMMERCIAL, без layout | [functional anchor] + [commercial intent] + [visual hook] + [quality signal] |
| 2B | Module A active | [format type] + [primary visual] + [text zone map] + [platform context] |
| 3A | ARTISTIC/PERSONAL default | [embodied scene] + [detail] + [emotional register] + [color/light] |
| 3B | artistic explicit | [metaphorical environment] + [symbolic displacement] + [emotional register] |
| 3C | ABSTRACT-HARD | специальный маршрут abstract → physical anchor |
| 4 | PERSONAL action-based | [scene with time+place] + [dominant mood] + [focal point] |

**Разрешено для всех ширин** (structural additions): environment type, time of day, mood register, scale indication, compositional orientation.

**Запрещено** (forbidden injections, если не из THEME/GOAL): price/market segment, single-material lock-in, ideological stance (manifesto / anti-*), hard style lock-in (brutalist only / Bauhaus-only), emotional extremes против CONTEXT.

### 3.8 Phase 3 — AUTO-GOAL

Если пользователь не задал GOAL — генерируется на основе THEME, CONTEXT, ENRICHED THEME.

Регистр по CONTEXT:
- **COMMERCIAL** → "precise", "confident", "clear", "trustworthy"
- **ARTISTIC** → "epic", "sublime", "mysterious"
- **SCIENTIFIC** → "neutral", "precise", "curious"
- **PERSONAL** → "intimate", "warm", "nostalgic"

AUTO-GOAL НЕ должен: принимать price segment / ideology, которых не было в THEME/GOAL; трактовать одну специализированную ветку как "единственную правду".

---

## 4. ZONE B — spectrum generation

### 4.1 Seeds

Seeds — это **направления, не сцены.**

❌ Слишком конкретно (блокирует RERUN variation):
```
Close-up detail of hands adjusting dress at hip — fingers
pressing matte crimson fabric, pulling at side seam
```

✅ Direction (оставляет место для вариации):
```
Macro tactile interaction — fingers engaging with fabric,
visible pressure response, cropped to gesture
```

Для COMPLEX track генерируется три сида, каждый feeds свой slot:
- **SEED 1 → S3** (Adjacent): та же тема, другой угол/масштаб/момент. Decode time <5 сек.
- **SEED 2 → S4** (Oblique): должен пройти Ring Test. Decode 10–15 сек.
- **SEED 3 → S5** (Absence): сцена, где carrying image отсутствует.

### 4.2 Ring Test (для S4)

Обязательная классификация S4:

- **Ring 1 (FAIL):** carrying image напрямую виден.  
  Пример: платье на вешалке в той же комнате.
- **Ring 2 (FAIL):** та же среда + часть carrying image.  
  Пример: платье на полу в той же бархатной комнате.
- **Ring 3 (PASS):** другая среда ИЛИ только косвенные следы.  
  Пример: красная нитка на верстаке портного в другой комнате.

Decode time test: описать S4 человеку, не видевшему S1–S3. Связь с темой должна проскочить за 10–15 секунд. <5 сек → слишком явно. >20 сек → слишком обскурно.

### 4.3 Environmental Departure (S5)

S5 показывает пространство, где carrying image отсутствует. Для compound themes ("женщина в красном платье") — отсутствовать должны оба компонента.

❌ Проваливает departure:
- Женщина без платья (X виден)
- Платье без женщины (Y виден)
- Силуэт женщины (X частично виден)
- Отражение фигуры в зеркале (X через отражение)

✅ Проходит departure:
- Пустая комната с примятым бархатом в месте, где она стояла, висящий запах духов, остывающее тепло на поверхностях.
- Шкаф с платье-образным пустым местом на перекладине, hanger, tissue paper.

### 4.4 Creative Lenses

Восемь канонических линз (стабилизированы в v7.2):

| Lens | Что делает |
|---|---|
| **PHOTO** | Фотореализм, явный focal length + f-stop |
| **CINE** | Кино-язык, широкоэкранный aspect |
| **TEXTURAL** | Макро, surface/texture focus |
| **PAINT** | Живопись, кисти, палитра, visible brushwork |
| **ENV** | Environment-dominant, subject embedded |
| **SYMBOLIC** | Объект-символ, графичная композиция |
| **MINIMAL** | Минимализм, negative space доминирует |
| **SENSORY** | Non-visual сенсорика как визуал (температура, звук, запах) |

**Правила распределения:**
- ≥4 разных линзы в серии
- Каждая линза ≤2 раза
- Смежные слоты ≠ identical lens

**Lens-Aspect compatibility** (v9.18, уточнено в v9.22 L7.5):

| Lens | Compatible aspects |
|---|---|
| CINE | 2.39:1 / 2.00:1 / 16:9 ONLY |
| SYMBOLIC | 1:1 / 4:5 preferred |
| TEXTURAL | any (macro framing) |
| ENV | 16:9 / 3:2 / 2.39:1 preferred |
| PHOTO / PAINT / MINIMAL / SENSORY | any |

**Lens-Magic compatibility** (Checklist G6): TEXTURAL = макро = face out of frame. Если в MUST_INCLUDE есть magic/signature element требующий видимых глаз — не назначать TEXTURAL на этот слот.

### 4.5 Entry Angles

Восемь типов входа в сцену (применяется к S1 и S2):

| Angle | Пример первой фразы |
|---|---|
| **SCALE** | "Fifteen-meter..." |
| **TIME** | "By third week..." |
| **LOCATION** | "At crater's edge..." |
| **WEATHER** | "Through morning fog..." |
| **CULTURAL** | "Shimenawa wraps..." |
| **MATERIAL** | "Oxidized copper..." |
| **PERSPECTIVE** | "From above..." |
| **ACTIVITY** | "Mid-pour..." |

**Ротация по темам:**
- A: SCALE + TIME
- B: TIME + LOCATION
- C: CULTURAL + LOCATION
- D: SCALE + LOCATION

S1 и S2 открываются РАЗНЫМИ angle. Entry Angle строго ограничен S1–S2 — в S3–S5 выводится автоматически (они эволюционируют через Spectrum Axis и Seeds).

---

## 5. ZONE C — craft, validate, output

### 5.1 Phase 5 — Prose Craft

Каждый слот пишется как flowing prose, не keyword list. Правила:
- **ONE dominant visual idea** на промпт, все детали работают на неё
- **Concrete over abstract** — "amber side-light catching dust motes" вместо "atmospheric lighting"
- **Front-load** — самая важная визуальная информация в начале
- **BAN REGISTRY active** в реальном времени (каждое слово сверяется с banned lists)

### 5.2 Phase 6 — VALIDATION STACK

Формализовано в v10. Слои L1 → L9.2:

| Layer | Что проверяет |
|---|---|
| **L1** | Safety propagation — никаких original terms в выходе |
| **L2** | Theme width bounds — нет narrowing injections в ENRICHED THEME |
| **L3** | Slot count соответствует TRACK (1/3/5) |
| **L4** | Lens distribution — ≥4 разных, ≤2 на каждую, no adjacent duplicates |
| **L5** | Entry Angle ограничен S1–S2 |
| **L6** | EIS tolerance — S1–S2 ±20 от THEME_RAW, S3–S4 ≥40%, S5 ≥20% |
| **L7** | Density counting (v9.22 — строгий метод по категориям, не "на глаз") |
| **L7.5** | Lens-Aspect compatibility (v9.22) |
| **L8** | BAN REGISTRY scan — 0 matches tolerated |
| **L9** | Final pattern check — нет banned финальных паттернов |
| **L9.2** | Propagation re-verify — финальная проверка safety_transform |

### 5.3 HARD CHECKS (v10)

P0–P1M — критические блокирующие проверки. Fail → prompt rewrite, не output.

- **P0** — safety hard fail (hate content, explicit violence as reward)
- **P1A** — EIS out of spec
- **P1B** — ban match found
- **P1M** — module mismatch (e.g., Module A expected but layout absent)

---

## 6. Подсистемы

### 6.1 BAN REGISTRY

Три уровня запретов. Canonical source с v9.15.

**Tier 1 banned adjectives** (must qualify with physical measurement OR replace):

| Banned | Replacement |
|---|---|
| `soft` | `diffused` / `muted` / `low-contrast` / `[material + Shore A]` |
| `fine` | `particulate` / `narrow` / `hairline` / `[measurement]` |
| `smooth` | `polished` / `satin` / `[surface finish]` |
| `gentle` | `gradual` / `low-angle` / `[degree]` |
| `subtle` | `understated` / `hint-of` / `[percentage]` |
| `elegant` | `proportioned` / `balanced` / `[geometric relationship]` |
| `delicate` | `thin-walled` / `lightweight` / `[thickness]` |
| `clean` | `uncluttered` / `minimal` / `[specific absence]` |
| `fresh` | `recently-cut` / `undried` / `[time since change]` |
| `simple` | `single-element` / `unadorned` / `[component count]` |

**Tier 2 banned** (always replace materially, no qualifier saves them):
`nice` / `beautiful` / `lovely` / `pure` / `clear` / `calm` / `quiet` / `refined` / `pretty` / `pleasant`

**Banned abstract nouns** (нельзя как финальный тег):
`essence` / `harmony` / `wonder` / `beauty` / `joy` / `soul` / `spirit`

**Banned final patterns** (размывают финальную строку любого промпта):
`"a sense of..."` / `"suggesting..."` / `"as if..."` / `"creating a feeling of..."` / `"with an atmosphere of..."`

### 6.2 EIS — Emotional Intensity Score

Шкала 0–100, введена в v6.0. Измеряется численно:
- EIS(THEME_RAW)
- EIS(ENRICHED THEME)
- EIS каждого слота S1–S5 после craft

**Tolerance:**
- S1–S2 — в пределах ±20 от THEME_RAW (drift minimal)
- S3–S4 — can drift, но ≥40% от original intensity
- S5 — не нейтрализовать, ≥20% от original

Drift считается численно, не "на глаз". EIS не подкручивается, чтобы попасть в tolerance — если слот fail, переписывается content слота, потом пересчитывается EIS.

### 6.3 Carrying Image (Checklist B)

Carrying Image — главный визуальный объект темы. Описывается 10 компонентами (Checklist v1.8.0 D1).

**Physical (7, минимум 5 заполнено):**
`SHAPE` · `SIZE` · `MATERIAL` · `COLOR` · `TEXTURE` · `CONDITION` · `UNIQUE`

**Behavioral (3, минимум 2 заполнено):**
- `LIGHT_RESPONSE` — как поверхность реагирует на свет
- `WEAR_PATTERN` — где и как проявляется износ
- `ENVIRONMENT_RESPONSE` — как выглядит в конкретных условиях

Минимум 7/10 components заполнено для PASS. Все entries проходят TIER 1/2 pre-scan (banned adjectives).

### 6.4 CAMERA_SYSTEM (v9.18)

Таблицы реальных камер + объективов для точной симуляции устройства.

**Bodies:** ARRI Alexa Mini LF · RED V-Raptor · Sony Venice 2 · Hasselblad X2D 100C · ...

**Lenses:** Zeiss Supreme Prime · Cooke S7/i Full Frame Plus · Leica Thalia · Panavision Primo · ...

**Для PHOTO слотов** — обязательный focal length + f-stop per slot:
- Macro: 100mm f/2.8
- Table/product: 85mm f/1.8
- Portrait: 85mm f/2
- Environmental: 35mm f/5.6
- Wide: 24mm f/8
- Street: 50mm f/4

### 6.5 THRESHOLD_ELEMENTS (v9.18)

Четыре уровня видимости элемента в кадре:

- **GHOST** — еле читается, на грани перцепции
- **HINT** — намёк без explicit statement
- **PARTIAL** — частично виден, часть за кадром
- **OBSCURED** — намеренно затемнён/размыт

Решает проблему "conditional language" (Checklist D5): вместо `maybe a dress shadow` пишется `dress-shadow OBSCURED at 30% visibility`. Conditional формулировки ("visible only at certain angles", "subtle", "may appear") автоматически ловятся на L8 и переписываются через THRESHOLD_ELEMENTS.

### 6.6 REALISM_ANCHOR (v9.18)

Для каждого слота — один конкретный физический якорь реализма: тень с указанной длиной, отражение на указанной поверхности, компрессия с указанной силой. Без anchor промпт плывёт в сторону "prettified stock".

### 6.7 REFERENCE_EXTRACTION (v9.18)

Таблица визуальных референсов, привязанных к авторам:

| Автор | Что берём |
|---|---|
| Lubezki | spatial depth through haze, handheld intimate |
| Deakins | hard golden hour sculptural light |
| Crewdson | cinematic suburban staged |
| Vermeer | window north-light intimate |
| Tarkovsky | meditative slow-burn |
| BR2049 | saturated fog, volumetric rim |

Используется как визуальный якорь, НЕ как прямая имитация ("in the style of" банится).

### 6.8 Generator Trigger Registry (v10)

Четыре категории:

- **Quality Boosters** — триггеры, повышающие технические параметры (`"shot on medium format film"`, `"studio lit"`, `"85mm f/1.8"`)
- **Aesthetic Magnets** — стилевые якоря (`"editorial"`, `"commercial hero"`, `"documentary grain"`)
- **Composition Overrides** — принудительные компоновки (`"rule of thirds with 1/3 negative sky"`, `"symmetric eye-level"`)
- **Platform-Specific Traps** — антипаттерны для конкретной платформы: Midjourney пожирает токены одних паттернов, Flux игнорит другие

### 6.9 Six Locks (v10)

Блокировки сквозной консистентности в серии S1–S5:

- **IDENTITY_LOCK** — персонаж/сущность тот же во всех слотах
- **LOCALE_DETAIL** — географическая/культурная аккуратность
- **STYLE_PROFILE** — жанровый якорь не мигрирует (не "из Vermeer в Crewdson посреди серии")
- **MATERIAL_FIDELITY** — ткань остаётся той же тканью (crepe 280gsm в S1 ≠ organza в S3)
- **AUTH_LAYER** — время/эпоха/среда не прыгают
- **DEVICE_SIM** — симуляция устройства съёмки едина для серии (или различается согласно явному плану)

---

## 7. MODE 1 / 2 / 3

**MODE 1 (default)** — independent prompts. Каждый слот — самостоятельная композиция. Между слотами нет нарратива, только spectrum. Большинство use-case-ов.

**MODE 2 (narrative arc)** — слоты образуют историю: S1 setup → S2 rising → S3 climax → S4 resolution → S5 epilogue. Активирует Module D.

**MODE 3 (remix permutation)** — слоты как permutations одного объекта. Carrying image фиксирован, меняется только модуль доставки (angle, time, condition, scale). BLOCK P в Checklist ведёт структурно.

---

## 8. Где что читать дальше

**Код системы (исходники):**
- [full_versions/UPG_v10.md](../full_versions/UPG_v10.md) — текущая стабильная версия
- [full_versions/UPG_v9_19_1.md](../full_versions/UPG_v9_19_1.md) — последняя докомпрессионная

**Документация:**
- [USAGE.md](USAGE.md) — как пользоваться в ChatGPT/Claude
- [EVOLUTION.md](EVOLUTION.md) — нелинейная история версий (почему именно так)
- [GLOSSARY.md](GLOSSARY.md) — термины

**Рядом с UPG:**
- [project_tools/UPG_Checklist_v1_8_0.txt](../project_tools/UPG_Checklist_v1_8_0.txt) — interview-first authoring темы
- [tools/VisualCorrespondenceProtocol_v1_0.md](../tools/VisualCorrespondenceProtocol_v1_0.md) — аудит image ↔ prompt

**Кампания валидации:**
- [../BENCHMARK.md](../BENCHMARK.md) — 32 теста / 18 LLM / 77 открытий

**Полный changelog:**
- [../CHANGELOG.md](../CHANGELOG.md)
