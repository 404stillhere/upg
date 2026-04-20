# UPG v9.17.0 — MODE 3: REMIX PATCH

---

## CHANGELOG v9.16.1 → v9.17.0

```
ADDED:
+ MODE: 3 (REMIX) — N elements combined with escalating absurdity gradient
+ ELEMENTS input field — accepts 2-10 nouns/phenomena
+ REMIX ARC: LITERAL → SHIFTED → SURREAL → ABSURD → RESOLUTION
+ S5 Resolution types: COLLAPSE / ABSENCE / MATRYOSHKA / EXPLOSION / LOOP
+ Element validation pipeline (photo test, abstraction translation, scale reconciliation)
+ Coherence thread system (mandatory for MODE 3)
+ Role rotation tracking
+ Interaction evolution ladder
+ Platform adaptation for surreal content
+ BAN REGISTRY: MODE 3 extensions
+ HARD CHECKS: MODE 3 specific validation

MODIFIED:
* INPUTS section — added ELEMENTS field
* Phase 4 — added Permutation Planning branch
* Slot Architecture — added REMIX ARC section
* Validation Stack — added MODE 3 checks

COMPATIBILITY:
- MODE 3 incompatible with SHALLOW ARC (auto-converts to artistic)
- MODE 3 incompatible with Module D (conflict error)
- MODE 3 + Module A/B = allowed with constraints
- MODE 3 + Module C = auto-activates if NSFW elements detected
```

---

## INPUTS — ADDITIONS

Add after `MODE:` field:

```
- ELEMENTS: [N nouns/phenomena separated by | ]
  Minimum: 2
  Optimal: 3-7
  Maximum: 10 (soft limit, warning at 8+)
  
  Activates MODE 3 automatically when provided.
  
  Format: "element1 | element2 | element3 | ..."
  Example: "clock | sand | raven | tower | echo"
  
  ELEMENT TYPES ACCEPTED:
  □ Objects: tree, key, mirror, clock
  □ Creatures: raven, lion, fish
  □ Phenomena: fire, rain, light, shadow
  □ Locations: tower, ocean, forest (treated as container OR object)
  □ Materials: sand, glass, iron (treated as substance OR object)
  □ Abstractions: silence, time, love → auto-translated to visual markers
  □ Actions: falling, burning → auto-frozen to peak moment
  □ Negatives: darkness, silence → visualized via boundary/effect
  
  ELEMENT VALIDATION (automatic):
  1. Photo Test: Can element be photographed? YES → accept. NO → translate.
  2. Abstraction Translation: Map to visual marker (see table below).
  3. Scale Reconciliation: Flag conflicts, apply perspective solution.
  4. Hostile Detection: Note elements that destroy each other.
  5. Semantic Overlap: Warn if elements are synonyms/variants.
  6. NSFW Detection: Auto-activate Module C if combination suggests explicit.
  
  ABSTRACTION → VISUAL MARKER TABLE:
  | Abstraction | Default Marker |
  |-------------|----------------|
  | time | clock, hourglass, wrinkles, decay |
  | silence | empty space, closed ears, still water, frozen sound wave |
  | love | heart, held hands, warmth glow, red thread |
  | death | skull, wilted flower, empty chair, stopped clock |
  | memory | photograph, faded image, mirror reflection |
  | fear | shadow, widened eyes, raised hackles |
  | freedom | broken chain, open door, spread wings |
  | infinity | spiral, mirror-in-mirror, horizon line |
  
  User may override: "silence (frozen sound waves)" → use specified marker.

- PRIMARY: [element name] (optional)
  Designates one element as dominant across series.
  If omitted: first element in ELEMENTS list = primary.
  If "NONE": all elements weighted equally, rotate primary per slot.

- S5_RESOLUTION: COLLAPSE | ABSENCE | MATRYOSHKA | EXPLOSION | LOOP
  Default: COLLAPSE
  
  COLLAPSE: All N elements merge into single hybrid entity
  ABSENCE: All N elements gone, only traces remain
  MATRYOSHKA: Elements nested inside each other (A contains B contains C...)
  EXPLOSION: Elements fragmented and scattered, pieces intermixed
  LOOP: S5 mirrors S1 but with all roles inverted, suggesting eternal cycle

- S5_TONE: WONDER | DREAD | MELANCHOLY | RELIEF | VERTIGO | LIBERATION | TRAP | ACCEPTANCE
  Default: WONDER (for COLLAPSE), MELANCHOLY (for ABSENCE)
  
  Emotional target for S5 resolution.

- GRADIENT: SMOOTH | SHARP | REVERSE | PEAK | VALLEY
  Default: SMOOTH
  
  SMOOTH: S1(0) → S2(1) → S3(2-3) → S4(3+) → S5(full) — gradual escalation
  SHARP: S1(0) → S2(0) → S3(full) → S4(full) → S5(full) — sudden break at S3
  REVERSE: S1(full) → S2(3+) → S3(2-3) → S4(1) → S5(0) — chaos to order
  PEAK: S1(0) → S2(1) → S3(full) → S4(1) → S5(0) — mountain shape
  VALLEY: S1(full) → S2(1) → S3(0) → S4(1) → S5(full) — reality as strange moment

- COHERENCE: [thread description] (optional)
  If omitted: auto-derived from elements (palette or texture or time).
  
  Types:
  □ PALETTE: "warm amber and cool steel through all slots"
  □ TIME: "pre-dawn light in every scene"
  □ TEXTURE: "grit and grain on every surface"
  □ ELEMENT_ANCHOR: "[element X] maintains consistent color/form"
  □ TEMPERATURE: "cold atmosphere throughout"
  
  Multiple threads allowed (max 3, different categories).

- NARRATIVE_MODE: PURE | IMPLIED | GUIDED
  Default: IMPLIED
  
  PURE: Visual experiment only, no story implication
  IMPLIED: Viewer constructs narrative from sequence
  GUIDED: Explicit story spine provided via NARRATIVE_SEED

- NARRATIVE_SEED: [one sentence] (optional, for GUIDED mode)
  Example: "A woman waits for a ship that will never return"
```

---

## ZONE B — PREPROCESSING ADDITIONS

Add new section after B.2:

```
### B.3 Permutation Planning (MODE 3 only)

When ELEMENTS field provided OR MODE: 3 specified:

**STEP 0 — ELEMENT PARSING:**

IF input = pipe-separated nouns:
  Accept directly as ELEMENTS array

IF input = sentence/scene description:
  Extract nouns automatically
  Print: `[ELEMENTS EXTRACTED: [list] — confirm or modify]`

IF input = mixed languages:
  Normalize to PLATFORM language or English
  Print: `[ELEMENTS NORMALIZED: [original] → [normalized]]`

**STEP 1 — ELEMENT VALIDATION:**

For each element, run checks in order:

1.1 PHOTO TEST:
  Can this be photographed as a single frame?
  YES → accept
  NO → check if abstraction, action, or negative

1.2 ABSTRACTION CHECK:
  Is element abstract (cannot point to it)?
  YES → translate using ABSTRACTION → VISUAL MARKER TABLE
  Print: `[ABSTRACTION: "[element]" → "[marker]"]`
  User override accepted: "silence (my marker)" → use "my marker"

1.3 ACTION CHECK:
  Is element a verb/process?
  YES → freeze to peak moment
  Print: `[ACTION FROZEN: "[element]" → "[frozen state]"]`
  Examples:
    falling → object mid-fall, frozen at peak arc
    burning → flames at maximum spread, frozen
    growing → plant mid-emergence, frozen

1.4 NEGATIVE CHECK:
  Is element absence/negation of something?
  YES → visualize via boundary or effect
  Print: `[NEGATIVE: "[element]" → "[boundary/effect]"]`
  Examples:
    darkness → edge where light ends, or objects in shadow
    silence → still air, closed ears, flat sound wave
    emptiness → container with nothing inside, negative space

1.5 SCALE CHECK:
  Flag elements with incompatible scales:
  Print: `[SCALE CONFLICT: "[large]" vs "[small]" — reconciliation: [method]]`
  
  Reconciliation methods:
  - PERSPECTIVE: small element in foreground, large in background
  - REPRESENTATION: large element as image/model/reflection
  - FRAGMENT: large element represented by fragment (ocean → wave, city → building)
  - CONTAINER: large contains small naturally

1.6 HOSTILE CHECK:
  Do elements destroy each other? (fire/water, light/darkness)
  Print: `[HOSTILE PAIR: "[A]" vs "[B]" — handling: [method]]`
  
  Handling methods:
  - MOMENT_BEFORE: show instant before contact
  - MOMENT_OF: show contact point (steam, eclipse, etc.)
  - COEXISTENCE: find context where both exist (kitchen: stove + sink)
  - EMBRACE: destruction IS the interaction (for S3+ surreal)

1.7 SEMANTIC OVERLAP CHECK:
  Are elements synonyms or variants?
  Print: `[OVERLAP: "[A]" ≈ "[B]" — handling: [EXPLOIT/SEPARATE/MERGE]]`
  
  Default: EXPLOIT (use similarity for irony/contrast)

1.8 NSFW CHECK:
  Does element combination suggest explicit content?
  YES → auto-activate Module C
  Print: `[MODULE C ACTIVATED: element combination suggests explicit content]`

1.9 COUNT CHECK:
  IF elements > 10:
    HARD REJECT: "Maximum 10 elements. Current: [N]. Remove [N-10]."
  IF elements > 7:
    WARN: "8+ elements may overload S1. Consider reducing."
  IF elements < 2:
    HARD REJECT: "Minimum 2 elements required for MODE 3."

**STEP 2 — S1 LITERAL SCENE CONSTRUCTION:**

Find ONE realistic scene containing ALL elements:

2.1 LOCATION SEARCH:
  Where could all N elements naturally coexist?
  Prioritize: settings where elements interact, not just coexist
  
2.2 INTERACTION MAPPING:
  Define minimum 2 interactions between elements:
  [A]──[relationship]──[B]
  
  Relationship types:
  PHYSICAL: touches, holds, contains, supports, breaks
  OPTICAL: reflects, shadows, illuminates, obscures
  SPATIAL: above, inside, through, around, beside
  CAUSAL: causes, prevents, transforms (for S1: use STATIC causal, e.g., "about to")

2.3 LITERAL TEST:
  Can S1 scene be photographed in reality?
  YES → proceed
  NO → revise until yes (S1 MUST be photographable)

2.4 S1 DENSITY RULES (by element count):
  2-4 elements: ALL must be ACTIVE (interacting, not just present)
  5-7 elements: 3-4 ACTIVE, rest PRESENT (visible but background)
  8-10 elements: 3-4 ACTIVE, 3-4 PRESENT, rest IMPLIED (mentioned, not focal)

Print: `[S1 SCENE: "[description]" — LITERAL TEST: PASS]`

**STEP 3 — COHERENCE THREAD SELECTION:**

IF user provided COHERENCE → use it
ELSE auto-derive:

3.1 Analyze elements for shared properties:
  - Color family (all warm? all cool? contrast pair?)
  - Texture family (all rough? all smooth? contrast?)
  - Scale family (all intimate? all vast?)
  - Temporal association (all ancient? all modern?)

3.2 Select strongest thread:
  Print: `[COHERENCE: [type] — "[description]"]`

3.3 CONFLICT CHECK:
  Does coherence conflict with any element?
  YES → modify coherence or element presentation
  Print: `[COHERENCE ADAPTED: "[element]" presented as "[adaptation]" to fit "[thread]"]`

**STEP 4 — GRADIENT PLANNING:**

Based on GRADIENT setting, plan mutations:

4.1 ELEMENT WEIGHT ROTATION:
  Each element must be PRIMARY in at least one slot.
  Track: [element] = PRIMARY in S[n]
  
  Default rotation (5 elements):
  S1: element 1 primary
  S2: element 2 primary
  S3: element 3 primary
  S4: element 4 primary
  S5: element 5 primary OR all equal (COLLAPSE)

4.2 ROLE ROTATION:
  No element may hold same role for 3+ consecutive slots.
  
  Roles:
  SUBJECT: performs action, focal point
  OBJECT: receives action, secondary focus
  LOCATION: contains others, setting
  INSTRUMENT: used by subject
  MATERIAL: substance others are made of

4.3 MUTATION SEQUENCE (SMOOTH gradient):

S2 — SHIFTED (exactly 1 strangeness):
  Select 1 element to mutate
  Mutation types:
  - PROPERTY TRANSFER: gains property of another element
  - BEHAVIOR CHANGE: acts unlike itself
  - SCALE SHIFT: becomes larger/smaller
  - MATERIAL SHIFT: changes substance slightly
  
  Print: `[S2 SHIFT: "[element]" gains "[property/behavior]"]`

S3 — SURREAL (2-3 role swaps):
  Select 2-3 elements to swap roles
  Additionally: 1 spatial violation allowed
  
  Spatial violations:
  - Inside-out (small contains large)
  - Gravity defiance (local, not scene-wide)
  - Scale coexistence (different scales in contact)
  
  Print: `[S3 SWAPS: [list of role changes]]`
  Print: `[S3 SPATIAL: "[violation]"]`

S4 — ABSURD (3+ physics breaks):
  Physics violations:
  - Gravity (global)
  - Containment (impossible containers)
  - Material (things made of wrong substances)
  - Causality (effects without causes)
  - Identity (A is also B simultaneously)
  - Space (non-Euclidean, recursive, infinite)
  - Time (frozen, reversed, simultaneous)
  
  Minimum 3 violations, may stack.
  
  Print: `[S4 PHYSICS: [list of violations]]`

S5 — RESOLUTION:
  Based on S5_RESOLUTION setting:
  
  COLLAPSE:
    All elements merge into single hybrid entity
    Each element contributes: shape OR texture OR color OR behavior
    Hybrid must be identifiable as containing all source elements
    
  ABSENCE:
    All elements removed from scene
    Traces remain: marks, residue, shadows, temperature, impressions
    Environment shows evidence of all N having been present
    
  MATRYOSHKA:
    Elements nested: A contains B contains C contains D...
    Order can be size-logical or inverted for surrealism
    Innermost element = most transformed
    
  EXPLOSION:
    All elements fragmented, pieces scattered and intermixed
    A-fragments near B-fragments, creating hybrid zones
    Motion implied (mid-explosion frozen) or aftermath (settled chaos)
    
  LOOP:
    Scene mirrors S1 but all roles inverted
    What was subject is now object
    What was container is now contained
    Creates implication of eternal cycle
  
  Print: `[S5 RESOLUTION: [type] — "[description]"]`

4.4 INTERACTION EVOLUTION LADDER:

  S1 LITERAL:
    Interactions: Physical, Optical, Spatial (realistic)
  
  S2 SHIFTED:
    Interactions: Add Property Transfer
    (element A gains visible property of element B)
  
  S3 SURREAL:
    Interactions: Add Containment Reversal, Scale Swap
    (small contains large, roles exchanged)
  
  S4 ABSURD:
    Interactions: Add Material Exchange, Identity Blur
    (A made of B, A is also B)
  
  S5 RESOLUTION:
    Interactions: Boundary Dissolution
    (cannot tell where A ends and B begins)

**STEP 5 — ELEMENT IDENTITY ANCHORS:**

For each element, define ONE property that persists across all slots:

  This ensures element remains identifiable even when transformed.
  
  Anchor types:
  - COLOR: element always has this hue
  - SHAPE: element always has this silhouette
  - TEXTURE: element always has this surface quality
  - BEHAVIOR: element always does/implies this action
  - SIZE RATIO: element always this size relative to another
  
  Print: `[ANCHORS: [element1]=[anchor], [element2]=[anchor], ...]`

**STEP 6 — FINAL MODE 3 ROUTING:**

  IF MODE 3 active:
    Arc type: REMIX
    Slot architecture: LITERAL → SHIFTED → SURREAL → ABSURD → RESOLUTION
    Seeds: replaced by TRANSFORMATION DIRECTIVES
    Entry Angle: OPTIONAL (default: interaction-first for S1-S2)
    Lens diversity: REQUIRED (recommend: PHOTO → CINE → SENSORY → PAINT → ENV)
    Contrast distribution: ADAPTED (see below)

Print Routing Summary (MODE 3):
```
Mode: REMIX ([N] elements)
Elements: [list with any translations noted]
Primary: [element or "rotating"]
S1 Scene: [literal scene description]
Coherence: [thread type]: "[description]"
Gradient: [type]
Mutations: S2=[shift] | S3=[swaps] | S4=[breaks]
S5: [resolution type] + [tone]
Anchors: [element:anchor pairs]
```
```

