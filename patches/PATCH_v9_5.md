# UPG v9.5 → v9.6 PATCH INSTRUCTIONS (FINAL)

---

## OVERVIEW

**Source:** Universal Prompt Generator v9.5
**Target:** Universal Prompt Generator v9.6
**Total Patches:** 10
**Validation:** 5 independent analyses + 22-output stress test

---

## PATCH 1: MIDJOURNEY MODE [P0 CRITICAL]

**Fixes:** Word count validation (Tier 1.1), Density incompatibility (Tier 2.2)

**Location:** Insert as new section AFTER `## INPUTS`, BEFORE `## OUTPUT PROTOCOL`

**INSERT:**

```markdown
---

## MIDJOURNEY MODE

**Activation:** When PLATFORM = Midjourney, ALL rules below override standard behavior.

### Sentence Limits (replaces word counting)
| Slot | Max Sentences | Max Elements |
|------|---------------|--------------|
| S1-S4 | 3 | 5 |
| S5 | 4 | 5 |

**Element definition:** Primary subject, key material/surface, light source, setting anchor, one secondary detail. No more than 5 per slot.

### Pre-Write Element Lock
Before writing each slot, silently identify:
1. [Primary subject]
2. [Material/surface]
3. [Light source]
4. [Setting anchor]
5. [Secondary detail — optional]

Write ONLY these elements. Adding more causes generation failure.

### Compression Rules
- One idea per sentence
- No stacked prepositions ("A on B beside C under D")
- No rendering phrases (glazed wash, impasto, canvas weave)
- Camera specs allowed but minimal (just "85mm f/2" not full description)

### Module Limits (Midjourney)
- **Module A active:** Format + 2 text zones + 1 copy line only
- **Module B active:** Size + closure + label only (skip compliance unless food/cosmetic)
- **Module A + B simultaneous:** Choose primary module, reduce secondary to 1 element

### Verification (Midjourney only)
After each slot, print:
`[S[n]: [X] sentences, [Y] elements — PASS]`

If >3 sentences (S1-S4) or >4 sentences (S5) or >5 elements: rewrite before proceeding.

### What NOT To Do (Midjourney)
- ❌ Count words
- ❌ Print word counts
- ❌ Use rendering execution phrases
- ❌ Stack 6+ visual elements
- ❌ Write sentences >25 words

---
```

---

## PATCH 2: REMOVE WORD COUNT ARITHMETIC [P1 HIGH]

**Fixes:** Self-verification arithmetic failure (Tier 1.2)

**Location:** Section `A.2 Mandatory Quality Rules`, Rule 6

**FIND:**

```markdown
   **Word Count Verification (print for Midjourney only):**
   When PLATFORM = Midjourney:
   After each slot, print exactly one line: `[S[n] words: [count] / limit: [limit] — PASS]`

   Rewrite silently until slot passes. Never print FAIL lines or intermediate counts. One PASS line per slot, nothing else.

   For other platforms: word counts remain silent, but non-compliance still blocks output. Treat word limit violation as equivalent to Zero Tolerance Ban violation — the slot cannot proceed to output until the violation is fixed. A slot that exceeds its platform word limit has failed Priority 1 and must be rewritten before any other processing continues.
```

**REPLACE WITH:**

```markdown
   **Length Control:**
   
   Word counting by LLMs is unreliable. Use sentence count as proxy:
   
   | Platform | Sentences per Slot | Guideline |
   |----------|-------------------|-----------|
   | Midjourney | 3 (S1-S4), 4 (S5) | See MIDJOURNEY MODE |
   | SD/SDXL | 3-5 | Natural paragraph length |
   | Flux/Aurora | 4-6 | Rich description permitted |
   | Unspecified | 4-5 | Default range |
   
   If a prompt feels too long, remove the least essential sentence.
   
   **Do NOT:**
   - Count words
   - Print word counts
   - Report word-based PASS/FAIL
   
   The only length verification is sentence count for Midjourney (see MIDJOURNEY MODE).
```

