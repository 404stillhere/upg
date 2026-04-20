# UPG PATCH v9.17.2

Apply the following 3 changes to UPG v9.17.1. Each change specifies exact location, BEFORE text (what to find), and AFTER text (what to replace with). Do not modify anything else.

---

## PATCH 1/3: SHALLOW ARC Observation Points for ENVIRONMENTAL RELIEF

**Location:** Section A.4 Creative Lenses, immediately after the existing ENVIRONMENTAL RELIEF paragraph that ends with "...4 different observation points satisfy ≥4 executions rule."

**Action:** ADD the following new paragraph directly after that paragraph:

**ADD:**

SHALLOW ARC OBSERVATION POINTS (PHOTO): When GOAL = commercial or scientific
and PHOTO repeats >2× across the set, each PHOTO slot must use a different
observation point from this list:
- HERO: primary 3/4 product view, full form visible
- ALTERNATE ANGLE: different face (profile, rear, top-down, low angle)
- LIFESTYLE CONTEXT: product in realistic use setting, different location from studio
- MACRO DETAIL: extreme close-up on material/craft quality (may overlap with TEXTURAL)
- E-COMMERCE FLAT: centered isolation, maximum negative space, shelf/catalog ready

If all PHOTO slots use different observation points from this list, ENVIRONMENTAL
RELIEF applies and lens diversity check (HC-22) prints:
`[ENVIRONMENTAL RELIEF: PHOTO×[count] — observation points: [list per slot]]`

If two PHOTO slots share the same observation point → lens diversity violation stands.

SHALLOW ARC S1→S2 DIFFERENTIATION: S2 must differ from S1 in ≥3 of these 5
categories even when showing the same product:
1. Light direction or quality (overhead→side, strobe→window, hard→diffused)
2. Camera distance or framing scale (full product→tight crop, medium→environmental)
3. Background treatment (gradient→contextual, light→dark, studio→lifestyle)
4. Composition axis (centered→rule-of-thirds, horizontal→diagonal, symmetric→asymmetric)
5. Supporting elements (none→surface props, clean→contextual objects)

Same studio + same light + same lens + only crop change = FAIL (1 difference, need ≥3).

---

## PATCH 2/3: SD Platform Entry Angle Reconciliation

**Location:** Section A.4 Creative Lenses, inside the TECHNICAL PARAMETERS BY LENS TYPE subsection, after the "Non-PHOTO execution note" paragraph.

**Action:** ADD the following new paragraph:

**ADD:**

SD PLATFORM ENTRY ANGLE RECONCILIATION: When PLATFORM = SD, positive prompts
begin with quality tags (masterpiece, best quality, etc.) per SD convention.
Entry Angle rule "first sentence MUST realize assigned angle" applies to the
first DESCRIPTIVE content after quality tags, not to absolute character position.

Compliant SD format:
"masterpiece, best quality, highly detailed, [ENTRY ANGLE content opens here]..."

Example — S1=MATERIAL:
✅ "masterpiece, best quality, highly detailed, 18k gold mechanical nightingale..."
   (MATERIAL "18k gold" is first descriptive element after tags)

Example — S1=SCALE:
✅ "masterpiece, best quality, highly detailed, a 15cm clockwork bird..."
   (SCALE "15cm" is first descriptive element after tags)

Quality tags are PLATFORM PREFIX, not prompt content. Entry Angle verification
scans from first non-tag word.

---

## PATCH 3/3: Contrast Distribution Threshold Clarification

**Location:** HARD CHECKS section, HC-20.

**FIND (BEFORE):**

HC-20. Contrast Diversity Check — print `[CONTRAST: S1-5=[H/M/L] — PASS/REVISE/OVERRIDE]`, max 2 per level.
  If user-provided CONTRAST_LEVELS exceed max 2 per level: print `[CONTRAST: S1-5=[levels] — OVERRIDE: [level]×[count] exceeds max 2, user levels honored]` instead of PASS. Do not rewrite — accept user authority, but flag the override.
  If user-provided CONTRAST_LEVELS exceed max 2 per level: print `[CONTRAST: S1-5=[levels] — OVERRIDE: [level]×[count] exceeds max 2, user levels honored]` instead of PASS. Do not rewrite — accept user authority, but flag the override.

**REPLACE WITH (AFTER):**

HC-20. Contrast Diversity Check — print `[CONTRAST: S1-5=[H/M/L] — PASS/REVISE/OVERRIDE]`, max 2 per level.
  ×2 of any level = AT LIMIT, not violation. Print PASS.
  ×3 or more of any level = EXCEEDS LIMIT. If user-provided, print `[CONTRAST: S1-5=[levels] — OVERRIDE: [level]×[count] exceeds max 2, user levels honored]` instead of PASS. Do not rewrite — accept user authority, but flag the override.

---

## VERIFICATION AFTER PATCHING

Run these 3 tests to confirm patches applied correctly:

**Test 1 (Patch 1):** Submit SHALLOW ARC commercial theme with LENS_SEQUENCE containing PHOTO×4.
- Expected: UPG prints `[ENVIRONMENTAL RELIEF: PHOTO×4 — observation points: hero, crop, lifestyle, e-commerce]` if observation points documented in template.
- Fail: UPG prints lens diversity violation despite documented observation points.

**Test 2 (Patch 2):** Submit SD platform theme with ENTRY_ANGLES: S1=MATERIAL.
- Expected: S1 opens "masterpiece, best quality, highly detailed, [material noun]..." and Entry Angle verification prints PASS.
- Fail: UPG flags Entry Angle violation because quality tags precede material noun.

**Test 3 (Patch 3):** Submit theme with CONTRAST_LEVELS: S1=H | S2=H | S3=M | S4=M | S5=L.
- Expected: `[CONTRAST: S1-5=[H,H,M,M,L] — PASS]` (H×2 = at limit).
- Fail: UPG prints OVERRIDE for H×2.

---

## PATCH NOTES

- Version: 9.17.1 → 9.17.2
- Changes: 3 (2 additions, 1 replacement)
- Architecture modified: NO
- Ban Registry modified: NO
- MODE 3 modified: NO
- Module system modified: NO
- Lines added: ~35
- Lines replaced: ~3
- Risk: LOW — all changes are clarifications and boundary definitions, no mechanism restructuring