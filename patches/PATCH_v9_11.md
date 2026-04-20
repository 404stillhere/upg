# Служебная записка: UPG v9.11 → v9.12

**От:** Claude (инстанс-исполнитель)
**Кому:** Claude (инстанс-рефакторщик)
**Тема:** Консолидация и исправление структурных проблем

---

## ПРЕАМБУЛА

Я работаю с UPG v9.11 + Checklist v1.4 несколько сессий. Промпт функционирует, генерирует качественные результаты, но накопил архитектурный долг. Ниже — конкретные проблемы и мои рекомендации по исправлению. Приоритеты расставлены по impact/effort.

---

## ПРИОРИТЕТ 1: КРИТИЧНО

### 1.1 Создать BAN REGISTRY

**Проблема:** Zero Tolerance бans дублируются в трёх местах с микро-различиями:
- `A.2.9` (основной список)
- `VISUAL_VOCABULARY Pre-Scan` (subset + русские слова)
- `HARD CHECKS Priority 1` (референс без списка)

**Решение:**
```
## BAN REGISTRY (canonical source)

### ZERO TOLERANCE — удалять/переписывать при обнаружении
[полный список из A.2.9]

### TIER 1 ADJECTIVES — заменять на материальные
[список soft/clean/fresh/fine/etc с заменами]

### ABSTRACT NOUNS — удалять всегда
[список stillness/silence/tension/etc]

### LOCALIZED (RU) — только если LANGUAGE=RU
[будто/словно/как будто/как если бы]
```

Все остальные секции ссылаются: `→ see BAN REGISTRY: ZERO TOLERANCE`

**Impact:** Убирает ~30% текста, устраняет риск рассинхронизации.

---

### 1.2 Консолидировать Entry Angle

**Проблема:** Логика разбросана по 4+ секциям:
- `B.2 Step 6` — типы и ротация
- `A.2.1` — требование к первому предложению
- `Phase 4.2` — slot assignment
- `HARD CHECKS #10` — верификация
- `Checklist G1` — ещё одна версия

**Решение:** Единый блок `### ENTRY ANGLE SYSTEM`

```
### ENTRY ANGLE SYSTEM

#### Types (8)
SCALE | TIME | LOCATION | WEATHER | CULTURAL | MATERIAL | PERSPECTIVE | ACTIVITY

#### Rotation Rules
A: SCALE+TIME | B: TIME+LOCATION | C: CULTURAL+LOCATION | D: SCALE+LOCATION
Exception: magic/fictional themes → WEATHER/CULTURAL+TIME

#### Execution (S1-S2 only)
First sentence of S1 and S2 MUST realize assigned angle.
SCALE: opens with number/dimension as subject or first modifier
LOCATION: opens with place preposition (at, within, beneath, inside)
[остальные типы]

#### Compliance Examples
✅ SCALE: "A fifteen-meter granite Buddha rises..."
❌ NOT SCALE: "The Buddha stands at the temple..." (это LOCATION)

#### Verification
Print: `Entry Angle: S1=[TYPE] | S2=[TYPE]`
If first sentence doesn't realize angle → REWRITE before output
```

Удалить фрагменты из B.2, A.2.1, Phase 4.2. В HARD CHECKS оставить только `→ see ENTRY ANGLE SYSTEM: Verification`.

---

### 1.3 Переименовать линзу TEXT → TEXTURAL

**Проблема:** В таблице A.4 линза `TEXT` означает макро/тактильную съёмку. Но во всём промпте `text` = типографика (Module A text zones, copy lines). Коллизия терминов.

**Факт:** В примерах и Lens Sequence уже используется `TEXTURAL`. Таблица отстала.

**Решение:** В таблице A.4:
```
| TEXTURAL | Macro | Tactile, magnified | ≤10cm field. Shallow DOF. |
```

Grep всего документа на `TEXT` как линзу, заменить на `TEXTURAL`.

---

### 1.4 Исправить S5 TRACE VERIFICATION логику

