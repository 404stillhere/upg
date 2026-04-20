PATCH INSTRUCTION FOR UNIVERSAL PROMPT GENERATOR v9.1 → v9.2
PURPOSE
This patch resolves 11 identified defects in UPG v9.1 while preserving all working mechanisms. Apply changes in the order specified. Do not modify any section not explicitly mentioned.

PRESERVED MECHANISMS — DO NOT MODIFY
The following systems work correctly and must remain unchanged:

Slot Architecture (SHALLOW ARC / FULL ARC tables in A.3)
Seed Generation & Metaphor Distance Check (Section 4.1)
Cliché Blacklist (STEP 1 in B.2)
Module B Four Minimums (Zone C, Module B)
Module D Transformation Arc (Zone C, Module D, S1–S5 progression)
Entry Angle Execution Rule (first-sentence lock in B.2 STEP 6)
Carrying Image Dominance Test (STEP 0 in B.2)
PATCH #1 — Aspect Ratio Suffix
Priority: Critical | Location: Section 5.2 Platform Suffixes

FIND:

text

**Midjourney:**
Append: --ar 3:2 --v 6 --style raw --s 50
REPLACE WITH:

text

**Midjourney:**
Append: --ar [VALUE FROM DECISION BLOCK "Aspect:" FIELD] --v 6 --style raw --s 50

The --ar parameter must match the aspect ratio derived during Aspect Ratio Selection and recorded in the Decision Block. Do not hardcode a default ratio.
PATCH #2 — Contrast Diversity Rule
Priority: High | Location: Section A.2, after the contrast term requirement

FIND the paragraph ending with:

text

Do not leave contrast implicit.
INSERT AFTER:

text

**Contrast Diversity Rule:** Across a 5-slot series, no more than 2 slots may use the same contrast level (high, medium, or low). Comparative forms ("higher contrast," "lower contrast") count as their base term. After drafting all slots, verify distribution; if 3 or more slots share the same contrast term, revise the slot whose lighting scenario most naturally supports a different level.

Exception: SCIENTIFIC context with comparative or typological intent may use uniform contrast across all slots when consistent lighting is required for objective documentation.
PATCH #3 — Material Metaphor Enrichment Exception
Priority: High | Location: Section B.2 STEP 2, after the Material Metaphor Rule

FIND the Material Metaphor Rule ending with:

text

rewrite it until the environment IS the material.
INSERT AFTER:

text

**Material Metaphor Abstraction Constraint:** For material-substitution themes, enrichment must describe the replacing material's behavioral CATEGORIES — light transmission type (translucent, opaque, refractive), viscosity class (rigid, viscous, fluid), structural behavior under gravity (sagging, floating, crystallizing), weather interaction type (absorbing, repelling, dissolving) — without naming specific visual instances. 

Example — PASS: "warm spectral absorption, high viscosity with slow deformation under gravity, surface tension creating curved boundaries against rigid structures."
FAIL: "golden light shafts, suspended bubbles, honey dripping from cables."

The distinction: PASS describes physics categories that guide slot-writing; FAIL describes camera-visible instances that slots must discover independently. If enrichment nouns appear verbatim in S1 prose, the enrichment is too specific — rewrite at category level.
PATCH #4 — CONCISE_MODE Scope Clarification
Priority: High | Location: OUTPUT PROTOCOL section, after CONCISE_MODE = true definition

FIND:

text

Follow immediately with five prompts.
INSERT AFTER (same paragraph or new line):

text

CONCISE_MODE controls planning-layer output format only. It does not suppress enforcement mechanisms. When PLATFORM = Midjourney and CONCISE_MODE = true, word count PASS lines are still printed after each slot.
PATCH #5 — Product-Line S2 Clarification
Priority: Medium | Location: Section A.3, SHALLOW ARC table, S2 row

FIND:

text

S2 TILT | Same subject, different angle/light/distance + Entry Angle | Instantly legible. Do not substitute a different object.
REPLACE WITH:

text

