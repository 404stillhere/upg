# UPG v9.8 → v9.9 TRANSFORMATION PROMPT

---

## INSTRUCTIONS FOR CLAUDE

You are updating the Universal Prompt Generator from v9.8 to v9.9. Apply ALL fixes below precisely. Preserve all unchanged sections exactly as they appear in v9.8.

---

## FIX REGISTRY

### FIX #1: Decision Block Enforcement [CRITICAL]

**LOCATION:** Add NEW section immediately before "## HARD CHECKS"

**ADD:**

```
## DECISION BLOCK ENFORCEMENT (MANDATORY)

**This check executes BEFORE any prompt writing.**

Before writing Slot 1, verify the Decision Block has been printed. If Decision Block is absent, STOP and print it now.

**Decision Block is NEVER optional.** Even under CONCISE_MODE = true, a Routing Summary must appear before prompts.

**Verification sequence:**
1. Scan your output so far
2. Is Decision Block (or Routing Summary for CONCISE_MODE) present?
3. If NO → print it immediately before continuing
4. If YES → proceed to prompts

**After Decision Block, print confirmation:**
`[DECISION BLOCK: COMPLETE — proceeding to prompts]`

**If this confirmation line is absent before Slot 1, the output is invalid.**
```

---

### FIX #2: HARD CHECKS Restructure [CRITICAL]

**LOCATION:** Section "## HARD CHECKS (MANDATORY — RUN FOR EACH SLOT)"

**REPLACE ENTIRE SECTION WITH:**

```
## HARD CHECKS (MANDATORY — RUN FOR EACH SLOT)

Execute these checks for EVERY slot BEFORE adding it to output.
If any check fails, rewrite the slot. Never output a failing slot.

**═══════════════════════════════════════════════════════════════**
**PRIORITY 0 — STRUCTURAL PREREQUISITE (execute ONCE before S1)**
**═══════════════════════════════════════════════════════════════**

0. **Decision Block Presence:** Verify Decision Block (or Routing Summary if CONCISE_MODE = true) has been printed. If absent → STOP, print Decision Block, then print `[DECISION BLOCK: COMPLETE — proceeding to prompts]` before writing any slot.

**═══════════════════════════════════════════════════════════════**
**PRIORITY 1 — NON-NEGOTIABLE (must pass before output)**
**═══════════════════════════════════════════════════════════════**

1. **Zero Tolerance Bans:** Scan for all banned phrases (suggests/implying, making X [adj], reads as, turning into, as if/as though, begins to, the viewer, evoking, creates a sense of, etc.). If found → rewrite.

2. **Final Sentence Content:** Verify final sentence describes visible element (surface, edge, light, material, position), not achievement/demonstration/style. For COMMERCIAL: no positioning language (sellable, marketplace ready, retail-ready). If violated → rewrite final sentence.

3. **Rendering Tail Scan (MANDATORY):** Scan the final sentence of each slot for these BANNED patterns:
   
   | BANNED FINAL PATTERNS | EXAMPLE |
   |-----------------------|---------|
   | "rendered with [X]" | "rendered with matte precision" |
   | "rendered in [X]" | "rendered in the tradition of" |
   | "in the manner of [X]" | "in the manner of Vuillard" |
   | "in the tradition of [X]" | "in the tradition of Bonnard" |
   | "[X] rendering" | "matte rendering" |
   | "with [X] precision" | "with documentary precision" |
   | "atmospheric perspective wash" | — |
   | "tactile surface simulation" | — |
   | "digital precision" | — |
   | "controlled edge softness" (at end) | — |
   | "sharp material edges" (at end) | — |
   
   **If ANY pattern found in final sentence → REWRITE to describe visible element.**
   
   **PERMITTED final content:**
   - Camera specs: "85mm f/2.8"
   - Physical detail: "dust gathered along the seam"
   - Light behavior: "shadow pooling at the base"
   - Material state: "rust blooming through the paint"
   - Spatial position: "the nearest shard offset left"

4. **Banned Language Scan:** Check for: abstract nouns (stillness, silence, tension, etc. — full list in A.2), banned generic adjectives. Apply fallback test: can you point to it in a photograph? If no → delete and replace.

5. **Tier 1 Adjective Micro-Scan:** Scan for: soft, clean, fresh, fine, smooth, gentle, subtle, elegant, delicate, simple. If found without material-specific qualifier → replace with specific descriptor from A.2 substitution list.

6. **Length Check:** For Midjourney: verify sentence count (≤3 for S1-S4, ≤4 for S5) and element count (≤5). See MIDJOURNEY MODE. For other platforms: apply sentence-count guideline from A.2 Rule 6. If prompt feels overlong → remove least essential sentence.

7. **Platform Suffix Check (Midjourney only):** Verify each of 5 prompts ends with --ar [ratio] --v 6 --style raw --s 50. If any prompt lacks suffix, append before output.

**═══════════════════════════════════════════════════════════════**
**PRIORITY 2 — STRUCTURAL (must pass for arc integrity)**
**═══════════════════════════════════════════════════════════════**

8. **Adjacent Slot Uniqueness:** Slot N differs from Slot N−1 in ≥3 of: setting, light source type, framing scale, lens, mood. Core subject may repeat for single-object/product themes.

9. **Entry Angle Execution:** First sentence of S1 and S2 realizes the selected Entry Angle as visible, camera-describable detail. If absent → rewrite opening.

10. **Module Compliance:** All activated modules (A, B, D) meet their required specifications. Module B: 4 minimums per slot. Module A: flat poster format unless GOAL specifies mockup.

11. **Carrying Image & Arc Integrity:** 
    - S1–S3: carrying image is primary visual subject
    - S4 (FULL ARC): may recede but slot still reads as being about the carrying image
    - S5: trace/environmental imprint (FULL ARC) or CONVERSION (SHALLOW ARC)
    - Series arc: theme traceable from S1 through S5
    - World Response (fantastical themes): ≥2 slots show everyday objects reacting

**═══════════════════════════════════════════════════════════════**
**PRIORITY 3 — QUALITY (final polish)**
**═══════════════════════════════════════════════════════════════**

12. **Contrast Diversity Check:** After writing S5, verify contrast distribution. No level (HIGH/MEDIUM/LOW) may appear more than twice. If any level appears 3+ times → revise the most flexible slot. Print after S5:
    `[CONTRAST: S1=[H/M/L] S2=[H/M/L] S3=[H/M/L] S4=[H/M/L] S5=[H/M/L] — PASS/REVISE]`

13. **TRACE Compliance (if TRACE = true):** For each slot's final version: setting differs from previous, banned phrases absent, secondary prop overlap minimal.

14. **Lens Diversity:** ≥4 of 5 slot executions are genuinely different. No lens appears >2x. No two adjacent slots share same lens unless explicitly permitted. Lens sequence not identical to previous themes in conversation.

15. **Separation Checks:** No final prompt closely echoes or paraphrases: (a) enriched theme text, (b) any Seed text. Each slot uses independent sentence structure, distinct vocabulary, own dominant image.

16. **Safety Final:** No names of living private persons, copyrighted IP, explicit content, or unsafe terms in any slot.
```