**Проблема:** Инвертированные условия создают ошибки парсинга:
```
1. Carrying Image visible? → REWRITE (rewrite если ДА)
3. Theme identifiable...? → NO → REWRITE (rewrite если НЕТ)
```

**Решение:**
```
S5 TRACE VERIFICATION (silent):
REWRITE if ANY true:
  □ Carrying image is visible in scene
  □ Prompt states what is absent (narrated absence)
  □ Theme NOT identifiable from physical evidence within 30 sec
```

Единообразная логика: всё через "rewrite if true".

---

## ПРИОРИТЕТ 2: ВАЖНО

### 2.1 Унифицировать Zone/Phase номенклатуру

**Проблема:** Смешение `Zone A/B/C` и `Phase 3/4/5` без объяснения иерархии.

**История:** Zones = функциональные области (A=стандарты, B=препроцессинг, C=модули). Phases = pipeline этапы. Они ортогональны, но это нигде не объяснено.

**Решение:** Добавить после SYSTEM ROLE:
```
## ARCHITECTURE

ZONES (functional domains):
- Zone A: Writing Standards — rules that apply during prompt composition
- Zone B: Preprocessing — decisions made before writing
- Zone C: Modules — conditional extensions (A/B/C/D)

PHASES (pipeline sequence):
1. Safety Scan
2. Decisions (Zone B.1)
3. Enrichment (Zone B.2)
4. Seeds (if FULL ARC)
5. Prompt Writing (Zone A applied)
6. Validation (Hard Checks)

EXECUTION: Phase 1→6 sequential. Zones activated as needed per phase.
```

---

### 2.2 Упростить Stateful-правила

**Проблема:** `VEHICLE-WITNESS CEILING`, `SEED 2 CATEGORY TRACKING`, `ANTI-ANCHOR` требуют памяти между сессиями. LLM этого не умеет без явного ввода.

**Решение:** Две опции:

**Опция A (user-assisted):** Добавить в INPUTS:
```
- SESSION_HISTORY: [omit for fresh | "PHOTO-PHOTO-CINE-PHOTO" for S1 anchors | etc]
```

**Опция B (моя рекомендация):** Переформулировать как soft preferences:
```
ANTI-ANCHOR: Prefer lens diversity in S1. If you notice repeating pattern 
across conversation, vary proactively. Not a hard failure.

SEED 2 CATEGORY: Prefer category variety. Same category acceptable 
if metaphorical distance sufficient.
```

Убрать "print check", убрать "CEILING → FORCED". Сделать guidance, не enforcement.

---

### 2.3 Синхронизировать Checklist v1.4 ↔ UPG v9.11

**Проблема:** Checklist добавляет структуры, которых нет в основном промпте:
- `LIGHT: { per slot breakdown }`
- `TEXTURE_PALETTE: { ... }`
- `TEMPORAL: { ... }`
- `SENSORY_MARKERS: { ... }`
- `DETAIL_DENSITY_TARGETS: { ... }`

**Решение:** Или добавить эти поля в UPG как optional enrichment, или пометить в Checklist как "extended mode". Текущий разрыв создаёт путаницу что canonical.

Моя рекомендация: Checklist = extended planning tool. UPG = execution engine. Checklist output feeds UPG input. Сделать это явным:
```
Checklist v1.4 generates THEME TEMPLATE
↓
UPG v9.11+ consumes THEME TEMPLATE as structured THEME input
```

---

### 2.4 Формат Feedback Adjustment Protocol

**Проблема:** Таблица записана как prose, нечитаема.

**Решение:**
```
| Signal | Action | Scope |
|--------|--------|-------|
| Too dark | Increase key light intensity, add fill | Affected slot |
| Too light | Reduce exposure, add shadow density | Affected slot |
| Unreadable (Module A) | Increase text size, add contrast | S1-S5 if Module A |
| Too abstract | Add physical anchor object | Affected slot |
| Boring | Add surprise element, shift lens | Affected slot |
| Mood mismatch | Adjust palette + light temperature | Series-wide |
| Composition off | Change camera angle/focal length | Affected slot |
| Theme drift | Re-anchor to carrying image | S3-S5 typically |
| Too violent | Apply aftermath rule, remove bodies | Affected slot |
| Real person resemblance | Shift to archetype, change features | Affected slot |
```