---

## PATCH 3: SIMPLIFY LENS MATCH CHECK [P1 HIGH]

**Fixes:** Arithmetic failure (Tier 1.2), Stochastic revision (Tier 2.4)

**Location:** Section `A.3 Slot Architecture`, block `LENS SEQUENCE DIVERSITY CHECK`

**FIND:**

```markdown
**LENS SEQUENCE DIVERSITY CHECK (FULL ARC or Module D active, mandatory print):**
Before finalizing slot plan, print in Decision Block:
```
Lens sequence: [S1] → [S2] → [S3] → [S4] → [S5]
Example sequence: PHOTOREALISTIC → CINEMATIC → TEXTURAL → PAINTERLY → ENVIRONMENTAL
Match count vs example: [N]/5 — must be ≤2
Previous theme sequence: [list or N/A if first theme]
Match count vs previous: [N]/5 — must be ≤3
S1+S2 anchor: [S1 lens] + [S2 lens] — if PHOTOREALISTIC + CINEMATIC: ANCHOR MATCH
Status: [PASS / REVISE — select different lenses]
```
If match vs example >2: change ≥3 lenses from example sequence.
If match vs previous >3: change ≥2 lenses from previous sequence.
If ANCHOR MATCH (S1=PHOTOREALISTIC and S2=CINEMATIC): select different lens for S1 or S2.
Reprint until PASS.
```

**REPLACE WITH:**

```markdown
**LENS SEQUENCE DIVERSITY CHECK (FULL ARC or Module D active):**

Before finalizing slot plan, verify these rules:

1. **S1 ≠ S2:** First two slots must use different lenses
2. **Max 2 repeats:** No lens appears more than twice in sequence
3. **No PHOTOREALISTIC + CINEMATIC anchor:** If S1=PHOTOREALISTIC and S2=CINEMATIC, change one
4. **Not identical to example:** Sequence must NOT be PHOTOREALISTIC → CINEMATIC → TEXTURAL → PAINTERLY → ENVIRONMENTAL

Print in Decision Block:
```
Lens sequence: [S1] → [S2] → [S3] → [S4] → [S5] — DIVERSITY CHECK: [PASS/REVISE]
```

If REVISE: select different lenses and reprint until PASS.

**Do NOT print:**
- Match counts
- Arithmetic comparisons
- Multiple status lines
```

---

## PATCH 4: POST-REVISION LOCK [P2 HIGH]

**Fixes:** Decision Block → Prompt propagation gap (Tier 1.3)

**Location:** Section `PHASE 5 — PROMPT WRITING`, beginning of `5.1 Writing Process`

**INSERT AS NEW STEP 0 (before existing step 1):**

```markdown
0. **Post-Revision Lock (MANDATORY if any REVISE occurred):**
   
   If the Decision Block contains "REVISE" anywhere (lens sequence, contrast, etc.), you MUST print this lock before writing any prompts:
   
   ```
   ═══ FINAL BINDING (post-revision) ═══
   S1: [lens] | [framing] | [Entry Angle type]: [specific element]
   S2: [lens] | [framing] | [Entry Angle type]: [specific element]  
   S3: [lens] | [framing] | Seed 1 element: [specific element]
   S4: [lens] | [framing] | Seed 2 element: [specific element]
   S5: [lens] | [framing] | Seed 3/trace: [specific element]
   ═══════════════════════════════════════
   ```
   
   Write ALL prompts from FINAL BINDING values, not from pre-revision assignments.
   
   **Verification:** After writing S1, check: does the prompt execute the lens shown in FINAL BINDING? If not, rewrite before proceeding to S2.
```

---

## PATCH 5: "AS THOUGH" FIRST-LINE CHECK [P3 MEDIUM]

**Fixes:** Ban list miss (Tier 2.3)

