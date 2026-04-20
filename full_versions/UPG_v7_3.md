


# Анализ IMAGE PROMPT GENERATOR v7.3

---

## 1. АРХИТЕКТУРНЫЕ ПРОБЛЕМЫ

### 1.1. Объём промта vs. контекстное окно

**Проблема:** Промт содержит ~6500 слов (~8500 токенов). При генерации полного ответа со всеми промежуточными декларациями (DECLARE-блоки, таблицы скоринга, чек-листы, audit log) + 5 финальных промтов — суммарный вывод может достигать 15 000–20 000 токенов. Это:
- Провоцирует обрезку, потерю поздних шагов, «усталость» модели к Step 8–9
- Снижает качество последних слотов — модель начинает упрощать, пропускать проверки
- Делает невозможным повторное использование (модель «забывает» начало при длинном контексте)

**Решение:** Ввести режим вывода:
```
OUTPUT MODE:
  FULL    → все промежуточные шаги + финальные промты (для отладки)
  COMPACT → только Analysis Summary + 5 финальных промтов
  DEBUG [N] → полный вывод только для Step N, остальное — compact
```
По умолчанию — COMPACT. Промежуточные шаги выполняются «молча» (silently), объявляются только при нарушениях.

---

### 1.2. Самооценка (self-scoring) в Step 5

**Проблема:** Модель оценивает свои же сцены по 4 критериям на /10. Это принципиально ненадёжно — нет внешнего арбитра. Модель склонна:
- Давать завышенные оценки (редко ниже 6/10)
- Выбирать «безопасные», а не действительно оригинальные сцены
- Подстраивать оценку под желаемый результат (confirmation bias)

**Решение:** Заменить числовой скоринг сравнительным ранжированием:
```
TOURNAMENT FORMAT:
  Round 1: 12 scenes → 6 winners (head-to-head comparison on Originality + Visual Power)
  Round 2: 6 scenes → 5 winners (head-to-head, loser = lowest Goal Fit)
  Each comparison: declare winner + one sentence why
```
Это объективнее, чем присвоение абсолютных баллов, и короче в выводе.

---

### 1.3. Избыточные проверки (redundant validation)

**Проблема:** Один и тот же аспект проверяется 4–6 раз в разных формулировках:

| Что проверяется | Где проверяется |
|---|---|
| Присутствие SUBJECT | Global Principle, Step 0 Theme Parse, Phase D Seed Coverage, Step 2 Topic Lock, Step 4 Scene Gen, Step 5 Subject Presence Gate |
| Соответствие формату | Step 2 Format Integrity Lock, Step 5 Format Check, Step 2 Frame Transplant Constraint |
| Покрытие осей | Step 3 Axis Coverage, Step 5 Axis Coverage Check, Step 6 Axis Distribution |
| Уникальность ERA/STYLE | Step 7 Layer 4 (candidates), Step 8 (finalization), Step 8 Re-validation |

Каждая проверка добавляет токены к выводу и создаёт точку потенциального «зависания» (hard stop).

**Решение:** Консолидировать проверки. Вместо 6 точек проверки SUBJECT — оставить 2:
1. Step 0 (декларация) — фиксирует SUBJECT
2. Step 5 (единственный gate перед финальным отбором) — проверяет все аспекты одновременно:
```
QUALITY GATE (Step 5, before scoring):
  [ ] SUBJECT visible as discrete entity
  [ ] All 3 FORMAT elements present
  [ ] Axis zone matches parent archetype
  [ ] At least 2 Visual Vocabulary items present
  NO on any → disqualified. Revise in Step 4.
```
Остальные упоминания заменить на `[SUBJECT ANCHOR verified silently]` без вывода.

---



## 3. ЛОГИЧЕСКИЕ ПРОТИВОРЕЧИЯ И ПРОБЕЛЫ

### 3.1. Прямые ссылки (forward references)

| Где объявлено | Где впервые используется | Проблема |
|---|---|---|
| Rupture Types — Step 3 | Steps 5, 8, 9 | Объявлены посреди Step 3 (Archetype Generation), но нужны только в Step 5+ |
| Slot Assignment — Step 7.5 | Step 8, 9 | OK |
| Seed-to-Slot — Step 8 | Step 9 | OK |
| Camera Engine — Step 9 | Step 7 Layer 5 говорит «Focal length assigned by Camera Engine in Step 9» | Ссылка вперёд |

