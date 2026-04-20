# USAGE

Прикладной гайд: как запускать UPG, как прогонять тему через Checklist, как ранжировать выдачу Tournament-ом, как аудировать картинку через VCP.

Этот файл отвечает на вопрос **"я пришёл с темой, что мне делать по шагам"**. Теория — в [ARCHITECTURE.md](ARCHITECTURE.md), термины — в [GLOSSARY.md](GLOSSARY.md).

<details>
<summary><b>📑 Содержание</b></summary>

- [Что тебе нужно](#что-тебе-нужно)
- [Быстрый старт (60 секунд)](#быстрый-старт-60-секунд)
- [Сценарий 1 — Голый UPG (для разведки)](#сценарий-1--голый-upg-для-разведки)
- [Сценарий 2 — Interview-first (Checklist → UPG)](#сценарий-2--interview-first-checklist--upg)
- [Сценарий 3 — Tournament (ранжирование выдачи)](#сценарий-3--tournament-ранжирование-выдачи)
- [Сценарий 4 — VCP (аудит картинки против промпта)](#сценарий-4--vcp-аудит-картинки-против-промпта)
- [Повторный прогон и итеративное редактирование](#повторный-прогон-и-итеративное-редактирование)
- [Часто встречающиеся ошибки](#часто-встречающиеся-ошибки)
- [Связанное](#связанное)

</details>

---

## Что тебе нужно

- **LLM с достаточным reasoning и контекстом.** UPG v10 — около 30 KB сжатой нотации + твой запрос + служебный вывод. На слабых моделях пайплайн схлопывается: фазы пропускаются, валидация превращается в один галочный пункт.
- **Image-модель или API к ней.** Midjourney / Flux / Stable Diffusion / xAI Aurora / Gemini Imagen / Firefly — всё это целевые платформы UPG. Любую тебе просто копируешь готовый промпт.
- **Место, куда вставляется system prompt.** В ChatGPT это Custom GPT или первое сообщение в чате. В Claude — Claude Project с System Prompt. В API — поле `system`.

**Что проверено и работает без обёрток** (best of 29/29 в [BENCHMARK.md](../BENCHMARK.md)): GPT-5.4 / GPT-5.2, Gemini 3.1, GLM-5, Sonnet-4.5 (с лёгким дрейфом).

**Что требует компенсирующую обёртку**: Claude-линейка (склонна к поэтизации), DeepSeek, Grok, ERNIE, Qwen. Подробности и рекомендации — [BENCHMARK.md](../BENCHMARK.md).

---

## Быстрый старт (60 секунд)

Минимальный сценарий — без Checklist, без структурированного ввода, просто кидаешь тему.

1. Открой [full_versions/UPG_v10.md](../full_versions/UPG_v10.md). Скопируй весь файл.
2. В ChatGPT / Claude / Gemini создай новый чат или проект. Вставь скопированный UPG как **system prompt** (или как самое первое сообщение).
3. Пришли своё сообщение одним блоком:

   ```
   THEME: красные кроссовки под дождём на бетоне
   GOAL: коммерческий пост в инстаграм
   PLATFORM: MJ
   ```

4. Модель пройдёт пайплайн Фаз 1→6 и отдаст 3 или 5 промптов (SIMPLE/STANDARD/COMPLEX подбирает сам роутинг Фазы 1.6, в v10 дефолт COMPLEX=5).
5. Берёшь любой из промптов, вставляешь в Midjourney. Всё.

Минимальный payload — одна строка **THEME**. Всё остальное (GOAL, PLATFORM, MODE, ELEMENTS) — опционально. Если не задал GOAL — включится AUTO-GOAL из Фазы 3.

---

## Сценарий 1 — Голый UPG (для разведки)

Когда использовать: хочешь быстро посмотреть, как UPG понимает твою тему, какие даёт S1–S5 и какие Lenses распределяет. Итерационно правишь на лету.

**Input**:
```
THEME: заброшенный советский санаторий зимой
GOAL: artistic
MODE: 1
```

**Output (сокращённо)**:
- Phase 1.2 classify: THEME_WIDTH=NARROW (конкретное место, эпоха, сезон)
- Phase 1.3 safety: passed (no real IDs / brands / violence)
- Phase 1.6 routing: COMPLEX → 5 prompts
- Phase 4.2 seeds: S1 Anchor / S2 Adjacent-contrast / S3 Oblique / S4 Drift / S5 Absence
- Phase 4.4 lenses: S1=PHOTO, S2=TEXTURAL, S3=ENV, S4=SYMBOLIC, S5=MINIMAL
- Phase 5 craft → 5 готовых промптов

Хорошо ложится на любую артистическую/эмоциональную тему, где ты сам не знаешь точно, что хочешь увидеть.

**Когда не сработает**: если в теме есть реальный человек (актёр, политик, певец), брендовое IP (персонажи Disney, Marvel), или graphic violence — Phase 1.3 перестроит вход и ты получишь safe-промпты, а не то, что просил. Это не баг, это политика.

---

## Сценарий 2 — Interview-first (Checklist → UPG)

Когда использовать: тема важная, один заход, нужно максимум контроля. Checklist — это 21 блок, 80 параметров, которые ты заполняешь ДО UPG. На выходе — `STRUCTURED THEME INPUT`, который UPG v9.15+ принимает как источник истины.

**Workflow (две сессии)**:

### Сессия 1 — Checklist

1. Открой [project_tools/UPG_Checklist_v1_8_0.txt](../project_tools/UPG_Checklist_v1_8_0.txt). Скопируй целиком.
2. Новый чат (отдельный от UPG!). Вставь Checklist как system prompt или первое сообщение.
3. Пришли тему и ответь на вопросы интервью. Checklist сам будет спрашивать:
   - **BLOCK A (Meta)**: GOAL, PLATFORM, MODE, ARC, AUDIENCE, AESTHETIC, VISUAL_VOCABULARY
   - **BLOCK B (Carrying Image)**: 10 компонентов физического описания главного объекта/идеи (7 физических + 3 поведенческих, минимум 7/10 заполнены). Single Object Test, S5 Trace.
   - **BLOCK C (Setting)**: UNIVERSE, GEOGRAPHY, ERA, FACTION_POV, AESTHETIC, MUST_INCLUDE, MUST_AVOID
   - **BLOCK D (Visual Vocabulary)**: 10 элементов с физическим описанием, Tier 1/2 pre-scan на запрещённые прилагательные, Mandatory Language check
   - **BLOCK E (Control)**: STYLE_PROFILE, REFERENCE_EXTRACTION, CAMERA_SYSTEM, DEVICE_SIM, IDENTITY_LOCK, LOCALE_DETAIL, MATERIAL_FIDELITY
   - **BLOCK F (Seeds F1–F7)**: Ring Test, Anti-Clustering Check, Coherence Thread
   - **BLOCK G (Arc Planning)**: 8 Entry Angles с ротацией A/B/C/D, Contrast Pairs, Lens Sequence, Lens-Magic Compatibility, Frame Scale Consistency
   - **BLOCK H (Technical)**: Aspect, Platform overrides, Density targets per slot
   - **BLOCK L (Light Design)**, **BLOCK X (Texture Palette)** и т.д.
4. Checklist выдаст финальный блок в формате `STRUCTURED THEME INPUT:` — это код-блок, который уже готов к UPG.

### Сессия 2 — UPG

1. Новый чат. Вставь [full_versions/UPG_v10.md](../full_versions/UPG_v10.md) как system prompt.
2. Пришли сообщение, содержащее ТОЛЬКО скопированный `STRUCTURED THEME INPUT` из Checklist.
3. UPG распарсит поля (Phase 4.1 видит `STRUCTURED THEME INPUT` и пропускает часть B.2 собственного enrichment), прогонит SEED QUALITY advisories, применит твои seeds как authoritative (не будет их переопределять), и отдаст спектр.

**Зачем так**: если тема имеет конкретные ограничения (бренд, эпоха, IP, конкретный objects/people to avoid), Checklist их фиксирует жёстко. UPG без Checklist может заменить твой "LADA 2107" на обобщённый "советский седан". С Checklist не заменит — поле `MUST_INCLUDE: LADA 2107` прожигается до финального промпта.

---

## Сценарий 3 — Tournament (ранжирование выдачи)

Когда использовать: у тебя 6 разных серий по 5 промптов (30 шт), все по одной теме — на разных моделях или с разными настройками. Хочешь отобрать ТОП-5 по взвешенным критериям.

1. Сгенерируй 6 серий одной темы через UPG (на разных моделях, или с разными CONSTRAINTS, или на разных SEED POLICY).
2. Открой [project_tools/tur_v2.txt](../project_tools/tur_v2.txt). Скопируй как system prompt в новый чат.
3. Вставь все 30 промптов в одно сообщение, обозначив Run/Slot (например: `Run A / S1: <prompt text>`, `Run A / S2: ...`).
4. Укажи CONTEXT (ARTISTIC / EDITORIAL / COMMERCIAL / SCIENTIFIC / PERSONAL). От него зависят веса.
5. Tournament пройдёт Phase 0 (Mode/Context detection) → Phase 1 (полная ранжирующая таблица с Density scoring на 70 очков) → Phase 2 (Top-5 selection with arc constraint — 5 промптов, которые не просто сильнейшие, но и складываются в связный arc S1→S5).
6. На выходе — финальный ТОП-5, пригодный для production-прогона.

**Веса по умолчанию (artistic)**: Clarity ×1.0 | Specificity ×1.5 | Originality ×1.5 | Technical ×1.0 | Arc Fit ×1.0 | Density ×1.0. Для commercial/scientific веса сдвигаются в сторону Clarity и Technical.

---

## Сценарий 4 — VCP (аудит картинки против промпта)

Когда использовать: картинка сгенерирована, и ты хочешь измерить, насколько точно image-модель нарисовала то, что ты описал в тексте. Это аудит **image ↔ prompt**, не аудит качества промпта.

1. Открой [tools/VisualCorrespondenceProtocol_v1_0.md](../tools/VisualCorrespondenceProtocol_v1_0.md). Это vision-capable протокол, нужна модель, которая умеет смотреть картинки (Claude Sonnet, GPT-4o/5, Gemini).
2. Новый чат. Вставь VCP как system prompt.
3. В сообщение положи:
   - `PROMPT:` полный текст промпта
   - `IMAGE:` приложенную картинку
   - `CONTEXT (optional):` MODE, ARC_POSITION, PLATFORM, MODULES, GOAL
4. VCP пройдёт 6 стадий:
   - **Stage 0 — Prompt Decomposition**: декомпозиция промпта на элементы (SUBJ / MAT / COL / LIGHT / COMP / ENV / TEX / TECH / THRESH / REAL), с присвоением приоритета ANCHOR / SUPPORTING / ATMOSPHERIC.
   - **Stage 1 — Image Scan**: объективное описание того, что на картинке, без знания промпта.
   - **Stage 2 — Element Correspondence**: поэлементный мэтч prompt vs image. Для каждого — PRESENT / MISSING / WRONG / PARTIAL.
   - **Stage 3 — Unauthorized Additions**: что модель добавила из себя (не было в промпте).
   - **Stage 4 — Batch / Cross-slot checks** (опционально, если анализируешь всю серию S1–S5 сразу): проверка, что arc соблюдён.
   - **Stage 5 — Fidelity Score + Verdict**: численная оценка + рекомендация (re-generate / accept / edit).
5. На выходе — структурированный отчёт: что сгенерилось, что пропало, что дорисовалось, где процент совпадения ниже порога, какие слоты пересгенерить.

**Когда особенно полезно**: при серии из 5 слотов, где у S5 ожидалось ABSENCE (отсутствие главного объекта), а модель на самом деле тупо опять его нарисовала — VCP это поймает в Stage 2 как "MISSING: Environmental Departure — subject still present in frame".

---

## Повторный прогон и итеративное редактирование

Когда одна из 5 картинок почти идеальная, но нужно поменять одно конкретное.

**Не пиши модели "поправь S3"** — UPG v10 принимает `PRESERVE_LIST`:

```
PRESERVE_LIST: [main subject, camera system, palette, composition]
FEEDBACK: В S3 нужно заменить задний план с городского на сельский, всё остальное оставь как есть.
```

UPG автоматически выведет PRESERVE_LIST из всех не-целевых элементов текущего промпта и инжектирует их как explicit locks в новый прогон. Constraint Precedence в v10: Policy → GOAL → CONSTRAINTS → PRESERVE_LIST → Context → AUTO-GOAL.

---

## Часто встречающиеся ошибки

### "UPG выдал одинаковые промпты, все 5 про одно и то же"

Симптом: S4 не отличается от S1. Причина — слабая модель или плохой Ring Test на стадии Phase 4.2. В качественной модели Ring Test должен ловить это на Ring 2/3. Попробуй явно указать `MODE: 3` (remix/permutation) — он форсирует гораздо более сильный спектр. Или ранжируй через Tournament и отбрасывай S4.

### "Промпт получился длинный, Midjourney не ест"

Midjourney v6 имеет мягкое ограничение ~60 слов на промпт. UPG v10 знает о `MJ_LIMITS: {max_sent:[3,3,3,3,4], max_elem:5}`. Укажи `PLATFORM: MJ` — UPG сам ужмётся до лимита. Если не указал — получишь полный Flux/Aurora-формат.

### "Я прошу 'нежный рассвет', получаю 'soft warm golden morning' — это же ban registry?"

Да, на промпте-выходе bannable не должно быть. Если получил `soft`, `subtle`, `elegant`, `essence`, `harmony` — у тебя либо слабая модель, либо она пропустила Phase 6 validation. Прогони через [project_tools/1__analysis_promt_v1_1.txt](../project_tools/1__analysis_promt_v1_1.txt) — он детектит compression artifacts и unauthorized injection.

### "Тема 'любовь' / 'свобода' / 'одиночество' — UPG ругается на ABSTRACT-HARD"

Это штатное поведение. Абстрактные темы идут через Pattern 3C (введён v6.0). Ты получишь не "визуализацию любви", а **carrier scene** — конкретную физическую сцену, из которой тема считывается. Это фича, не баг. Если хочешь конкретную интерпретацию — задай её через BLOCK B в Checklist (Carrying Image).

### "Модель пропустила Phase 3 и сразу пошла в Phase 4"

Слабая модель. Попробуй `TRACE: true` в запросе — UPG напечатает промежуточные CHECK-блоки, станет видно, где именно пайплайн сломался. Перейди на более сильную модель из [BENCHMARK.md](../BENCHMARK.md) top tier.

---

## Связанное

- [ARCHITECTURE.md](ARCHITECTURE.md) — как устроен пайплайн внутри
- [EVOLUTION.md](EVOLUTION.md) — как v10 получился из v0
- [GLOSSARY.md](GLOSSARY.md) — термины (EIS, Drift, Ring Test, Carrying Image, Lens, Seed, Zone, Slot)
- [BENCHMARK.md](../BENCHMARK.md) — на каких моделях прогонять, каких избегать, где нужны обёртки
- [CHANGELOG.md](../CHANGELOG.md) — что менялось по версиям