**Location:** Section `A.2 Mandatory Quality Rules`, Rule 9, Zero Tolerance Bans

**FIND the table row:**

```markdown
   | "as if" / "as though" / "might" / "could" / "would" in descriptive context (introduces hypothetical, not visible)
```

**REPLACE WITH:**

```markdown
   | "as if" / "as though" | Rewrite as visible physical state. Example: "as though tiles softened" → "tiles carry frozen wave ridges and trapped air pockets" |
```

**THEN ADD after the Zero Tolerance Bans table:**

```markdown
   **FIRST-LINE SCAN (mandatory for "as if" / "as though"):**
   
   These phrases are the most frequently missed. Before outputting ANY slot:
   1. Scan final draft for "as if" or "as though"
   2. If found anywhere: STOP
   3. Rewrite the clause to describe visible physical evidence
   4. Re-scan before output
   
   Common failure pattern:
   - ❌ "as though the surface had melted and refrozen"
   - ✅ "the surface carries rippled ridges and trapped bubbles in its hardened glaze"
   
   The test: can a camera see "as though"? No. Rewrite to what the camera CAN see.
```

---

## PATCH 6: INSTITUTIONAL COUNTER [P4 LOW]

**Fixes:** Ceiling tracking (Tier 5.1)

**Location:** Section `4.1 Seed Generation`, under `SEED 2 CONTEXT DIVERSITY`

**FIND:**

```markdown
After generating Seed 2, print in Decision Block:
```
Seed 2 context: [location description]
Context type: [INSTITUTIONAL / NON-INSTITUTIONAL]
Previous 2 Seed 2 types: [list or N/A]
Status: [OK / CEILING REACHED — regenerate with non-institutional frame]
```
```

**REPLACE WITH:**

```markdown
After generating Seed 2, print in Decision Block:
```
Seed 2 context: [location description]
Context type: [INSTITUTIONAL / NON-INSTITUTIONAL]
```

**Ceiling Rule:** Count institutional Seed 2 contexts in last 3 FULL ARC themes:
- 0 or 1 institutional: OK, proceed
- 2 institutional: CEILING — regenerate with non-institutional context

If uncertain whether a context is institutional, choose non-institutional.

Institutional contexts: museum, archive, evidence room, storage facility, records office, specimen storage, cataloging station, municipal documentation.

Non-institutional alternatives: field sites, workshops, backstage areas, transit spaces, domestic interiors, commercial venues, natural settings.
```

---

## PATCH 7: "ECHOES" BAN [P4 LOW]

**Fixes:** Metaphorical verbs (Tier 5.3)

**Location:** Section `A.2 Mandatory Quality Rules`, Rule 9, add to "Additional banned constructions"

**ADD:**

```markdown
   - "echoes" / "mirrors" / "reflects" (metaphorical use — describing conceptual relationship, not literal reflection)
   
   Test: Is there an actual mirror or reflective surface creating a literal reflection? If NO, rewrite.
   
   - ❌ "the red ring echoes the bottle's earlier use"
   - ✅ "a faint red ring on the card matches the diameter of the bottle's base"
   
   - ❌ "the composition mirrors the chaos of the event"  
   - ✅ "scattered papers and overturned chairs fill the frame"
```

---

## PATCH 8: CONTRAST CHECK SIMPLIFICATION [P4 LOW]

**Fixes:** Decorative arithmetic (Tier 5.5)

**Location:** Section `A.5 Universal Prompt Structure`, under `Contrast Tracking`

**FIND:**

```markdown
**Contrast Tracking (printed, mandatory after all 5 slots drafted):**
After completing all 5 slot drafts, print:
```
Contrast: S1=[H/M/L] S2=[H/M/L] S3=[H/M/L] S4=[H/M/L] S5=[H/M/L] | H:[n] M:[n] L:[n] — [PASS/REVISE]
```
If any count >2: print REVISE, revise slot where contrast change is most natural, reprint until PASS.

This check is PRINTED, not silent. Printing enables verification and self-correction.
```

