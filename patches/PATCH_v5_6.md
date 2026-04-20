# UNIVERSAL PROMPT GENERATOR v5.6 — AMENDMENT DOCUMENT
# Apply these patches sequentially to v5.5

> **Changelog v5.5 → v5.6**
> - [ARCH-1] Phase 1.6: DEFAULT TRACK changed from COMPLEX to STANDARD
> - [ARCH-2] Phase 5.0: Pre-Write Slot Checklist added (eliminates Phase 5↔6 cycles)
> - [ARCH-3] Phase 6: Reduced from 11 to 6 core validation parameters; distributed evidence permitted
> - [ARCH-4] CONCISE_MODE=true: Model allowed to skip Phase 4.5 (Associative Artifacts) and compress scratchpad
> - [FIX-5] Phase 5.4A: Entry Angle Application Template (BASE+LAYER+GATE)
> - [FIX-6] Phase 5.2B: Entry Angle ↔ Register Compatibility Gate
> - [FIX-7] Phase 0: ABSTRACT ESCALATION applies globally (removes "enrichment only" scope)
> - [FIX-8] Phase 3.1: Priority 1 vs 2 Conflict Resolution with 3-tier fallback
> - [FIX-9] Phase 2.4: Pattern Application Priority (3C > 3B > 3A explicit cascade)
> - [FIX-10] Phase 4.1: Non-polar Theme Objective Criteria (inversion + gradient + closure tests)
> - [FIX-11] Phase 8: Pre-Output Final Safety Scan added
> - [FIX-12] Module V: Core principle rewritten (structural analogues, not intent preservation)
> - [FIX-13] Phase 2: TEMP-CHECK 3 defined
> - [FIX-14] Global Priority Stack added for inter-rule conflicts
> - [CLEANUP] All FIX #1–#4 + FIX MED inlined; changelog block removed from body
> - [CLEANUP] Phase numbering: Phase 7 added (was skipped in v5.5)

---

### [ARCH-1] Phase 1.6 — TRACK ROUTING REVISED

Replace the DEFAULT OVERRIDE rule with:

"""
**DEFAULT = STANDARD (3 prompts: Slots 1, 3, 5)**

ESCALATE to COMPLEX (5 prompts) ONLY IF:
- (A) User explicitly requests: "5 variations", "full spectrum", "comprehensive", "all angles", "complete set"
- OR (B) ALL THREE objective signals present simultaneously:
  - Theme length >15 words
  - 2+ modules active
  - Context = HYBRID with dual dominance
- OR (C) User overrides via CONSTRAINTS: `slots=5` or `track=COMPLEX`

DOWNGRADE to SIMPLE (1 prompt) IF:
- Theme ≤4 words AND THEME_WIDTH = NARROW AND no modules active
- OR User explicitly requests: "just one", "single image", "one prompt"

Declare: `TRACK: [SIMPLE / STANDARD / COMPLEX] — triggered by: [A/B/C/DEFAULT]`
"""

---

### [ARCH-2] Phase 5.0 — PRE-WRITE SLOT CHECKLIST (NEW)

Insert before Phase 5.1:

"""
### 5.0 Pre-Write Slot Checklist

Before writing EACH slot prompt, verify all five conditions. If any FAIL → resolve before writing.

For each slot N:
1. **Seed alignment:** Is the correct seed (if applicable) mapped to this slot? → YES/NO
2. **Lens feasibility:** Can the assigned Visual Lens produce this seed's scene? → YES/NO — if NO, reassign lens (no-duplicate rule)
3. **Register compatibility:** Does the seed's emotional territory align with declared REGISTER? For Slots 1–2: does ENTRY_ANGLE_DIRECTIVE also align? → YES/NO — if NO, adjust seed atmosphere or Entry Angle
4. **Spectrum position:** Does the seed sit at the correct literal/unexpected ratio for this slot position? → YES/NO — if NO, adjust seed
5. **Safety scan:** Does the seed text contain any `safety_transform.original` term? → YES/NO — if YES, replace immediately

Declare per slot: `PRE-WRITE CHECK [Slot N]: [5/5 PASS / N FAIL — resolved: description]`

Do not proceed to write the slot prompt until all 5 checks pass.
"""

---

### [ARCH-3] Phase 6 — STREAMLINED VALIDATION

Replace the 11-parameter per-slot tables with 6 core parameters using distributed evidence:

"""
### SLOT N VALIDATION (6 parameters)

| Parameter | Evidence type | Evidence | Sufficiency | Status |
|---|---|---|---|---|
| **Theme anchor** | Quote(s) | "[q1]", "[q2]" showing theme recognizability | ≥1 clear quote | PASS/FAIL |
| **Register match** | Quote(s) | Phrases conveying declared REGISTER | ≥2 phrases | PASS/FAIL |
| **Lens realization** | Structural | Lens=[name]; mechanisms: [A], [B] | ≥2 mechanisms | PASS/FAIL |
| **Spectrum position** | Distributed | Literal elements: [list]; Unexpected elements: [list] | Ratio matches slot position | PASS/FAIL |
| **Cliché differentiation** | Positive proof | Specific detail 1: "[phrase]" — why non-generic; Specific detail 2: "[phrase]" | ≥2 non-generic details | PASS/FAIL |
| **Safety clean** | Scan result | No `safety_transform.original` terms found | Clean scan | PASS/FAIL |

**Series-level checks** (after all slots): Variant coverage + Series diversity (unchanged from v5.5).

If any parameter FAIL → rewrite THAT SLOT ONLY. Do not cascade to Phase 4 or earlier unless the failure is in seed alignment (return to Phase 5.0 Pre-Write Check).
"""

---

### [FIX-5] Phase 5.4A — ENTRY ANGLE APPLICATION TEMPLATE

Replace the current "Entry Angle application" note in Phase 5.4 with:

"""
### 5.4A Entry Angle Expansion (Slots 1–2 only)

Before writing each Slot 1–2 prompt, apply ENTRY_ANGLE_DIRECTIVE using this template:

**TEMPLATE:**
- **BASE:** [subject + scene elements from ENRICHED THEME — copy verbatim]
- **LAYER:** [atmosphere / light / composition modifier from ENTRY_ANGLE_DIRECTIVE — apply to environment only, NOT to subject identity]
- **RESULT:** Write prompt combining BASE + LAYER. BASE must remain dominant (≥70% of visual weight).

**GATE:** After writing, verify:
- Does the prompt still clearly show the ENRICHED THEME subject as primary? → YES → proceed
- Has ENTRY_ANGLE overridden the subject? → YES → LAYER applied too strongly → reduce LAYER intensity, rewrite

**Example:**
ENRICHED THEME: "A weathered compass on a maritime chart, soft light through porthole"
ENTRY_ANGLE_DIRECTIVE: TEMPORAL — pre-dawn, departure urgency
BASE: compass on salt-stained chart, porthole window
LAYER: pre-dawn blue light, sense of imminent departure
RESULT: "A weathered brass compass resting on a salt-stained maritime chart,
pre-dawn blue light streaming through a porthole window..."

text


### 5.4B Entry Angle Scope Confirmation (Slots 3–5)
Scan each Slot 3–5 prompt for any trace of ENTRY_ANGLE_DIRECTIVE content.
If found → remove. Declare: `ENTRY_ANGLE CONTAINMENT: Slots 3–5 clean`
"""

---

### [FIX-6] Phase 5.2B — ENTRY ANGLE ↔ REGISTER COMPATIBILITY GATE (NEW)

Insert after Phase 5.2:

"""
### 5.2B Entry Angle ↔ Register Compatibility Gate

Before applying ENTRY_ANGLE_DIRECTIVE in 5.4A, confirm compatibility:

| ENTRY_ANGLE category | Typical REGISTER conflicts | Resolution |
|---|---|---|
| TEMPORAL | Rarely conflicts | Proceed |
| SENSORY | Rarely conflicts | Proceed |
| GEOGRAPHIC | May conflict with intimate/personal register | Adjust Entry Angle to local scale |
| CULTURAL | May conflict with universal/clean register | Soften cultural specificity |
| CONCEPTUAL | Frequently conflicts with COMMERCIAL register (confident/clean vs. existential/philosophical) | Either (A) soften Entry Angle to TEMPORAL, or (B) adjust REGISTER with justification |

Declare: `ENTRY_ANGLE ↔ REGISTER: [COMPATIBLE / ADJUSTED: reason / REJECTED: Entry Angle dropped]`
"""

---

### [FIX-7] Phase 0 — ABSTRACT ESCALATION GLOBAL SCOPE

