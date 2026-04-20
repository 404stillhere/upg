# PROMPT INSTRUCTION FOR EDITING UPG v9.10

---

## TASK

Apply 7 fixes to Universal Prompt Generator v9.10 to address confirmed problems. Fixes are divided into two priority groups.

---

## GROUP A: CRITICAL FIXES (IP Fidelity)

These fixes solve the main problem — loss of IP specificity for themes with established universes.

---

### FIX #5: IP Visual Vocabulary Field

**Location:** INPUTS section, inside SETTING block

**Action:** ADD new field VISUAL_VOCABULARY

**FIND:**
```
- SETTING: [optional — use for established IP or specific universe]
  {
    UNIVERSE:     [IP name / "original"]
    GEOGRAPHY:    [permitted locations]
    ERA:          [time period / tech level]
    FACTION_POV:  [whose perspective]
    AESTHETIC:    [visual language]
    MUST_INCLUDE: [required elements]
    MUST_AVOID:   [forbidden elements]
  }
```

**REPLACE WITH:**
```
- SETTING: [optional — use for established IP or specific universe]
  {
    UNIVERSE:     [IP name / "original"]
    GEOGRAPHY:    [permitted locations]
    ERA:          [time period / tech level]
    FACTION_POV:  [whose perspective]
    AESTHETIC:    [visual language]
    MUST_INCLUDE: [required elements]
    MUST_AVOID:   [forbidden elements]
    VISUAL_VOCABULARY: [optional — detailed visual descriptions of IP-specific elements]
  }
  
  **VISUAL_VOCABULARY Usage:**
  When UNIVERSE ≠ "original" and the IP is niche or unfamiliar, provide explicit visual descriptions for key elements. Format each entry as:
  "[Element name] ([physical description: size, shape, color, materials, distinctive features])"
  
  Example:
  ```
  VISUAL_VOCABULARY: [
    "Avatar warmech (12m bipedal walker, reverse-jointed legs, red-black Nod armor, twin laser pods on shoulders, scorpion emblem on chest plate)",
    "Hand of Nod (stepped black pyramid, 4 floors tall, angular exhaust vents, red-lit slit windows, barracks function)",
    "Obelisk of Light (30m slender black spire, focusing lens at apex, red charge indicators along shaft, laser defense tower)"
  ]
  ```
  
  If VISUAL_VOCABULARY is provided, every prompt must use these descriptions when depicting the listed elements — do not substitute with generic descriptions. If an element from MUST_INCLUDE is not in VISUAL_VOCABULARY, describe it using AESTHETIC guidance and IP-consistent visual logic.
```

---

### FIX #6: Preserve IP Names in Enrichment

**Location:** B.2 Theme Enrichment, STEP 2 — Enrich

**Action:** ADD rule after Material Metaphor Abstraction Constraint

**FIND:**
```
**Material Metaphor Abstraction Constraint:** For material-substitution themes, enrichment must describe the replacing material's behavioral CATEGORIES...
[existing text]
...If enrichment nouns appear verbatim in S1 prose, the enrichment is too specific — rewrite at category level.
```

**ADD IMMEDIATELY AFTER:**
```
**IP Name Preservation Rule:** When SETTING.UNIVERSE ≠ "original", proper nouns and named elements from the IP (character names, faction names, technology names, location names, creature names, material names specific to the universe) must be PRESERVED verbatim in the enriched theme — do not abstract them to generic categories.

Test: If a noun is capitalized in the source IP or appears in MUST_INCLUDE, it is a proper noun. Preserve it.

Examples:
- ❌ FAIL: "Tiberium" → "luminous crystalline contaminant" (IP material name lost)
- ✅ PASS: "Tiberium" → "Tiberium, a luminous green crystal that..." (IP name preserved)
- ❌ FAIL: "Space Marine" → "armored supersoldier" (IP faction name lost)
- ✅ PASS: "Space Marine" → "Space Marine in ceramite armor..." (IP name preserved)
- ❌ FAIL: "lightsaber" → "energy blade" (IP weapon name lost)
- ✅ PASS: "lightsaber" → "lightsaber, its plasma blade..." (IP name preserved)

This rule takes precedence over the Category vs Instance Test for IP-specific terms. The test "Can the term apply to 3+ visually different manifestations?" does not apply to named IP elements — they refer to ONE specific thing in that universe.
```

---

### FIX #7: Smart Cliché Blacklist for IP Themes