**REPLACE WITH:**

```markdown
**Contrast Tracking:**

Rule: No contrast level (HIGH / MEDIUM / LOW) may appear more than twice across 5 slots.

**While writing (not after):**
- Before S3: Have you used HIGH twice? If yes, S3-S5 must be MEDIUM or LOW only.
- Before S4: Check distribution. Adjust if any level would exceed 2.
- Before S5: Final check. Change S5 contrast if needed to satisfy rule.

**Safe patterns (use as guides):**
- H-M-L-M-H ✓
- M-H-L-H-M ✓
- H-M-H-L-M ✓
- L-M-H-M-L ✓

**Do NOT print:**
- Contrast counts
- Arithmetic tallies
- Post-draft verification blocks

Apply the rule while writing. If final series violates max-2, revise the most flexible slot.
```

---

## PATCH 9: RENDERING CHECK SIMPLIFICATION [P4 LOW]

**Fixes:** Decorative count (Tier 5.4)

**Location:** Section `A.4 Creative Lenses`, under `Rendering Check`

**FIND:**

```markdown
**Rendering Check (non-photographic media, mandatory print in Decision Block):**
When Medium is painting, illustration, or concept art, print in Decision Block:
```
Rendering: S1=[phrase/—] S2=[phrase/—] S3=[phrase/—] S4=[phrase/—] S5=[phrase/—] | Count: [n]/5 — [PASS if ≥3 / REVISE]
```
If count <3: add rendering phrase to slot where most natural, reprint until PASS.
```

**REPLACE WITH:**

```markdown
**Rendering Execution (non-photographic media):**

When Medium is painting, illustration, or concept art:
- Include a rendering phrase in at least 3 of 5 slots
- Natural slots: S1 (establish style), S4 (PAINTERLY often assigned), S5 (final impression)
- PAINTERLY lens automatically satisfies requirement (brushwork IS rendering)

Place rendering phrase near end of slot, integrated into description.

**Do NOT print:**
- Rendering counts
- Slot-by-slot rendering tallies
- Count verification

Apply while writing. If draft has <3 rendering phrases, add to the most natural slot before output.
```

---

## PATCH 10: BIDIRECTIONAL MEDIUM-LENS RECONCILIATION [P2 MEDIUM]

**Fixes:** Lens/Medium ontological collision (Tier 2.1)

**Location:** Section `A.4 Creative Lenses`, AFTER existing `MEDIUM-LENS RECONCILIATION` block

**ADD NEW BLOCK:**

```markdown
**PHOTOGRAPHY-LENS RECONCILIATION (reverse direction):**

When Medium = photography AND assigned Lens is PAINTERLY, GRAPHIC, or SYMBOLIC:

**Do NOT use these terms:**
- dry-brush, impasto, canvas weave, wash layers, glazed layers
- vector edges, ruled edges, diagrammatic
- any painting/illustration material terminology

**DO translate Lens to photographic equivalents:**

| Lens | Photography Translation |
|------|------------------------|
| PAINTERLY | Soft pictorialist focus, warm halation, shallow DOF, Lensbaby blur, golden-hour diffusion, Orton effect glow |
| GRAPHIC | Harsh direct flash, high-contrast silhouette, flat frontal lighting, orthographic compression, strong shape separation |
| SYMBOLIC | Spare composition, centered framing, dominant negative space, single isolated object, minimal depth layers |

**Verification test:** If prompt contains BOTH an f-stop AND a painting technique name → reconciliation failed. Rewrite painting term as photographic equivalent.

Example:
- ❌ "85mm f/2.8, dry-brush grain across the wooden surface"
- ✅ "85mm f/2.8, soft pictorialist glow across the wooden surface"

This rule ensures the Lens defines VISUAL OUTCOME, not physical medium. A "Painterly" photograph achieves softness through optics, not paint.
```