---

## SLOT ARCHITECTURE — ADDITIONS

Add new section after FULL ARC:

```
### REMIX ARC (MODE 3):

**Structure:**
S1 LITERAL → S2 SHIFTED → S3 SURREAL → S4 ABSURD → S5 RESOLUTION

**Gradient Levels:**

| Slot | Level | Strangeness Count | Physics | Reality Status |
|------|-------|-------------------|---------|----------------|
| S1 | LITERAL | 0 | Obeyed | Photographable |
| S2 | SHIFTED | 1 | Mostly obeyed | Almost photographable |
| S3 | SURREAL | 2-3 | Dream logic | Internally consistent impossibility |
| S4 | ABSURD | 3+ | Broken | Multiple simultaneous impossibilities |
| S5 | RESOLUTION | Variable | Collapsed/Dissolved | Hybrid state |

**Slot Specifications:**

**S1 — LITERAL:**
- All N elements visible in single realistic scene
- Photographable in real world (test: could you take this picture?)
- Elements interact naturally (minimum 2 interactions)
- Entry angle optional but recommended
- Coherence thread established
- Technical specs: standard lens parameters
- Primary element = first or user-specified

**S2 — SHIFTED:**
- Same scene as S1 OR slight location shift
- Exactly ONE element behaves strangely
- Strange behavior must be visually clear, not subtle
- Other elements react naturally to the strangeness
- "Almost photographable" — one impossible thing in real scene
- Coherence thread maintained

**S3 — SURREAL:**
- Scene may transform but remains readable
- 2-3 elements swap roles (subject↔object, container↔contained)
- 1 spatial violation allowed
- Logic of dream: internally consistent impossibility
- Viewer should understand "what" but question "how"
- Coherence thread maintained
- Style may shift toward surrealist painters (Magritte, Chirico)

**S4 — ABSURD:**
- Physics fully optional
- Minimum 3 simultaneous impossibilities
- Elements may exchange materials, identities, behaviors
- Space may be non-Euclidean, recursive, infinite
- Viewer should feel "this cannot exist, but I see it"
- Coherence thread = anchor in chaos
- Style may shift toward Dalí, Beksiński, Remedios Varo

**S5 — RESOLUTION:**
- Depends on S5_RESOLUTION type:

  COLLAPSE:
    Single hybrid entity containing aspects of all elements
    Each element contributes identifiable feature
    Entity should pass "Friend Test" (viewer names 50%+ elements from visual)
    Emotional tone per S5_TONE
    
  ABSENCE:
    All elements removed from scene
    Only traces remain (marks, residue, temperature, impressions)
    Scene clearly RECENTLY held all elements
    Environmental departure: elements NOT visible
    Friend Test: viewer identifies WHAT was here from traces
    
  MATRYOSHKA:
    Nested structure: element A contains B contains C...
    Each layer visible (cutaway, transparency, partial opening)
    Creates infinite regress feeling
    
  EXPLOSION:
    All elements fragmented, mid-scatter or just-settled
    Fragment intermixing creates hybrid zones
    Chaos with underlying pattern (coherence thread)
    
  LOOP:
    S1 scene with all roles inverted
    Subject now object, container now contained
    Creates cycle implication: S5 leads back to S1
    May be subtle or obvious inversion

**Element Presence Rules:**

| Slot | Presence Requirement |
|------|---------------------|
| S1 | ALL elements visually distinct and identifiable |
| S2 | ALL elements present, one behaving strangely |
| S3 | ALL elements present, may be transformed but identifiable via anchor |
| S4 | ALL elements present, may be merged/exchanged but anchor property visible |
| S5-COLLAPSE | All elements fused, each identifiable via contributed feature |
| S5-ABSENCE | NO elements present, all identifiable via traces |
| S5-MATRYOSHKA | All elements present in nested structure |
| S5-EXPLOSION | All elements present as fragments |
| S5-LOOP | All elements present with inverted roles |

**Primary Element Rotation (if PRIMARY: NONE):**

| Slot | Primary Element |
|------|-----------------|
| S1 | Element 1 (or user choice) |
| S2 | Element 2 |
| S3 | Element 3 |
| S4 | Element 4 |
| S5 | Element 5 OR all equal |

For fewer elements: rotate and repeat.
For more elements: group by semantic similarity.

**Visual Rhythm:**

| Slot | Density | Composition |
|------|---------|-------------|
| S1 | HIGH | Balanced (all elements weighted) |
| S2 | MEDIUM | Focal (mutating element highlighted) |
| S3 | HIGH | Dynamic (elements in tension) |
| S4 | HIGHEST | Controlled chaos |
| S5 | MEDIUM-LOW | Unified (resolution, not overload) |

**Contrast Levels (MODE 3 adaptation):**

Standard H/M/L distribution applies, but:
- S1-S2: Prioritize readable contrast (HIGH or MEDIUM)
- S3-S4: May use any level (chaos can be low-contrast)
- S5: Match emotional tone (DREAD=HIGH, MELANCHOLY=LOW, etc.)

**Lens Sequence (MODE 3 recommendation):**

| Slot | Recommended | Rationale |
|------|-------------|-----------|
| S1 | PHOTO | Establish reality baseline |
| S2 | CINE | Slight narrative shift |
| S3 | SENSORY | Dream-adjacent feeling |
| S4 | PAINTERLY | Absurdity benefits from artistic treatment |
| S5 | ENV or SYMBOLIC | Resolution scale or abstraction |

Alternatives acceptable. Standard diversity rules apply (≥4 different, none >2×).

**Entry Angle (MODE 3):**

OPTIONAL. If applied:
- S1: Recommend INTERACTION-FIRST (relationship opens, elements follow)
- S2: Recommend ELEMENT-FIRST (mutating element opens)
- S3-S5: Not applicable (surreal content > angle discipline)

If ENTRY_ANGLES provided by user → apply to S1-S2 only.

**Rendering Phrases (MODE 3):**

| Slot | Rendering Vocabulary |
|------|---------------------|
| S1 | Standard photo/cine realism |
| S2 | "almost real, one impossible element" |
| S3 | "surrealist clarity, Magritte-logic" |
| S4 | "Dalí-precision on impossible topology" or "Beksiński organic fusion" |
| S5 | Match resolution type |

Rendering phrase placement: 2nd or 3rd-to-last sentence.
```

