# GLOSSARY

Терминология UPG. Каждый термин — одно определение, один пример, иногда — краткая история (когда и в какой версии появился).

Алфавитный порядок. Термины, меняющие значение между версиями, помечены звёздочкой — у них есть секция `До / После`.

<details>
<summary><b>📑 Термины по алфавиту</b></summary>

**A** · [ABSTRACT-HARD](#abstract-hard) · [ANCHOR](#anchor) · [ARC](#arc) · [Associative Artifacts](#associative-artifacts) · [AUTH_LAYER](#auth_layer) · [AUTO-GOAL](#auto-goal)

**B** · [BAN REGISTRY](#ban-registry)

**C** · [Carrying Image](#carrying-image) · [CAMERA_SYSTEM](#camera_system) · [Coherence Thread](#coherence-thread-) · [CONCISE_MODE](#concise_mode) · [Contrast Pairs](#contrast-pairs)

**D** · [Density Scoring](#density-scoring) · [DEVICE_SIM](#device_sim) · [Drift](#drift)

**E** · [EIS — Emotional Intensity Score](#eis--emotional-intensity-score) · [Entry Angle](#entry-angle)

**F** · [FACTION_POV](#faction_pov) · [Frame Scale](#frame-scale)

**G** · [GTR — Generator Trigger Registry](#gtr--generator-trigger-registry)

**H** · [HARD CHECKS](#hard-checks-p0--p1a--p1b--p1m)

**I** · [IDENTITY_LOCK](#identity_lock) · [INTENT_SIGNAL](#intent_signal)

**L** · [Lens (Creative Lens)](#lens-creative-lens) · [LOCALE_DETAIL](#locale_detail)

**M** · [Mandatory Language](#mandatory-language) · [MATERIAL_FIDELITY](#material_fidelity) · [MODE](#mode) · [Module (A/B/C/D/V)](#module-abcdv) · [MUST_INCLUDE / MUST_AVOID](#must_include--must_avoid)

**P** · [Pattern 3C](#pattern-3c) · [Phase (1.x / 2.x / ... / 6.x)](#phase-1x--2x---6x) · [PRESERVE_LIST](#preserve_list) · [Propagation Lock](#propagation-lock)

**R** · [REALISM_ANCHOR](#realism_anchor) · [REFERENCE_EXTRACTION](#reference_extraction) · [Ring Test](#ring-test)

**S** · [S5 — Environmental Departure](#s5--environmental-departure) · [Safety Transform](#safety-transform) · [Seed](#seed) · [SLOT (S1–S5)](#slot-s1s5) · [STYLE_PROFILE](#style_profile)

**T** · [THEME_WIDTH](#theme_width) · [THRESHOLD_ELEMENTS](#threshold_elements) · [Tier 1 / Tier 2 adjectives](#tier-1--tier-2-adjectives-) · [Track (SIMPLE / STANDARD / COMPLEX)](#track-simple--standard--complex)

**V** · [VALIDATION STACK (L1–L9.2)](#validation-stack-l1l92) · [VCP — Visual Correspondence Protocol](#vcp--visual-correspondence-protocol)

**Z** · [ZONE (A / B / C)](#zone-a--b--c)

</details>

---

## ABSTRACT-HARD

Флаг, поднимаемый в Phase 1.2 для тем, которые невозможно визуализировать напрямую: "любовь", "свобода", "одиночество", "время", "справедливость", "память". Для таких тем система принципиально не рисует "визуализацию концепта", а строит **carrier scene** — физическую сцену, из которой тема считывается зрителем.

Появился: v5.4. Обрабатывается: Pattern 3C (см. ниже).

---

## ANCHOR

- **Как слот** — S1, якорь спектра. Самое близкое к буквальной теме, минимальный EIS-дрейф, высокая density.
- **Как приоритет элемента** (VCP Stage 0) — ANCHOR, SUPPORTING, ATMOSPHERIC. ANCHOR-элемент — без него картинка проваливает промпт целиком. SUPPORTING — важен, но кадр выживет. ATMOSPHERIC — обогащение, потеря косметическая.

---

## ARC

Последовательность из 5 слотов, складывающаяся в связную художественную арку. Типы:

- **FULL ARC** (artistic / editorial / personal, MODE 1): S1 ANCHOR → S2 TILT → S3 COLLISION → S4 DRIFT → S5 RUPTURE.
- **SHALLOW ARC** (commercial / scientific): S1 HERO → S2 TILT → S3 CONTEXT → S4 DETAIL → S5 CONVERSION.
- **REMIX ARC** (MODE 3): S1 LITERAL → S2 SHIFTED → S3 SURREAL → S4 ABSURD → S5 RESOLUTION.

Появилось: v7.2 (arc planning). MODE 3 REMIX arc — v8.x.

---

## Associative Artifacts

Структурированный выход ассоциативного движка (Фаза 0 в старых версиях): 6 прямых ассоциаций → мутация через 5 линз (инверсия / эмоция / метафора / масштаб / время) → турнир мутаций. Предок Entry Angle System.

Появился: v3.x. Растворился в Entry Angles: v7.2.

---

## AUTH_LAYER

Слой фото-аутентичности. Когда активен — модель инжектит в промпт описания FRAMING (off-center / tilt / crop), SENSOR (noise / grain pattern), MOTION (micro-blur), LENS_ART (flare / smudge / distortion), EXPOSURE (blown highlights / crushed shadows). Важно: это физические описания, не ярлыки.

Auto-активация: когда (PHOTO/CINE lens + candid/street/lifestyle/documentary context) AND GOAL≠Commercial.

Появился: v9.18.

---

## AUTO-GOAL

Если пользователь не указал GOAL, Phase 3 выводит его из темы и контекста по editorial-логике. Выход — одна строка: `AUTO-GOAL: [chosen goal] — [sentence reasoning]`.

Появился: v4.0 (формально документирован), существовал неявно в v0–v3 в упрощённой форме.

---

## BAN REGISTRY

Канонический список запрещённых слов, фраз и паттернов, активный на Phase 5 (crafting) и проверяемый на Phase 6 (validation).

Структура:
- **Zero Tolerance** — полностью удалить или переписать (`suggests/implies → shows/reveals`, `as if → [visible state]`, `camera pulls/tracks/focuses → describe scene directly`).
- **Tier 1 adjectives** — заменить материально (`soft → diffused/muted/[ShoreA]`, `clean → uncluttered/[absence]`, `elegant → proportioned/balanced/[geom]`).
- **Tier 2 adjectives** — nice / beautiful / lovely / pure / clear / calm / quiet / refined / pretty / pleasant → заменить материально без исключений.
- **Banned abstract nouns** — stillness / silence / tension / energy / absence / void / memory / time / presence / atmosphere / essence / spirit / soul / beauty / power / grace / elegance / serenity / tranquility / harmony / balance / chaos / mystery. Тест: "указываемо пальцем на фото?" Нет → ban.
- **Banned final patterns** — финальное предложение промпта может быть только видимым физическим элементом, никаких clauses о цели/эффекте/абстрактном состоянии.
- **Localized bans (RU)** — будто / словно / как будто / как если бы → [visible state].

Появился распределённо начиная с v2–v3. **Канонизирован в v9.15** — до этого список был размазан по телу системы.

---

## Carrying Image

Спецификация главного объекта/идеи через **10 компонентов**: 7 физических (материал, форма, цвет, текстура, условие, размер, пространственная позиция) + 3 поведенческих (действие, взаимодействие, временная фаза). Минимум 7/10 должны быть заполнены физически-измеримо. Проверяется Single Object Test (если два объекта — разделить). Проверяется S5 Trace (carrying image должен быть прослеживаемым даже в S5 Absence, хотя бы через отсутствие).

Появился: v7.2. Канонизирован формально в Checklist BLOCK B (v1.8.0).

Прямой предок: слот-блок v0.

---

## CAMERA_SYSTEM

Модуль для привязки PHOTO/CINE lens к реальным системам. Формат: `{BODY: [model], LENS_LINE: [series]}`. Таблицы встроены: ARRI Alexa 35 + Zeiss Master Primes, RED V-Raptor + Cooke S7/i, Sony Venice + Leica Summilux-C, Hasselblad H + HC line, Panavision Millennium DXL2 + Primo. Фокусные длины подбираются под slot (S1 — нейтральный, S4 — extreme).

Появился: v9.18.

---

## CONCISE_MODE

Контроль объёма диагностического вывода. `omit` (default в v10) / `true` (Routing Summary + promt) / `false` (full Diagnostic Template).

До v7.2: дефолт — full diagnostic. Смена дефолта в v7.2 сократила выдачу в среднем на 60%.

---

## Coherence Thread *

До v8.x — свободная концепция "общей ниточки" между слотами.

После v9.x — явный параметр в MODE 3, жёстко задающий smysl (smysl-thread), проходящий через все 5 слотов. Валидируется L-слоем.

---

## Contrast Pairs

Механика в Phase 4 (Arc Planning): S1↔S2, S3↔S4, S5 — always contrast. Для каждой пары задаётся вид контраста (lighting / palette / subject-density / scale / era / movement). Ring Test гарантирует, что S4-контраст не сваливается обратно к S1.

---

## Density Scoring

Метрика Phase 6 / Tournament Phase 1. Per slot считает количество: named materials + specific colors + measurements + texture descriptors + light behavior + spatial prepositions + condition indicators.

**Detail Counting Rule** (v9.22): каждое слово/фраза считается ровно в ОДНУ категорию. "oxidized copper" = 1 material ИЛИ 1 condition, не оба.

Минимумы по slots (MODE 1/2): S1≥10, S2≥8, S3≥9, S4≥8, S5≥7. Для MJ platform: S1≥5, S2≥4, S3≥5, S4≥4, S5≥4.

---

## DEVICE_SIM

Симуляция конкретного камерного устройства. Переопределяет CAMERA_SYSTEM, активирует AUTH_LAYER=ON автоматически. Встроенная таблица: iPhone / GoPro / Polaroid / Disposable / DSLR_Consumer / Webcam. Для каждого — фокус, искажения, характерные артефакты (flash falloff, light leaks, date stamp, computational HDR).

Появился: v10.

---

## Drift

Разница между слотом и темой (или между S1 и Sn) по одной из измеримых осей: EIS-drift (emotional intensity), palette-drift, composition-drift, density-drift, subject-drift.

**Допуски**: S1–S2 ±20, S3–S4 ≥40% (должны уйти на 40%+ от anchor), S5 ≥20% (минимум, но не обязан быть максимальным — S5 про absence, не про дальность).

Появился в численном виде: v6.0.

---

## EIS — Emotional Intensity Score

Шкала 0–100 для emotional intensity слота. Считается по спецификациям: light quality + palette saturation + subject density + motion markers + threshold presence. Используется для контроля drift.

- 0–20: flat / neutral / clinical
- 20–40: understated / quiet
- 40–60: moderate / balanced
- 60–80: heightened / charged
- 80–100: extreme / saturated

Появился: v6.0. До v6.0 — 6 эмпирических шкал без единой метрики (см. v0 "само-оценка").

---

## Entry Angle

Ракурс входа в тему. 8 канонических углов: SCALE, TIME, LOCATION, WEATHER, CULTURAL, MATERIAL, PERSPECTIVE, ACTIVITY. Распределяются между 5 слотами по правилам ротации A/B/C/D (чтобы два соседних слота не использовали один и тот же угол).

Появился: v7.2.

---

## FACTION_POV

В Setting — точка зрения определённой фракции/группы внутри вселенной темы. Влияет на выбор Aesthetic, Lens, Light. Пример: тема "кибер-разработчик", FACTION_POV = "корпоративный CEO" vs "underground hacker" — даёт радикально разные палитры.

---

## Frame Scale

Общий масштаб кадра для слота. FULL SCENE (wide establishing) / MIXED / CLOSE-UP. Валидируется на совместимость с выбранной Lens (L7.5 lens-aspect compat). CINE + SQUARE aspect — несовместимо. TEXTURAL + face as subject — несовместимо. FULL SCENE + длинный focal (>85mm) — несовместимо без motivated reason.

Правило совместимости добавлено: v9.22.

---

## GTR — Generator Trigger Registry

v10-реестр платформо-специфичных триггеров. 4 категории:
- **Quality Boosters** — фразы, которые на этой платформе форсируют качество.
- **Aesthetic Magnets** — слова, к которым платформа тяготеет и интерпретирует сильно (например, MJ и слово "cinematic").
- **Composition Overrides** — что сработает вопреки дефолтам платформы.
- **Platform-Specific Traps** — чего нельзя писать, иначе уведёт в стоковую кашу.

Появился: v10.

---

## HARD CHECKS (P0 / P1A / P1B / P1M)

Бинарные проверки в Phase 6. Проваленная проверка = полная пересборка, не частичная правка.

- **P0** — safety. Не прошёл — output blocked.
- **P1A** — carrying image fidelity. Carrying Image должен быть считываем в каждом слоте S1–S4 (в S5 — Environmental Departure).
- **P1B** — arc coherence. 5 слотов должны складываться в arc, а не быть 5 несвязанными вариантами.
- **P1M** — material fidelity. Если MATERIAL_FIDELITY ON — минимум 3 micro-texture details на каждый primary material.

Появился: v10.

---

## IDENTITY_LOCK

Модуль для сохранения признаков персонажа между слотами. `{SUBJ: [label], ATTRS: "[locked attributes]", PERSIST: [ALL/S1-S3/custom]}`. Категории: FACE / BODY / HAIR / MARKS / WARDROBE / PROPS. Auto-derive: если subject повторяется между слотами и lock не задан — extract из S1 на Phase 4.

Критическое правило: **lock descriptive, never generative.** Нельзя: "beautiful / attractive" — это generative. Можно: "narrow chin, asymmetric eyebrows, left-cheek mole" — это descriptive.

Появился: v10.

---

## INTENT_SIGNAL

Сигнал, извлекаемый из формулировки темы, задающий границы enrichment:
- **LITERAL** — тема конкретная, не расширять ("красные кроссовки").
- **EXPANSIVE** — тема просит расширения ("цвет настроения", "что-то про осень").
- **COMPLEXITY** — тема сложная и многомерная, нужен COMPLEX routing.
- **DEFAULT** — ничего явного не сигналит, дефолтная обработка.

**ABSTRACT ESCALATION RULE**: если тема ABSTRACT-HARD, INTENT_SIGNAL автоматически эскалируется в EXPANSIVE или COMPLEXITY.

Появился: v5.4.

---

## Lens (Creative Lens)

Визуальный фильтр, через который слот исполняется. 8 канонических:

- **PHOTO** — photographic realism, конкретные lens specs, natural light.
- **CINE** — cinematic, широкий кадр, motivated lighting, colour grade.
- **TEXTURAL** — макро/микро-текстура, материал на переднем плане.
- **PAINT** — painterly, кисть/масло/акварель читается.
- **ENV** — environmental, установочный widescreen, место как главный "актёр".
- **SYMBOLIC** — символический, элемент-метафора как фокус.
- **MINIMAL** — пустота, one-element composition, negative space.
- **SENSORY** — synesthetic, multisensory cue (запах, звук через визуальную метафору).

Канонизированы: v7.2. Lens-Aspect compatibility matrix: v9.22.

---

## LOCALE_DETAIL

Модуль для геокультурной аутентичности. Активируется автоматически когда SETTING.GEOGRAPHY — конкретный город/регион. Категории: SIGNAGE, FOOD, FURNISH, DRESS, ARCH, TRANSPORT, FLORA. Требование: ≥3 locale-specific concrete details, распределённых по слотам. Не generic "local atmosphere" — конкретные брендовые/предметные имена.

Появился: v10.

---

## Mandatory Language

Жёсткий язык, который УЖЕ находится в теме пользователя и должен дословно попасть в финальные промпты. Детектится в BLOCK D Checklist. Пример: тема "шерстяное пальто с костяными пуговицами" — "шерсть" и "костяные пуговицы" — Mandatory, не заменять на "fiber / button material" в pursuit of variety.

---

## MATERIAL_FIDELITY

Protocol микро-текстуры для primary материалов. Минимум 3 micro-texture details на материал из категорий: FINISH (polish/matte/satin/patina), AGING (wear/oxidation), TOOLMARKS (fingerprints/brush strokes/cast lines/seams), IMPERFECTION (chips/bubbles/inclusions/warping), LIGHT_INT (subsurface scatter / specular character / reflection type).

Auto ON когда: ModB active OR material-centric theme OR ELEMENTS содержат material nouns.

Появился: v10. P1M hard check.

---

## MODE

Режим генерации:
- **MODE 1** — independent prompts (default). 5 слотов независимы, связаны через arc.
- **MODE 2** — narrative arc (v7.2–v9.x). 5 слотов — это 5 моментов одной истории. В v10 помечен как оставленный в минимуме.
- **MODE 3** — remix/permutation. Пользователь задаёт ELEMENTS (2–10), система комбинирует их через REMIX arc (LITERAL → SHIFTED → SURREAL → ABSURD → RESOLUTION).

---

## Module (A/B/C/D/V)

Специализированные подсистемы, активируемые по признакам темы:
- **A — Layout** — плакат / упаковка / журнал / инфографика: композиция подчинена формату с местом под текст.
- **B — Package** — продукт, упаковка, товарный рендер: material fidelity максимум.
- **C — Explicit redirect** — safety-редирект для тем, где нужна замена subject (реальные люди, брендовое IP).
- **D — Narrative** — narrative-ориентированная тема, активирует narrative thread и cross-slot coherence.
- **V — Violence redirect** — редирект для graphic violence: перевод в aftermath / threshold / absence без изображения самого акта.

---

## MUST_INCLUDE / MUST_AVOID

Явные списки в SETTING. MUST_INCLUDE прожигается до финального промпта как MANDATORY S1–S3. MUST_AVOID — жёсткий фильтр на всех стадиях.

---

## Pattern 3C

Алгоритм обработки ABSTRACT-HARD тем. Тема не визуализируется напрямую; вместо этого выбирается **carrier scene** — физическая ситуация, которая несёт смысл темы. Carrier должен быть специфичным, ограниченным во времени и пространстве, с конкретным материальным содержимым. Тема "одиночество" → carrier: "пустой автобус в 4 утра, поручни ещё тёплые от предыдущего пассажира, за окном — предрассветный пригород в тумане".

Появился: v6.0.

---

## Phase (1.x / 2.x / ... / 6.x)

Шаги пайплайна. Всего 6 фаз, каждая разделена на под-шаги (1.1 Raw Input, 1.2 Theme Width, 1.3 Safety, 1.4 Context, 1.5 Module Activation, 1.6 Complexity Routing). Каждая фаза имеет чёткие input / output / validation gates.

Структура 6 фаз: **v3.x**. Группировка в ZONE A/B/C: **v7.2**.

---

## PRESERVE_LIST

Список элементов, которые инжектируются в каждый итеративный промпт как explicit locks при редактировании. Формат: "preserve: [locked], change only: [target]". Auto-populate: если feedback говорит "измени X, оставь остальное" → PRESERVE_LIST выводится автоматически.

Precedence: CONSTRAINTS > PRESERVE_LIST > FEEDBACK edits.

Появился: v10.

---

## Propagation Lock

Механизм, гарантирующий, что safety-преобразование (Phase 1.3) не откатится на более поздних фазах. Если на 1.3 "Tom Cruise" заменён на "middle-aged male actor in aviator sunglasses", то этот generic placeholder прокидывается в phase 4 (seed assignment), phase 5 (prompt craft), phase 6 (validation), без возможности "вспомнить оригинал".

Появился: v5.4 (формализован).

---

## REALISM_ANCHOR

Якорь реализма, переключатель ON/OFF. Default behavior:
- MODE 3 / Supernatural / Fantasy → ON (без якоря сцена сваливается в generic fantasy).
- GRAPHIC / SYMBOLIC / MINIMAL majority → OFF (там реализм не уместен).
- Else → ON.

Precedence: MODE 3 ON > lens-based OFF. Explicit user OFF > всё.

Появился: v9.18.

---

## REFERENCE_EXTRACTION

Модуль извлечения техники конкретного author/cinematographer/director. Формат: "[name]: [technique]". Встроенные профили: Lubezki (наturalistic window light + handheld + long take), Deakins (motivated source + restrained palette + geometric precision), Crewdson (staged tableau + fluorescent pools + large format crisp), Vermeer (warm amber + single window + smooth oil), Tarkovsky (subdued sepia + contemplative 50-85mm + overcast), Hopper, Hitchcock, Wong Kar-wai, Beksiński, Blade Runner 2049.

Появился: v9.18. Расширен STYLE_PROFILE-ами в v10.

---

## Ring Test

Валидационный тест для S4 (oblique slot). S4 не должен сваливаться обратно в S1. Проверка классифицирует S4 по 3 кольцам:
- **Ring 1** — дальний thematic extension (проходит).
- **Ring 2** — тангенциальный (проходит).
- **Ring 3** — скрытый S1-клон (не проходит → regenerate).

Время декодирования: 10–15 секунд. Если зритель прочитает S4 как "то же, что S1, только чуть иначе" — Ring 3, проваливает.

Появился: v7.2.

---

## S5 — Environmental Departure

Правило для слота S5 (absence). Для compound themes (X + Y) в S5 отсутствуют ОБА — и X, и Y. Не: "X исчез, Y остался как напоминание" (это S4). S5 — пустое место, в котором читается "здесь что-то БЫЛО".

Появилось: v6.x.

---

## Safety Transform

Преобразование на Phase 1.3, триггерится на:
- Реальных людей (actor / politician / singer / activist / athlete) → generic archetype preserving function.
- Брендированное IP (Disney / Marvel / Pixar / конкретных персонажей) → жанровый аналог.
- Graphic violence → aftermath / threshold / absence.
- Hate speech → rejection + user notice.

Результат — **propagation lock** (см. выше): замена прокидывается до финального output.

Полностью формализовано: v5.4.

---

## Seed

Направление (не сцена!) для одного слота. Пример неверного seed: "закат в пустыне с верблюдом" (это сцена). Верный seed: "temporal dissonance + material fatigue" (это направление). Сценой направление становится только на Phase 5.

Канонизировано: Checklist F1–F7.

---

## SLOT (S1–S5)

Пять ролей в спектре:
- **S1 ANCHOR** — якорь, максимально близок к теме, минимальный drift.
- **S2 CONTRAST / TILT** — оппозиция или небольшой сдвиг по одной оси (light / palette / era / scale).
- **S3 ADJACENT / COLLISION** — тангенциальная тема или столкновение двух seed-ов.
- **S4 OBLIQUE / DRIFT** — далеко от anchor, проходит Ring Test.
- **S5 ABSENCE / RUPTURE** — отсутствие, Environmental Departure для compound themes.

Роли в v10. В v5.x набор slots был более плоским ("5 вариантов темы"), семантика ролей оформилась в v7.2.

---

## STYLE_PROFILE

Именованный стилевой пресет, привязывающий Palette / Contrast / Texture / Lens / Light / Grade к одному ярлыку. Встроенные: HITCHCOCK, TARKOVSKY, LEONE, VERMEER, CREWDSON, HOPPER, WONGKARWAI, BEKSIŃSKI. Custom: пользователь задаёт поля вручную.

Появился: v10.

---

## THEME_WIDTH

Ширина темы, определяется на Phase 1.2:
- **NARROW** — конкретная, узкая ("красный велосипед в луже после дождя").
- **MODERATE** — средняя ("городской велосипед").
- **BROAD** — umbrella, широкая ("транспорт", "любовь", "эко-упаковка").

Для BROAD тем enrichment НЕ сужает в одну ideologue — генерируются Specialized Variants как side branches.

Появилось: v5.4.

---

## THRESHOLD_ELEMENTS

Механизм для частично видимых элементов. 4 уровня видимости: **GHOST** (едва-едва), **HINT** (намёк), **PARTIAL** (частично видно), **OBSCURED** (скрыто, но читается). Через 9 механизмов: FOG / BOKEH / SHADOW / REFL (reflection) / PERIPH (peripheral) / OVER (over-exposed) / UNDER (under-exposed) / MOTION / TRANS (translucent).

Формат: "[elem] at [level] via [mechanism]".

Появился: v9.18.

---

## Tier 1 / Tier 2 adjectives *

Категории в BAN REGISTRY.

До v9.15 — термин использовался неформально.

После v9.15 — Tier 1 жёстко задан списком замен (soft / clean / fresh / fine / smooth / gentle / subtle / elegant / delicate / simple → конкретные материальные замены). Tier 2 — менее критичный слой (nice / beautiful / lovely / pure / clear / calm / quiet / refined / pretty / pleasant). Tier 2 также bannable, но replacement не табличный — по контексту.

**Exception**: Tier 1 adjective допустим ТОЛЬКО с measurable qualifier. "soft" — ban. "soft clay Shore A 20" — ok.

---

## Track (SIMPLE / STANDARD / COMPLEX)

Результат Phase 1.6 routing. Определяет число финальных промптов:
- **SIMPLE** — 1 prompt (очень узкая / конкретная тема).
- **STANDARD** — 3 prompts.
- **COMPLEX** — 5 prompts (дефолт в v10 через DEFAULT OVERRIDE).

Появилось: v5.4. Дефолт COMPLEX: v10.

---

## VALIDATION STACK (L1–L9.2)

Слои валидации в Phase 6. Каждый слой имеет input, метрику, порог, действие.

- **L1** — ban registry scan (Tier 1/2 adjectives, abstract nouns, banned final patterns).
- **L2** — camera-as-agent ban.
- **L3** — propagation lock integrity (safety не откатился).
- **L4** — EIS drift в пределах допусков.
- **L5** — ring test pass для S4.
- **L6** — S5 environmental departure.
- **L7** — density counting per slot (с v9.22 patch — strict one-category-per-phrase).
- **L7.5** — lens-aspect-frame scale compatibility (v9.22).
- **L8** — carrying image fidelity per slot.
- **L9** — arc coherence.
- **L9.2** — GTR platform-specific traps scan (v10).

Появился полностью: v10. Отдельные слои — v6.0 (5-Gate Boundary).

---

## VCP — Visual Correspondence Protocol

Пост-продакшн аудит: image vs prompt. 6 стадий:
- **Stage 0** — Prompt Decomposition (инвентарь элементов с priority).
- **Stage 1** — Image Scan (объективное описание).
- **Stage 2** — Element Correspondence (PRESENT / MISSING / WRONG / PARTIAL).
- **Stage 3** — Unauthorized Additions (что модель добавила из себя).
- **Stage 4** — Batch / Cross-slot (опционально, S1–S5 целиком).
- **Stage 5** — Fidelity Score + Verdict.

Живёт отдельно от UPG. v1.0 — текущий.

---

## ZONE (A / B / C)

Три логические группы фаз (v7.2 refactor):
- **ZONE A** — Phases 1–3. Parse theme, enrich, derive goal.
- **ZONE B** — Phase 4. Generate spectrum: seeds, slots, lenses, entry angles.
- **ZONE C** — Phases 5–6. Craft prompts, validate, output.

Границы зон имеют валидационные гейты: вход в ZONE B заблокирован, пока parse/enrich/goal не прошли; вход в ZONE C — пока spectrum не собран правильно.

Появилось: v7.2.

---

## Смотри также

- [ARCHITECTURE.md](ARCHITECTURE.md) — как эти термины соединяются в пайплайн
- [USAGE.md](USAGE.md) — практическое применение
- [EVOLUTION.md](EVOLUTION.md) — когда каждый термин появился и почему
- [CHANGELOG.md](../CHANGELOG.md) — пофайловая хронология
