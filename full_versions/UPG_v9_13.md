# UPG v9.13 → v9.14 PATCH INSTRUCTION

**Recipient:** Claude instance with UPG v9.13 loaded
**Source:** 6-pass verification of 30-prompt shawarma test compilation
**Problems addressed:** P1, P3, P6, P7, P8
**Documentation fix:** P10 (not a prompt issue)

---

## EXECUTION PROTOCOL

Apply patches in order. After each patch, confirm with ✅. Do not reorder. Do not paraphrase — use exact text provided.

---

## PATCH 1 → P7 (TIER 1 "soft" escape)

**Problem:** "soft", "softens", "softened" passed through BAN REGISTRY 4 times across 30 prompts. Diagnostic report claimed zero violations.

**Root cause:** TIER 1 scan covers root adjectives but conjugation enforcement for "soft" → "softens/softened" not prioritized like "fine".

**Location:** BAN REGISTRY: TIER 1 ADJECTIVES

**Action:** ADD priority note after "fine" priority scan

### FIND:
```
**"fine" has highest escape rate — scan with priority.**
```

### INSERT AFTER:
```
**"soft" has second-highest escape rate in rendering contexts.** Common violations:
- "soft edge transitions" → "gradual edge transitions" / "blurred edge transitions"
- "soft light" → "diffused light" / "low-contrast light"
- "softens the shadows" → "diffuses the shadows" / "reduces shadow contrast"
- "softened boundaries" → "blurred boundaries" / "feathered boundaries"

If "soft" or any conjugation (softens, softened, softening, softer) appears without Shore A rating or measured material qualifier → REWRITE before output.
```

**Verification:** Search all outputs for `/soft/i` — must be zero or qualified.

---

## PATCH 2 → P8 (Entry Angle S2 pattern swap)

**Problem:** Theme A outputs S2=LOCATION (should be TIME). Theme D outputs S2=TIME (should be LOCATION). Patterns A and D have swapped S2 values in execution.

**Root cause:** Either table implementation error or rotation logic bug.

**Location:** ENTRY ANGLE SYSTEM → Rotation Across Themes

**Action:** ADD verification rule after rotation table

### FIND:
```
| D | SCALE | LOCATION |

Exception: Magic/substance/fictional themes → WEATHER/CULTURAL + TIME
```

### INSERT AFTER:
```
**Rotation Verification (mandatory):**
Before printing Entry Angle line, verify S2 matches table:
- Theme A → S2 must be TIME (not LOCATION)
- Theme B → S2 must be LOCATION
- Theme C → S2 must be LOCATION
- Theme D → S2 must be LOCATION (not TIME)

If mismatch detected → correct to table value before output.

Common error: A↔D S2 swap. If S2=LOCATION for Theme A or S2=TIME for Theme D → WRONG. Fix immediately.
```

**Verification:** Run Theme A — S2 must open with temporal marker. Run Theme D — S2 must open with location preposition.

---

## PATCH 3 → P3 (User Entry Angle override ignored)

**Problem:** When user provides explicit ENTRY_ANGLES in ARC_PLANNING, system follows internal rotation instead of user specification without acknowledgment.

**Root cause:** No precedence rule between user input and rotation system.

**Location:** ENTRY ANGLE SYSTEM → after Rotation Verification block (from Patch 2)

**Action:** ADD user override rule

### INSERT AFTER Patch 2 block:
```
**User Override Rule:**
If STRUCTURED THEME INPUT contains ARC_PLANNING → ENTRY_ANGLES field:
1. User specification takes PRECEDENCE over rotation table
2. Print: `Entry Angle: S1=[user type] | S2=[user type] (USER OVERRIDE — Theme [X] rotation would be [system type]/[system type])`
3. Execute S1/S2 per user specification, not rotation

If ARC_PLANNING → ENTRY_ANGLES is absent or empty:
→ Apply rotation table per theme position
→ Print: `Entry Angle: Theme [X] → S1=[TYPE] | S2=[TYPE]`

DO NOT silently ignore user-provided Entry Angles.
```

