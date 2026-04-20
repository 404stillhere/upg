# Changelog

Все значимые изменения UPG задокументированы здесь.

Формат основан на [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/). Нумерация — авторская, SemVer не гарантируется: патчи могут менять структуру фаз, а одна major-серия может иметь несовместимые промежуточные версии.

> Полная таблица файлов — в [README.md](README.md). Логика ветвления (нелинейная эволюция GREETING → UNIVERSAL → IMAGE PG → UPG) расписана в [docs/EVOLUTION.md](docs/EVOLUTION.md). Отчёт о валидационной кампании — [BENCHMARK.md](BENCHMARK.md).

---

## [v10] — current

**Статус:** текущая стабильная версия. Файл: [full_versions/UPG_v10.md](full_versions/UPG_v10.md).

### Added
- **Generator Trigger Registry (GTR)** — внутренний реестр триггеров по категориям: Quality Boosters, Aesthetic Magnets, Composition Overrides, Platform-Specific Traps.
- **Шесть locks:**
  - `IDENTITY_LOCK` — фиксация персонажа / сущности сквозь серию.
  - `LOCALE_DETAIL` — географическая / культурная аккуратность.
  - `STYLE_PROFILE` — жанрово-стилистический якорь.
  - `MATERIAL_FIDELITY` — верность материалу (ткань, дерево, металл).
  - `AUTH_LAYER` — слой аутентичности (время, эпоха, среда).
  - `DEVICE_SIM` — симуляция устройства съёмки / записи.
- **VALIDATION STACK** — унифицированные слои L1 — L9.2.
- **HARD CHECKS P0 — P1M** — обязательные проверки с чётким priority level.

### Changed
- Компрессия нотации: финальный размер ≈ 30 KB при сохранённом функционале.
- Ban registry, camera system, reference extraction — унаследованы из v9.18 и реорганизованы.

---

## [v9.22] — валидационный патч (не в репо как отдельный файл)

**Статус:** промежуточная версия. В репо отдельным файлом не лежит — её содержимое вошло в v10. Подробности кампании, приведшей к выпуску, см. [BENCHMARK.md](BENCHMARK.md).

### Fixed
- **N-75 (Density counting):** плотность элементов считалась "на глаз", до 24% ложных PASS. Введён строгий метод подсчёта по категориям в слое L7.
- **N-76 (Lens-Aspect compat):** правила совместимости линз и aspect ratio были разбросаны по промпту. Собраны в единый чеклист L7.5: `CINE → widescreen only`, `TEXTURAL ≠ face`, `FULL SCENE → wide focal`.

### Notes
- Патч выпущен после self-audit v9.21.
- Основан на 32 тестах / 18 LLM-моделях / 77 открытиях.
- Промпт после патча — 9.5/10 по внутренней оценке.

---

## [v9.x series] — 2026-03-26 → 2026-04-06 — эпоха компрессии

**Статус:** архив, не поддерживается. 13+ итераций и 11 патчей.

### Highlights
- **v9.4 → v9.8:** подготовка к компрессии, реструктуризация PHASE-слоёв.
- **v9.15 (компрессия):** BAN REGISTRY становится canonical source of truth. Введён MIDJOURNEY MODE со строгими лимитами длины.
- **v9.17.0 → v9.17.1:** рефакторинг routing и module activation.
- **v9.18:** большой апгрейд — добавлены `MOOD_ANTI_PATTERN`, `SPATIAL_MEANING_MAP`, `CAMERA_SYSTEM` (таблицы объективов ARRI / RED / Sony / Hasselblad + Zeiss / Cooke / Leica / Panavision), `THRESHOLD_ELEMENTS` (GHOST / HINT / PARTIAL / OBSCURED), `REALISM_ANCHOR`, `REFERENCE_EXTRACTION` (таблица Lubezki / Deakins / Crewdson / Vermeer / Tarkovsky / BR2049).
- **v9.19.1:** формализация patch-notation как самостоятельного документа.
- **v9.21:** self-audit (предшественник v9.22).

### Full versions в репо
`UPG_v9_4.md` · `UPG_v9_8.md` · [`UPG_v9_11.md`](full_versions/UPG_v9_11.md) (2026-04-03) · `UPG_v9_13.md` · `UPG_v9_15.md` · `UPG_v9_17_1.md` · [`UPG_v9_19_1.md`](full_versions/UPG_v9_19_1.md) (2026-04-06)

### Patches
`PATCH_v9_1.md` (2026-04-01) · `PATCH_v9_5.md` (2026-04-01) · `PATCH_v9_7.md` (2026-04-02) · `PATCH_v9_10.md` (2026-04-02) · `PATCH_v9_11.md` (2026-04-03) · `PATCH_v9_12.md` (2026-04-03) · `PATCH_v9_13.md` · `PATCH_v9_14.md` · `PATCH_v9_17_0.md` (2026-04-03) · `PATCH_v9_17_1.md` · `PATCH_v9_18.md` (2026-04-04) · `PATCH_v9_26.md`

