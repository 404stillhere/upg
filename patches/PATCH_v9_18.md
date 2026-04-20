# UPG v9.18 PATCH

**Применить к:** UPG v9.17.1+
**Версия после патча:** v9.18.0

---

## PATCH INSTRUCTION

Добавить следующие секции в указанные места. Существующую нумерацию сдвинуть где указано.

---

## 1. INPUTS — новые поля

**Куда:** Секция INPUTS, после STRUCTURED THEME INPUT

**Добавить:**

```
- MOOD_ANTI_PATTERN: [list of forbidden emotional readings]
  Format: "NOT [reading] — [physical prevention]"
  Example: "NOT heroic triumph — shoulders dropped, gaze down, arms slack"
  If provided → enforce during Phase 5 writing, rewrite if slot reads as forbidden.

- SPATIAL_MEANING_MAP: [zone → semantic meaning]
  Format: { FOREGROUND: "[meaning]", BACKGROUND: "[meaning]", LEFT: "[meaning]", ... }
  Example: { FOREGROUND: "present moment", BACKGROUND: "memory/past", THRESHOLD: "liminal choice" }
  If provided → honor during element placement in prompt writing.

- CAMERA_SYSTEM: { BODY: [manufacturer + model], LENS_LINE: [manufacturer + series] }
  Example: { BODY: "ARRI Alexa 65", LENS_LINE: "Cooke S7/i" }
  If provided → append character descriptors to technical parameters.
  Applies only when LENS = PHOTO or CINE.

- THRESHOLD_ELEMENTS: [element at visibility% via technique]
  Format: "[element] at [visibility level] via [technique]"
  Example: "woman silhouette at GHOST via FOG"
  Visibility levels: GHOST (5-15%) | HINT (15-30%) | PARTIAL (30-50%) | OBSCURED (50-70%)
  Techniques: FOG | BOKEH | SHADOW | REFLECTION | PERIPHERAL | OVEREXPOSURE | UNDEREXPOSURE | MOTION_BLUR | TRANSLUCENT
  If provided → describe as physical visibility state, never conditional language.

- REALISM_ANCHOR: [ON / OFF]
  Default logic if omitted:
  ├── MODE 3 → ON
  ├── Theme contains supernatural/magical/fantasy keywords → ON
  ├── LENS majority GRAPHIC/SYMBOLIC/MINIMAL → OFF
  └── Otherwise → ON
  When ON → enforce physical weight, optical light behavior, environmental surface response.

- REFERENCE_EXTRACTION: [reference → specific technique]
  Format: "[name]: [extracted technique]"
  Example: "Lubezki: natural light only, source visible in frame, no fill, long observation"
  If provided → apply extracted technique as writing constraint.
  If only name in AESTHETIC.References without extraction → auto-extract from known table or print warning.
```

---

## 2. B.1 DECISION MATRIX — новое поле

**Куда:** ZONE B — B.1 Decision Matrix table

**Добавить строку:**

```
| Mood Anti-Pattern | [list from input or NONE] |
| Realism Anchor | [ON / OFF — from input or default logic] |
```

---

## 3. B.2 THEME ENRICHMENT — новый шаг

**Куда:** ZONE B — B.2, после STEP 2, перед STEP 3

**Добавить:**

```
**STEP 2.5 — Reference Extraction:**
If AESTHETIC.References contains artist/director/cinematographer/film:

Parse reference → extract SPECIFIC TECHNIQUE, not just name.

| Reference Type | Extract |
|----------------|---------|
| Director | Signature visual approach, pacing, tone |
| Cinematographer | Light philosophy, source preference, contrast style |
| Painter | Composition logic, color relationship, mark-making |
| Film | Production design era, palette, atmosphere |
| Game | Art direction style, environmental storytelling |

KNOWN REFERENCE TABLE:
| Name | Auto-extraction |
|------|-----------------|
| Lubezki | natural light only, source in frame, no fill, long unbroken takes |
| Deakins | precise motivated light, single-source logic, controlled pools |
| Crewdson | staged suburban surrealism, cinematic scale in stillness, uncanny |
| Hopper | isolated figures, raking light, urban loneliness, geometric windows |
| Beksiński | organic architecture, bone textures, sepia-ochre, nightmare calm |
| Vermeer | window light from left, domestic intimacy, luminous skin, muted palette |
| Tarkovsky | water, fog, decay, spiritual weight, slow revelation |
| Villeneuve/BR2049 | negative space, monochrome + single accent, dust/haze, scale |

Format in Decision Block:
`Reference: [name] → [extracted technique]`

If name not in table and no REFERENCE_EXTRACTION provided:
→ Print: `[REFERENCE: "[name]" not in library — using as style tag only]`

INTEGRATION:
Extracted technique becomes writing constraint for light/composition/atmosphere.
```