---

## BAN REGISTRY — ADDITIONS

Add new section:

```
### MODE 3 EXTENSIONS (apply when MODE 3 active)

**ADDITIONAL ZERO TOLERANCE:**

| Banned | Replacement |
|--------|-------------|
| represents / symbolizes | [physical description of hybrid] |
| fusion of / combination of | [describe result directly] |
| mix of / blend of | [describe result directly] |
| impossible (as adjective) | [show impossibility, don't label] |
| unreal / surreal (as adjective) | [specific visual quality] |
| dreamlike / dream-like | [specific quality: soft focus, floating, etc.] |
| transforms into / becomes | [frozen state description] |
| is becoming / merging | [static hybrid description] |
| in the process of | [peak moment frozen] |

**RATIONALE:**
MODE 3 prompts describe STATES, not PROCESSES.
Camera captures frozen moment, even if moment is impossible.
Show, don't label. "Surreal" in prompt ≠ surreal image.

**EXAMPLES:**

❌ "The bird is transforming into a tree"
✅ "A creature with raven-body and branch-wings, feathers becoming bark at the joints"

❌ "A surreal fusion of fire and water"
✅ "Steam-veined flames, water-shaped fire frozen mid-flow, surface both wet and burning"

❌ "The impossible combination of clock and ocean"
✅ "Clock-face floating on waves, hour hand pointing at tide, minute hand dripping salt water"

**PROCESS → STATE TRANSLATIONS:**

| Process Word | State Replacement |
|--------------|-------------------|
| melting | half-melted, drip frozen mid-fall |
| growing | mid-emergence, growth frozen at peak |
| falling | mid-fall, suspended in descent |
| exploding | mid-explosion, debris frozen in spray |
| merging | partially merged, boundary half-dissolved |
| dissolving | half-dissolved, edge becoming mist |
```

---

## HARD CHECKS — ADDITIONS

Add new priority section:

```
### PRIORITY 1-F: MODE 3 Validation (if MODE 3 active)

**HC-25. Element Presence Check:**
  For each slot, verify all N elements present (or traceable in COLLAPSE):
  
  S1-S4: Each element must be visually identifiable OR identifiable via anchor property
  S5-COLLAPSE: Each element must contribute identifiable feature to hybrid
  S5-ABSENCE: Each element must leave identifiable trace
  
  Print: `[ELEMENT PRESENCE S[n]: [element1]:✓ [element2]:✓ ... ]`
  If any missing → REWRITE slot to include element

**HC-26. Gradient Compliance Check:**
  Verify each slot matches its gradient level:
  
  | Slot | Required |
  |------|----------|
  | S1 | 0 impossibilities, photographable |
  | S2 | Exactly 1 strangeness |
  | S3 | 2-3 role swaps or spatial violations |
  | S4 | 3+ physics violations |
  | S5 | Matches S5_RESOLUTION type |
  
  Count impossibilities per slot.
  Print: `[GRADIENT: S1=[0] S2=[1] S3=[2] S4=[4] S5=[COLLAPSE] — PASS]`
  If count wrong → REWRITE

**HC-27. Role Rotation Check:**
  Verify no element holds same role for 3+ consecutive slots:
  
  Track: [element] → S1:[role] S2:[role] S3:[role] S4:[role] S5:[role]
  If any element has same role ×3 in a row → REWRITE middle slot with different role
  
  Print: `[ROLE ROTATION: PASS]` or `[ROLE ROTATION: [element] stuck as [role] S[n]-S[m] — REVISED]`

**HC-28. Coherence Thread Check:**
  Verify coherence thread visible in all 5 slots:
  
  Thread types:
  - PALETTE: color family present in each slot
  - TIME: lighting consistent with time of day
  - TEXTURE: material quality consistent
  - ELEMENT_ANCHOR: specified element maintains property
  
  Print: `[COHERENCE: "[thread]" — S1:✓ S2:✓ S3:✓ S4:✓ S5:✓]`
  If missing in any slot → REWRITE to include thread

**HC-29. Anchor Property Check:**
  Verify each element's identity anchor appears in all slots:
  
  For each element:
    Anchor = [color/shape/texture/behavior/size ratio]
    Check: anchor present in S1? S2? S3? S4? S5?
  
  If anchor missing → element unrecognizable → REWRITE

**HC-30. S5 Resolution Match:**
  Verify S5 content matches declared S5_RESOLUTION:
  
  COLLAPSE: Is there a single hybrid entity? Can viewer identify N/2+ source elements?
  ABSENCE: Are all elements absent? Are traces visible?
  MATRYOSHKA: Is nesting structure clear?
  EXPLOSION: Are fragments from all elements present?
  LOOP: Are all roles inverted from S1?
  
  Print: `[S5 RESOLUTION: [type] — [PASS/FAIL: reason]]`

**HC-31. S5 Friend Test:**
  Verify S5 is identifiable:
  
  COLLAPSE: "Could someone name 50%+ source elements from visual?"
  ABSENCE: "Could someone name what WAS here from traces?"
  MATRYOSHKA: "Could someone describe nesting order?"
  EXPLOSION: "Could someone identify fragment sources?"
  LOOP: "Could someone recognize inverted S1?"
  
  If NO → S5 too abstract → add identifying features

**HC-32. MODE 3 Ban Check:**
  Scan all slots for MODE 3 banned phrases:
  "represents", "symbolizes", "fusion of", "combination of",
  "impossible" (adj), "surreal" (adj), "dreamlike", "transforms into"
  
  If found → replace per MODE 3 EXTENSIONS table
  Print: `[MODE 3 BANS: CLEAN]` or `[MODE 3 BAN FIXED: "[orig]" → "[new]" in S[n]]`

**HC-33. S1 Literal Test:**
  Verify S1 is photographable:
  
  Questions:
  - Could a photographer capture this scene? (with props, location, timing)
  - Are all elements physically possible in their depicted state?
  - Is there exactly ZERO supernatural/impossible content?
  
  If ANY impossibility in S1 → REWRITE to remove
  Exception: if ALL elements are inherently fantastical (unicorn, dragon), S1 = "normal for them"

**HC-34. Interaction Presence:**
  Verify S1 has minimum 2 interactions between elements:
  
  Count explicit relationships: "A on B", "C reflects D", "E holds F"
  If <2 → elements just coexist, not interact → ADD interactions

  Print: `[INTERACTIONS S1: [count] — [PASS/ADD]]`
```

---

## SLOT VALIDATION STACK — ADDITIONS

Add to existing stack:

```
### Level 8: MODE 3 Specific (if MODE 3 active)

SV-25. Element presence — all N elements identifiable per slot
SV-26. Gradient compliance — impossibility count matches slot level
SV-27. Role rotation — no element same role ×3 consecutive
SV-28. Coherence thread — visible in all slots
SV-29. Anchor properties — each element's anchor present
SV-30. S5 resolution match — content matches declared type
SV-31. S5 friend test — resolution identifiable
SV-32. MODE 3 bans — no process words, no labels
SV-33. S1 literal — photographable, zero impossibilities
SV-34. Interactions — S1 has ≥2 element interactions
```

---

## PHASE 4 — ADDITIONS

Add new subsection:

```
### 4.4 Permutation Execution (MODE 3)

When MODE 3 active, replace standard seed generation with:

**4.4.1 TRANSFORMATION DIRECTIVES:**

Instead of Seeds 1-3, generate Directives:

S2_DIRECTIVE: {
  element: "[which element shifts]"
  shift_type: "[PROPERTY_TRANSFER / BEHAVIOR / SCALE / MATERIAL]"
  description: "[specific shift]"
}

S3_DIRECTIVE: {
  swaps: [
    { element: "[A]", from_role: "[role]", to_role: "[role]" },
    { element: "[B]", from_role: "[role]", to_role: "[role]" }
  ]
  spatial_violation: "[description]" or "NONE"
}

S4_DIRECTIVE: {
  physics_breaks: [
    "[violation 1]",
    "[violation 2]",
    "[violation 3]"
  ]
  material_exchanges: "[description]" or "NONE"
  identity_blurs: "[description]" or "NONE"
}

S5_DIRECTIVE: {
  resolution_type: "[COLLAPSE/ABSENCE/MATRYOSHKA/EXPLOSION/LOOP]"
  tone: "[emotional target]"
  description: "[specific resolution visualization]"
  element_contributions: {
    "[element1]": "[what it contributes to hybrid/traces]",
    "[element2]": "[what it contributes]",
    ...
  }
}

Print directives in Routing Summary.

**4.4.2 SLOT-TO-DIRECTIVE BINDING:**

| Slot | Source |
|------|--------|
| S1 | S1 LITERAL SCENE (from B.3) |
| S2 | S2_DIRECTIVE |
| S3 | S3_DIRECTIVE |
| S4 | S4_DIRECTIVE |
| S5 | S5_DIRECTIVE |

**4.4.3 COHERENCE THREADING:**

Before writing each slot:
1. Check: coherence thread present in slot plan?
2. If NO → add coherence element before writing
3. Track: coherence type, specific manifestation per slot

**4.4.4 ELEMENT TRACKING:**

Maintain running check:
| Element | S1 | S2 | S3 | S4 | S5 |
|---------|----|----|----|----|-----|
| [name] | [role] | [role] | [role] | [role] | [contribution] |

Verify:
- All cells filled (no missing elements)
- No element has same role ×3 consecutive
- Each element is PRIMARY at least once

**4.4.5 LENS ASSIGNMENT (MODE 3):**

Apply standard lens diversity with MODE 3 recommendations:
- S1: PHOTO (reality baseline)
- S2: CINE or PHOTO (still near-real)
- S3: SENSORY or PAINTERLY (dream shift)
- S4: PAINTERLY or SYMBOLIC (absurdity)
- S5: ENV, SYMBOLIC, or PAINTERLY (resolution scale)

Verify: ≥4 different lenses, none >2×
```

---

## PHASE 5 — MODIFICATIONS

Add to Writing Process:

```
### 5.1.5 MODE 3 Prompt Construction

When writing MODE 3 slots:

**S1 STRUCTURE:**
1. Open with scene establishment (all elements visible)
2. Describe minimum 2 interactions
3. Primary element in focus position
4. Technical specs (lens, f-stop)
5. Coherence thread visible
6. Final sentence: physical detail

**S2 STRUCTURE:**
1. Reference S1 scene OR slight location shift
2. Name the mutating element early
3. Describe EXACTLY ONE impossibility
4. Other elements react naturally
5. Technical specs
6. Coherence maintained
7. Final sentence: the strange element

**S3 STRUCTURE:**
1. Transformed scene (may be very different from S1-S2)
2. Role swaps clear in description
3. Spatial violation integrated naturally
4. Elements identifiable via anchors
5. Surrealist rendering reference optional
6. Coherence maintained
7. Final sentence: physical impossibility

**S4 STRUCTURE:**
1. Physics-defying scene
2. Multiple violations stacked (list or integrated)
3. Material/identity exchanges if present
4. All elements present, possibly merged/exchanged
5. Dalí/Beksiński rendering reference optional
6. Coherence maintained
7. Final sentence: specific impossible detail

**S5 STRUCTURE (varies by resolution):**

COLLAPSE:
1. Single hybrid entity described
2. Each element's contribution named
3. Entity anatomy/physiology detailed
4. Emotional tone (wonder/dread/etc.)
5. Coherence as unifying thread
6. Final sentence: what viewer feels or hybrid's state

ABSENCE:
1. Empty space described
2. Each element's trace named
3. Evidence arranged spatially
4. Melancholy or mystery tone
5. Coherence in residue
6. Final sentence: most telling trace

MATRYOSHKA:
1. Nesting structure described outside-in or inside-out
2. Each layer named with element
3. Transitions between layers
4. Vertigo or wonder tone
5. Coherence across layers
6. Final sentence: innermost or implication

EXPLOSION:
1. Scatter pattern described
2. Fragment sources identifiable
3. Hybrid zones where fragments mix
4. Energy or chaos tone
5. Coherence in underlying pattern
6. Final sentence: single frozen fragment

LOOP:
1. S1 scene recognizable but inverted
2. Each role swap named
3. Cycle implication clear
4. Trap or acceptance tone
5. Coherence links S5 to S1
6. Final sentence: what begins again

**DESCRIPTION MODE RULE:**
All MODE 3 prompts describe STATES, not PROCESSES.
Even mid-transformation → describe as frozen moment.
Camera captures what IS, not what is HAPPENING.
```

---

## OUTPUT PROTOCOL — ADDITIONS

Add to Routing Summary:

```
### MODE 3 Routing Summary

When CONCISE_MODE = true and MODE 3:

```
Mode: REMIX ([N] elements)
Elements: [element1] | [element2] | [element3] | ...
Primary: [element] or "rotating"
S1 Scene: [one sentence literal scene]
Coherence: [thread type]: "[anchor]"
Gradient: [type]
Shifts: S2=[element:shift] | S3=[swaps] | S4=[breaks]
S5: [resolution] + [tone]
[ROUTING COMPLETE — proceeding to prompts]
```

When CONCISE_MODE = false or omitted:

Full Decision Block includes:
- Mode: REMIX
- Element count: [N]
- Elements: [list with any translations/freezes noted]
- Primary: [element or "rotating"]
- S1 Literal Scene: [2-3 sentences]
- Coherence Thread: [type]: "[description]"
- Gradient: [type]
- S2 Directive: [element] [shift type] "[description]"
- S3 Directive: [swaps], spatial: [violation or none]
- S4 Directive: [physics breaks], material: [exchanges or none]
- S5 Directive: [resolution] + [tone] + "[description]"
- Element Anchors: [element:anchor pairs]
- Lens Sequence: [S1→S2→S3→S4→S5]
- Interaction Map: [element relationships]

Then standard prompt output.

### MODE 3 Mandatory Verification

After all slots, print:

```
[MODE 3 VERIFICATION:
  Elements: [e1]:✓ [e2]:✓ [e3]:✓ ... (all present in all slots)
  Gradient: S1=[0] S2=[1] S3=[3] S4=[4] S5=[resolution] — PASS
  Coherence: "[thread]" — all slots ✓
  Roles: no element stuck — PASS
  S5 Friend Test: [X]/[N] elements identifiable — PASS]
```
```

---

## COMPATIBILITY RULES

Add new section:

```
### MODE 3 COMPATIBILITY MATRIX

**ARC COMPATIBILITY:**
| Arc | MODE 3 | Resolution |
|-----|--------|------------|
| FULL ARC | REPLACED | MODE 3 uses REMIX ARC instead |
| SHALLOW ARC | INCOMPATIBLE | If GOAL: commercial + ELEMENTS → auto-convert to artistic + warn |

Print if conflict: `[ARC CONFLICT: SHALLOW incompatible with MODE 3 — converted to artistic]`

**MODULE COMPATIBILITY:**
| Module | MODE 3 | Notes |
|--------|--------|-------|
| A (poster) | COMPATIBLE | Surreal poster content allowed |
| B (packaging) | CONSTRAINED | Product element must remain identifiable S1-S3 |
| C (explicit) | AUTO-ACTIVATE | If NSFW elements detected |
| D (lifecycle) | INCOMPATIBLE | Lifecycle and Permutation are different axes |

Print if Module D requested: `[MODULE CONFLICT: D incompatible with MODE 3 — choose one]`

**Module B + MODE 3 rules:**
- One element must be designated as PRODUCT
- PRODUCT element maintains form in S1-S3
- S4-S5 may transform PRODUCT (surreal packaging)
- Print: `[MODE 3 + MODULE B: "[element]" designated as product — form maintained S1-S3]`

**PLATFORM COMPATIBILITY:**
| Platform | MODE 3 Support | Notes |
|----------|---------------|-------|
| Midjourney v6+ | EXCELLENT | Add `--style raw` for S4-S5 |
| Flux Pro | GOOD | Add "highly detailed surrealist" for S3-S5 |
| SDXL | VARIABLE | Recommend dreamshaper/dynavision checkpoint |
| DALL-E 3 | POOR | Safety filters may reject; NOT RECOMMENDED |
| Aurora | GOOD | Add "metaphorical visualization" for S3-S5 |

Print if DALL-E 3: `[PLATFORM WARNING: DALL-E 3 not recommended for MODE 3 — safety filters may reject surreal content]`

**MODE 2 + MODE 3 (EXPERIMENTAL):**

If user requests both lifecycle AND permutation:

Enable with: `MODE: 2+3` or `MODE: HYBRID`

Combined arc:
| Slot | Lifecycle | Permutation | Combined |
|------|-----------|-------------|----------|
| S1 | intact | literal | All elements new, realistic scene |
| S2 | use | shifted | Elements in use, one strange |
| S3 | wear | surreal | Elements worn, roles swapped |
| S4 | repurpose | absurd | Elements repurposed, physics broken |
| S5 | trace | resolution | Traces + collapse/absence |

Print: `[MODE 2+3: EXPERIMENTAL — high complexity, recommend ≤4 elements]`

**GOAL COMPATIBILITY:**
| GOAL | MODE 3 | Notes |
|------|--------|-------|
| artistic | NATIVE | Full creative freedom |
| personal | NATIVE | Full creative freedom |
| editorial | COMPATIBLE | Surreal editorial possible |
| commercial | CONVERT | Auto-convert to artistic, warn |
| scientific | CONVERT | Auto-convert to artistic, warn |

Print if commercial/scientific: `[GOAL CONVERTED: [original] → artistic for MODE 3 compatibility]`
```

---

## RERUN HANDLING — ADDITIONS

Add new section:

```
### MODE 3 RERUN TRACKING

When RERUN detected with same ELEMENTS:

**REQUIRED DIFFERENCES (all must change):**
1. S1 Literal Scene — different location/time/interaction
2. S2 Shift — different element mutates, or different mutation type
3. S5 Resolution — different type OR different tone
4. Coherence Thread — different category (palette→texture→time)
5. Primary Rotation — different starting primary

**TRACKING FORMAT:**

SESSION_HISTORY (MODE 3): {
  ELEMENTS: "[e1|e2|e3|...]"
  S1_SCENE: "[description]"
  S2_SHIFT: "[element:type]"
  S5_RESOLUTION: "[type+tone]"
  COHERENCE: "[thread]"
  PRIMARY_ORDER: "[e1,e3,e2,...]"
}

**RERUN ENFORCEMENT:**

IF RERUN detected:
  Compare to SESSION_HISTORY (MODE 3)
  FOR each tracked field:
    IF same as previous → force alternative
  Print: `[MODE 3 RERUN: [field] changed from [old] to [new]]`

**CROSS-SERIES DIVERSITY:**

Track across conversation:
- S5_RESOLUTION types used (max same type ×2 in 4 runs)
- Coherence categories used (rotate through all before repeat)
- S2 shift elements used (each element should shift at least once)

Print ceiling if exceeded: `[S5 TYPE CEILING: COLLAPSE used ×2 — forcing ABSENCE]`
```

---

## DIAGNOSTIC TEMPLATE — ADDITIONS

Add for CONCISE_MODE = false:

```
### MODE 3 DIAGNOSTIC (if CONCISE_MODE = false and MODE 3 active)

Print after Routing Summary:

```
═══════════════════════════════════════════════════════════════
MODE 3 DIAGNOSTIC
═══════════════════════════════════════════════════════════════

ELEMENTS RECEIVED: [N]
├── [element1]: [type] → [any translation]
├── [element2]: [type] → [any translation]
└── ...

VALIDATION:
├── Photo Test: [list any translations]
├── Scale Reconciliation: [method if needed]
├── Hostile Pairs: [list or NONE]
├── Semantic Overlap: [list or NONE]
├── NSFW Detection: [CLEAR or MODULE C ACTIVATED]

S1 LITERAL CONSTRUCTION:
├── Location: [where]
├── Time: [when]
├── Interactions: [A-rel-B, C-rel-D, ...]
├── Photographable: YES
└── All elements active/present: [breakdown]

COHERENCE THREAD:
├── Type: [PALETTE/TIME/TEXTURE/ELEMENT_ANCHOR]
├── Description: "[specific anchor]"
└── Derived/User-specified: [which]

GRADIENT PLAN:
├── Type: [SMOOTH/SHARP/REVERSE/PEAK/VALLEY]
├── S2 Shift: [element] + [type] = "[description]"
├── S3 Swaps: [list]
├── S3 Spatial: [violation or NONE]
├── S4 Physics: [list of 3+ violations]
├── S4 Material/Identity: [exchanges or NONE]
└── S5 Resolution: [type] + [tone] = "[description]"

ELEMENT TRACKING:
│ Element │ Anchor │ S1 │ S2 │ S3 │ S4 │ S5 │
├─────────┼────────┼────┼────┼────┼────┼────┤
│ [e1]    │ [prop] │[role]│[role]│[role]│[role]│[contrib]│
│ ...     │        │    │    │    │    │     │