---

## [v8.x series] — зрелые зоны

**Статус:** архив. ZONE A/B/C окончательно стабилизированы. Восемь Creative Lenses как финальный канон (PHOTO / CINE / TEXTURAL / PAINT / ENV / SYMBOLIC / MINIMAL / SENSORY).

### Highlights
- **v8.0:** зоны + CONCISE_MODE работают как дефолт. Подготовка к компрессии v9.
- **v8.5, v8.9:** стабилизация safety-пропагации и spectrum-генерации.

### Full versions в репо
`UPG_v8_0.md` · `UPG_v8_5.md` · `UPG_v8_9.md`

### Patches
`PATCH_v8_6.md`

---

## [v7.x series] — рефакторинг в зоны

**Статус:** архив. Критический поворот архитектуры.

### Changed (architectural)
- **v7.2:** вся цепочка фаз реорганизована в **ZONE A** (Phases 1–3: Parse / Enrich / Goal), **ZONE B** (Phase 4: Spectrum / Seeds / Lenses), **ZONE C** (Phases 5–6: Craft / Validate / Output). До v7.2 фазы шли линейно — с v7.2 зоны дают логическую группировку и точки возврата при ошибке.
- **CONCISE_MODE:** введён как альтернатива диагностическому выводу. С v8.0 становится дефолтом.
- **Creative Lenses:** канонизированы до 8 типов с матрицей совместимости.

### Full versions в репо
`UPG_v7_2.md` · `UPG_v7_3.md` · `UPG_v7_6.md`

### Patches
`PATCH_v7_8.md` (2026-03-31) · `PATCH_v7_9.md`

---

## [v6.x series] — priority stack, EIS, abstract-hard

**Статус:** архив. Закладывается основа "драйвинг-контроля" промпта.

### Added
- **GLOBAL PRIORITY STACK** — иерархия правил (что важнее чего при конфликте).
- **EIS 0–100** — шкала эмоциональной интенсивности темы и каждого слота. С этого момента drift-контроль становится количественным, а не "на глаз".
- **5-Gate Boundary** — пять gate-ов валидации между фазами.
- **Pattern 3C** (Abstract-Hard) — отдельный маршрут для тем без физических якорей ("emptiness without emptiness").

### Full versions в репо
[`UPG_v6_0.md`](full_versions/UPG_v6_0.md) (2026-03-24) · `UPG_v6_1.md` · `UPG_v6_2.md` · [`UPG_v6_6.md`](full_versions/UPG_v6_6.md) (2026-03-26)

---

## [v5.x series] — safety-слой, INTENT_SIGNAL, параллельная линия

**Статус:** архив. Самая разветвлённая серия.

### Added
- **v5.1 — meta-critic / surgeon** (отдельный инструмент, не генератор): 7 фаз A–G для аудита чужого UPG-прогона. Нашёл место в [tools/](tools/).
- **v5.4:**
  - **PHASE 0 INTENT_SIGNAL** — распознаёт намерение пользователя (LITERAL / EXPANSIVE / COMPLEXITY / DEFAULT).
  - **ABSTRACT-HARD flag** + escalation rule.
  - **THEME_WIDTH** — формальная классификация NARROW / MODERATE / BROAD с разными правилами enrichment.
  - Полная **safety-таксономия** (Identity, Explicit, Violence, Hate) с `safety_transform` map и propagation lock на все downstream-выходы.
  - **Module activation** (A / B / C / D / V) как формальная таблица.
  - Objective-signal routing с DEFAULT OVERRIDE на COMPLEX.
  - Энричмент-паттерны 1, 2A, 2B, 3A, 3B, 3C, 4.

### Full versions в репо
[`UPG_v5_0.md`](full_versions/UPG_v5_0.md) (2026-03-23) · `UPG_v5_1.md` · [`UPG_v5_3.md`](full_versions/UPG_v5_3.md) (2026-03-28) · `UPG_v5_4.md` · [`UPG_v5_6.md`](full_versions/UPG_v5_6.md) (2026-03-28)

### Patches
`PATCH_v5_2.md` (2026-03-28) · `PATCH_v5_6.md` (2026-03-28)

---

## [v4.x series] — параллельная ветка IMAGE PROMPT GENERATOR

**Статус:** архив. Ветка, идущая параллельно UNIVERSAL PG (v2–v3).

### Added
- **9-шаговый пайплайн** (до зон).
- **Таблицы ERA / STYLE** — эра съёмки, стиль, киношный референс.
- Специализация на изображениях как явной цели (тогда как UNIVERSAL PG стартовала с более широкой амбиции).

### Full versions в репо
[`UPG_v4_0.md`](full_versions/UPG_v4_0.md) (2026-03-21) · [`UPG_v4_1.md`](full_versions/UPG_v4_1.md) (2026-03-21)