---

### FIX #3: CONCISE_MODE Enforcement [HIGH]

**LOCATION:** Section "### CONCISE_MODE = true" within OUTPUT PROTOCOL

**REPLACE:**

```
### CONCISE_MODE = true
Output only a Routing Summary (≤3 lines): Scope | Context | Medium | Arc | Modules.
If conversation tracking assigns a fixed Entry Angle pair to Slots 1–2, append it as one additional line.
Follow immediately with five prompts.
```

**WITH:**

```
### CONCISE_MODE = true

**MANDATORY OUTPUT SEQUENCE:**

1. **Print Routing Summary (required):**
   `Routing: [Scope] | [Context] | [Medium] | [Arc] | [Modules or NONE]`

2. **If Entry Angle rotation active, print:**
   `Entry Angle: [Type]: "[element]" | [Type]: "[element]"`

3. **Print confirmation:**
   `[ROUTING COMPLETE — proceeding to prompts]`

4. **Then write five prompts.**

**VERIFICATION:** If output begins with a prompt paragraph (not "Routing:"), STOP and prepend Routing Summary. An output without Routing Summary when CONCISE_MODE = true is invalid.

CONCISE_MODE controls planning-layer output format only. It does not suppress enforcement mechanisms. When PLATFORM = Midjourney and CONCISE_MODE = true, sentence/element count verification lines are still printed after each slot (see MIDJOURNEY MODE).
```

---

### FIX #4: Midjourney Verification Enforcement [HIGH]

**LOCATION:** Section "### 5.2 Platform Suffixes" — Midjourney subsection

**FIND:**

```
**SUFFIX VERIFICATION (mandatory):** After writing all 5 prompts, confirm each ends with the parameter string. Print:
`[SUFFIX CHECK: 5/5 prompts end with --ar [ratio] --v 6 --style raw --s 50 — PASS]`
If any prompt lacks suffix, add it before final output.
```

**REPLACE WITH:**

```
**SUFFIX VERIFICATION (MANDATORY — execute after S5):**

1. Scan all 5 prompts for suffix: `--ar [ratio] --v 6 --style raw --s 50`
2. Count matches
3. Print verification:
   - If 5/5: `[MJ SUFFIX: 5/5 ✓]`
   - If <5/5: `[MJ SUFFIX: X/5 — FIXING]` → Add missing suffixes → Print: `[MJ SUFFIX: 5/5 ✓]`

**If this verification line is absent after Midjourney output, the output is incomplete.**
```

---

### FIX #5: Midjourney Sentence Verification Enforcement [HIGH]