**Verification:** Provide input with `ARC_PLANNING: { ENTRY_ANGLES: S1=WEATHER / S2=CULTURAL }` — output must use WEATHER/CULTURAL, not rotation.

---

## PATCH 4 → P1 (Lens sequence identical across RERUNs)

**Problem:** 6 consecutive runs used identical lens sequence PHOTO→CINE→TEXTURAL→PHOTO→PAINT. RERUN HANDLING requires "≥3 changes" between runs.

**Root cause:** Lens sequence from input template copied verbatim without RERUN variance check.

**Location:** RERUN HANDLING

### FIND:
```
Diversity (if RERUN): Diff anchor, Seed1 subject, S1 location, lens seq (≥3 changes), enrichment vocab. S1≠Seed1 (always). Print: `RERUN DETECTED... ALL DIFFERENT:[YES/NO]` + S1/Seed1 line.
```

### REPLACE WITH:
```
Diversity (if RERUN): Diff anchor, Seed1 subject, S1 location, lens seq (≥3 slot changes), enrichment vocab. S1≠Seed1 (always). Print: `RERUN DETECTED... ALL DIFFERENT:[YES/NO]` + S1/Seed1 line.

**Lens Sequence RERUN Enforcement:**
When RERUN detected and input provides LENS_SEQUENCE in ARC_PLANNING:
1. Compare provided sequence to last run's sequence
2. If <3 slots differ → OVERRIDE input sequence with variant
3. Variant generation rules:
   - Swap at least 3 lens assignments
   - Maintain ≥4 unique lenses
   - Maintain no lens >2×
   - S1 lens ≠ previous run S1 lens
   - Prefer: TEXTURAL↔SENSORY, PHOTO↔CINE, PAINT↔SYMBOLIC, ENV↔MINIMAL
4. Print: `Lens sequence: [new] (RERUN OVERRIDE — input was [old], <3 changes)`

If no LENS_SEQUENCE in input → generate fresh sequence with RERUN diversity automatically.
```

**Verification:** Run same theme twice — lens sequences must differ by ≥3 slots.

---

## PATCH 5 → P6 (WORKSHOP category 6/6 consecutive)

**Problem:** All 6 runs used WORKSHOP for Seed 2 category. Rule: "Same ≤2 of 4 consecutive."

**Root cause:** Input template fixed Seed 2 scene. System should override or request alternative when ceiling hit.

**Location:** PHASE 4.1 Seed Generation → SEED 2 CATEGORY TRACKING

### FIND:
```
**SEED 2 CATEGORY TRACKING:** Classify: WORKSHOP/DOMESTIC/TRANSIT/FIELD/COMMERCIAL/BACKSTAGE/RELIGIOUS. Print: `Seed 2 category: [CATEGORY]`. Same ≤2 of 4 consecutive. Ceiling → shift adjacent. (requires SESSION_HISTORY; if not provided, print: `[within-set only]`)
```

### REPLACE WITH:
```
**SEED 2 CATEGORY TRACKING:** Classify: WORKSHOP/DOMESTIC/TRANSIT/FIELD/COMMERCIAL/BACKSTAGE/RELIGIOUS. Print: `Seed 2 category: [CATEGORY]`. Same ≤2 of 4 consecutive. Ceiling → shift adjacent. (requires SESSION_HISTORY; if not provided, print: `[within-set only]`)

**RERUN Category Enforcement:**
When RERUN detected within same conversation (even without SESSION_HISTORY):
1. Track Seed 2 categories used in current conversation
2. If adding current category would exceed ≤2 of 4 consecutive:
   → DO NOT use input's Seed 2 verbatim
   → Generate alternative Seed 2 in different category while preserving:
     - Same technique (TEMPORAL SHIFT, FUNCTIONAL SHIFT, etc.)
     - Same decode time (10-15 sec)
     - Same carrying image relationship
   → Print: `Seed 2 category: [NEW] (RERUN OVERRIDE — [OLD] at ceiling, shifted to [NEW])`
3. Alternative category selection priority:
   - If WORKSHOP at ceiling → prefer DOMESTIC or TRANSIT
   - If DOMESTIC at ceiling → prefer FIELD or BACKSTAGE
   - If TRANSIT at ceiling → prefer COMMERCIAL or FIELD

**Shawarma example alternatives:**
- WORKSHOP (default): mise en place, prep station
- DOMESTIC: home kitchen morning after takeout, containers in fridge
- TRANSIT: delivery bag interior, scooter compartment
- COMMERCIAL: restaurant supply shelf, wholesale packaging
- FIELD: street cart setup before opening, market stall
```