S2 TILT | Same subject, different angle/light/distance + Entry Angle | Instantly legible. Do not substitute a different object. **Product-line rule:** When THEME is a product line (multiple items), S1 establishes a hero arrangement of specific items. S2 must depict the SAME specific items from S1, not different items from the same line. Additional products may appear in S3 onward.
PATCH #6 — Photography Camera Spec Requirement
Priority: High | Location: Section A.5, after "Technical framing" bullet

FIND the bullet:

text

- **Technical framing:** Specific to the assigned lens
INSERT AFTER:

text

- **Photography Camera Spec Rule:** When Medium = photography, every slot MUST include one focal length (e.g., 85mm, 35mm, 100mm macro) and one f-stop (e.g., f/2.8, f/4, f/8). These are classified as "technical framing" under Compression Priority and must NOT be sacrificed. Under extreme word pressure, use compact form: "85mm f/2.8" (3 words). This compact form always fits within platform limits.
PATCH #7 — Banned Adjective Enforcement
Priority: Medium | Location: Section A.2, after the banned adjective list

FIND the exception clause ending with:

text

it may be retained with qualifying detail.
INSERT AFTER:

text

**High-Frequency Violation List (check with extra attention):** soft, clean, fresh, fine, smooth, gentle, subtle, elegant, delicate, simple. These 10 adjectives account for ~90% of ban violations. For each, preferred replacements:
- soft → diffused, muted, low-contrast, scattered
- clean → uncluttered, minimal, single-tone, dust-free
- fresh → recently-cut, undried, unoxidized, morning-harvested
- fine → narrow, hairline, granular, micron-scale
- smooth → polished, satin-finish, continuous-surface, unridged
- gentle → gradual, slow-gradient, low-angle, indirect
- subtle → understated, 10%-opacity, hint-of, barely-visible
- elegant → proportioned, balanced, deliberate, considered
- delicate → thin-walled, lightweight, breakable, filigree
- simple → single-element, monochrome, unadorned, plain-surface

When drafting, if any of these 10 appear, immediately substitute from the replacement list or invent a materially specific alternative.
PATCH #8 — Absence Description Technique
Priority: Medium | Location: Section A.2, after the Narrated Absence Ban examples

FIND the line:

text

PASS sentences describe only physical evidence without naming what caused it.
INSERT AFTER:

text

**Absence Description Technique (positive method):** When writing trace or absence (FULL ARC S5, Module D RUPTURE, Environmental Departure), use this three-step construction:

1. **Name visible evidence** — dust patch, compression mark, discoloration zone, residue ring, fade boundary, pressure ridge, scorch shadow, adhesive rectangle
2. **Describe physical properties** — dimensions, color, texture, edge sharpness, depth, pattern regularity
3. **Anchor spatially** — positioned between, aligned with, centered on, radiating from, offset from, flush against

Do NOT add explanation of what caused the evidence or what previously occupied the space.

FAIL: "a rectangular patch on the wall where a frame once hung"
PASS: "a rectangular patch of unfaded wallpaper, 40 by 30 centimeters, bounded by a faint dust shadow on three sides, two small nail holes visible at the upper corners, centered between the window and the doorframe"

The reader infers absence from physical evidence. You describe evidence only.
PATCH #9 — Slot Plan Format
Priority: Low | Location: Decision Block specification in OUTPUT PROTOCOL

FIND:

text

Slot plan (S1–S5: lens + framing scale + dominant image)
REPLACE WITH:

text

Slot plan (S1–S5, format each entry as: [LENS from A.4] + [framing scale] + [dominant image]. Example: "S1: PHOTOREALISTIC, tabletop hero, mug centered on oak board." Every entry must begin with a named lens from the A.4 Creative Lenses table.)
PATCH #10 — Scientific Comma-List Exemption
Priority: Low | Location: Section A.2, Comma-List Test scope exemption

FIND:

text

Module B technical specifications (container size, closure type, label description, compliance marks) and Module A format specifications (dimensions, text zone positions, type hierarchy) are classified as design shorthand and exempt from this test.
REPLACE WITH:

text

Module B technical specifications (container size, closure type, label description, compliance marks), Module A format specifications (dimensions, text zone positions, type hierarchy), and SCIENTIFIC technical enumeration (device components, anatomical features, measurement parameters, material specifications) are classified as technical shorthand and exempt from this test. Under word pressure, technical specs may appear as compact clauses within otherwise flowing prose.
PATCH #11 — Redundancy Consolidation
Priority: Medium | Location: Three locations (see below)