**Решение:** Перенести Rupture Types из Step 3 в Step 8 (Creative Spectrum Mapping), где они фактически используются. В Step 3 оставить только Narrative Archetype и Scene Archetypes.

---

### 3.2. Step 3 — «6 scene archetypes» vs. заголовок «4 archetypes»

**Проблема:** Заголовок секции Step 3 в PROCESS MAP говорит `Archetype Generation (4 archetypes)`, но тело инструкции говорит «Generate 6 scene archetypes [...] Select TOP 4». Это технически верно (output = 4), но заголовок вводит в заблуждение о процессе.

**Решение:**
```
Step 3  → Archetype Generation (6 candidates → 4 selected)
```

---

### 3.3. VALENCE подтипы без критериев выбора

**Проблема:** Объявлены WARM-PURE и WARM-BITTERSWEET, но нигде не указано, **как модель выбирает** между ними. Нет теста, нет критерия — только описание того, что они значат.

**Решение:**
```
WARM subtype determination:
  Parse PROPERTY from Theme Parse.
  Does PROPERTY inherently contain loss, transience, ending, or irreversibility?
    YES → WARM-BITTERSWEET
    NO  → WARM-PURE
  
  Examples:
    "childhood wonder" → WARM-PURE (no inherent loss)
    "last summer together" → WARM-BITTERSWEET (inherent ending)
    "grandmother's kitchen" → WARM-BITTERSWEET (implies past, transience)
    "birthday celebration" → WARM-PURE
```

---

### 3.4. Отсутствие лимита итераций

**Проблема:** Несколько точек в процессе создают потенциальные бесконечные циклы:
- Phase D: Inversion Diversity Test FAIL → «return to Phase B [...] Re-run Phase C and Inversion Diversity Test» — нет лимита
- Step 5: «0 pass → return to Step 1» — нет лимита
- REDIRECT-8: «self-check → loop max 2×» — единственное место с лимитом

**Решение:** Добавить глобальное правило:
```
ITERATION LIMIT: Any revision loop executes max 2 times.
If still failing after 2 iterations:
  - Accept best available result
  - Declare: ITERATION LIMIT REACHED: [step] — [what compromise was made]
  - Continue to next step
```

---

### 3.5. Step 4 — «Built-in cliché check» vs. «Literal-end exception»

**Проблема:** Cliché check говорит: «Would this image appear on the first page of Google Image search? If yes → apply enhancement.» Literal-end exception говорит: «For literal-end scenes: if it DOES look like the first Google page — it passes.» Это противоречие — literal-end сцена проходит cliché check, но тут же освобождается от него. Зачем проверять?

**Решение:** Объединить в одно правило:
```
CLICHÉ CHECK:
  Literal-end scenes: SKIP — cliché is the point. Verify scene IS obvious
    (if it's not obvious enough → it belongs in middle zone, reassign)
  Middle and unexpected-end scenes: Would this appear on first page of
    Google Image search? If yes → apply one enhancement.
```

---

### 3.6. Slot 4 — «Tension Through Absence» — необоснованное ограничение

**Проблема:** Блок SLOT 4 — TENSION THROUGH ABSENCE требует описывать тело/фигуру только через негативное пространство. Но это ограничение привязано к номеру слота, а не к содержанию сцены. Если Slot 4 — пейзаж без фигуры, правило неприменимо. Если фигура в Slot 2 была бы выгоднее показать через absence — правило не позволяет.

**Решение:** Сделать Absence technique контекстным, не привязанным к слоту:
```
ABSENCE TECHNIQUE (apply when a scene would benefit from implied rather
than explicit figure presence — most natural in Slots 4-5, available for any slot):
  [declaration block]
```

---

## 4. ПРАКТИЧЕСКИЕ И ТЕХНИЧЕСКИЕ ПРОБЛЕМЫ

### 4.1. Устаревание платформенных тегов

**Проблема:** Конкретные версии и параметры устаревают:
- `--v 6.1` для Midjourney (уже есть v7)
- `--style raw` и `--q 2` могут измениться
- `(photorealistic:1.3)` синтаксис для SD — зависит от модели
- `shot on [camera body]` — некоторые генераторы игнорируют это