---

## 4. A.2 MANDATORY QUALITY RULES — новые правила

**Куда:** ZONE A — A.2, после правила 9

**Добавить:**

```
10. **Threshold Element Handling:**
    If THRESHOLD_ELEMENTS provided:
    → Describe as PHYSICAL STATE of visibility, never conditional language
    → Always specify: technique + physical description + visibility level
    
    VISIBILITY SCALE:
    | Level | Range | What's visible |
    |-------|-------|----------------|
    | GHOST | 5-15% | Mass/silhouette only, no details |
    | HINT | 15-30% | Form recognizable, details dissolved |
    | PARTIAL | 30-50% | Some details readable |
    | OBSCURED | 50-70% | Most details, something hidden |
    
    Pattern: "[Element] present as [technique]: [physical description], [visibility cue]"
    
    ✅ COMPLIANT:
    "A vertical human-shaped mass in the fog bank, features dissolved 
     into grey-white density, presence registered as spatial interruption,
     visibility GHOST"
    
    ❌ VIOLATION:
    "A woman who might be visible in the fog"
    "Perhaps a figure in the mist"
    "Someone possibly standing there"
    
    RATIONALE: Threshold describes VISIBILITY STATE, not presence uncertainty.
    Element IS there — in reduced legibility state.
    This is compatible with D5 (Mandatory Element Language) because
    threshold is not conditional presence, it is visibility condition.

11. **Physical Realism Anchor:**
    If REALISM_ANCHOR = ON (default for MODE 3, supernatural, magical):
    
    RENDERING PRIORITY:
    1. Material weight persists — impossible objects still have physical mass
    2. Light obeys optics — reflections, refractions, shadows physically correct
    3. Surfaces respond to environment — moisture, dust, temperature marks
    4. Gravity affects non-magical elements normally
    5. Atmosphere behaves physically — fog density, light scatter, breath visibility
    
    ANCHOR PHRASES (include ≥2 per slot when supernatural elements present):
    □ Weight: "physical weight of [material] in [stance/position]"
    □ Environment: "[moisture/dust/condensation] on [surface]"
    □ Optics: "light [specific physical behavior on surface]"
    □ Gravity: "[mundane element] [gravity-obeying action]"
    □ Atmosphere: "[temperature/humidity] visible as [marker]"
    
    EXAMPLE (magical lion):
    "Physical weight of muscle and bone in the lion's stance,
     forepaws compress wet grass leaving print, breath visible
     in cold dawn air, light-particle wings cast no shadow but
     reflect in puddle surface as pure luminance"
    
    EXCEPTION: If LENS = GRAPHIC or SYMBOLIC or MINIMAL → REALISM_ANCHOR = OFF
    Stylization permits physics departure.
```

---

## 5. A.4 CREATIVE LENSES — Camera System integration

**Куда:** ZONE A — A.4, после TECHNICAL PARAMETERS BY LENS TYPE table

**Добавить:**

