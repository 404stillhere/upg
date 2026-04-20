# 📋 PROMPT-INSTRUCTION FOR FIX IMPLEMENTATION

---

## CONTEXT

You are receiving UPG v9.11 system prompt for minor fixes. Two issues identified:
1. Decision Block line limit (25 → 35 lines)
2. Redundant "fine" subsection deletion

Additionally, three output-level issues require documentation update only (not prompt changes):
1. Contrast distribution guidance (ensure max 2 per level)
2. MUST_AVOID enforcement note (S4 passenger issue)
3. Entry Angle simile awareness (prefer "functions as" over "like")

---

## TASK

Apply fixes to UPG v9.11 prompt text. Make ONLY the specified changes. Preserve all working mechanisms.

---

## FIX #1: Decision Block Line Limit

**Location:** OUTPUT PROTOCOL section, CONCISE_MODE omitted subsection

**Current text:**
```
Output a Decision Block (≤25 lines for FULL ARC, or ≤30 lines if RERUN block present; ≤15 for SHALLOW ARC; group single-value fields onto shared lines separated by pipes)
```

**Replace with:**
```
Output a Decision Block (≤35 lines for FULL ARC, or ≤40 lines if RERUN block present; ≤20 for SHALLOW ARC; group single-value fields onto shared lines separated by pipes)
```

**Verification:**
- [ ] Only numbers changed: 25→35, 30→40, 15→20
- [ ] No other words modified
- [ ] Grouping instruction preserved

---

## FIX #2: Delete "fine" Priority Scan

**Location:** A.2.9 Camera-Visible Prose, after Tier 1 Micro-Scan

**Current text (DELETE ENTIRELY):**
```
**Priority scan for "fine":** This adjective has the highest escape rate. Common violations:
- "fine dust" → "particulate dust" or "ite powder"
- "fine powder" → "ite powder" or "ite particulate"
- "fine lines" → "hairline" or "narrow"
- "fine detail" → "granular detail" or specific description

If "fine" appears without physical qualifier (measurement, material comparison), REWRITE before output.
```

**Replace with:**
```
[ENTIRE SUBSECTION DELETED — "fine" is already covered by Tier 1 Micro-Scan above]
```

**Verification:**
- [ ] Entire subsection removed (heading + 4 bullet examples + enforcement instruction)
- [ ] Tier 1 Micro-Scan still lists "fine" in its banned adjective list
- [ ] No other content affected

---

## FIX #3: Add Contrast Distribution Reminder (NEW)

**Location:** Hard Checks Priority 3, after check #13 (Contrast Diversity)

**Current text:**
```
Contrast Diversity | After all slots | Max 2 per H/M/L level | ≤2 per level | Rewrite slot
```

**Add guidance note after this line:**
```
Note: Distribute levels for variety. Prefer balanced spread (e.g., H/M/L/M/H or H/M/H/L/M) over clustering at one level.
```

**Verification:**
- [ ] Note added immediately after Contrast Diversity check line
- [ ] Does not alter the check itself
- [ ] Provides tactical guidance for execution

---

## FIX #4: Add MUST_AVOID Enforcement Note (NEW)

**Location:** SETTING parameter description, MUST_AVOID section

**Current text ends with:**
```
For each trap, provide replacement standard in VV.
```

**Add after this:**
```

**Strict enforcement:** "Other people" means zero human figures or silhouettes except the carrying image subject. Background presence (e.g., "distant passenger") violates this rule unless explicitly permitted in SETTING. If realism requires human context (public spaces), use traces instead: empty seat, forgotten item, security camera implies staff presence.
```

**Verification:**
- [ ] Added as new paragraph after Detail Traps section
- [ ] Provides alternative approaches for human-context spaces
- [ ] Does not change existing MUST_AVOID examples

---

## FIX #5: Entry Angle Simile Warning (NEW)

**Location:** B.2 Theme Enrichment, Entry Angle Execution Guidance section, SCALE compliance check

**Current text ends with:**
```
❌ Non-compliant (actually LOCATION):
- "Lunokhod-2 stands at the edge..." (location leads)
- "An abandoned forge occupies..." (location leads)
- "The sakura trunk fills..." (subject leads)
```

**Add after this:**
```

**Simile awareness:** Avoid "like [noun]" constructions in Entry Angle execution. "The hoodie sits like armor" reads as comparison, not physical state. Prefer "functions as," "serves as visible," or direct description. Exception: tactile similes with material properties ("soft as fleece" = material comparison, permitted if VV specifies).
```

**Verification:**
- [ ] Added as new paragraph in Entry Angle section
- [ ] Distinguishes banned simile from permitted material comparison
- [ ] Does not alter SCALE/LOCATION guidance above

---

## PRESERVATION CHECKLIST

**DO NOT MODIFY:**
- [ ] Zero Tolerance Ban System (A.2.9)
- [ ] FULL ARC Slot Structure (A.3)
- [ ] Visual Vocabulary Enforcement (SETTING, Hard Checks #8)
- [ ] S5 Environmental Departure rules (A.3)
- [ ] Adjacent Slot Uniqueness (A.2.7, Hard Checks #9)
- [ ] Lens Diversity (A.4, Hard Checks #15)
- [ ] Final Sentence test (A.2.9, Hard Checks #2)
- [ ] Rendering Tail Ban (A.4)
- [ ] Tier 1 Micro-Scan list (must still include "fine")
- [ ] Any other mechanism from Block 1.5 of Diagnostic Report

---

## POST-FIX VERIFICATION PROTOCOL

After implementing all fixes:

### 1. Token count check
- [ ] Measure prompt length before and after
- [ ] Expected change: ~+60 tokens (new guidance) - 80 tokens (deleted "fine") = **-20 tokens net**

### 2. Mechanism integrity check
- [ ] Search prompt for all 10 preserved elements from Block 1.5
- [ ] Verify each is unchanged

### 3. Test generation (optional but recommended)
- [ ] Run 1 test with same "Dead Inside Girl Avatar" input
- [ ] Verify: Decision Block ≤35 lines, no "fine" in output, contrast distributed H/M/H/L/M or similar
- [ ] Check S4 for "other people" (should be absent)

---

## VERSION UPDATE

After successful implementation:

**Current:** Universal Prompt Generator v9.11

**Update to:** Universal Prompt Generator v9.12

**Change location:** SYSTEM ROLE first line

**Changelog entry (add to end of prompt):**
```
---
## CHANGELOG

### v9.12 (2025-01-XX)
- Decision Block limits: 25→35 (FULL), 30→40 (RERUN), 15→20 (SHALLOW)
- Removed redundant "fine" priority scan subsection (covered by Tier 1)
- Added contrast distribution guidance note
- Added MUST_AVOID strict enforcement note for "other people"
- Added Entry Angle simile awareness warning
- Net token change: -20 (efficiency improvement)
```

---

## FINAL CONFIRMATION

Before delivering updated prompt:
- [ ] All 5 fixes applied
- [ ] No unintended changes to preserved mechanisms
- [ ] Version number updated to v9.12
- [ ] Changelog added
- [ ] Token count verified

**Estimated implementation time:** 5-10 minutes

**Risk level:** Low (all changes are additive guidance or limit adjustments)

---

**END OF INSTRUCTION**

Ready to receive UPG v9.11 text for fix implementation.