**Решение:** Выделить платформенные теги в отдельный модуль с пометкой о дате:
```
PLATFORM MODULE (last updated: [date])
  Midjourney → [flags]
  ...
  
NOTE: Platform parameters change frequently. Verify current syntax
before generation. When uncertain — omit platform-specific flags
and use universal descriptive language only.
```

---

### 4.2. «8K resolution» и подобные теги

**Проблема:** Теги вроде `8K resolution`, `highly detailed`, `RAW photo` — постепенно теряют эффективность в современных генераторах (Flux, Aurora, Imagen 3). Они были актуальны для SD 1.5 / SDXL, но новые модели обучены на других данных и реагируют на описательный язык, а не на «quality boosters».

**Решение:** Дифференцировать Universal Quality Tags по поколению генератора:
```
QUALITY TAGS:
  Legacy generators (SD 1.5, SDXL):
    Append: [current tags with resolution markers]
  Modern generators (Flux, Aurora, Imagen 3, MJ v6+):
    Omit resolution markers. Quality communicated through
    descriptive precision, not meta-tags.
    Append only medium-specific descriptors (e.g., "visible brushwork"
    for oil painting, "shallow depth of field" for photography).
```

---

### 4.3. Negative prompts — не все платформы поддерживают

**Проблема:** Gemini Imagen, Midjourney v6+, xAI Aurora — не поддерживают или слабо поддерживают negative prompts. Промт генерирует их для всех платформ.

**Решение:**
```
NEGATIVE PROMPTS:
  Supported: Stable Diffusion, SDXL, ComfyUI, Automatic1111
  Partial:   Midjourney (--no flag, limited)
  Unsupported: Flux, Aurora, Gemini Imagen, Firefly
  
  Generate negative prompt only when platform supports it.
  For unsupported platforms: encode exclusions as positive descriptors
  (e.g., instead of "no cartoon" → "photorealistic textures, analog film grain")
```

---

### 4.4. Camera body — бессмысленный для большинства генераторов

**Проблема:** `shot on Hasselblad 500C/M` или `shot on Leica M6` — красиво звучит, но большинство генераторов не различают камеры. Это занимает токены без визуального результата.

**Решение:** Сделать camera body опциональным:
```
CAMERA BODY: [include only for Midjourney and Stable Diffusion where
it influences aesthetic. For Flux/Aurora/Imagen — omit, use descriptive
equivalents: "medium format film rendering" instead of "shot on Mamiya RZ67"]
```

---

### 4.5. Banned Words — неполный список и нет механизма обновления

**Проблема:** Список запрещённых слов статичен. «Cinematic masterpiece» забанено, но «masterfully executed» только в мета-описаниях. Нет «moody», «dreamy», «surreal» (часто злоупотребляют).

**Решение:** Расширить и категоризировать:
```
BANNED VOCABULARY (scan before output):

TIER 1 — Always remove (zero information content):
  stunning, breathtaking, epic, gorgeous, majestic, incredible, magical,
  masterpiece, perfect, flawless, timeless, iconic, awe-inspiring,
  very, extremely, super, highly, amazingly, ultra-

TIER 2 — Remove unless serving specific function (explain retention):
  moody, dreamy, surreal, ethereal, cinematic, atmospheric, dramatic,
  evocative, haunting, powerful, striking
  
  Retention test: does removing this word lose specific visual information?
    YES → keep, but verify the next word isn't also vague
    NO  → replace with concrete visual fact

TIER 3 — Meta-descriptions (never include):
  professionally composed, art directed, thoughtfully framed,
  masterfully lit, expertly captured, beautifully rendered
```

---

## 5. ПОШАГОВЫЕ ЗАМЕЧАНИЯ

### Step 0 — Association Mutation Engine

**Проблема 1:** 6 ассоциаций × 3 линзы × оценка × турнир — это ~1500 токенов только на промежуточную работу. При COMPACT-режиме это избыточно.

**Проблема 2:** FRAME TRANSPLANT CONSTRAINT (в Step 2) ограничивает Frame Transplant до «sub-register within the declared format». Но в Step 0 формат ещё не объявлен (он определяется в Step 1). Forward reference.