**LOCATION:** Section "### Verification (Midjourney only)" within MIDJOURNEY MODE

**FIND:**

```
### Verification (Midjourney only)
After each slot, print:
`[S[n]: [X] sentences, [Y] elements — PASS]`

If >3 sentences (S1-S4) or >4 sentences (S5) or >5 elements: rewrite before proceeding.
```

**REPLACE WITH:**

```
### Verification (Midjourney only)

**MANDATORY:** After each slot, print sentence/element count:
`[S[n]: [X] sentences, [Y] elements — PASS]`

**Limits:**
- S1-S4: max 3 sentences, max 5 elements
- S5: max 4 sentences, max 5 elements

**If over limit:** Rewrite slot, then print verification showing PASS.

**If verification lines are absent from Midjourney output, the output is incomplete.**

This verification is NOT suppressed by CONCISE_MODE or any other parameter.
```

---

### FIX #6: Anti-Anchor Self-Check [MODERATE]

**LOCATION:** Section "### A.4 Creative Lenses" — after "**ANTI-ANCHOR RULE (rolling window):**"

**FIND:**

```
**ANTI-ANCHOR RULE (rolling window):** Track last 4 FULL ARC themes in conversation.
- S1 must NOT be PHOTOREALISTIC in more than 2 of last 4
- S2 must NOT be CINEMATIC in more than 2 of last 4
If threshold reached, select from: TEXTURAL, SENSORY, PAINTERLY, ENVIRONMENTAL, SYMBOLIC, MINIMALIST, GRAPHIC for affected slot.
```

**REPLACE WITH:**

```
**ANTI-ANCHOR RULE (rolling window):** Track last 4 FULL ARC themes in conversation.
- S1 must NOT be PHOTOREALISTIC in more than 2 of last 4
- S2 must NOT be CINEMATIC in more than 2 of last 4
If threshold reached, select from: TEXTURAL, SENSORY, PAINTERLY, ENVIRONMENTAL, SYMBOLIC, MINIMALIST, GRAPHIC for affected slot.

**MANDATORY Decision Block line (FULL ARC only):**
Before assigning S1 lens, count PHOTOREALISTIC S1 uses in last 4 FULL ARC themes. Print in Decision Block:
`Anti-Anchor: [X]/4 PHOTO S1 in last 4 → S1 = [assigned lens] [OK/FORCED ALTERNATIVE]`

If count = 2 and you would assign PHOTOREALISTIC → select alternative and mark "FORCED ALTERNATIVE".
```

---

### FIX #7: Version Header Update [ADMINISTRATIVE]

**LOCATION:** First line of prompt

**CHANGE:**

```
# UNIVERSAL PROMPT GENERATOR v9.8
```

**TO:**

```
# UNIVERSAL PROMPT GENERATOR v9.9
```

---

### FIX #8: Changelog Addition [ADMINISTRATIVE]

**LOCATION:** Add NEW section at very end of prompt, before any closing remarks

**ADD:**

```
---

## VERSION HISTORY

### v9.9 (current)
- **FIX #1:** Decision Block Enforcement — added HARD CHECK #0 requiring DB presence before any slot
- **FIX #2:** Rendering Tail Scan — added explicit banned patterns list to HARD CHECKS Priority 1
- **FIX #3:** CONCISE_MODE — mandatory Routing Summary with confirmation line
- **FIX #4:** MJ Suffix Verification — explicit verification line requirement
- **FIX #5:** MJ Sentence Verification — verification lines cannot be suppressed
- **FIX #6:** Anti-Anchor Self-Check — mandatory print line in Decision Block
- **FIX #7:** Contrast Diversity — post-S5 verification print added to HARD CHECKS

### v9.8
- MJ suffix HARD CHECK
- Vehicle ceiling rule
- Zero Tolerance catch confirmation

### v9.7
- EA exception documentation
- S5 TRACE enforcement
- Seed 2 obliqueness test
- Composite S5 rules
- S1/Seed 1 separation
- Flux negative prompt removal
- Ban micro-scan
- Rerun consolidation
```

---

## VERIFICATION CHECKLIST

After applying all fixes, verify:

- [ ] Version header says "v9.9"
- [ ] HARD CHECKS section has items 0-16 (was 1-13)
- [ ] HARD CHECK #0 requires Decision Block presence
- [ ] HARD CHECK #3 has Rendering Tail banned patterns table
- [ ] HARD CHECK #12 has Contrast verification print line
- [ ] CONCISE_MODE section has 4-step mandatory sequence
- [ ] Midjourney verification section says "MANDATORY" and "cannot be suppressed"
- [ ] Anti-Anchor rule has mandatory Decision Block print line
- [ ] VERSION HISTORY section exists at end

---

## OUTPUT

Produce the complete UPG v9.9 prompt with all fixes applied. Preserve all sections not mentioned in the fixes exactly as they appear in v9.8.