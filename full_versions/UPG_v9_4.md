# UNIVERSAL PROMPT GENERATOR v9.4 → v9.5 PATCH INSTRUCTIONS

---

## OVERVIEW

This document contains 7 surgical fixes to be applied to Universal Prompt Generator v9.4. Each fix is self-contained with exact location, current text, and replacement text. Apply in order listed.

---

## FIX #1: Extend Lens Sequence Diversity Check Scope

**Priority:** HIGH

**Location:** Section A.3, inside FULL ARC block, find the heading "LENS SEQUENCE DIVERSITY CHECK"

**FIND:**
```
**LENS SEQUENCE DIVERSITY CHECK (FULL ARC, mandatory print):**
```

**REPLACE WITH:**
```
**LENS SEQUENCE DIVERSITY CHECK (FULL ARC or Module D active, mandatory print):**
```

**Rationale:** Module D creates arc-like narrative progression even within SHALLOW ARC contexts. This ensures lens diversity validation runs for MODE=2 poster series, packaging narratives, and any Module D activation regardless of base arc depth label.

---

## FIX #2: Expand Obliqueness Threshold Examples

**Priority:** MEDIUM

**Location:** Section 4.1 Seed Generation, inside "Obliqueness Test" block

**FIND:**
```
FAIL (first-ring, obvious): watch → repair shop; wine → dinner table; typewriter → writer's desk; coffee → café
FAIL (second-ring, institutional): watch → museum display; wine → cellar inventory; typewriter → archive shelf; coffee → evidence bag

PASS (third-ring, oblique): watch → geological core sample display in field research tent; wine → theatrical prop table backstage with masking tape labels; typewriter → shipping container manifest board in cargo yard; coffee → weather station logbook shelf in remote alpine hut
```

**REPLACE WITH:**
```
FAIL (first-ring, obvious): watch → repair shop; wine → dinner table; typewriter → writer's desk; coffee → café
FAIL (second-ring, institutional): watch → museum display; wine → cellar inventory; typewriter → archive shelf; coffee → evidence bag
FAIL (second-ring, municipal/infrastructure): watch → city records basement; wine → health inspection lab; typewriter → transit authority office; coffee → airport security checkpoint

PASS (third-ring, oblique): watch → geological core sample display in field research tent; wine → theatrical prop table backstage with masking tape labels; typewriter → shipping container manifest board in cargo yard; coffee → weather station logbook shelf in remote alpine hut; watch → veterinary surgery prep table; wine → film continuity supervisor's clipboard station; typewriter → radio telescope control room logbook desk; coffee → lighthouse keeper's morning duty station
```

**Rationale:** Adding explicit municipal/infrastructure FAIL examples closes the ambiguity gap. Expanding PASS examples to 8 total provides stronger pattern recognition. Distinction is now clear: formal custody = FAIL; active working environment = PASS.

---

## FIX #3: Add Module D Slot Plan Vocabulary Rule

**Priority:** HIGH

**Location:** Zone C — MODULES, at the END of Module D section (after the letter example), BEFORE "Module Interaction Priority" or HARD CHECKS

**FIND:**
```
[End of Module D section - insert new block here]
```

**INSERT:**
```
**SLOT PLAN VOCABULARY FOR MODULE D:**
When Module D is active (regardless of arc depth label), use Module D role vocabulary in the slot plan:
- S1: ANCHOR (element intact)
- S2: INTERACTION (active use)
- S3: TRANSFORMATION (wear/change visible)
- S4: REPURPOSE (unexpected context)
- S5: RUPTURE (trace only) — unless CONTEXT = COMMERCIAL, then CONVERSION with trace element permitted

This ensures the planning layer accurately predicts actual output structure. When writing the Slot plan field in Decision Block, use these role names if Module D is active.
```

**Rationale:** Prevents planning/output mismatch where slot plan says "CONVERSION" but actual S5 delivers "RUPTURE." Users now see accurate prediction of what each slot will contain.

---

## FIX #4: Expand SENSORY Lens Execution Guidance

**Priority:** MEDIUM

**Location:** Section A.4 Creative Lenses table, SENSORY row

**FIND:**
```
| SENSORY | Non-visual sense dominates | Touch / sound / temperature implied by visuals | Synaesthetic detail — texture implies sound, surface implies temperature. |
```

**REPLACE WITH:**
```
| SENSORY | Non-visual sense dominates | Touch / sound / temperature implied by visuals | Synaesthetic detail — texture implies sound (vibration marks, resonance geometry, acoustic dampening surfaces), surface implies temperature (condensation beads, frost crystals, heat shimmer, thermal warping), material implies smell (residue gloss, oxidation bloom, fermentation bubbles, oil sheen). Include at least one explicit synaesthetic marker per SENSORY slot. |
```

**Rationale:** Concrete marker examples for each sense type give the model recognizable patterns. The "at least one per slot" requirement creates accountability. SENSORY lens now clearly distinguishable from TEXTURAL.

---

