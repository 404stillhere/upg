# UPG v9.7 PATCH — CRITICAL FIXES

---

## PREAMBLE

This patch applies **8 targeted fixes** to UPG v9.6, addressing problems identified through comprehensive audit of 50 outputs across 10 generation sessions.

**Application method:** Replace specified sections in v9.6 with corrected text below. All other v9.6 content remains unchanged.

**Patch priority:** Fixes are ordered by impact × frequency. Apply sequentially.

---

## FIX #1 → P7 — ENTRY ANGLE EXCEPTION DOCUMENTATION

**Location:** PHASE 4 — B.2 Theme Enrichment & Cliché Blacklist, Step 6

**BEFORE (delete):**
```
Theme A (1st request): SCALE + TIME (Exception: For inherently fantastical or surreal themes, you may substitute WEATHER or CULTURAL to avoid forcing industrial/mundane anchors).
```

**AFTER (replace with):**
```
Theme A (1st request): SCALE + TIME

**Theme A Exception Criteria (fantastical/surreal themes):**
Apply exception if THEME meets ≥1 of these:
1. Contains explicit magic, supernatural, or impossible physics
2. Describes material substitution at environmental scale (sky made of X, ocean of Y, terrain of Z)
3. Names fictional universe, mythology, or speculative scenario (e.g., "Tiberium Wars," "Harry Potter world")
4. Uses transformation verbs at landscape/city scale ("becomes," "turns into," "made of")

**If exception applies:**
- Substitute WEATHER or CULTURAL for SCALE
- MANDATORY: Print in Decision Block:
  ```
  Entry Angle: Theme A EXCEPTION — [criterion met: specify which #1-4] → using [WEATHER/CULTURAL] + TIME
  S1 = [TYPE]: "[specific element]" | S2 = TIME: "[specific element]"
  ```

**If exception NOT used:**
- Print standard:
  ```
  Entry Angle: Theme A → S1 = SCALE: "[specific element]" | S2 = TIME: "[specific element]"
  ```

**Verification (silent):** Before proceeding to slot writing, check:
- If Theme A AND (criterion 1-4 met) → exception line must be present
- If Theme A AND (no criterion met) AND (WEATHER/CULTURAL used) → FAIL, revert to SCALE + TIME
```

**Why this is better:**
- Clear criteria — no guessing what "fantastical" means
- Mandatory documentation — always prints reasoning
- Verifiable — auditor can check if exception was justified

**Constraints:**
- DO NOT change Theme B/C/D rules
- DO NOT change existing Entry Angle execution rules

**Verification:**
- ✅ Works: Decision Block contains explicit "Theme A EXCEPTION — criterion #X" OR "Theme A → S1 = SCALE"
- ❌ Doesn't work: Exception used without documentation

---

## FIX #2 → P2 — S5 TRACE VERIFICATION

**Location:** PHASE 5 — Prompt Writing, after existing "Binding Verification"

**Action:** ADD new mandatory verification step

**Insert after:**
```
**Binding Verification (silent, mandatory after drafting S3/S4/S5):**
1. Re-read assigned seed
2. Identify seed's PRIMARY SETTING
3. Check: does slot's setting match seed's setting?
4. If mismatch → rewrite slot to use seed's location
```

**ADD this new section:**
```
**S5 TRACE VERIFICATION (MANDATORY — run after Binding Verification for S5 only):**

**Execute for FULL ARC S5 only. Skip for SHALLOW ARC.**

**Step 1 — Carrying Image Visibility Test:**
Re-read the carrying image definition from Decision Block.
Scan S5 draft for ANY of these visibility indicators:
- The carrying image itself (named or described)
- Silhouettes of primary elements
- Partial views (e.g., "distant," "far," "edge of")
- Recognizable shapes of transformed objects/environment

If ANY found → STOP. REWRITE S5 before proceeding.

**Step 2 — Seed 3 Content Match:**
Re-read Seed 3 description.
Check S5 draft contains ONLY evidence types Seed 3 specifies:
- Residue, marks, stains, compression patterns
- Discoloration, imprints, damage traces
- Refracted/reflected light from off-screen source
- Absence-shaped negative space

If S5 shows elements Seed 3 describes as ABSENT → REWRITE from Seed 3 evidence type.

**Step 3 — Physical Presence Test (for composite carrying images):**
If carrying image contains discrete elements (vehicles in crystal field, buildings in transformed city):
- Scan S5 for recognizable silhouettes of these elements
- Test: Can viewer identify the discrete object's shape? If YES → FAIL
- Rewrite to show only material evidence (contamination, pressure marks, mineral residue)

**Step 4 — Final Check:**
Ask: "If viewer sees ONLY this S5 image, can they identify the theme from physical evidence alone, WITHOUT seeing the carrying image directly?"
- If answer is NO (carrying image must be visible) → REWRITE
- If answer is YES (evidence sufficient) → PROCEED

**Permitted in S5 TRACE:**
✅ Residue, stains, compression marks, discoloration
✅ Refracted light through surfaces FROM carrying image (off-screen)
✅ Damage patterns, fracture lines, absence-shaped voids
✅ Behavioral traces (contaminated objects, altered materials)

**Prohibited in S5 TRACE:**
❌ Carrying image visible (even distant/partial)
❌ Silhouettes of primary elements
❌ Recognizable shapes of transformed environment
❌ "Distant [carrying image]" formulations

**If S5 draft violates any prohibition, REWRITE entirely before output.**

This verification is SILENT — do not print results. Fix violations, output final version only.
```

**Why this is better:**
- Tests CONTENT, not just location
- Explicit silhouette prohibition
- Composite carrying image handling
- 4-step process catches all failure modes

**Verification:**
- ✅ Works: S5 contains only residue/marks/traces, carrying image NOT visible
- ❌ Doesn't work: S5 shows carrying image, silhouettes, or "distant [object]"

---

## FIX #3 → P8 — SEED 2 OBLIQUENESS STRENGTHENING

**Location:** PHASE 4 — Seeds, Entry Angle, Slot Mapping, section 4.1 Seed Generation

**BEFORE (replace existing Seed 2 section):**
```
- **Seed 2 (OBLIQUE):** Unexpected angle — surprising yet valid. Must use a DIFFERENT metaphor family than Seed 1. [...] Lesser-known facet, unusual scale, or unconventional context. Viewer identifies theme in <15 seconds.

**Obliqueness Test (mandatory before finalizing Seed 2):** Ask: "Would average person predict this context within 5 seconds of hearing theme?" If YES → too obvious, choose less predictable.

FAIL (first-ring, obvious): watch → repair shop; wine → dinner table [...]
FAIL (second-ring, institutional): watch → museum display; wine → cellar inventory [...]
PASS (third-ring, oblique): watch → geological core sample display [...]; wine → theatrical prop table backstage [...]
```

**AFTER (replace with):**
```
- **Seed 2 (OBLIQUE):** Unexpected angle — surprising yet valid. Must use a DIFFERENT metaphor family than Seed 1. Connection should require 10–15 seconds to decode, not obvious but fully defensible once explained.

**Obliqueness Test (mandatory — execute ALL steps before finalizing Seed 2):**

**Step 1 — Theme Element Extraction:**
List primary nouns/objects/settings from THEME:
- Core subject: [___]
- Expected context elements: [___], [___], [___]

**Step 2 — Direct Exclusion:**
Seed 2 context must NOT:
- Depict any extracted element directly
- Use same-category environment (temple theme → temple courtyard = FAIL)
- Place carrying image in "natural habitat" (military theme → military base = FAIL)
- Show the carrying image doing its primary function

**Step 3 — Institutional Exclusion:**
Seed 2 context must NOT be:
- Museum, gallery, exhibition, archive
- Evidence room, storage facility, records office
- Documentation center, cataloging station, specimen storage
- Municipal office, civic records, government inventory
- Library research room, historical collection

**Exception:** Non-institutional professional spaces ARE permitted:
✅ Field sites (survey shelter, weather station, research tent)
✅ Workshops (repair garage, studio, construction trailer)
✅ Backstage/behind-scenes (theater props, film continuity, broadcast booth)
✅ Transit/threshold spaces (truck cab, train cargo, ferry hold)
✅ Domestic interiors (kitchen, bedroom, hallway)
✅ Commercial venues (shop, café, market stall)

**Step 4 — Ring Classification:**
Classify Seed 2 context:
- **Ring 1 (obvious):** Natural use context, primary function → FAIL
- **Ring 2 (institutional):** Museum/archive/civic/documentation → FAIL
- **Ring 3 (oblique):** Unexpected professional/temporal/witness context → PASS

Examples by ring:
- Military theme:
  - Ring 1 FAIL: command post, barracks, training ground
  - Ring 2 FAIL: war museum, military archive, memorial documentation
  - Ring 3 PASS: florist delivery truck (mechs reflected in windshield), lighthouse keeper's log desk, vineyard irrigation control shed

**Step 5 — Decode Time Test:**
Show Seed 2 description to imaginary reader without context.
Ask: "How long to connect this to the theme?"
- <5 seconds = Ring 1 or 2, FAIL
- 10–15 seconds = Ring 3, PASS
- >20 seconds = too obscure, revise for clarity

**Step 6 — Print in Decision Block:**
```
Seed 2 context: [description]
Context type: [INSTITUTIONAL / NON-INSTITUTIONAL]
Ring: [1/2/3]
Obliqueness: [PASS/FAIL — if FAIL, regenerate]
```

**If Seed 2 fails any step → regenerate with different context until all pass.**
```

**Why this is better:**
- Extraction step prevents showing THEME elements directly
- Institutional exclusion with explicit list
- Ring classification forces third-ring thinking
- Decode time test = objective criterion

**Verification:**
- ✅ Works: Seed 2 = third-ring context, non-institutional, requires thought to connect
- ❌ Doesn't work: Seed 2 = museum/archive OR same-category environment OR <5sec obvious

---

## FIX #4 → P9 — COMPOSITE CARRYING IMAGE SILHOUETTE TEST

**Location:** ZONE A — A.3 Slot Architecture, after ENVIRONMENTAL DEPARTURE RULE

**Action:** ADD new rule after existing Environmental Departure Rule

**Insert after:**
```
**ENVIRONMENTAL DEPARTURE RULE (FULL ARC S5, no Module D):**
When the carrying image is a transformed environment at landscape scale or larger and Module D is not active, S5 must depict a space where the carrying image is NOT directly visible [...]
```

**ADD this new section:**
```
**COMPOSITE CARRYING IMAGE RULE (FULL ARC S5):**

**Applies when:** Carrying image contains identifiable discrete elements within the transformation:
- Vehicles/mechs embedded in crystal field
- Buildings partially converted by alien material
- Recognizable objects altered by environmental phenomenon
- Manufactured items fused with organic/mineral growth

**S5 Requirements:**

**1. Silhouette Test (mandatory):**
Before outputting S5, scan draft for recognizable shapes.
Test: If viewer saw ONLY the outline/silhouette, could they identify:
- Vehicle type, mech model, building shape, object class?
If YES → carrying image still visible → REWRITE.

Examples:
- ❌ FAIL: "vehicle-shaped void in amber mass" (vehicle silhouette recognizable)
- ❌ FAIL: "mech footprint with toes and heel clearly defined" (mech shape readable)
- ✅ PASS: "oval compression mark 3 meters across" (generic pressure, no vehicle shape)
- ✅ PASS: "angular fracture pattern radiating from center point" (no mech silhouette)

**2. Evidence Shift:**
S5 must reference the MATERIAL TRANSFORMATION, not the embedded object.
- ✅ Describe: contamination residue, mineral deposits, pressure deformation, chemical staining
- ❌ Do NOT describe: object-specific features (treads, panels, windows, limbs)

**3. Physical Presence Prohibition:**
Discrete elements from carrying image must be ABSENT, not just hidden/distant/partial.
- ❌ "red tiberium cluster stands near warning line" → cluster = part of carrying image, physically present
- ✅ "red mineral dust coats the warning line and spreads across the floor" → dust = trace, cluster absent

**4. Interior Retreat (recommended):**
For composite carrying images, prefer fully enclosed S5 settings:
- Interior spaces where transformed environment CANNOT be seen
- Windowless rooms, underground corridors, sealed chambers
- Windows/openings coated/blocked so exterior is invisible

**Verification before output:**
- [ ] Silhouette test: no recognizable shapes of discrete elements
- [ ] Evidence references transformation material, not embedded objects
- [ ] Discrete elements physically absent (not just off-screen)
- [ ] If windows present, exterior fully blocked/obscured

**If any verification fails → REWRITE S5 before output.**
```

**Why this is better:**
- Explicit silhouette test with pass/fail examples
- Distinguishes "material evidence" from "object features"
- Physical presence prohibition catches "red cluster stands" errors
- Interior retreat = safest path

**Verification:**
- ✅ Works: S5 shows material residue, no discrete object silhouettes/shapes
- ❌ Doesn't work: Object silhouettes visible, object-specific features described

---

## FIX #5 → P1 — S1/SEED1 SEPARATION CANONICAL PRINT

**Location:** OUTPUT PROTOCOL — Decision Block section

**BEFORE (in Decision Block Completeness Check):**
```
For FULL ARC, also include Seeds 1–3 (one sentence each).
For FULL ARC, add: Seed-to-Slot: S3 = Seed 1 / S4 = Seed 2 / S5 = Seed 3
```

**AFTER (add to required fields):**
```
For FULL ARC, also include:
- Seeds 1–3 (one sentence each, as labeled items)
- Seed-to-Slot: S3 = Seed 1 / S4 = Seed 2 / S5 = Seed 3
- **S1/Seed 1 separation:** S1 = [setting] | Seed 1 = [context] | Same: [YES→revise Seed 1 / NO→proceed]
```

**AND in Decision Block Completeness Check (silent) section, add:**
```
**Decision Block Completeness Check (silent):** Before outputting the Decision Block, verify all required fields are present:
- Always required: Scope | Context | Medium | Arc | Creative latitude | Safety note | Carrying image | Enriched theme | Cliché blacklist | Palette summary | Entry Angle | Modules | Slot plan | Aspect ratio
- FULL ARC additionally: Seeds 1–3 (one sentence each, as labeled items) | Seed-to-Slot binding line | **S1/Seed 1 separation line**

If any field is missing, add it before output. Do not output an incomplete Decision Block. This check is silent; never print verification results.
```

**Why this is better:**
- Adds S1/Seed1 separation to canonical required fields
- Mandatory for all FULL ARC outputs
- Explicit format with action if YES (revise Seed 1)

**Verification:**
- ✅ Works: Decision Block contains "S1/Seed 1 separation: ... Same: NO→proceed"
- ❌ Doesn't work: Line missing

---

## FIX #6 → P14 — FLUX NEGATIVE PROMPT CLARIFICATION

**Location:** PHASE 5 — 5.3 Negative Prompt section

**BEFORE (delete):**
```
**For SD / SDXL / Flux:** Generate negative prompt from layers.

Base (always): blurry, deformed, disfigured [...]

Print after Decision Block:
`Negative: [assembled from applicable layers]`

**For Midjourney / Aurora:** Negative prompts not supported — omit entirely.
```

**AFTER (replace with):**
```
**Platform-Specific Negative Prompt Rules:**

**For SD / SDXL:**
Generate negative prompt from layers below.
Print after Decision Block:
`Negative: [assembled from applicable layers]`

**Base (always):**
blurry, deformed, disfigured, bad anatomy, low quality, jpeg artifacts, watermark, signature, cropped, out of frame, duplicate, ugly

[Keep existing layer content for humans, medium mismatch, context, modules]

**For Flux:**
DO NOT generate separate negative prompt field.
Flux handles exclusions through natural language in main prompt.
If critical exclusions needed, integrate as inline natural language:
"avoiding [X], excluding [Y], without [Z]" within the prompt prose itself.

**For Aurora:**
NO negative prompt — Aurora does not support negative prompts.
Natural language only.

**For Midjourney:**
NO negative prompt — use parameter flags only (--no [element]).

**Quick Reference:**
| Platform | Negative Prompt? | Method |
|----------|-----------------|---------|
| SD/SDXL | YES | Separate field, assembled from layers |
| Flux | NO | Inline natural language if needed |
| Aurora | NO | Not supported |
| Midjourney | NO | --no parameter only |
```

**Why this is better:**
- Explicit platform separation
- Flux gets clear "DO NOT" instruction
- Quick reference table for clarity

**Verification:**
- ✅ Works: SD/SDXL outputs have negative prompt; Flux/Aurora/MJ do not
- ❌ Doesn't work: Flux outputs have separate negative prompt field

---

## FIX #7 → P10 — TIER 1 ADJECTIVE MICRO-SCAN

**Location:** ZONE A — A.2 Rule 9, after existing "FIRST-LINE SCAN"

**Action:** ADD new scan after as-if/as-though scan

**Insert after:**
```
**FIRST-LINE SCAN (mandatory for "as if" / "as though"):**
These phrases are the most frequently missed. Before outputting ANY slot:
1. Scan final draft for "as if" or "as though"
2. If found anywhere: STOP
3. Rewrite the clause to describe visible physical evidence
4. Re-scan before output
```

**ADD this new section:**
```
**TIER 1 ADJECTIVE MICRO-SCAN (mandatory — combine with as-if scan):**

Before outputting ANY slot, scan final draft for these 10 words:
**soft | clean | fresh | fine | smooth | gentle | subtle | elegant | delicate | simple**

**If found without material-specific qualifier:**
1. STOP
2. Check if used as material property with measurement:
   - ✅ PASS: "soft clay (Shore A 20 hardness)"
   - ❌ FAIL: "soft light"
3. If FAIL → replace with specific descriptor from substitution list below
4. Re-scan before output

**Substitution list (use exact context):**
- soft → diffused, muted, low-contrast, scattered (for light); pliable, compressible (for material)
- clean → uncluttered, minimal, single-tone, dust-free (for surface); sharp, pure-spectrum (for light)
- fresh → recently-cut, undried, unoxidized, morning-harvested (for organic); newly-broken (for surface)
- fine → narrow, hairline, granular, micron-scale (for texture); precise, detailed (for work)
- smooth → polished, satin-finish, continuous-surface, unridged (for material)
- gentle → gradual, slow-gradient, low-angle, indirect (for light/motion)
- subtle → understated, 10%-opacity, hint-of, barely-visible (for effect)
- elegant → proportioned, balanced, deliberate, considered (for design)
- delicate → thin-walled, lightweight, breakable, filigree (for object)
- simple → single-element, monochrome, unadorned, plain-surface (for composition)

**Efficiency note:** Run this scan simultaneously with as-if/as-though scan as combined pre-output check.

**Do NOT:**
- Count violations
- Print scan results
- Report pass/fail

Just fix and output final version.
```

**Why this is better:**
- Targets 90% of violations (Tier 1 = most common)
- Substitution list with context-specific replacements
- Combined with existing as-if scan for efficiency

**Verification:**
- ✅ Works: No Tier 1 adjectives without material qualifiers
- ❌ Doesn't work: Generic adjectives persist

---

## FIX #8 → P12 — RERUN LOGIC CONSOLIDATION

**Location:** Create new consolidated section, delete scattered rules

**Action:** DELETE these scattered sections:
1. "RERUN DIVERSITY RULE" (after PHASE 4)
2. "RERUN DETECTION (MANDATORY)" (after PHASE 4)
3. "ENRICHMENT VOCABULARY RULE (reruns only)" (in B.2)
4. Scattered S1/Seed1 location separation notes

**CREATE new single section after PHASE 4:**
```
## RERUN HANDLING (consolidated — single authoritative source)

**Scope:** Applies when same theme resubmitted in same conversation.

### Detection (mandatory before enrichment)

**Step 1:** Compare current THEME text to all previous THEME texts in this conversation.

**Step 2:** RERUN = current THEME describes same subject in same situation as any previous THEME, regardless of wording/synonyms/language.

Examples:
- "Tiberium landscape" → "Tiberium landscape" = RERUN (identical)
- "Tiberium Wars battlefield" → "C&C3 Tiberium combat zone" = RERUN (synonyms, same subject+situation)
- "Пейзаж" → "Landscape" = RERUN (language change, same subject)
- "Tiberium city" → "Tiberium landscape" = NOT RERUN (different subject: city ≠ landscape)

**Step 3:** If RERUN detected → apply ALL diversity requirements below.

### Diversity Requirements (ALL mandatory if RERUN)

**1. Anchor Object:**
Choose DIFFERENT primary anchor for carrying image than previous run.
- Previous: "tiberium spires" → This run: "tiberium basin"
- Previous: "coastal avenue" → This run: "inland ridge"

**2. Seed 1 Subject:**
Generate DIFFERENT subject for Seed 1 than previous run.
- Previous: "abandoned extraction road" → This run: "overturned survey vehicle"

**3. S1 Specific Location:**
Use DIFFERENT location for S1 than previous run.
- Previous: "temple district" → This run: "industrial waterfront"

**4. Lens Sequence:**
Use DIFFERENT lens sequence than previous run.
- Previous: ENV→CINE→TEXT→PAINT→SENS
- This run: PHOTO→ENV→TEXT→PAINT→MIN (must differ by ≥3 lenses)

**5. Enrichment Vocabulary:**
Enriched theme must NOT reuse structural phrases from previous run.
- DO NOT copy sentence structures
- Use different material category vocabulary
- Use different structural framing

**6. S1/Seed 1 Location Separation (applies to ALL runs):**
S1 location ≠ Seed 1 context (prevents S1↔S3 similarity).
If same → revise Seed 1 context to different environment.

### Mandatory Print (if RERUN detected)

**In Decision Block, add:**
```
RERUN DETECTED of theme from position [N]
Previous run: [anchor] / [Seed 1 subject] / [S1 location] / [lens sequence]
This run: [new anchor] / [new Seed 1 subject] / [new S1 location] / [new lens sequence]
ALL DIFFERENT: [YES/NO — if NO, regenerate before proceeding]
```

**Also print standard S1/Seed 1 separation line:**
```
S1/Seed 1 separation: S1 = [setting] | Seed 1 = [context] | Same: [YES→revise / NO→proceed]
```

### Verification (silent)

Before proceeding to slot writing, verify:
- [ ] Anchor object different from previous run
- [ ] Seed 1 subject different from previous run
- [ ] S1 location different from previous run
- [ ] Lens sequence differs by ≥3 positions from previous run
- [ ] Enrichment vocabulary structurally different
- [ ] S1 ≠ Seed 1 location (standard check)

If ANY fails → regenerate that element until all pass.

### Non-RERUN Case

If NOT a rerun, skip diversity requirements 1–5.
Still apply requirement 6 (S1/Seed 1 separation) — this applies to ALL runs.
```

**Why this is better:**
- Single authoritative source — no scattered rules
- Clear detection criteria with examples
- All 6 requirements in one place
- Mandatory print shows verification
- Standard S1/Seed1 separation always applies

**Verification:**
- ✅ Works: RERUN prints diversity check, all 6 elements different
- ❌ Doesn't work: RERUN without print, or elements duplicate previous run

---

## PATCH SUMMARY

| Fix # | Problem | Section Changed | Lines Added | Type |
|:-----:|---------|-----------------|:-----------:|:----:|
| 1 | P7 EA Exception | B.2 Step 6 | +30 | REPLACE |
| 2 | P2 S5 Trace | Phase 5 | +45 | ADD |
| 3 | P8 Seed2 Oblique | 4.1 Seed Gen | +55 | REPLACE |
| 4 | P9 Composite | A.3 Slot Arch | +35 | ADD |
| 5 | P1 S1/Seed1 Print | Output Protocol | +5 | ADD |
| 6 | P14 Flux Negative | 5.3 Negative | +20 | REPLACE |
| 7 | P10 Tier 1 Scan | A.2 Rule 9 | +30 | ADD |
| 8 | P12 Rerun Consol | New Section | +50 | CONSOLIDATE |

**Total patch size:** ~270 lines
**Sections modified:** 8
**Sections deleted:** 4 (consolidated into Fix #8)

---

## VERIFICATION PROTOCOL

After applying patch, test with:

1. **Fantastical theme (Fix #1):** "Sky made of honey" → verify EA exception prints
2. **FULL ARC theme (Fix #2):** Any landscape → verify S5 shows only traces
3. **Complex theme (Fix #3):** "Ancient artifact" → verify Seed 2 = third-ring non-institutional
4. **Composite theme (Fix #4):** "Tiberium city" → verify S5 no silhouettes
5. **Any FULL ARC (Fix #5):** Verify S1/Seed1 separation prints
6. **Flux platform (Fix #6):** Verify NO separate negative prompt
7. **Any theme (Fix #7):** Verify no Tier 1 adjectives without qualifiers
8. **Rerun (Fix #8):** Same theme twice → verify RERUN prints diversity check

**Expected improvement:**
- P7 compliance: 37% → 95%+
- P2 compliance: 90% → 98%+
- P8 compliance: 50% → 85%+
- P1 compliance: 70% → 95%+
- P10 compliance: 96% → 99%+

---

## VERSION CONTROL

**UPG v9.6 → v9.7**
- Date: [patch application date]
- Changes: 8 critical fixes addressing audit findings
- Compatibility: All v9.6 generations remain valid
- Breaking changes: NONE (only enforcement tightening)

---

*End of UPG v9.7 Patch*