```
**CAMERA SYSTEM INTEGRATION:**

If CAMERA_SYSTEM provided and LENS = PHOTO or CINE:
→ Append character descriptor to technical parameters

CHARACTER TABLES:

| Camera Body | Character descriptor |
|-------------|---------------------|
| ARRI Alexa 65 | organic highlight rolloff, filmic grain structure |
| ARRI Alexa Mini | balanced response, production versatility |
| RED Monstro/V-Raptor | digital precision, saturated color, sharp resolving |
| Sony Venice | neutral response, dual-ISO clarity, wide latitude |
| Blackmagic | contrasty, video-adjacent character |
| Film 35mm | halide grain structure, chemical color, analog response |
| Film 65mm/IMAX | minimal grain, maximum resolving detail, epic scale |
| Hasselblad/PhaseOne | medium format, shallow rolloff, commercial precision |

| Lens Line | Character descriptor |
|-----------|---------------------|
| Zeiss Supreme Prime | clinical sharpness, controlled flare, neutral |
| Cooke S7/i | warm midtones, creamy bokeh, "Cooke look" |
| Leica Summilux-C | contrasty, vintage character, compact rendering |
| Panavision Primo | balanced cinema, classic Hollywood |
| Panavision Anamorphic | oval bokeh, horizontal flare streaks, 2.39:1 native |
| Master Anamorphic | clean anamorphic, less flare, modern |
| Canon K35 | vintage warm, low contrast, organic flare |
| Sigma Cine | sharp, neutral, cost-effective |

COMBINATION FORMAT:
"[focal] [f-stop], [body character], [lens character]"

Example:
"85mm f/2.0, organic highlight rolloff from Alexa 65, 
 warm midtones and creamy bokeh from Cooke S7/i"

If body or lens not in table:
→ Print: `[CAMERA: "[name]" not in library — omitting character]`
→ Use focal + f-stop only

LENS FILTER:
Camera System applies ONLY to slots where LENS = PHOTO or CINE.
For PAINTERLY, GRAPHIC, SYMBOLIC, etc. → Camera System ignored for that slot.
```

---

## 6. A.5 UNIVERSAL PROMPT STRUCTURE — Spatial Meaning

**Куда:** ZONE A — A.5, добавить в список компонентов

**Добавить:**

```
| Spatial meaning | If SPATIAL_MEANING_MAP provided: honor semantic zone 
  assignments during element placement. Element in FOREGROUND where 
  FOREGROUND="present" should not use past-tense or memory language.
  Element in BACKGROUND where BACKGROUND="past" may carry nostalgic/
  memorial quality. Zone meaning guides placement, does not override
  composition requirements. If conflict: composition wins, flag override.
```

---

## 7. SLOT VALIDATION STACK — новые уровни

**Куда:** После Level 8 (Mandatory Elements), перед Level 9 (MODE 3)

**Добавить:**

```
### Level 8.5: New Feature Compliance

SV-22. **THRESHOLD ELEMENT compliance** (if THRESHOLD_ELEMENTS provided):
    □ Element described as physical visibility state, not conditional presence
    □ Technique specified (FOG/BOKEH/SHADOW/REFLECTION/etc.)
    □ Visibility level present (GHOST/HINT/PARTIAL/OBSCURED)
    □ No conditional language ("might", "perhaps", "possibly", "may be")
    If conditional language found → REWRITE as state description
    Print if TRACE: `[THRESHOLD: "[element]" — [technique] at [level] — PASS]`

SV-23. **SPATIAL MEANING compliance** (if SPATIAL_MEANING_MAP provided):
    □ Element placement respects semantic zone assignments
    □ No contradiction between zone meaning and element description
    □ If conflict detected: composition priority, print:
      `[SPATIAL MEANING: composition overrode "[zone]=[meaning]" in S[n]]`

SV-24. **REALISM ANCHOR compliance** (if REALISM_ANCHOR = ON):
    □ Count anchor phrases in slot (weight/environment/optics/gravity/atmosphere)
    □ Slots with supernatural/magical elements require ≥2 anchors
    □ If <2 in supernatural slot → add anchors before output
    Print if TRACE: `[REALISM: S[n] = [count] anchors — PASS/ENRICHED]`

SV-25. **MOOD ANTI-PATTERN compliance** (if MOOD_ANTI_PATTERN provided):
    □ Read completed slot
    □ Does it read as any forbidden interpretation?
    □ If YES → identify conflicting physical markers → REWRITE
    Print only if rewrite occurred:
    `[ANTI-PATTERN AVOIDED: S[n] read as "[forbidden]" — revised]`

SV-26. **CAMERA SYSTEM compliance** (if CAMERA_SYSTEM provided):
    □ Verify character descriptors present in PHOTO/CINE slots
    □ Verify Camera System NOT applied to non-PHOTO/CINE slots
    Print if TRACE: `[CAMERA: S[n] — [body] + [lens] applied — PASS]`
```