## FIX #5: Add Enrichment Vocabulary Rule for Reruns

**Priority:** MEDIUM

**Location:** After the existing "RERUN DIVERSITY RULE" paragraph (in the section before FEEDBACK ADJUSTMENT PROTOCOL)

**FIND:**
```
[End of RERUN DIVERSITY RULE paragraph - insert new block here]
```

**INSERT:**
```
**ENRICHMENT VOCABULARY RULE (reruns only):**
When rerunning the same theme, the Enriched theme text must NOT reuse structural phrases from the previous run. Specifically:
- Do not copy sentence structures ("remains legible through," "shaped by," "marked by long")
- Use different material category vocabulary (if previous used "leather fatigue," use "hide degradation" or "tanned surface breakdown")
- Use different structural framing (if previous focused on "hardware and shell," focus on "frame and closure" or "stitching and corner reinforcement")

The enrichment should read as genuine reinterpretation, not reformatted previous enrichment. If three or more words from previous enrichment appear in sequence, rewrite before proceeding.
```

**Rationale:** Extends structural diversity rule to prose level. The "three words in sequence" test provides concrete threshold for detecting copying. Reduces vocabulary fatigue across multiple runs of same theme.

---

## FIX #6: Clarify Rendering Check Placement

**Priority:** LOW

**Location:** Section A.4 Creative Lenses, find "Rendering Check" block

**FIND:**
```
**Rendering Check (non-photographic media, printed):**
After completing all 5 slot drafts, print:
```

**REPLACE WITH:**
```
**Rendering Check (non-photographic media, mandatory print in Decision Block):**
When Medium is painting, illustration, or concept art, print in Decision Block:
```

**Rationale:** "Mandatory print in Decision Block" aligns instruction with natural generation flow (planning content generated together). Removes ambiguity about placement timing.

---

## FIX #7: Add S1/Seed 1 Location Separation Check

**Priority:** LOW

**Location:** Immediately AFTER the new "ENRICHMENT VOCABULARY RULE" block from Fix #5

**INSERT:**
```
**S1/SEED 1 LOCATION SEPARATION:**
S1 location must differ from Seed 1 context. If initial generation places both in the same setting (same building type, same room category, same environmental class), revise Seed 1 to use a different environment before proceeding to slot writing. This prevents repetition between S1 and S3.

Print verification in Decision Block:
```
S1/SEED 1 LOCATION SEPARATION CHECK:
S1 location: [location]
Seed 1 context: [context]
Same setting? [YES/NO]
Status: [PASS / FAIL — revise Seed 1]
```
```

**Rationale:** Explicit separation check prevents collision where both S1 and S3 share the same environment. Printed verification creates accountability.

---

## VERIFICATION CHECKLIST

After applying all fixes, verify:

| Fix # | Test | Expected Result |
|-------|------|-----------------|
| 1 | Run Module A + Module D theme | Lens sequence check prints in Decision Block |
| 2 | Generate 5 Seed 2 contexts | No municipal/infrastructure settings appear |
| 3 | Run artistic + MODE 2 theme | Slot plan uses RUPTURE vocabulary for S5 |
| 4 | Force SENSORY lens | Synaesthetic markers (condensation, heat shimmer, etc.) present |
| 5 | Run same theme 3× | Enrichment vocabulary differs each run |
| 6 | Run illustration theme | Rendering check appears in Decision Block |
| 7 | Check S1/Seed 1 | Separation check printed, collision detected if present |

---

## VERSION UPDATE

After applying all fixes, update version marker:

**FIND (in document header or comment):**
```
<!-- v9.4 Changes:
```

**ADD NEW VERSION BLOCK:**
```
<!-- v9.5 Changes: Lens sequence check scope extended to include Module D; obliqueness threshold examples expanded with municipal/infrastructure FAIL tier; Module D slot plan vocabulary rule added; SENSORY lens execution guidance expanded with concrete synaesthetic markers; enrichment vocabulary variation rule added for reruns; rendering check placement clarified to Decision Block; S1/Seed 1 location separation check added. -->
```

---

## IMPLEMENTATION ORDER

Apply fixes in this sequence:

1. **Fix #1** — Lens check scope (no dependencies)
2. **Fix #3** — Module D vocabulary (no dependencies)
3. **Fix #6** — Rendering check placement (no dependencies)
4. **Fix #4** — SENSORY lens expansion (no dependencies)
5. **Fix #5** — Enrichment vocabulary rule (no dependencies)
6. **Fix #7** — S1/Seed 1 separation (place after Fix #5)
7. **Fix #2** — Obliqueness examples (no dependencies)

Fixes 1, 3, 6 can be applied in parallel.
Fixes 5 and 7 should be applied together (same section).

---

## SUMMARY

- **Total fixes:** 7
- **High priority:** 2 (Fixes #1, #3)
- **Medium priority:** 3 (Fixes #2, #4, #5)
- **Low priority:** 2 (Fixes #6, #7)
- **Expected improvement:** v9.4 (8.0/10) → v9.5 (9.0/10)