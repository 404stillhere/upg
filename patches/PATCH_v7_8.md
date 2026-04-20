# TASK

You are given the full text of UNIVERSAL PROMPT GENERATOR v7.8.
Perform ONLY the 10 edits described below.
Make NO other changes.
Do not fix grammar, do not rephrase, do not "improve".
If an instruction does not cover a fragment — do not touch it.

---

# EDIT 1: VERSION NUMBER

FIND: v7.8 (in the title)
REPLACE WITH: v7.9

This is the ONLY place where v7.8 appears. Change it once.

---

# EDIT 2: SEED GENERATION — SEED 2 DEFINITION (section 4.1)

FIND this exact bullet point:

- **Seed 2 (OBLIQUE):** Unexpected angle — surprising yet valid. Lesser-known facet, unusual scale,
  or unconventional context. Viewer identifies theme in <15 seconds.

REPLACE WITH:

- **Seed 2 (OBLIQUE):** Unexpected angle — surprising yet valid. Must use a DIFFERENT metaphor family than Seed 1. If Seed 1 uses organic/growth imagery, Seed 2 must NOT use organic/growth — choose instead from: mechanical, temporal, social, archival, geological, or sensory frames. If Seed 1 uses mechanical framing, Seed 2 must use organic, temporal, social, or other non-mechanical frame. The viewer should experience genuine conceptual surprise, not a continuation of Seed 1's direction at different scale. Lesser-known facet, unusual scale, or unconventional context. Viewer identifies theme in <15 seconds.

Do not modify any text before or after this bullet point.

---

# EDIT 3: SEED GENERATION — METAPHORICAL DISTANCE CHECK (section 4.1)

FIND this exact block:

**Metaphorical Distance Check (run before writing slots):**
- Seed 1 and Seed 2 must not share the same object, location, or light type.
- Seed 2 and Seed 3 must not share the same metaphor family (both "decay", both "growth",
  both "isolation", etc.).
- At least one seed must shift frame of reference entirely: scale, time period,
  or witness point of view.
- If any pair is too similar, regenerate the most generic seed before proceeding.

REPLACE WITH:

**Metaphorical Distance Check (MANDATORY — print result in Decision Block):**
After generating Seeds 1–3, classify each seed's metaphor family using ONE of these labels: organic/growth, mechanical/industrial, temporal/decay, social/behavioral, archival/documentary, geological/elemental, sensory/synaesthetic, spatial/architectural.

Print in Decision Block:
`Metaphor families: Seed 1 = [label] | Seed 2 = [label] | Seed 3 = [label] — ALL DISTINCT: [YES/NO]`

Requirements:
- Seed 1 and Seed 2 must have DIFFERENT labels.
- Seed 2 and Seed 3 must have DIFFERENT labels.
- No two adjacent seeds may share a label.
- At least one seed must shift frame of reference entirely: scale, time period, or witness point of view.
- If ANY adjacent pair shares a label, regenerate the more generic seed with a DIFFERENT label before proceeding. Do not output seeds that share adjacent labels.

This check is PRINTED, not silent. If the line is missing from Decision Block, seeds have not been validated.

Do not modify any text before or after this block.

---

# EDIT 4: THEME ENRICHMENT — STEP 2 (section B.2)

FIND this exact block:

**STEP 2 — Enrich:**
Use blacklist as guardrail. Add material character, light behavior, and implied tension.
- Specific object: Add material + light + tension.
- Abstract concept: Translate into one concrete embodied scene.
- Broad domain: Keep enriched theme structural; move specifics to slots via seeds.
- Product: Add functional anchor, context of use, visual hook.
- Vague state: Ground in specific time, place, and focal point.

REPLACE WITH:

**STEP 2 — Enrich:**
Use blacklist as guardrail. Add material character, light behavior, and implied tension.

Enrichment must remain STRUCTURAL: specify material category (not specific objects), time period or season (not exact time of day), emotional register (not specific mood-props), and scale class (not exact dimensions). Do NOT list specific visual elements such as named flowers, particular textures, or concrete shapes — these must be discovered independently by each slot.

Test: if the enriched theme contains a noun that could appear verbatim in a slot description (e.g., "blossom forms," "dew," "tender leaves"), the enrichment is too specific. Rewrite using the category instead: "spring botanical vocabulary" instead of "blossom forms, dew, tender leaves."

- Specific object: Add material category + light direction + tension source.
- Abstract concept: Translate into one concrete embodied scene at structural level.
- Broad domain: Keep enriched theme structural; move specifics to slots via seeds.
- Product: Add functional anchor, context of use, visual hook.
- Vague state: Ground in specific season, region type, and focal object category.

Do not modify any text before or after this block.

---

# EDIT 5: HARD CHECKS — SEED INTERPRETATION TEST (section "HARD CHECKS")

FIND this exact item:

11. **Seed Separation:** No final prompt closely echoes or paraphrases any Seed text.
    Each slot derived from a seed must use its own dominant image, distinct vocabulary,
    and independent sentence structure. If a slot draft mirrors a seed's wording or
    imagery, rewrite before output.

    **Seed Interpretation Test:** The slot built from a seed must contain at least one
    major visual element — setting detail, secondary object, spatial relationship, or
    material behavior — that the seed does not mention. If the slot's opening sentence
    could be produced by minor rewording of the seed text, the slot has copied rather
    than interpreted. Rewrite with a shifted perspective or a different entry point
    into the same scenario before output.

REPLACE WITH:

11. **Seed Separation:** No final prompt closely echoes or paraphrases any Seed text.
    Each slot derived from a seed must use its own dominant image, distinct vocabulary,
    and independent sentence structure. If a slot draft mirrors a seed's wording or
    imagery, rewrite before output.

    **Seed Interpretation Test:** The slot built from a seed must satisfy ALL of the following:
    1. The slot's OPENING SENTENCE introduces a visual element ABSENT from the seed text.
    2. The slot contains at least TWO major visual elements — setting details, secondary objects, spatial relationships, or material behaviors — that the seed does not mention.
    3. The slot must TRANSFORM the seed's direction into a scene the seed could not have specifically predicted — different dominant image, different spatial arrangement, or different scale of observation.
    
    Noun overlap test: count the concrete nouns shared between seed text and slot text. If more than 2 concrete nouns (excluding the carrying image) are shared, the slot has copied rather than interpreted. Rewrite with different vocabulary and a different entry point into the same conceptual direction.

Do not modify any text before or after this item.

---

# EDIT 6: A.2 RULE 2 — ADD BANNED GENERIC ADJECTIVES (section A.2)

FIND this exact text:

2. **Specificity Test:** If an adjective could describe any scene → replace with a
   scene-specific detail.

REPLACE WITH:

2. **Specificity Test:** If an adjective could describe any scene → replace with a
   scene-specific detail.

   **Banned generic adjectives (replace on sight):** soft, clean, fresh, nice, beautiful, lovely, gentle, delicate, simple, pure, clear, fine, smooth, calm, quiet, subtle, elegant, refined, pretty, pleasant. For each banned adjective, substitute a materially specific descriptor tied to the current scene. Examples: "soft light" → "north-window diffused daylight"; "clean lines" → "single-pixel-weight dividers"; "fresh color" → "unoxidized mint"; "gentle gradient" → "four-stop tonal ramp from ivory to sage."
   
   Exception: if the adjective describes a MATERIAL PROPERTY that is technically specific (e.g., "soft clay" = Shore A hardness, "smooth glass" = optical-grade surface), it may be retained with qualifying detail.

Do not modify any text before or after this rule.

---

# EDIT 7: A.2 RULE 9 — EXTEND CAMERA-VISIBLE BAN LIST (section A.2)

FIND the end of the banned constructions list in Rule 9. It currently ends with:

   - "proudly" / "boldly" / "gracefully" / "defiantly"
     (anthropomorphic attribution to inanimate objects)

IMMEDIATELY AFTER this line, ADD:

   - "keeping X [adjective]" / "maintaining X" (describes state management, not visible feature — exception: acceptable when describing physical material state in engineering context, e.g., "maintaining structural rigidity")
   - "turning X into Y" / "making X [adjective]" (causation or process, not frozen result)
   - "while still [verb-ing]" when applied to composition or design intent (temporal process in static image)
   - "without losing" / "without breaking" / "without sacrificing" (describes constraint preservation, not visible element)

Do not modify any other text in Rule 9.

---

# EDIT 8: PHASE 5 PRE-WRITE CHECK — CONSOLIDATE (section 5.1)

FIND this exact text in step 2:

2. **Pre-write check (before drafting each slot):**
   - Does Slot N differ from Slot N−1 in at least 2 of: framing scale, setting,
     light source type, lens, mood?
   - Any banned phrases in draft?
   - If core subject repeats (allowed): do secondary props and setting change?
   If NO to any → rewrite before continuing.

REPLACE WITH:

2. **Pre-write check (before drafting each slot):**
   - Verify Adjacent Slot Uniqueness (Rule A.2.7).
   - Any banned phrases in draft?
   - If core subject repeats (allowed): do secondary props and setting change?
   If NO to any → rewrite before continuing.

Do not modify any text before or after this step.

---

# EDIT 9: HARD CHECKS ITEM 1 — CONSOLIDATE (section "HARD CHECKS")

FIND this exact item:

1. **Adjacent Slot Uniqueness:** Each slot differs from the previous in ≥2 of:
   setting, light source type, framing scale, lens, mood. Core subject may repeat
   for single-object themes, product photography, or Module D. Secondary props
   and setting must vary between adjacent slots.

REPLACE WITH:

1. **Adjacent Slot Uniqueness (Rule A.2.7):** Verified. Core subject may repeat
   for single-object themes, product photography, or Module D. Secondary props
   and setting must vary between adjacent slots.

Do not modify any text before or after this item.

---

# EDIT 10: HARD CHECKS — ADD ITEM 14 (section "HARD CHECKS")

FIND the last numbered item. After Edit 5 applied, there should be item 13 ("Interpretation Gradient").

AFTER item 13, ADD:

14. **Metaphor Family Distinctness:** Decision Block contains the line `Metaphor families: Seed 1 = [label] | Seed 2 = [label] | Seed 3 = [label] — ALL DISTINCT: [YES/NO]`. If line is missing or shows NO, seeds have not been validated — regenerate before proceeding.

---

# PROHIBITIONS

- Do NOT change any text other than the 10 locations specified above
- Do NOT add comments like "changed", "updated", or "modified"
- Do NOT rephrase surrounding text "for consistency"
- Do NOT touch examples (matchbox, ceramic mug, etc.)
- Do NOT touch modules (A, B, C, D, V) except where explicitly specified
- Do NOT delete or add sections
- Do NOT reorder anything
- Do NOT touch any rules, definitions, or explanations outside the 10 edit locations
- Do NOT renumber existing Hard Checks items (they stay 1–13; you only ADD item 14)

Output the COMPLETE prompt text with all 10 edits applied.