**Решение:** Перенести FRAME TRANSPLANT CONSTRAINT в Step 0, Phase B, как часть описания линзы, с оговоркой:
```
FRAME TRANSPLANT: [...existing description...]
  Pre-constraint: if the GOAL (when resolved in Step 1) declares a specific
  format — this mutation must stay within sub-registers of that format.
  If GOAL is not yet known — mark mutation as [FORMAT-DEPENDENT] and
  re-validate after Step 2.
```

---

### Step 1 — Theme & Goal Analysis

**Проблема:** Таблица Goal содержит 13 целей. Нет механизма для **гибридных целей** (например, «poster + dark fantasy», «editorial + watercolor»). Модель вынуждена выбрать одну строку.

**Решение:**
```
HYBRID GOAL: When theme naturally spans two goals, declare both:
  PRIMARY GOAL:   [dominant format] — [70% of visual decisions]
  SECONDARY GOAL: [supporting format] — [30% influence on palette/mood/framing]
  CONFLICT RESOLUTION: where primary and secondary disagree, primary wins.
```

---

### Step 1.5 — Spectrum Calibration

**Проблема:** Axis MEANING описан как «same visual, one shifted detail carries both readings» — это описание Slot 3 resolution, не оси. Ось должна описывать **что меняется**, а не как это выглядит в одном слоте.

**Решение:** Переписать:
```
| MEANING | What implication the viewer draws | From surface reading to inverted reading |
```

---

### Step 3 — Narrative Archetype

**Проблема:** 5 архетипов — мало. Отсутствуют:
- **Genesis** (creation, emergence from nothing)
- **Sacrifice** (loss that enables something else)
- **Mirror** (encounter with exact duplicate that reveals difference)
- **Descent** (going deeper/lower to find something)

**Решение:** Расширить до 8–9 архетипов или добавить:
```
If none of the 5 archetypes fits naturally — declare:
  NARRATIVE ARCHETYPE: NONE — [one sentence: why the theme resists archetypical framing]
  Series will rely on SPECTRUM AXIS alone for coherence.
```
(Это уже предусмотрено `[chosen / none]`, но не хватает объяснения, когда выбирать NONE.)

---

### Step 6 — Narrative Mode Test

**Проблема:** Тест из 3 вопросов (temporal arc? recurring element? self-contained goal?) — слишком грубый. Некоторые «self-contained» цели (poster) могут быть серией с нарративом. Некоторые «temporal» темы плохо работают с повторяющимся элементом.

**Решение:** Добавить 4-й вопрос:
```
4. Would a story thread ADD value, or would it CONSTRAIN creative diversity? ADD / CONSTRAIN

Rule: (1=Yes AND 2=Yes AND 4=ADD) AND 3=No → ON
      Any other combination → OFF
```

---

### Step 7 — Layer 4 ERA/STYLE

**Проблема:** Sub-style banks для «Oil painting» содержат 5 вариантов (impasto / glazing / alla prima / tenebrism / plein air), и правило гласит «no repeats within a series» из 5 слотов. Если серия — целиком oil painting, все 5 sub-styles обязательно используются, что лишает выбора и может дать негармоничную серию.

**Решение:** Расширить каждый sub-style bank до минимум 7 вариантов:
```
Oil painting: impasto / glazing / alla prima / tenebrism / plein air /
              sfumato / scumbling
```
Или ослабить правило:
```
SINGLE-MEDIUM SERIES: At least 3 of 5 slots must use different sub-styles.
Remaining 2 may repeat if justified by narrative coherence.
Declare: SUB-STYLE REPEAT: Slot [N] and [M] share [sub-style] — reason: [one clause]
```

---

### Step 9 — Prompt Structure

**Проблема 1:** Структура промта содержит ~15 элементов. Для генераторов с жёстким лимитом (Midjourney: 60–85 слов) невозможно уместить всё. Нет приоритизации — что резать первым?

**Решение:**
```
TOKEN BUDGET PRIORITY (cut from bottom when over word limit):
  1. [MEDIUM + SUBJECT + ACTION]           — never cut
  2. [ENVIRONMENT + ATMOSPHERE + MOOD]     — never cut
  3. [MEANING DEVICE encoded]              — cut last
  4. [LIGHTING + COLOR STORY]              — compress to 1 phrase if needed
  5. [ERA/STYLE + STYLE LABEL]             — compress to 1 phrase
  6. [WOW DETAIL + CONCEPT ANCHOR]         — keep one, merge other into scene
  7. [CAMERA/FRAMING SPECS]                — cut for non-photography
  8. [SIGNATURE DETAILS]                   — first to cut
  9. [FAMILIARITY DEVICE]                  — merge into environment description
```