---

## ПРИОРИТЕТ 3: УЛУЧШЕНИЯ

### 3.1 Decision Block — убрать line limits

**Текущее:** `≤25 lines for FULL ARC... ≤15 for SHALLOW`

**Проблема:** Не верифицируется, конфликтует с "group fields", создаёт anxiety без пользы.

**Решение:** Заменить на:
```
Format: Compact. Group related single-value fields on shared lines.
No essays. Reference example:

Scope: MODERATE | Context: ARTISTIC | Medium: photography
Arc: FULL | Latitude: EXPANSIVE | Modules: NONE
[etc — example of proper density]
```

---

### 3.2 RERUN trigger definition

**Текущее:** `Same subject/situation → RERUN` — неопределённо.

**Решение:**
```
RERUN DETECTION:
Explicit: User states "ещё раз" / "another set" / "RERUN"
Implicit: THEME string identical to previous in conversation
Implicit: Core noun + Medium + Context ALL match previous run

If uncertain → ask user: "Это продолжение темы [X] или новая тема?"
```

---

### 3.3 Module combination rules

**Проблема:** `Priority: A→B→D→C` указан, но что если несколько активны?

**Решение:** Добавить:
```
MODULE COMBINATIONS:
A+B: Packaging with text zones — B provides form, A provides graphics
A+D: Poster series with wear — apply D degradation to A format
B+D: Packaging lifecycle — B form persists, D affects condition
A+B+D: Full packaging narrative — rare, apply all three

Conflict resolution: Physical constraints (B) → Visual system (A) → Temporal state (D)
```

---

### 3.4 CONCISE_MODE + TRACE interaction

**Проблема:** Оба флага активны — что печатать?

**Решение:** Добавить в OUTPUT PROTOCOL:
```
CONCISE_MODE + TRACE both true:
Print Routing Summary (from CONCISE_MODE)
Print CHECK blocks (from TRACE)
Suppress Decision Block
```

---

## РЕКОМЕНДУЕМЫЙ ПОРЯДОК РЕФАКТОРИНГА

1. **BAN REGISTRY** — создать, удалить дубли (высокий impact, средний effort)
2. **ENTRY ANGLE consolidation** — объединить 4 места в 1 (высокий impact, средний effort)
3. **TEXT→TEXTURAL** — find/replace (низкий effort, устраняет путаницу)
4. **S5 TRACE logic** — исправить инверсию (низкий effort, устраняет баги)
5. **Architecture section** — добавить (низкий effort, высокая clarity)
6. **Stateful rules** — смягчить до preferences (средний effort, убирает impossible requirements)
7. **Остальное** — по возможности

---

## СОХРАНИТЬ БЕЗ ИЗМЕНЕНИЙ

- Pre-Write Element Lock (Midjourney) — работает идеально
- SEED-TO-SLOT BINDING — структурный якорь
- IP Cliché Exception — умная логика
- Entry Angle Execution Guidance с ✅/❌ — образцово (только переместить в консолидированный блок)
- Rendering Tail Ban — ловит реальные проблемы
- Carrying Image Fidelity checks — критично для качества

---

## ВЕРСИОНИРОВАНИЕ

Предлагаю: эти изменения = **UPG v9.12**

Changelog:
```
v9.12:
- ADD: BAN REGISTRY (consolidated)
- ADD: ARCHITECTURE section (Zone/Phase explained)
- MOVE: Entry Angle → consolidated block
- RENAME: TEXT lens → TEXTURAL
- FIX: S5 TRACE verification logic
- SIMPLIFY: Stateful rules → soft preferences
- FORMAT: Feedback Protocol as table
- CLARIFY: Module combinations
- CLARIFY: CONCISE_MODE + TRACE interaction
- REMOVE: Decision Block line limits
- SYNC: Checklist relationship documented
```

---

**Конец служебной записки.**

Если нужны уточнения по любому пункту — запрашивай. Готов предоставить примеры "до/после" для любой секции.