---

## [v3.x series] — associative artifacts + scratchpad CoT

**Статус:** архив.

### Added
- **STEP 3.5 Associative Artifacts** — разрешение вводить неочевидные объекты-усилители по теме.
- **`<scratchpad>` Chain-of-Thought** — скрытый слой рассуждения перед финальным промптом.

### Full versions в репо
`UPG_v3_0.md` · `UPG_v3_3.md` · `UPG_v3_5.md`

### Patches
[`PATCH_v3_0.md`](patches/PATCH_v3_0.md) (2026-03-27) · [`PATCH_v3_2.md`](patches/PATCH_v3_2.md) (2026-03-27)

---

## [v2.x series] — English pivot, universal intent

**Статус:** архив.

### Changed
- **Переход на английский** — все последующие промпты пишутся только на английском.
- **6 STEPS** — упрощённая структура после 11-шагового v1.0.
- **REDIRECT-8** — восемь категорий safety-редиректов (предшественник полной таксономии v5.4).

### Full versions в репо
`UPG_v2_0.md` · `UPG_v2_2.md` · `UPG_v2_3.md`

---

## [v1.0] — 2026-03-27 — первая версия

**Статус:** архив. Исторический артефакт.

### Added
- **11-шаговый генератор открыток на русском.** Называется "Universal Prompt Generator v1.0", но по факту — специализированный GREETING CARD PROMPT GENERATOR (название "Universal" — аспирация).
- Русский язык генерации (с v2.0 перешли на английский).

### Full versions в репо
[`UPG_v1_0.md`](full_versions/UPG_v1_0.md)

### Patches
`PATCH_v1_0.md`

---

## [v0] — pre-1.0 — задумка

**Статус:** архив. Самый ранний артефакт — концепт, с которого всё началось.

### Notes
- **5-шаговый автономный генератор на русском:** _Анализ клише → Разрушение шаблона → Усиление (Художественное ДНК) → Создание профессионального prompt → Самооценка_.
- В промпт встроен конкретный пример (`Spring Energy`, спортивная одежда, коммерция) — ещё не отделён generator от theme.
- Уже присутствует **структурированный вывод** `[Subject] [Environment] [Lighting] [Composition] [Camera/Lens] [Textures] [Color palette] [Mood] [Artistic references] [Technical tags] [Aspect ratio]` — прообраз современной слотовой структуры.
- **Самооценка по 6 критериям** (новизна / визуальная сила / художественная глубина / запоминаемость / коммерческий потенциал / риск клишированности) — предшественник EIS 0–100 из v6.0.
- Максимум **3 цикла переписывания** при неудовлетворительной оценке — предшественник validation loop.
- Термин "художественное ДНК" в последующих версиях исчез.

### Full versions в репо
[`UPG_v0.md`](full_versions/UPG_v0.md)

---

## [v666.x] — параллельная ветка

**Статус:** самостоятельная линия развития, отдельная от основной цепочки v1–v10. Накопленные правила в альтернативной конфигурации.

### Versions
- **v666.4.1** — зрелая версия ветки со всеми накопленными правилами.
- **v666.5.2.1, v666.5.2.3** — строгие patch-instructions поверх v666.4.1 (не standalone-генераторы).

### Full versions в репо
[`UPG_v666_4_1.md`](full_versions/UPG_v666_4_1.md) · [`UPG_v666_5_2_1.md`](full_versions/UPG_v666_5_2_1.md) · [`UPG_v666_5_2_3.md`](full_versions/UPG_v666_5_2_3.md)

---

## Companion tools — версии

Инструменты-спутники не входят в основную нумерацию UPG.

| Инструмент | Версия | Файл |
|---|---|---|
| Checklist | v1.8.0 | [project_tools/UPG_Checklist_v1_8_0.txt](project_tools/UPG_Checklist_v1_8_0.txt) |
| Analysis Prompt | v1.1 | [project_tools/1__analysis_promt_v1_1.txt](project_tools/1__analysis_promt_v1_1.txt) |
| Audit Analysis | v1.2 | [project_tools/2__AUDIT_ANALYSIS_v1_2.txt](project_tools/2__AUDIT_ANALYSIS_v1_2.txt) |
| Analysis Report | v2.1 | [project_tools/3__ANALYSIS_REPORT_v2_1.txt](project_tools/3__ANALYSIS_REPORT_v2_1.txt) |
| Visual Correspondence Protocol | v1.0 | [tools/VisualCorrespondenceProtocol_v1_0.md](tools/VisualCorrespondenceProtocol_v1_0.md) |
| Session Dashboard | v1.0 | [project_tools/5__SESSION_DASHBOARD_v1_0.txt](project_tools/5__SESSION_DASHBOARD_v1_0.txt) |
| Tournament | v2 | [project_tools/tur_v2.txt](project_tools/tur_v2.txt) |

---

_Последнее обновление: 2026-04-20._
