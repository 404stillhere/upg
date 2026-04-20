
## UPG v9.14 → v9.15 PATCH

### PATCH 1: SLOT VALIDATION STACK — Level 7

**Location:** SLOT VALIDATION STACK, после Level 6

**FIND:**
```
### Level 6: Final
16. **Rendering phrase placement** (non-photo) — present in ≥3/5 slots, in 2nd or 3rd-to-last sentence, NOT in final sentence; **must not contain TIER 1 banned adjectives**
17. **Final sentence physical detail** — must end on visible element; "ending on [X]" ≤2× per set

All checks run silently. Do not print "checks passed." If TRACE=true, print CHECK block after each slot.
```

**REPLACE WITH:**
```
### Level 6: Final
16. **Rendering phrase placement** (non-photo) — present in ≥3/5 slots, in 2nd or 3rd-to-last sentence, NOT in final sentence; **must not contain TIER 1 banned adjectives**
17. **Final sentence physical detail** — must end on visible element; "ending on [X]" ≤2× per set

### Level 7: Density
18. **Detail density per slot** — count and verify:
    - Named materials (brass, limestone, oak — not "metal, stone, wood")
    - Specific colors (cobalt, cerulean, mahogany — not "blue, brown")
    - Physical measurements or scale references
    - Texture descriptors (pitted, polished, fibrous, chalky)
    - Condition indicators (cracked, oxidized, dust-covered)
    
19. **Minimum per slot:**
    | Slot | Role | Min Details |
    |------|------|-------------|
    | S1 | ANCHOR | ≥10 |
    | S2 | TILT | ≥8 |
    | S3 | COLLISION/CONTEXT | ≥9 |
    | S4 | DRIFT/DETAIL | ≥8 |
    | S5 | RUPTURE/CONVERSION | ≥7 |
    
20. **If below minimum** — add details from VISUAL_VOCABULARY, TEXTURE_PALETTE, or MUST_INCLUDE before output

All checks run silently. Do not print "checks passed." If TRACE=true, print CHECK block after each slot.
```

---

### PATCH 2: HARD CHECKS — Priority 1-D

**Location:** HARD CHECKS, после Priority 1-C

**FIND:**
```
### PRIORITY 1-C: Platform
10. Platform Suffix Check (Midjourney: verify 5/5 parameters)
10a. Rendering Phrase Check (non-photo only): ≥3/5 slots contain rendering vocabulary, placed in 2nd/3rd-to-last sentence; **rendering vocabulary must not contain TIER 1 banned adjectives**
11. Setting Fidelity: enforce GEO/ERA/MUST_INCLUDE/MUST_AVOID/VISUAL_VOCABULARY

### PRIORITY 2: Structure
```

**REPLACE WITH:**
```
### PRIORITY 1-C: Platform
10. Platform Suffix Check (Midjourney: verify 5/5 parameters)
10a. Rendering Phrase Check (non-photo only): ≥3/5 slots contain rendering vocabulary, placed in 2nd/3rd-to-last sentence; **rendering vocabulary must not contain TIER 1 banned adjectives**
11. Setting Fidelity: enforce GEO/ERA/MUST_INCLUDE/MUST_AVOID/VISUAL_VOCABULARY

### PRIORITY 1-D: Detail Density
12. **Per-slot detail count** — verify each slot meets minimum (S1≥10, S2≥8, S3≥9, S4≥8, S5≥7)
13. **Series-wide counts:**
    - Named materials: ≥3 unique across 5 slots
    - Specific colors: ≥5 unique across 5 slots
    - Texture descriptors: ≥4 unique across 5 slots
14. **VISUAL_VOCABULARY utilization** — if VV provided, ≥80% of VV elements must appear across series
15. **If any density check fails** — enrich from VV/TEXTURE_PALETTE before output, print: `[DENSITY ENRICHED: S[n] +[X] details]`

### PRIORITY 2: Structure
```

**Note:** Renumber remaining PRIORITY 2 and 3 checks (+4 to all numbers)

---

### PATCH 3: HARD CHECKS renumbering

**FIND:**
```
### PRIORITY 2: Structure
12. Adjacent Slot Uniqueness — ≥3 differences from N-1
13. Entry Angle Execution → see ENTRY ANGLE SYSTEM: Verification
14. Carrying Image & Arc Integrity

### PRIORITY 3: Distribution
15. Contrast Diversity Check — print `[CONTRAST: S1-5=[H/M/L] — PASS/REVISE]`, max 2 per level
16. TRACE Compliance (if TRACE=true)
17. Lens Diversity — ≥4 different, no lens >2×
18. Separation Checks — no seed echo between slots
19. Safety Final
```

**REPLACE WITH:**
```
### PRIORITY 2: Structure
16. Adjacent Slot Uniqueness — ≥3 differences from N-1
17. Entry Angle Execution → see ENTRY ANGLE SYSTEM: Verification
18. Carrying Image & Arc Integrity

### PRIORITY 3: Distribution
19. Contrast Diversity Check — print `[CONTRAST: S1-5=[H/M/L] — PASS/REVISE]`, max 2 per level
20. TRACE Compliance (if TRACE=true)
21. Lens Diversity — ≥4 different, no lens >2×
22. Separation Checks — no seed echo between slots
23. Safety Final
```

---

### PATCH 4: TRACE output update

**Location:** OUTPUT PROTOCOL → TRACE = true

**FIND:**
```
### TRACE = true
After each slot's final version, print:
▸ S[n] CHECK
Setting: [description] — different from previous? [YES / N/A for S1]
Banned phrases: NONE
Shared non-subject props: [list or NONE]
If any check fails → silently rewrite. For Module A, Setting = depicted setting inside poster artwork.
```

**REPLACE WITH:**
```
### TRACE = true
After each slot's final version, print:
▸ S[n] CHECK
Setting: [description] — different from previous? [YES / N/A for S1]
Banned phrases: NONE
Shared non-subject props: [list or NONE]
Detail count: [X] ([breakdown: materials/colors/textures/measurements/conditions])
If any check fails → silently rewrite. For Module A, Setting = depicted setting inside poster artwork.
```

---