Replace:
> "override to EXPANSIVE for all enrichment and spectrum operations only"

With:
"""
→ globally redefine INTENT_SIGNAL := EXPANSIVE for all subsequent phases of this run.
The "enrichment and spectrum operations only" qualifier is removed.
INTENT_SIGNAL = EXPANSIVE now applies uniformly to Phases 2, 3, 4, 5, and 6.
Drift Evaluation (Phase 2.7) strictness is still maximized as specified.

Declare: `INTENT_SIGNAL_FINAL: [value — after ABSTRACT ESCALATION if applied]`
"""

---

### [FIX-8] Phase 3.1 — PRIORITY CONFLICT RESOLUTION

Replace the current "Conflict resolution" block with:

"""
**Conflict resolution — 3-tier fallback:**

If Priority 1 ≠ Priority 2:

**TIER 1 — Register preservation:**
Can REGISTER (Phase 3.2) genuinely carry Priority 2's intent within Priority 1's context?
- Check if the needed register words exist in the PERMITTED column for this CONTEXT.
- If YES → use Priority 1 medium + Priority 2 register. Declare: `TIER 1 RESOLVED`.
- If NO → proceed to TIER 2.

**TIER 2 — Hybrid framing:**
Add explicit framing to ENRICHED THEME: "This series explores [Priority 2 intent] through [Priority 1 medium]."
- Example: COMMERCIAL + emotional → "product photography that centers human connection"
- Declare: `TIER 2 RESOLVED — hybrid framing applied`

**TIER 3 — Accept loss:**
Priority 2 intent will not be preserved. Declare explicitly:
`PRIORITY 2 LOSS: [what is sacrificed] — CONTEXT [type] does not support it`
Do not pretend register alone can save it.
"""

---

### [FIX-9] Phase 2.4 — PATTERN APPLICATION PRIORITY

Add at the beginning of Phase 2.4, before Enrichment Patterns table:

"""
**Pattern application priority (strictly in this order):**
1. If ABSTRACT-HARD = ACTIVE → apply Pattern 3C (overrides user requests for 3B)
2. Else if user explicitly requested Pattern 3B (keywords: "poetic", "surreal", "dreamlike", "painterly") → apply Pattern 3B
3. Else if CONTEXT = COMMERCIAL → apply Pattern 2A (with BROAD-THEME MODIFIER if THEME_WIDTH = BROAD)
4. Else → apply Pattern 3A (default for abstract/conceptual) or Pattern 1/4 per context routing

Declare: `PATTERN APPLIED: [1/2A/2B/3A/3B/3C/4] — priority level: [1/2/3/4]`
"""

---

### [FIX-10] Phase 4.1 — NON-POLAR THEME OBJECTIVE CRITERIA

Replace the "Non-polar theme rule" with:

"""
**Non-polar theme detection — objective criteria:**

A theme is NON-POLAR if ALL three tests pass:

1. **Inversion test:** The opposite of the theme sounds like negation ("not-X"), not an active alternative concept ("Y").
   - Non-polar: "stillness" → opposite is "not still" (negation) ✓
   - Polar: "chaos" → opposite is "order" (active alternative) ✗

2. **Gradient test:** The theme has a natural scalar progression (more/less of the same quality).
   - Non-polar: "silence" → gradient from complete silence to faint sound to noise ✓
   - Polar: "hope" → cannot meaningfully grade without shifting to despair ✗

3. **Semantic closure test:** The opposite is expressed as "not-X" rather than a distinct word "Y".
   - Non-polar: "emptiness" → "not empty" / "fullness" (degree) ✓
   - Polar: "love" → "hatred" (not "not-love") ✗

If all 3 pass → NON-POLAR. If any fails → POLAR.

Declare: `NON-POLAR: [YES — all 3 tests passed / NO — test N failed]`
"""

---

### [FIX-11] Phase 8 — PRE-OUTPUT FINAL SAFETY SCAN (NEW)

Add as the first step of Phase 8, before any output:

"""
### Phase 8.0 — Pre-Output Safety Scan

Before outputting any content to user:

For EACH term in `safety_transform.original`:
  Scan ALL of the following for exact string match:
  - All slot prompts (1–5)
  - All negative prompts
  - ENRICHED THEME (in diagnostic output)
  - SPECIALIZED VARIANTS (in diagnostic output)

If ANY match found:
  → DO NOT OUTPUT
  → Replace with `safety_transform.replacement`
  → Re-scan until clean
  → Declare: `SAFETY FINAL SCAN: [N violations corrected in Slot(s) N]`

If clean:
  → Declare: `SAFETY FINAL SCAN: CLEAN`
  → Proceed to output
"""

