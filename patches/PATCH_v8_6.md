# PROMPT INSTRUCTION: v8.6 → v8.7

## CONTEXT FOR EXECUTOR

You are receiving the Universal Prompt Generator v8.6 prompt for targeted fixes. You have NOT seen the original prompt before. You will receive:
1. This instruction document (what to change)
2. The full v8.6 prompt text (separately)

Your task: Apply exactly the fixes described below. Do not make other changes. Preserve all unmarked sections exactly as they are.

---

## WHAT WORKS AND MUST NOT BE CHANGED

Before making any changes, understand these elements are functioning correctly and must be preserved exactly:

| Element | Location | Why Protected |
|---------|----------|---------------|
| Zero Tolerance Bans Table | A.2 Rule 9 | 100% compliance across all tests |
| Metaphor Family Check (printed) | Phase 4.1 Seed Generation | Proven accountability pattern |
| Module B Four Minimums | Zone C, Module B | 100% compliance |
| Entry Angle First-Sentence Lock | B.2 Step 6 | Works when counter is correct |
| Final Sentence Content Rule | A.2 Rule 9 | 100% compliance |
| Abstract Noun Ban + Modifier Trap | A.2 Rule 9 | 100% compliance |
| Feedback Adjustment Protocol | End of prompt | Works correctly |
| Theme Position Detection (existing) | A.4 Creative Lenses | Keep existing — we ADD to it |

---

## FIX #1: Add Rerun Detection Block

**Priority:** Critical

**Action:** ADD new block

**Location:** Insert IMMEDIATELY AFTER the existing "Theme Position Detection (MANDATORY)" block in section A.4 Creative Lenses, BEFORE "On loop repeat (Theme A₂, B₂, etc.)..."

**Insert this exact text:**

```
**RERUN DETECTION (MANDATORY):**

Before generating, compare current THEME text to all previous THEME texts in this conversation.

**If current THEME text matches any previous THEME exactly or near-exactly:**

1. Print in Decision Block: `RERUN DETECTED of theme from position [N] — applying diversity rule`

2. Apply diversity requirements:
   - Choose a DIFFERENT anchor object for carrying image
   - Generate a DIFFERENT subject for Seed 1
   - Use a DIFFERENT specific location for S1
   - Select a DIFFERENT lens sequence

3. Print diversity verification in Decision Block:
   ```
   Previous run: [anchor] / [Seed 1 subject] / [S1 location]
   This run: [new anchor] / [new Seed 1 subject] / [new S1 location]
   ALL DIFFERENT: [YES/NO]
   ```

4. If ANY element matches previous run, rewrite before proceeding.

Treat theme repetition as a request for creative variation, not consistency.
```

**Verification after fix:**
- Correct: New block appears between "Theme Position Detection" and "On loop repeat"
- Correct: Block contains "RERUN DETECTED" print instruction and diversity verification format

---

## FIX #2: Add Rerun Counting Clarification

**Priority:** Critical

**Action:** ADD clarification text

**Location:** Inside the existing "Theme Position Detection (MANDATORY)" block, INSERT immediately after the paragraph that begins "**Definition:** A new THEME input is any user message..."

**Find this text:**
```
**Definition:** A new THEME input is any user message requesting generation for a new subject, topic, or concept. Feedback on previous output, parameter adjustments, or clarification requests for the SAME theme do NOT increment the counter.
```

**Insert this text IMMEDIATELY AFTER that paragraph:**

```
**Rerun Counting Clarification:**
A rerun (identical or near-identical THEME text resubmitted) DOES increment the counter. Each generation request counts as a new THEME input regardless of text similarity.

Example sequence:
- 1st submission of "X" = Theme A (1st THEME)
- Feedback on "X" = no increment (not a generation request)
- 2nd submission of "X" (rerun) = Theme B (2nd THEME)
- 1st submission of "Y" = Theme C (3rd THEME)

Do NOT reset counter when THEME text repeats. The counter tracks GENERATION REQUESTS, not unique theme concepts.
```

**Verification after fix:**
- Correct: "Rerun Counting Clarification" appears immediately after "Definition" paragraph
- Correct: Example sequence shows rerun incrementing counter (X→A, X again→B, Y→C)

---

## FIX #3: Add Printed Word Count Verification for Midjourney

**Priority:** Medium

**Action:** REPLACE one sentence

**Location:** Section A.2 Rule 6 → "Post-Write Verification (HARD ENFORCEMENT)"

**Find this exact sentence:**
```
Word counts are not printed in output, but **non-compliance BLOCKS output**.
```

**Replace with:**
```
**Word Count Verification (print for Midjourney only):**
When PLATFORM = Midjourney:
After completing each slot, print: `[S[n] words: [count] / limit: [limit] — [PASS/FAIL]]`

If FAIL: apply Compression Priority, rewrite, recount, print new verification.
Do not proceed to next slot until current slot shows PASS.

For other platforms: word counts remain silent, but non-compliance still blocks output.
```

**Verification after fix:**
- Correct: Old sentence removed
- Correct: New block contains print instruction with format `[S[n] words: [count] / limit: [limit] — [PASS/FAIL]]`
- Correct: Specifies "Midjourney only" and "other platforms: silent"

---

## SUMMARY OF CHANGES

| Fix | Action | Location | Lines Added |
|-----|--------|----------|-------------|
| #1 | ADD block | After Theme Position Detection | ~20 lines |
| #2 | ADD paragraph | Inside Theme Position Detection, after Definition | ~10 lines |
| #3 | REPLACE sentence | Post-Write Verification section | ~8 lines (net +6) |

**Total changes:** 3 targeted insertions/replacements
**Sections NOT changed:** Everything else

---

## OUTPUT FORMAT

After applying fixes, output the complete v8.7 prompt with:
1. Header changed to `# UNIVERSAL PROMPT GENERATOR v8.7`
2. All three fixes applied in their exact locations
3. All other content preserved exactly as in v8.6

Do not summarize or explain. Output only the complete updated prompt.