PRIMARY ROTATION: [order]
ROLE ROTATION CHECK: [PASS or violations]

LENS SEQUENCE: [S1]→[S2]→[S3]→[S4]→[S5]
ASPECT: [ratio]

ESTIMATED COMPLEXITY: [LOW/MEDIUM/HIGH/VERY HIGH]
═══════════════════════════════════════════════════════════════
```
```

---

## ERROR HANDLING

Add new section:

```
### MODE 3 ERROR HANDLING

**SOFT ERRORS (warn, continue):**

| Error | Message | Action |
|-------|---------|--------|
| Abstraction detected | `[ABSTRACTION: "[X]" → "[marker]"]` | Auto-translate |
| Action detected | `[ACTION FROZEN: "[X]" → "[state]"]` | Auto-freeze |
| Scale conflict | `[SCALE: reconciled via [method]]` | Auto-reconcile |
| Hostile pair | `[HOSTILE: "[A]" vs "[B]" — handling: [method]]` | Note, proceed |
| Semantic overlap | `[OVERLAP: "[A]" ≈ "[B]" — EXPLOIT]` | Note, proceed |
| 8-10 elements | `[WARN: [N] elements may overload S1]` | Proceed with caution |

**HARD ERRORS (block, request fix):**

| Error | Message | Required Fix |
|-------|---------|--------------|
| Elements > 10 | `[ERROR: Maximum 10 elements. Current: [N]]` | User must reduce |
| Elements < 2 | `[ERROR: Minimum 2 elements required]` | User must add |
| All abstract, no visual | `[ERROR: No visualizable elements. Add concrete object.]` | User must add object |
| Content policy | `[ERROR: Element "[X]" violates content policy]` | User must replace |
| Module D conflict | `[ERROR: Module D incompatible with MODE 3]` | User must choose one |

**GRACEFUL DEGRADATION:**

| Situation | Degradation |
|-----------|-------------|
| 8+ elements, S1 overloaded | First 4 ACTIVE, next 3 PRESENT, rest IMPLIED |
| S4 physics too complex to describe | Prioritize 3 most visual violations |
| S5 COLLAPSE too many features | Each element gets 1 feature, not multiple |
| Coherence conflicts with element | Adapt element presentation, note override |

Print: `[DEGRADATION: [situation] — [adaptation]]`
```

---

## EXAMPLES

Add new section:

```
### MODE 3 EXAMPLE OUTPUTS

**Example 1: Simple (3 elements)**

```
ELEMENTS: mirror | fire | key
MODE: 3
```

Routing:
```
Mode: REMIX (3 elements)
Elements: mirror | fire | key
Primary: mirror
S1 Scene: Brass key on mantle before fireplace, flames reflected in standing mirror
Coherence: PALETTE: warm amber and brass throughout
Gradient: SMOOTH
Shifts: S2=mirror reflects fire that isn't there | S3=key opens mirror, fire pours out | S4=inside mirror is endless burning corridor with floating keys
S5: COLLAPSE + WONDER
```

**Example 2: Complex (6 elements)**

```
ELEMENTS: clock | sand | raven | tower | echo | moon
MODE: 3
S5_RESOLUTION: ABSENCE
```

Routing:
```
Mode: REMIX (6 elements)
Elements: clock | sand (material) | raven | tower | echo (→ ripple-rings in dust) | moon
Primary: rotating
S1 Scene: Abandoned clock tower at moonrise, sand drifted through cracks, raven on minute hand, echo-ripples visible in dusty air
Coherence: TEXTURE: grit and grain on every surface
Gradient: SMOOTH
Shifts: S2=sand flows upward | S3=raven made of gears, tower becomes hourglass | S4=inside clock is desert under multiple moons
S5: ABSENCE + MELANCHOLY — empty tower floor with gear-shaped scratches, raven feathers, sand piles, echo-ring marks in dust, moon-shaped bleach marks
```

**Example 3: With abstractions**

```
ELEMENTS: love | door | storm | silence | red
MODE: 3
```

Routing:
```
Mode: REMIX (5 elements)
Elements: love (→ heart/warmth/red glow) | door | storm | silence (→ still air/frozen drops) | red (→ color anchor)
Primary: door
S1 Scene: Red door in field during approaching storm, heart carved in wood, moment of silence before rain
Coherence: PALETTE: red against grey storm, warmth vs cold
[ABSTRACTION: "love" → "heart carving + warmth glow"]
[ABSTRACTION: "silence" → "frozen raindrops, still grass"]
```
```

---

## QUICK REFERENCE

Add to end of document:

```
### MODE 3 QUICK REFERENCE

**ACTIVATION:**
ELEMENTS: [2-10 nouns separated by |]
MODE: 3 (or auto-detected from ELEMENTS)

**GRADIENT LEVELS:**
S1: LITERAL (0 impossibilities, photographable)
S2: SHIFTED (exactly 1 strangeness)
S3: SURREAL (2-3 role swaps)
S4: ABSURD (3+ physics violations)
S5: RESOLUTION (per S5_RESOLUTION type)

**S5 TYPES:**
COLLAPSE — all merge into hybrid
ABSENCE — all gone, traces remain
MATRYOSHKA — nested inside each other
EXPLOSION — fragmented and scattered
LOOP — S1 inverted, cycle implied

**REQUIRED CHECKS:**
□ All elements present each slot
□ Gradient counts correct
□ No role stuck ×3
□ Coherence in all slots
□ Anchors maintained
□ S5 friend test passes

**INCOMPATIBLE WITH:**
- SHALLOW ARC (converts to artistic)
- Module D (choose one)
- DALL-E 3 (not recommended)

**PROMPT RULES:**
- Describe STATES, not PROCESSES
- Show impossibility, don't label it
- Frozen moments, even mid-transformation
- Physical details, even for surreal
```

---

## VERSION

```
UPG v9.17.0
MODE 3: REMIX [BETA]
Release: [date]

For feedback on MODE 3, report:
- Element combinations that fail
- Gradient compliance issues
- Platform-specific problems
- Unexpected edge cases
```

---

# END OF PATCH

---

**Патч готов.**

**Следующий шаг:** BLOCK P для Checklist v1.6.1 → v1.7?