**Проблема 2:** `[SOURCE GENRE GRAMMAR — only when Meaning Device = Genre Collision]` — этот элемент огромен (3 компонента) и раздувает промт. Для Genre Collision сцен слово-лимит почти нереален.

**Решение:** Для Genre Collision увеличить лимит на +15 слов или слить genre grammar elements в основное описание сцены (не выделять отдельным блоком).

---

## 6. ПРЕДЛАГАЕМЫЕ СТРУКТУРНЫЕ ИЗМЕНЕНИЯ

### 6.1. Добавить OUTPUT MODE (как описано в п.1.1)

Вставить после «Generate 5 final image prompts»:
```
**OUTPUT MODE:** [FULL / COMPACT / DEBUG [N]] — default: COMPACT
  COMPACT: Analysis Summary + 5 prompt blocks. All intermediate steps silent.
  FULL: All steps with declarations (for debugging or learning).
  DEBUG [N]: Full output for Step N only; rest compact.
```

### 6.2. Заменить числовой скоринг в Step 5 (как описано в п.1.2)

### 6.3. Добавить обработку edge cases

```
EDGE CASES:
  - Theme is a single abstract word (e.g., "nothing"):
    → Theme Parse: SUBJECT = [closest embodiable entity]; PROPERTY = [the abstraction]
    → If no embodiable entity → LENS A = OUTSIDE; proceed
  
  - Theme contains multiple subjects:
    → Select PRIMARY SUBJECT (most visually dominant) for SUBJECT ANCHOR
    → Declare SECONDARY SUBJECTS — not anchor-protected, may be dissolved
  
  - Theme and GOAL contradict:
    → GOAL wins for format decisions; THEME wins for content decisions
    → Declare: THEME-GOAL TENSION: [what was sacrificed, what was preserved]
  
  - Theme is in non-English language:
    → Translate to English for processing; preserve cultural connotations
    → Declare: CULTURAL CONTEXT: [one sentence about visual tradition]
```

### 6.4. Добавить COHERENCE SCORE для финальной серии

После Step 8, перед Step 9:
```
SERIES COHERENCE SCORE (self-check):
  [ ] A viewer seeing all 5 images recognises them as one series
  [ ] The progression from Slot 1 to 5 has a perceivable direction
  [ ] No two slots could be swapped without losing narrative logic
  [ ] Each slot is individually strong — none is "filler"
  Any NO → identify the weakest slot, return to Step 7 for that slot only.
```

### 6.5. Упростить Camera Engine

Текущая таблица содержит много повторов и edge cases. Предлагаю сжать:
```
CAMERA ENGINE (photography only):

| Slot | Focal (FF) | Aperture | Feel |
|---|---|---|---|
| 1 | 24–35mm | f/5.6–8 | Wide, stable, documentary |
| 2 | 50mm | f/2.8 | Normal, slightly uneasy |
| 3 | 85–105mm | f/1.8–2.0 | Intimate, collision |
| 4 | 85mm | f/2.0 | Drifting, selective |
| 5A | 85mm | f/2.0–2.8 | Steady, quiet |
| 5B/C | 135–200mm or <24mm | f/1.4 | Destabilised |

OVERRIDE: Shot type always wins over focal length table.
Camera body: include only for SD/MJ; omit for Flux/Aurora/Imagen.
```

---

## 7. КОНКРЕТНЫЕ РЕДАКЦИИ (ключевые)

---

### Редакция 2 — Итерации

**Добавить** после PROCESS MAP:
```
GLOBAL ITERATION LIMIT: No revision loop executes more than 2 times.
After 2 failed iterations → accept best available, declare compromise,
continue. This applies to: Phase D retries, Step 5 fallbacks,
REDIRECT self-checks, and any other loop in this document.
```

---

### Редакция 3 — Platform Module