---

## VERSION HEADER UPDATE

**Location:** Very top of prompt

**FIND:**

```markdown
# UNIVERSAL PROMPT GENERATOR v9.5

<!-- v9.4 Changes: ... -->

<!-- v9.5 Changes: ... -->
```

**REPLACE WITH:**

```markdown
# UNIVERSAL PROMPT GENERATOR v9.6

<!-- v9.4 Changes: ... -->

<!-- v9.5 Changes: ... -->

<!-- v9.6 Changes: Added MIDJOURNEY MODE with sentence-count proxy and 5-element limit; removed all word count arithmetic; simplified lens diversity check to binary rules; added POST-REVISION LOCK for propagation integrity; strengthened "as though"/"as if" with first-line scan; added "echoes"/"mirrors"/"reflects" to metaphorical verb ban; simplified contrast and rendering checks; added bidirectional Medium-Lens reconciliation for photography contexts; explicit institutional ceiling counter. -->
```

---

## APPLICATION ORDER

```
PHASE 1: CRITICAL (do first, in order)
│
├── 1. Patch 1 (MIDJOURNEY MODE) — new section
├── 2. Patch 2 (Word Count Removal) — depends on Patch 1 reference
├── 3. Patch 3 (Lens Check Simplification) — independent
└── 4. Patch 4 (POST-REVISION LOCK) — independent

PHASE 2: IMPORTANT (do after Phase 1)
│
├── 5. Patch 5 ("as though" scan) — independent
└── 6. Patch 10 (Bidirectional Reconciliation) — independent

PHASE 3: POLISH (do when convenient)
│
├── 7. Patch 6 (Institutional Counter) — independent
├── 8. Patch 7 ("echoes" ban) — independent
├── 9. Patch 8 (Contrast Simplification) — independent
└── 10. Patch 9 (Rendering Simplification) — independent

FINAL: Version header update — do last
```

---

## POST-PATCH VERIFICATION

Run these tests after applying all patches:

### Test A: Midjourney Mode
```
THEME: Victorian greenhouse containing a Japanese garden inside an abandoned submarine
PLATFORM: Midjourney
TRACE: true
```
**Expected:** 3-sentence slots, 5-element max, sentence/element count printed, no word counts

### Test B: Revision Propagation
```
THEME: wristwatch
```
**If ANCHOR MATCH or other REVISE triggers:** FINAL BINDING block must appear before prompts, and prompts must match FINAL BINDING lenses

### Test C: Photography + PAINTERLY
```
THEME: still life with fruit
CONTEXT: ARTISTIC
MEDIUM: photography
```
**Assign PAINTERLY to one slot.** That slot must contain "soft focus" / "halation" / "pictorialist" — NOT "dry-brush" / "canvas weave"

### Test D: Ban Detection
```
THEME: abandoned factory
```
**Verify:** No slot contains "as though," "as if," "echoes," "mirrors," or "reflects" (metaphorical)

---

## WHAT NOT TO TOUCH

These mechanisms work correctly — preserve exactly:

| Mechanism | Location | Why Preserve |
|-----------|----------|--------------|
| Entry Angle Rotation | B.2 Step 6 | 100% execution compliance |
| Seed-to-Slot Binding | 4.2 | Perfect slot differentiation |
| Zero Tolerance Ban List | A.2 Rule 9 | 99% enforcement rate |
| Module A/B/C/D Logic | Zone C | 100% compliance |
| Safety Scan | B.0 | Zero violations |
| TRUE ABSENCE Technique | A.3 FULL ARC S5 | Excellent trace descriptions |
| Cliché Blacklist | B.2 Step 1 | Effective prevention |
| Adjacent Slot Uniqueness | A.2 Rule 7 | Working correctly |

---

**END OF PATCH INSTRUCTIONS v9.6**