**Location:** B.2 Theme Enrichment, STEP 1 — Cliché Blacklist

**Action:** ADD exception for IP-defining features

**FIND:**
```
**STEP 1 — Cliché Blacklist:**
Identify 3 most predictable stock-photo representations of THEME. Ban as primary visual
concept. At least one of Slots 1–5 must avoid all three entirely.
```

**REPLACE WITH:**
```
**STEP 1 — Cliché Blacklist:**
Identify 3 most predictable stock-photo representations of THEME. Ban as primary visual
concept. At least one of Slots 1–5 must avoid all three entirely.

**IP Cliché Exception:** When SETTING.UNIVERSE ≠ "original", do not blacklist elements that are DEFINING FEATURES of the IP universe — only blacklist GENERIC INTERPRETATIONS of those features.

Test: Would removing this element make the image unrecognizable as belonging to the IP? If YES → it is a defining feature → do NOT blacklist.

Examples:
- Command & Conquer: "battlefield with GDI/Nod forces" = defining feature (KEEP). "Generic green crystal field with no faction markers" = generic interpretation (BAN).
- Warhammer 40K: "Space Marines in combat" = defining feature (KEEP). "Generic armored soldiers with no chapter heraldry" = generic interpretation (BAN).
- Star Wars: "X-wing dogfight" = defining feature (KEEP). "Generic spaceship battle" = generic interpretation (BAN).
- Fallout: "Vault interior" = defining feature (KEEP). "Generic underground bunker" = generic interpretation (BAN).

When writing cliché blacklist for IP themes, frame each banned item as "[GENERIC description] WITHOUT [IP-specific markers]" to preserve the ability to depict IP-authentic versions.
```

---

## GROUP B: STRUCTURAL FIXES (Quality & Consistency)

These fixes address less critical but confirmed problems.

---

### FIX #1: Rendering Phrase Enforcement in Hard Checks

**Location:** HARD CHECKS section, Priority 1

**Action:** ADD check 7a between existing checks 7 and 7b

**FIND:**
```
7. **Platform Suffix Check (Midjourney only):** Verify each of 5 prompts ends with --ar [ratio] --v 6 --style raw --s 50. If any prompt lacks suffix, append before output.

7b. **Setting Fidelity (skip if SETTING omitted or UNIVERSE = "original"):**
```

**INSERT BETWEEN THEM:**
```
7a. **Rendering Phrase Check (non-photographic media only):** If Medium is painting, illustration, or concept art, verify that at least 3 of 5 slots contain rendering vocabulary (brushwork terms, texture descriptions, or technical style phrases — see A.4 Rendering Execution table). If count < 3: add rendering phrase to S1, then S4, then S5 until count ≥ 3. Place rendering phrases in second-to-last or third-to-last sentence of each slot, never in final sentence. Do not print count.
```

---

### FIX #2: Seed 2 Category Tracking

**Location:** Phase 4.1 Seed Generation, after Vehicle-Witness Ceiling

**Action:** ADD new tracking mechanism

**FIND:**
```
**VEHICLE-WITNESS CEILING:** Vehicle interior contexts...
[existing text]
...Print in Decision Block after Seed 2 context line:
`Vehicle-witness check: [count] in last 3 FULL ARC → [OK / CEILING — using alternative]`
```

**ADD IMMEDIATELY AFTER:**
```
**SEED 2 CATEGORY TRACKING:** Classify Seed 2 context into ONE of these categories:
- WORKSHOP (repair, maintenance, assembly, foundry, forge)
- DOMESTIC (home interior, kitchen, bedroom, living space)
- TRANSIT (vehicle interior, station, dock, cargo hold)
- FIELD (outdoor site, tent, temporary shelter, excavation)
- COMMERCIAL (shop, café, market, retail space)
- BACKSTAGE (theater, broadcast, film set, behind-scenes)
- RELIGIOUS (chapel, shrine, temple interior — non-institutional worship space)

Print in Decision Block after Vehicle-witness check:
`Seed 2 category: [CATEGORY]`

**Category Ceiling Rule:** Same category may not appear in more than 2 of 4 consecutive FULL ARC themes. Before assigning category, count appearances in last 3 FULL ARC themes:
- 0 or 1 of same category: OK, proceed
- 2 of same category: CEILING — select from unused categories

If theme strongly suggests a specific category (e.g., religious theme → RELIGIOUS), and ceiling is reached, shift to an adjacent unexpected category (e.g., RELIGIOUS ceiling → try WORKSHOP with religious elements, or DOMESTIC with shrine corner).
```