**Заменить** финальную секцию Platform Adaptation на:
```
PLATFORM ADAPTATION (verify current syntax before use):

  Universal (Flux, Aurora, Gemini Imagen):
    → Prompt works as-is. Omit camera body, resolution tags, negative prompts.
  
  Midjourney:
    → Append: --ar [AR] --v [current version] --style raw
    → Negative: use --no [key exclusions, max 5 items]
    → Camera body: include in prompt text
  
  Stable Diffusion / SDXL / ComfyUI:
    → Append quality weights: (photorealistic:1.3), (film grain:1.1)
    → Full negative prompt supported
    → Camera body: include
  
  Firefly:
    → Append content type tag
    → No negative prompt support
    → Camera body: omit

NOTE: Generator capabilities evolve. When version-specific flags are
uncertain, omit them — well-written descriptive prose transfers better
than outdated technical flags.
```

---

### Редакция 4 — Visual Reference Pool

**Проблема:** Список конкретных имён художников/фотографов огромен (~40 имён) и занимает ~400 токенов. При этом правило гласит: «names never enter the prompt» — они только internal scaffold.

**Решение:** Вынести reference pool в отдельный модуль, подгружаемый только при OUTPUT MODE: FULL. Для COMPACT — достаточно:
```
LAYER 5 — VISUAL REFERENCE:
  Choose an internal reference whose work exemplifies the target aesthetic.
  Extract 5 SIGNATURE descriptors (aperture, lighting, color temp, texture, composition).
  Derive STYLE LABEL (4–8 words describing the school/movement).
  Never include the reference name in the prompt.
```

---

## 8. НЕДОСТАЮЩИЕ ЭЛЕМЕНТЫ

### 8.1. Нет механизма для пользовательских ограничений

Пользователь может хотеть: «без людей», «только тёплые тона», «обязательно вертикальный формат». Промт не предусматривает пользовательские constraints.

**Решение:**
```
**CONSTRAINTS:** [USER CONSTRAINTS — if not specified, none apply]

User constraints override defaults but not Content Policy.
Append to DUAL LOCK as additional Goal Lock requirements.
```

### 8.2. Нет обработки повторных запросов

Если пользователь делает второй запрос на ту же тему с другой целью — нет механизма переиспользования предыдущего анализа.

**Решение:**
```
REPEAT THEME PROTOCOL:
  If THEME matches previous generation in this conversation:
    → Reuse Steps 0–2 unless user says "fresh start"
    → Re-run Steps 3–9 with new GOAL
    → Declare: REUSING ANALYSIS from previous generation. Steps 0–2 unchanged.
```

### 8.3. Нет feedback loop

Пользователь генерирует промт, видит результат в генераторе, хочет скорректировать. SLOT REVISION MODE существует, но нет механизма для feedback типа «получилось слишком тёмное» или «субъект не читается».

**Решение:**
```
[OPTIONAL MODULE] — FEEDBACK REFINEMENT

Activate with: `FEEDBACK SLOT [N]: [what went wrong in generated image]`

| Feedback type | Adjustment |
|---|---|
| "Too dark/light" | Revise Layer 3 Color Story + Layer 1 lighting |
| "Subject not readable" | Increase subject dominance %, simplify background |
| "Too abstract" | Shift slot ratio 20% toward literal pole |
| "Too boring" | Shift slot ratio 20% toward unexpected pole |
| "Wrong mood" | Revise Layer 2 emotional trigger + Layer 3 temperature |
| "Style doesn't match" | Revise Layer 4 ERA/STYLE + Layer 5 reference |

Output: revised prompt only for that slot.
```

---

## 9. РЕЗЮМЕ ПРИОРИТЕТОВ

| Приоритет | Проблема | Секция |
|---|---|---|
| 🔴 Критическая | Объём вывода превышает контекстное окно | §1.1 |
| 🟠 Высокая | Самооценка ненадёжна | §1.2 |
| 🟠 Высокая | Избыточные проверки раздувают вывод | §1.3 |
| 🟠 Высокая | Отсутствие лимита итераций | §3.4 |
| 🟡 Средняя | Устаревание платформенных тегов | §4.1–4.4 |
| 🟡 Средняя | Forward references в структуре | §3.1 |
| 🟡 Средняя | Нет механизма user constraints | §8.1 |
| 🟢 Низкая | Неполный banned words list | §4.5 |
| 🟢 Низкая | Мало narrative archetypes | §5, Step 3 |
| 🟢 Низкая | Sub-style banks слишком малы | §5, Step 7 |