**Verification:** Run same theme 4+ times — Seed 2 category must shift by run 3 at latest.

---

## PATCH 6 → Diagnostic Report accuracy note

**Problem:** Original diagnostic report claimed "zero ban violations across 30 prompts" — this was incorrect (4 "soft" violations existed).

**Action:** This is not a UPG patch. Note for future diagnostic processes:

```
DIAGNOSTIC PROTOCOL AMENDMENT:

When claiming "zero violations" for any ban category:
1. Run explicit regex search for ALL conjugations of each banned term
2. For TIER 1 adjectives, search: [root], [root]s, [root]er, [root]est, [root]ly, [root]en, [root]ens, [root]ed, [root]ing
3. "soft" conjugations: soft, softs, softer, softest, softly, soften, softens, softened, softening
4. Do not claim "zero" without character-level scan

This prevents false confidence in validation reports.
```

---

## VERIFICATION PROTOCOL

After applying Patches 1-5, run this test:

**Test Input:**
```
THEME: Shawarma — the most appetizing dish in the world

GOAL: artistic

SETTING: {
  ARC_PLANNING: {
    ENTRY_ANGLES: S1=WEATHER / S2=MATERIAL
    LENS_SEQUENCE: S1=PHOTO → S2=CINE → S3=TEXTURAL → S4=PHOTO → S5=PAINTERLY
  }
}

[Mark as RERUN if this is 2nd+ generation in conversation]
```

**Expected behaviors:**

| Check | Expected output |
|-------|-----------------|
| Entry Angle | `Entry Angle: S1=WEATHER \| S2=MATERIAL (USER OVERRIDE — Theme [X] rotation would be...)` |
| S1 opening | Weather/atmospheric marker first |
| S2 opening | Material/substance as subject first |
| Lens sequence (if RERUN) | Different from previous by ≥3 slots, with override note |
| Seed 2 category (if 3rd+ RERUN) | Shifts from WORKSHOP to DOMESTIC/TRANSIT/etc |
| "soft" anywhere | ZERO — or qualified with measurement |

Print: `[v9.14 VERIFICATION: PASS/FAIL per check]`

---

## SUMMARY

| Patch | Problem | Severity fixed | Location |
|-------|---------|----------------|----------|
| 1 | P7: "soft" escape | HIGH | BAN REGISTRY |
| 2 | P8: A↔D S2 swap | MEDIUM-HIGH | ENTRY ANGLE SYSTEM |
| 3 | P3: User override ignored | MEDIUM | ENTRY ANGLE SYSTEM |
| 4 | P1: Lens seq no RERUN variance | HIGH | RERUN HANDLING |
| 5 | P6: WORKSHOP ceiling | MEDIUM-HIGH | PHASE 4.1 |
| 6 | Diagnostic accuracy | PROCESS | (not UPG) |

**After all patches: UPG v9.14**

---

## CHANGELOG ENTRY

```
v9.14:
FIX: "soft" conjugations added to priority scan (P7)
FIX: Entry Angle S2 verification prevents A↔D swap (P8)
ADD: User Override Rule for Entry Angles in ARC_PLANNING (P3)
ADD: Lens Sequence RERUN Enforcement with ≥3 slot change requirement (P1)
ADD: RERUN Category Enforcement for Seed 2 with in-conversation tracking (P6)
NOTE: Diagnostic protocol amendment for conjugation-level ban scanning
```