---

### FIX #3: Decision Block Line Limit Update

**Location:** OUTPUT PROTOCOL, CONCISE_MODE omitted section

**Action:** MODIFY line limit

**FIND:**
```
Output a Decision Block (≤25 lines for FULL ARC, ≤15 lines for SHALLOW ARC; group single-value fields onto shared lines separated by pipes)
```

**REPLACE WITH:**
```
Output a Decision Block (≤25 lines for FULL ARC, or ≤30 lines if RERUN block is present; ≤15 lines for SHALLOW ARC; group single-value fields onto shared lines separated by pipes)
```

---

### FIX #4: Rendering Placement Clarification

**Location:** A.4 Creative Lenses, RENDERING EXECUTION section

**Action:** MODIFY placement guidance

**FIND:**
```
Place rendering phrase near end of slot, integrated into description.
```

**REPLACE WITH:**
```
Place rendering phrase in the second-to-last or third-to-last sentence of each slot, integrated into the description. Do not place rendering vocabulary in the final sentence (see Rendering Tail Ban in A.2.9). The final sentence must end on a visible physical detail — surface, edge, light behavior, spatial position, or material state.
```

---

## APPLICATION ORDER

1. **First:** Fixes #5, #6, #7 (IP fidelity — critical)
2. **Then:** Fixes #1, #4 (rendering system — interconnected)
3. **Then:** Fix #2 (Seed 2 category tracking)
4. **Last:** Fix #3 (cosmetic line limit)

---

## VERIFICATION AFTER APPLICATION

Run test with this input:

```
THEME: Nod temple complex harvesting Tiberium while GDI forces approach

SETTING {
  UNIVERSE:     Command & Conquer (1995-2010)
  GEOGRAPHY:    North African desert, underground caverns
  ERA:          Near-future 2030-2050, Kane's vision era
  FACTION_POV:  Brotherhood of Nod
  AESTHETIC:    Cult architecture, red-black color scheme, scorpion motifs, subterranean industry, religious tech-worship
  MUST_INCLUDE: Nod scorpion insignia, Hand of Nod structure, Tiberium harvesters, obelisk of light, Kane imagery/statues, red illumination, Avatar warmechs
  MUST_AVOID:   GDI blue/gold colors as dominant, clean suburban areas, Soviet aesthetic
  VISUAL_VOCABULARY: [
    "Nod scorpion insignia (stylized black scorpion with curved tail, segmented body, on red or gold field, 30-50cm emblems on structures)",
    "Hand of Nod (stepped black pyramid, 4 floors, ~20m tall, angular exhaust vents, red-lit slit windows along each level, serves as barracks)",
    "Tiberium harvester (tracked industrial vehicle, 8m long, red-black Nod colors, front-mounted scoop, rear hopper container for green crystals)",
    "Obelisk of Light (30m slender black spire, pyramidal cross-section, focusing lens at apex surrounded by red charge rings, laser defense tower)",
    "Kane imagery (bald male figure in robes or military coat, charismatic pose, often with raised hand, Nod prophet-leader)",
    "Avatar warmech (12m bipedal walker, reverse-jointed legs, hunched torso, red-black armor plates, twin weapon pods on shoulders, scorpion emblem on chest)"
  ]
}
```

**Success criteria:**

1. ✅ Enriched theme contains the word "Tiberium", not "crystalline mineral"
2. ✅ Cliché blacklist does NOT ban "battlefield" or "military" as a category
3. ✅ Prompts contain visual descriptions from VISUAL_VOCABULARY (sizes, shapes, colors)
4. ✅ Seed 2 category printed in Decision Block
5. ✅ Rendering phrases in ≥3 slots, not in final sentences
6. ✅ Decision Block ≤30 lines when RERUN is present

---

## PRESERVE WITHOUT CHANGES

The following mechanisms work correctly and must NOT be affected by fixes:

1. Entry Angle Rotation System
2. Rerun Detection and Diversity
3. Seed Metaphorical Distance Check
4. Lens Sequence Diversity
5. Contrast Diversity Rule
6. Zero Tolerance Bans
7. Adjacent Slot Uniqueness
8. S1/Seed 1 Location Separation
9. Carrying Image Fidelity
10. SETTING.MUST_INCLUDE/MUST_AVOID enforcement (Hard Check 7b)

---

**END OF INSTRUCTION**