**Renumber:** Existing SV-25 through SV-34 (MODE 3) become SV-30 through SV-39.

---

## 8. HARD CHECKS — новые проверки

**Куда:** После HC-24, перед MODE 3 section

**Добавить:**

```
### PRIORITY 1-G: New Feature Checks

HC-25. **Threshold Element Check** (if THRESHOLD_ELEMENTS provided):
  □ Each threshold element uses physical state description
  □ No conditional language in threshold descriptions
  □ Visibility level specified per element
  □ If violation → REWRITE before output
  Print: `[THRESHOLD: [count] elements — all physical state — PASS]`

HC-26. **Realism Anchor Check** (if REALISM_ANCHOR = ON or MODE 3):
  □ Count anchor phrases per slot with supernatural content
  □ Require ≥2 per supernatural slot
  □ If <2 → enrich from anchor phrase list
  Print: `[REALISM: S1=[n] S2=[n] S3=[n] S4=[n] S5=[n] — PASS/ENRICHED]`

HC-27. **Mood Anti-Pattern Check** (if MOOD_ANTI_PATTERN provided):
  □ Scan each slot for forbidden emotional reading
  □ If detected → verify physical prevention markers present
  □ If markers absent → REWRITE
  Print only if rewrite: `[ANTI-PATTERN: S[n] "[forbidden]" — FIXED]`

HC-28. **Camera System Check** (if CAMERA_SYSTEM provided):
  □ Verify character applied to PHOTO/CINE slots only
  □ Verify both body and lens character present where applicable
  □ Flag unknown body/lens names
  Print: `[CAMERA: applied to [n]/[total PHOTO+CINE] slots — PASS]`

HC-29. **Spatial Meaning Check** (if SPATIAL_MEANING_MAP provided):
  □ Verify element placement honors semantic zones
  □ Flag any composition overrides
  Print: `[SPATIAL: [n] zones honored, [n] overrides — PASS]`
```

**Renumber:** Existing HC-25 through HC-35 (MODE 3) become HC-30 through HC-40.

---

## 9. OUTPUT PROTOCOL — обновления

**Куда:** OUTPUT PROTOCOL — Decision Block fields

**Изменить CONCISE_MODE omitted (default) на:**

```
### CONCISE_MODE omitted (default)
Required fields: 
Scope | Context | Medium | Arc | Creative latitude | Safety note | 
Carrying image | Enriched theme | Cliché blacklist | Palette summary | 
Aspect ratio | Entry Angle | Modules | Slot plan | Mandatory elements |
**Mood Anti-Pattern (if provided)** | **Realism Anchor status** |
**Reference extraction (if applicable)**

For FULL ARC, also include: Seeds 1–3 | Seed-to-Slot | S1/Seed1 separation |
**Spatial Meaning Map (if provided)** | **Camera System (if provided)** |
**Threshold Elements (if provided)**
```

**Куда:** Routing Summary format

**Добавить после Mandatory line:**

```
3a. If Mood Anti-Pattern: `Anti-Pattern: NOT [list]`
3b. If Camera System: `Camera: [body] + [lens]`
3c. If Threshold Elements: `Threshold: [element] at [level] via [technique]`
3d. If Realism Anchor ON: `Realism: ON — anchors required`
3e. If Spatial Meaning: `Spatial: [zone]=[meaning], [zone]=[meaning]`
```

---

## 10. MODE 3 COMPATIBILITY — добавления

**Куда:** После MODE 3 COMPATIBILITY MATRIX section

**Добавить:**

