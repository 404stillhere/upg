ПРОМПТ-ИНСТРУКЦИЯ v8.5 → v8.6
ПРЕАМБУЛА ДЛЯ ИСПОЛНИТЕЛЯ
Ты получишь текст промпта Universal Prompt Generator v8.5. Твоя задача — внести 4 точечных исправления строго по инструкциям ниже.

Правила работы:

Вноси ТОЛЬКО указанные изменения
НЕ меняй ничего другого — даже если кажется, что можно улучшить
Сохраняй форматирование, стиль, отступы оригинала
После всех изменений выведи полный текст обновлённого промпта
КРИТИЧЕСКИ ВАЖНО: НЕ ТРОГАТЬ
Следующие элементы работают корректно. НЕ ИЗМЕНЯЙ их ни при каких обстоятельствах:

Zero Tolerance Bans Table (секция A.2 Rule 9)
Abstract noun ban включая Modifier trap
Final Sentence Content Rule + Non-photography extension
Environmental Departure Rule
Metaphor Family Check с printed verification
Module A + Module D interaction rules
COMMERCIAL + MODE 2 S5 Conversion Rule
Entry Angle First-Sentence Lock и Entry Angle Execution Rule
ИСПРАВЛЕНИЕ #1: Theme Position Detection
Где: Секция A.4 Creative Lenses → подсекция "CONVERSATION TRACKING (lens sequences + entry angles):"

Найди этот текст:

text

**CONVERSATION TRACKING (lens sequences + entry angles):**
Track themes sequentially per session. First theme = Theme A, second = Theme B,
third = Theme C, fourth = Theme D; loop back to A after D. Reset to Theme A if
user explicitly restarts the workflow. The Entry Angle Rotation Rule is active by default within a session and resets to Theme A only when the user explicitly restarts the workflow or a new session begins. If context is unclear, treat current as Theme A.

On loop repeat (Theme A₂, B₂, etc.), lens sequence must also differ
from the previous cycle's lens sequence for the same theme position.
Действие: ЗАМЕНИТЬ ПОЛНОСТЬЮ на:

text

**CONVERSATION TRACKING (lens sequences + entry angles):**
Track themes sequentially per session. First theme = Theme A, second = Theme B,
third = Theme C, fourth = Theme D; loop back to A after D. Reset to Theme A if
user explicitly restarts the workflow. The Entry Angle Rotation Rule is active by default within a session and resets to Theme A only when the user explicitly restarts the workflow or a new session begins.

**Theme Position Detection (MANDATORY):**

Count THEME inputs sequentially within this conversation:
- 1st THEME input → Theme A
- 2nd THEME input → Theme B
- 3rd THEME input → Theme C
- 4th THEME input → Theme D
- 5th THEME input → Theme A₂ (cycle repeats)

**Definition:** A new THEME input is any user message requesting generation for a new subject, topic, or concept. Feedback on previous output, parameter adjustments, or clarification requests for the SAME theme do NOT increment the counter.

Each new THEME input increments the counter by exactly 1. Do NOT reset to Theme A unless user explicitly writes "restart workflow" or "reset to Theme A."

**Before selecting Entry Angle, print in Decision Block:**
`Theme position: [N]th THEME in conversation → Theme [A/B/C/D]`

If this line is missing from Decision Block, count THEME inputs from conversation start and add the line before proceeding to Entry Angle selection.

On loop repeat (Theme A₂, B₂, etc.), lens sequence must also differ
from the previous cycle's lens sequence for the same theme position.
ИСПРАВЛЕНИЕ #2: Platform Word Limit в Priority 1
Где: Секция HARD CHECKS (MANDATORY — RUN FOR EACH SLOT) → подсекция PRIORITY 1 — NON-NEGOTIABLE

Найди этот текст:

text

4. **Banned Phrases:** Check against System Banned Phrases list (12 items in section 5.1). If found → rewrite.

**If ANY Priority 1 check fails → rewrite slot before proceeding to Priority 2.**
Действие: ЗАМЕНИТЬ на:

text

4. **Banned Phrases:** Check against System Banned Phrases list (12 items in section 5.1). If found → rewrite.

5. **Platform Word Limit (when PLATFORM specified):** Count words in completed slot. Compare to platform limit:
   - Midjourney: ≤60 words (≤80 with Module A or B active)
   - SD/SDXL: ≤75 words
   - Flux/Aurora: default ranges apply
   
   If slot exceeds limit by ANY amount, apply Compression Priority and rewrite until compliant. **Platform word limit is NEVER negotiable** — no exception for module checklist completeness, prose quality, or any other requirement. If all sacrificeable elements are minimal and slot still exceeds limit, compress module elements to compact clause form (e.g., "kraft box, 200ml, twist-cap, organic badge").

**If ANY Priority 1 check fails → rewrite slot before proceeding to Priority 2.**
ИСПРАВЛЕНИЕ #3: Post-Write Verification Hard Enforcement
Где: Секция A.2 Mandatory Quality Rules → Rule 6 (Word count) → подсекция Post-Write Verification

Найди этот текст:

text

   **Post-Write Verification (mandatory):**
   After completing each slot draft, count actual words. If count exceeds
   platform limit, apply Compression Priority until compliant. Do not
   output any slot that exceeds its platform word limit. This check is
   silent; never print word counts or budget calculations in output.
Действие: ЗАМЕНИТЬ на:

text

   **Post-Write Verification (HARD ENFORCEMENT):**
   After completing each slot draft:
   1. Count actual words in the slot
   2. Compare to platform limit (if PLATFORM specified) or default range
   3. If count exceeds limit → STOP output, apply Compression Priority, rewrite the slot
   4. Re-count after rewrite
   5. Repeat steps 3–4 until slot is compliant
   
   Word counts are not printed in output, but **non-compliance BLOCKS output**. Treat word limit violation as equivalent to Zero Tolerance Ban violation — the slot cannot proceed to output until the violation is fixed. A slot that exceeds its platform word limit has failed Priority 1 and must be rewritten before any other processing continues.
ИСПРАВЛЕНИЕ #4: Long Theme Enrichment Rule
Где: Секция B.2 Theme Enrichment & Cliché Blacklist → STEP 2 — Enrich: → последний bullet point в списке

Найди этот текст:

text

- If theme is already highly specific (>100 words or extremely detailed), apply the
  relevant enrichment rule above in 1 sentence only. Do not narrow unnecessarily.
Действие: ЗАМЕНИТЬ на:

text

- **Highly Specific Theme Rule (>100 words):**
  If THEME input exceeds 100 words, enrichment must be **exactly 1 sentence** containing only:
  - The carrying image identification
  - The physical coherence principle (how the transformed world behaves)
  
  Do not add texture, tension sources, or structural guidance beyond this single sentence. For highly specific themes, the theme itself IS the enrichment — your job is to identify the carrying image, not to expand.
  
  **Verification:** Count sentences in Enriched theme. If THEME >100 words and Enriched theme >1 sentence, rewrite Enriched theme to single sentence before proceeding.
ВЕРИФИКАЦИЯ
После внесения всех изменений проверь:

#	Что проверить	Ожидаемый результат
1	Секция CONVERSATION TRACKING	Содержит новый блок "Theme Position Detection (MANDATORY)" с printed verification line
2	Hard Checks Priority 1	Содержит 5 пунктов (был 4), пятый — Platform Word Limit с "NEVER negotiable"
3	Rule 6 Post-Write Verification	Заголовок "(HARD ENFORCEMENT)", содержит 5-step process, содержит "BLOCKS output"
4	STEP 2 — Enrich	Последний bullet содержит "exactly 1 sentence" и verification instruction
ПОРЯДОК ВНЕДРЕНИЯ
Исправление #1 — независимое, можно первым
Исправление #2 — независимое, можно параллельно с #1
Исправление #3 — дополняет #2, делать после или вместе с #2
Исправление #4 — независимое, можно в любом порядке