This patch consolidates the narrated absence rule from three locations into one authoritative statement.

LOCATION A — Additional banned constructions list in A.2

FIND:

text

- "of what X once [verb]" / "what X used to" / "what was once" / "where X [past-verb]" / "where something [past-verb]" (temporal narration of absent state — describe visible residue, not vanished history)
REPLACE WITH:

text

- "of what X once [verb]" / "what X used to" / "what was once" / "where X [past-verb]" (temporal narration — see Narrated Absence Ban below for full rule and technique)
LOCATION B — Narrated Absence Ban subsection

KEEP this section intact. It is now the single authoritative location. Patch #8 (Absence Description Technique) is inserted here.

LOCATION C — Module D RUPTURE definition

FIND the detailed absence instructions starting with:

text

You must physically erase the recurring element from the scene entirely. Render strictly the empty space where it used to be...
REPLACE WITH:

text

Apply the Narrated Absence Ban and Absence Description Technique from A.2. The recurring element must be fully erased; only physical evidence remains.
PATCH #12 — Theme Position Recount Instruction
Priority: Low | Location: Section A.4, Theme Position Detection

FIND:

text

Do NOT reset counter when THEME text repeats. The counter tracks GENERATION REQUESTS, not unique theme concepts.
INSERT AFTER:

text

**Recount Safeguard:** If conversation exceeds 8 exchanges or if Entry Angle selection feels uncertain, recount THEME inputs from conversation start before proceeding. Silent miscounts propagate through the entire series.
IMPLEMENTATION CHECKLIST
Apply patches in numerical order. After each patch:

Patch	Verification
#1	Generate Midjourney prompt with vertical subject. Confirm --ar matches Decision Block Aspect field.
#2	Generate 5-slot series. Confirm no more than 2 slots share same contrast term.
#3	Generate material-metaphor theme. Confirm enrichment uses categories; no enrichment nouns appear verbatim in S1.
#4	Generate CONCISE_MODE + Midjourney output. Confirm PASS lines present, word counts ≤60.
#5	Generate product-line theme. Confirm S1 and S2 show identical specific items.
#6	Generate photography output. Confirm every slot contains focal length + f-stop.
#7	Search all outputs for the 10 high-frequency banned adjectives. Confirm zero violations or valid exceptions.
#8	Generate FULL ARC with S5 trace. Confirm three-step method used, no temporal narration.
#9	Check Decision Block slot plan. Confirm each entry begins with named lens.
#10	Generate SCIENTIFIC theme. Confirm technical enumeration flows without forced spatial anchoring.
#11	Generate Module D output. Confirm RUPTURE follows absence ban via cross-reference.
#12	In long conversation, confirm Entry Angle rotation remains accurate.
COMPRESSION OPPORTUNITY (OPTIONAL)
This patch adds approximately +280 words and removes approximately −80 words (Patch #11), for a net increase of ~+200 words. To maintain attention budget, consider trimming:

A.1 Reference Quality Examples: Reduce from 3 examples to 2 (remove COMMERCIAL, keep PHOTOGRAPHY and CONCEPT ART) — saves ~75 words
A.3 Ceramic mug example: Reduce from 5 slots to 3 (keep S1, S3, S5) — saves ~80 words
Feedback Adjustment Protocol table: Reduce from 14 rows to 8 most common — saves ~50 words
These are optional. The patch is functional without compression, but a shorter prompt improves compliance on rules appearing late in the document.

VERSION MARKING
After applying all patches, update the header:

text

# UNIVERSAL PROMPT GENERATOR v9.2
Add changelog note:

text

v9.2 Changes: Aspect ratio suffix dynamic insertion; contrast diversity rule; material metaphor abstraction constraint; CONCISE_MODE scope clarification; product-line S2 rule; photography camera spec requirement; banned adjective replacements; absence description technique; slot plan lens format; scientific comma-list exemption; redundancy consolidation; theme position recount safeguard.
END OF PATCH INSTRUCTION