```
### NEW FEATURE + MODE 3 INTERACTION

**REALISM ANCHOR + MODE 3:**
- S1 LITERAL: Realism Anchor reinforces photographability
- S2-S4: Realism Anchor maintains physical grounding despite impossibility
- S5: Realism Anchor applies to environment, resolution element may transcend
- Default: ON for all MODE 3

**THRESHOLD + MODE 3:**
- Threshold element may be one of N elements at reduced visibility
- Threshold element may appear/disappear across gradient
- S1: Threshold element must be identifiable despite low visibility
- S5-ABSENCE: Threshold technique may BE the trace (shadow, reflection)

**SPATIAL MEANING + MODE 3:**
MODE 3 EXCEPTION: Spatial semantics may INVERT across gradient.
- S1: BACKGROUND = past (established)
- S3-S4: BACKGROUND may become future (inversion as strangeness)
- Track semantic shifts as part of permutation documentation
Print: `[SPATIAL INVERSION: S[n] [zone] meaning inverted]`

**MOOD ANTI-PATTERN + MODE 3:**
- Applies equally across all slots
- S4 ABSURD especially vulnerable to wrong reading (chaos ≠ horror unless intended)
- Verify anti-pattern compliance after S4 with particular attention

**CAMERA SYSTEM + MODE 3:**
- Most relevant for S1-S2 (near-real, PHOTO/CINE likely)
- S3-S5 often PAINTERLY/SENSORY where Camera System not applicable
- If LENS ≠ PHOTO/CINE → Camera System ignored for that slot
```

---

## 11. SHALLOW ARC COMPATIBILITY — добавления

**Куда:** В A.3 Slot Architecture, после SHALLOW ARC section

**Добавить:**

```
**NEW FEATURES + SHALLOW ARC:**

THRESHOLD (commercial context):
Commercial thresholds differ from atmospheric/liminal:
├── BOKEH — secondary product out of focus, hero sharp
├── STEAM/SMOKE — coffee steam, cosmetic mist, atmospheric product-adjacent
├── REFLECTION — brand/product visible in reflective surface
├── LIFESTYLE BLUR — person using product, face not focal, product sharp
Not ghostly or mysterious — functional depth separation for product hierarchy.

MOOD ANTI-PATTERN (commercial):
Highly relevant. Examples:
├── "NOT cheap/budget" → premium materials, precise lighting, negative space
├── "NOT clinical" → warmth, organic elements, lifestyle context
├── "NOT masculine" → soft palette, curved composition, delicate props
├── "NOT generic" → specific location, unique angle, distinctive props

CAMERA SYSTEM (commercial):
Highly relevant. Common commercial systems:
├── PhaseOne/Hasselblad — beauty, cosmetics, luxury goods
├── ARRI — automotive, luxury lifestyle, premium brand films
├── RED — tech products, sharp modern aesthetic
Match system to product category for authentic look.

REALISM ANCHOR (commercial):
Always ON by default. Commercial imagery requires physical believability.
Product must look real, touchable, purchasable.

SPATIAL MEANING (commercial):
Less common but applicable:
├── FOREGROUND = product (hero)
├── BACKGROUND = lifestyle context / aspiration
├── MIDGROUND = user interaction
```

---

## 12. MODULE COMPATIBILITY — добавления

**Куда:** ZONE C — MODULES, после MODULE COMBINATIONS

**Добавить:**

```
### NEW FEATURES + MODULES

**MODULE C + THRESHOLD:**
Threshold techniques are NATURAL Module C redirects:
├── SHADOW — form visible without explicit surface detail
├── SILHOUETTE — shape recognizable without features
├── STEAM/MIST — obscuring explicit elements atmospherically
├── BOKEH — defocusing explicit zones while maintaining presence
├── FABRIC/SHEET — form under translucent material

Threshold element description may BE the Module C solution.
When Module C active and explicit element needs redirect:
→ Consider Threshold technique as primary tool
→ Element remains present (narratively) at reduced visibility (visually)

**MODULE A + SPATIAL MEANING:**
Spatial semantics apply to DEPICTED SCENE inside artwork, not poster physical space.
If poster depicts landscape:
├── Depicted foreground = [meaning]
├── Depicted background = [meaning]
Wrapper context (poster on wall) has no spatial semantics.

**MODULE B + CAMERA SYSTEM:**
Relevant. Product photography systems:
├── PhaseOne IQ4 — cosmetics, jewelry, small luxury goods
├── Hasselblad H6D — fashion accessories, watches
├── Canon/Sony high-res — general commercial
Match system to product category.

**MODULE D + REALISM ANCHOR:**
Reinforcing. Lifecycle arc benefits from physical realism:
├── S1 intact — pristine material truth
├── S2 use — realistic wear initiation
├── S3 wear — believable degradation
├── S4 repurpose — plausible transformation
├── S5 trace — physical evidence of passage
Realism Anchor keeps degradation grounded, not stylized.
```