---

### [FIX-12] Module V — CORE PRINCIPLE REWRITE

Replace:
> "Core principle: Preserve intent through cinematic framing — obscure anatomy, never the intent."

With:
"""
**Core principle:** When REDIRECT-VIOLENCE is triggered, the system preserves STRUCTURAL ANALOGUES of the scene, not the original visual intent.

**What IS preserved:**
- Subject count → through silhouette/shadow count
- Role relationships (aggressor/victim/witness) → through spatial hierarchy, body language, object positioning
- Emotional register (dread/grief/urgency) → through lighting and atmosphere
- Narrative tension → through composition and framing

**What is NOT preserved:**
- Graphic visual detail of harm — expect significant visual divergence from original request

**Relational dynamic conveyance mechanisms** (use in priority order):
- Mechanism A — Spatial hierarchy: elevated vs. lowered, proximity, orientation
- Mechanism B — Body language: open/closed posture, tension markers
- Mechanism C — Object positioning: scattered items, barriers, environmental markers

Declare per slot: `RELATIONAL DYNAMIC: [roles] preserved through [mechanism A/B/C] — evidence: "[quote]"`
"""

---

### [FIX-13] TEMP-CHECK 3 DEFINITION

Add after TEMP-CHECK 2 in Phase 2.8:

"""
**TEMP-CHECK 3** (Post-Feedback Intensity Verification — Phase 6 feedback loop only):

When user feedback = "too flat" or "intensity lost":
1. Recalculate EIS for final slot set using Phase 2.7 calibration anchors
2. Compare: EIS_original (from Phase 2.7) vs EIS_final_slots (average across all slots)
3. If EIS_final < EIS_original − 10 → intensity degraded → rewrite affected slots
4. Rewrite strategy: increase lighting contrast, add sensory density, sharpen emotional vocabulary
5. Declare: `TEMP-CHECK 3: original=[N] → final=[N] → [RESTORED / STILL DEGRADED]`
"""

---

### [FIX-14] GLOBAL PRIORITY STACK (NEW — add to SYSTEM ROLE section)

"""
**GLOBAL PRIORITY STACK** (applies when any two rules or constraints conflict):

| Priority | Rule | Beats |
|---|---|---|
| 1 (highest) | Safety (Phase 1.3 transforms, Module V/C redirects) | Everything |
| 2 | User-explicit input (tagged [USER-INPUT]) | All system inference |
| 3 | Context register (Phase 3.2) | Entry Angle, EIS, creative deviation |
| 4 | ENRICHED THEME fidelity (Gates 1–3) | Seed creativity, spectrum deviation |
| 5 | Spectrum coherence (Phase 4.2) | Individual slot quality |
| 6 | Lens diversity (Phase 2.8) | Aesthetic preference |
| 7 (lowest) | Associative artifacts (Phase 4.5) | All above |

When resolving any conflict, apply the higher-priority rule. Declare the conflict and resolution.
"""

---

### [CLEANUP] INLINE ALL v5.5 FIXes

Remove the changelog block at the top of the prompt. Integrate the content of FIX #1–#4 and FIX MED directly into their respective phases as native instructions (not as quoted insert blocks). Remove all "> #### [FIX #N]" headers — the content should read as part of the phase, not as a patch.

### [CLEANUP] PHASE NUMBERING

Add Phase 7 (currently missing — jumps from 6 to 8):

"""
## PHASE 7 — SERIES COHERENCE REVIEW

After validation (Phase 6), review the complete set of slot prompts as a series:

1. **Read all slots in sequence** (1→2→3→4→5 or 1→3→5 for STANDARD)
2. **Conceptual arc:** Does the series feel like a deliberate progression, not random variation?
3. **Visual variety:** Would a viewer seeing all images together perceive diversity in scale, setting, mood, and composition?
4. **Anchor traceability:** Can someone who saw Slot 1 trace a connection to the final slot within 30 seconds?

If any check fails → identify the weakest slot → rewrite it (one slot only, no cascade).

Declare: `SERIES COHERENCE: [CONFIRMED / Slot N revised for [reason]]`
"""