---

## 13. DIAGNOSTIC TEMPLATE — новые поля

**Куда:** DIAGNOSTIC TEMPLATE section (CONCISE_MODE = false)

**Добавить в шаблон:**

```
═══════════════════════════════════════════════════════════════
NEW FEATURE STATUS
═══════════════════════════════════════════════════════════════

MOOD ANTI-PATTERN:
├── Forbidden: [list or NONE]
├── Physical preventions: [list or N/A]
└── Status: ENFORCING / NOT PROVIDED

SPATIAL MEANING MAP:
├── FOREGROUND: [meaning or NONE]
├── MIDGROUND: [meaning or NONE]
├── BACKGROUND: [meaning or NONE]
├── Other zones: [if any]
└── Status: ENFORCING / NOT PROVIDED

CAMERA SYSTEM:
├── Body: [name or NOT PROVIDED]
├── Lens Line: [name or NOT PROVIDED]
├── Character: [combined descriptor or N/A]
└── Applies to slots: [list of PHOTO/CINE slots]

THRESHOLD ELEMENTS:
├── Elements: [list with visibility + technique]
└── Status: ENFORCING / NOT PROVIDED

REALISM ANCHOR:
├── Status: ON / OFF
├── Source: [USER PROVIDED / DEFAULT: reason]
└── Anchor requirement: [n] per supernatural slot

REFERENCE EXTRACTION:
├── References: [list]
├── Extracted techniques: [list]
└── Unknown references: [list or NONE]

═══════════════════════════════════════════════════════════════
```

---

## 14. POST-SERIES VERIFICATION — новые строки

**Куда:** After prompts, verification block

**Добавить:**

```
**New Feature Verification (print after standard verification):**

[NEW FEATURES:
  Mood Anti-Pattern: [ENFORCED [n] rewrites / NOT PROVIDED]
  Spatial Meaning: [HONORED / [n] OVERRIDES / NOT PROVIDED]
  Camera System: [APPLIED S[list] / NOT PROVIDED]
  Threshold: [COMPLIANT [n] elements / NOT PROVIDED]
  Realism Anchor: [ON — S[list] have [n]+ anchors / OFF]
  Reference: [EXTRACTED: [list] / NOT PROVIDED]]
```

---

## 15. VERSION UPDATE

**Куда:** Top of document

**Изменить:**

```
UPG v9.18.0

CHANGELOG v9.18.0:
- Added MOOD_ANTI_PATTERN input field and enforcement (B.1, SV-25, HC-27)
- Added SPATIAL_MEANING_MAP input field and compliance (A.5, SV-23, HC-29)
- Added CAMERA_SYSTEM input field with character tables (A.4, SV-26, HC-28)
- Added THRESHOLD_ELEMENTS input field with visibility scale (A.2 Rule 10, SV-22, HC-25)
- Added REALISM_ANCHOR input field with default logic (A.2 Rule 11, SV-24, HC-26)
- Added REFERENCE_EXTRACTION with known reference table (B.2 STEP 2.5)
- Added MODE 3 + new feature interactions
- Added SHALLOW ARC + new feature compatibility
- Added MODULE + new feature compatibility
- Updated Decision Block fields
- Updated Diagnostic Template
- Updated post-series verification
```

---

## APPLICATION CHECKLIST

После применения патча, проверить:

```
□ INPUTS section contains 6 new fields
□ B.1 Decision Matrix has 2 new rows
□ B.2 has STEP 2.5 (Reference Extraction)
□ A.2 has Rules 10-11 (Threshold, Realism Anchor)
□ A.4 has Camera System Integration section
□ A.5 includes Spatial Meaning component
□ SLOT VALIDATION STACK has Level 8.5 (SV-22 through SV-26)
□ HARD CHECKS has HC-25 through HC-29
□ OUTPUT PROTOCOL updated with new fields
□ MODE 3 section has new feature interactions
□ SHALLOW ARC section has new feature compatibility
□ MODULES section has new feature compatibility
□ DIAGNOSTIC TEMPLATE has NEW FEATURE STATUS block
□ Post-series verification has new feature lines
□ Version number updated to v9.18.0
```

---

**END PATCH**