# UPG v9.12 → v9.13 REFACTORING INSTRUCTION

**Document type:** Comprehensive implementation guide
**Source synthesis:** Memo (3 rounds of review) + Diagnostic Report + Behavioral Verification (6 runs)
**Target:** Claude instance performing the refactoring

---

## PREAMBLE

You are receiving UPG v9.12 (current) and must produce UPG v9.13. This document contains all verified problems and ready-to-implement solutions. Problems are ordered by implementation dependency, not severity.

**Behavioral evidence from 6 test runs confirmed:**
- P1: "ending on" used in 60-80% of final sentences across runs
- P2: "soft knit" passes Tier 1 scan without qualification
- P3: Portrait SCALE uses framing descriptors naturally, contradicting written guidance
- P5: Identical lens sequence (PHOTO→CINE→PAINT→TEXT→ENV) and Seed 2 category (DOMESTIC) across all 6 runs — stateful rules not enforced

**Not confirmed:** P7 (planning bloat) — Decision Blocks were already compact in outputs.

---

## IMPLEMENTATION ORDER

Execute fixes in this exact sequence. Each step may depend on previous steps.

```
Step 1: BAN REGISTRY (creates canonical reference point)
Step 2: SLOT VALIDATION STACK (consolidates checks, references BAN REGISTRY)
Step 3: ENTRY ANGLE SYSTEM (consolidates fragments, adds portrait guidance)
Step 4: OUTPUT MODE PRECEDENCE (resolves mode conflicts)
Step 5: HARD CHECKS reorder (modules before platform suffix)
Step 6: TEXT → TEXTURAL rename
Step 7: S5 TRACE VERIFICATION logic fix
Step 8: SESSION_HISTORY input field + runtime note
Step 9: Final-sentence variation rule
Step 10: Adjective exception clarification
Step 11: Module A+D conflict resolution
Step 12: Feedback Protocol table format
Step 13: ARCHITECTURE section
Step 14: RERUN trigger clarification
Step 15: STRUCTURED THEME INPUT documentation
Step 16: Decision Block format (remove line limits)
```

---

## STEP 1: CREATE BAN REGISTRY

**Location:** Insert as new section immediately after INPUTS, before MIDJOURNEY MODE.

**Action:** Create new section with consolidated ban lists.

**Insert this content:**

```markdown
## BAN REGISTRY (canonical source — all other sections reference this)

### ZERO TOLERANCE — delete or rewrite on detection
| Banned | Replacement |
|--------|-------------|
| suggests / implying | shows / reveals |
| making X [adj] | X is [state] |
| reads as | resembles / matches |
| turning X into | X becomes |
| as if / as though | [visible physical state] |
| begins to / starting to / about to | [frozen result] |
| viewer / observer | [scene detail] |
| evoking / establishing / conveys | [physical detail] |
| juxtaposition / tension / interplay | [spatial arrangement] |
| echoes / mirrors / reflects (metaphorical) | [literal match or remove] |
| commands / dominates / anchors | [object properties] |
| proudly / boldly / gracefully | [remove] |
| while still [verb-ing] | [state] |
| from the [slot] / hero shot / S[n] | [independent scene] |

Conjugation Rule: All grammatical forms of listed terms are banned.
Print only if caught: `[ZERO TOLERANCE FIXED: "[orig]" → "[new]" in S[n]]`

### TIER 1 ADJECTIVES — qualify with material/measurable detail or replace
| Banned | Replacement examples |
|--------|---------------------|
| soft | diffused / muted / low-contrast / [material] + Shore A rating |
| clean | uncluttered / minimal / [specific absence] |
| fresh | recently-cut / undried / [time since state change] |
| fine | particulate / narrow / hairline / [measurement] |
| smooth | polished / satin / [surface finish spec] |
| gentle | gradual / low-angle / [degree measure] |
| subtle | understated / hint-of / [percentage or ratio] |
| elegant | proportioned / balanced / [geometric relationship] |
| delicate | thin-walled / lightweight / [thickness or weight] |
| simple | single-element / unadorned / [component count] |

**"fine" has highest escape rate — scan with priority.**

Tier 2 (also replace materially): nice, beautiful, lovely, pure, clear, calm, quiet, refined, pretty, pleasant

**Exception rule:** A banned adjective may remain ONLY when paired with a measurable or technically specific material qualifier. Examples:
- ✅ KEEP: "soft clay Shore A 20" / "soft wool 120gsm" / "fine mesh 400-count"
- ❌ REPLACE: "soft knit" / "soft fabric" / "fine detail" / "gentle curve"

### ABSTRACT NOUNS — delete always
stillness, silence, tension, energy, absence, void, memory, time, presence, atmosphere, essence, spirit, soul, beauty, power, grace, elegance, serenity, tranquility, harmony, balance, chaos, mystery

Test: Can you point to it in a photograph? NO → delete.
Modifier trap: Banned in ALL syntactic positions (subject, object, modifier, complement).

### BANNED FINAL PATTERNS
Final sentence must describe visible physical element (surface, edge, light, position, material).

Banned final verbs: turning, creating, demonstrating, achieving, establishing, serving as

Banned final constructions:
- Purpose/effect clauses ("...creating a sense of...")
- Abstract state claims ("...establishing mood...")
- Rendering instructions ("...rendered in...")

### LOCALIZED BANS (apply when input contains Russian)
| Banned (RU) | Replacement |
|-------------|-------------|
| будто / словно | [visible physical state] |
| как будто / как если бы | [visible physical state] |
```

---

## STEP 2: CREATE SLOT VALIDATION STACK

**Location:** Insert as new section after PHASE 5, before ZONE C — MODULES.

**Action:** Create unified validation procedure that references BAN REGISTRY.

**Insert this content:**

```markdown
## SLOT VALIDATION STACK (run per slot before output)

Execute checks in this order. If any check fails → rewrite silently before proceeding.

### Level 1: Structure
1. **Slot role compliance** — S1=ANCHOR, S2=TILT, S3=COLLISION/CONTEXT, S4=DRIFT/DETAIL, S5=RUPTURE/CONVERSION
2. **Entry Angle execution** (S1-S2 only) — first sentence realizes assigned angle type → see ENTRY ANGLE SYSTEM
3. **Carrying image presence** — S1-S3: dominant; S4: may recede but theme-connected; S5: traces only

### Level 2: Language
4. **BAN REGISTRY: ZERO TOLERANCE scan** — all forms of listed terms
5. **BAN REGISTRY: TIER 1 ADJECTIVES scan** — qualify or replace
6. **BAN REGISTRY: ABSTRACT NOUNS scan** — delete
7. **BAN REGISTRY: BANNED FINAL PATTERNS scan** — rewrite final sentence if violated

### Level 3: Distribution
8. **Adjacent slot uniqueness** — ≥3 differences from previous slot (setting, light, framing, lens, mood)
9. **Lens diversity** — verify running count: ≥4 different across set, no lens >2×
10. **Contrast level** — assign H/M/L, verify max 2 per level across set

### Level 4: Fidelity
11. **VISUAL_VOCABULARY enforcement** — if VV provided, use exact descriptions, no generic substitutes
12. **Setting fidelity** — enforce GEOGRAPHY/ERA/MUST_INCLUDE/MUST_AVOID
13. **Seed-to-slot binding** (FULL ARC) — S3=Seed1, S4=Seed2, S5=Seed3

### Level 5: Platform/Module
14. **Module minimums** (if active):
    - Module A: format + 2 text zones + copy line
    - Module B: form + closure + label
    - Module D: lifecycle stage matches slot
15. **Platform suffix** (if PLATFORM specified):
    - Midjourney: `--ar [ratio] --v 6 --style raw --s 50`
    - SD: negative prompt appended
16. **Length check** — Midjourney: ≤3 sentences S1-S4, ≤4 S5; SD: ≤100 words

### Level 6: Final
17. **Rendering phrase placement** (non-photo) — present in ≥3/5 slots, in 2nd or 3rd-to-last sentence, NOT in final sentence
18. **Final sentence physical detail** — must end on visible element

All checks run silently. Do not print "checks passed." If TRACE=true, print CHECK block after each slot.
```

---

## STEP 3: CONSOLIDATE ENTRY ANGLE SYSTEM

**Location:** Replace B.2 Step 6 entirely with new consolidated block.

**Action:** 
1. Delete current "STEP 6 — Entry Angle" content from B.2
2. Insert new ENTRY ANGLE SYSTEM block
3. Update cross-references in A.2.1, Phase 4.2, HARD CHECKS #10, Phase 5 #1

**Insert this content (replacing B.2 Step 6):**

```markdown
**STEP 6 — Entry Angle:** → see ENTRY ANGLE SYSTEM below.

### ENTRY ANGLE SYSTEM

#### Types (8)
| Type | What opens first sentence | Compliance level |
|------|---------------------------|------------------|
| SCALE | Number or dimension as subject/first modifier | Low — requires attention |
| TIME | Temporal marker | Medium |
| LOCATION | Place preposition (on, within, beneath, inside, at) | High — natural |
| WEATHER | Weather or atmospheric state | Medium |
| CULTURAL | Cultural element or artifact | Medium |
| MATERIAL | Material or substance as subject | Medium |
| PERSPECTIVE | Viewpoint or vantage indicator | Medium |
| ACTIVITY | Frozen peak action or arrested result | Medium |

#### Rotation Across Themes
| Pattern | S1 | S2 |
|---------|----|----|
| A | SCALE | TIME |
| B | TIME | LOCATION |
| C | CULTURAL | LOCATION |
| D | SCALE | LOCATION |

Exception: Magic/substance/fictional themes → WEATHER/CULTURAL + TIME

Print: `Entry Angle: Theme [X] → S1=[TYPE] | S2=[TYPE]`

#### Execution Rules
- Apply to S1 and S2 ONLY. Never in S3-S5.
- First sentence MUST realize assigned angle as visible framing.
- Must reference THEME noun.
- Do not defer angle to second sentence.

#### Execution Guidance by Type

**SCALE** (low natural compliance — requires attention):
Opens with number or dimension as grammatical subject or first modifier.

✅ Compliant:
- "A fifteen-meter granite Buddha rises..."
- "A half-meter strip of steel lies..."
- "Three hundred years of growth have..."
- "The eight-wheeled chassis spans..."

❌ Non-compliant (actually LOCATION or SUBJECT):
- "Lunokhod-2 stands at the edge..." → LOCATION leads
- "The sakura trunk fills..." → SUBJECT leads

**Portrait/human-subject exception:** For portrait or human-subject themes, framing-boundary descriptors satisfy SCALE when they visibly establish size/framing in the first sentence:
- ✅ "A tight shoulder-up crop frames..."
- ✅ "A close square portrait fills..."
- ✅ "Full-body framing captures..."

If theme lacks obvious dimensional hook → prefer LOCATION or TIME for S1 instead.

**LOCATION** (high natural compliance):
Opens with place preposition. No additional guidance needed.
- "Inside a modern apartment..."
- "At the crater's edge..."
- "Within the greenhouse..."

**TIME** (medium compliance):
Opens with temporal marker.
- "By the third week..."
- "At 3:47 AM..."
- "After forty years of exposure..."

**WEATHER** (medium compliance):
Opens with weather or atmospheric state.
- "Through morning fog..."
- "Under freezing rain..."
- "In the humidity of..."

**CULTURAL** (medium compliance):
Opens with cultural element or artifact.
- "Shimenawa rope wraps..."
- "Ottoman tilework frames..."
- "Soviet-era instruments display..."

**MATERIAL** (medium compliance):
Opens with material or substance as subject.
- "Oxidized copper covers..."
- "Wet concrete holds..."
- "Cracked lacquer reveals..."

**PERSPECTIVE** (medium compliance):
Opens with viewpoint or vantage indicator.
- "From the fourteenth floor..."
- "Through a gap in the shutters..."
- "Reflected in the puddle..."

**ACTIVITY** (medium compliance):
Opens with frozen peak action or arrested result.
- "Mid-pour, the molten glass freezes..."
- "A half-folded map rests..."
- "Sawdust still hangs at cutting height..."

#### Verification
Silent check after writing S1 and S2: Does first sentence realize assigned angle?
If NO → rewrite before output.
If S3-S5 contains Entry Angle language → remove it.
```

**Update cross-references:**

In A.2.1, change:
> "S1–S2 first sentence must present core subject as dominant anchor while realizing Entry Angle as visible framing. Do not defer Entry Angle."

To:
> "S1–S2 first sentence must present core subject as dominant anchor. → see ENTRY ANGLE SYSTEM for first-sentence requirements."

In Phase 4.2, change:
> "Verify rotation, uniqueness, Entry Angle S1–2"

To:
> "Verify rotation, uniqueness. Entry Angle → see ENTRY ANGLE SYSTEM: Verification"

In HARD CHECKS #10, change:
> "Entry Angle Execution (visible S1/S2 first sentence)"

To:
> "Entry Angle Execution → see ENTRY ANGLE SYSTEM: Verification"

In Phase 5 Writing Process #1, change:
> "Entry Angle prep (first sentence MUST realize)"

To:
> "Entry Angle prep → see ENTRY ANGLE SYSTEM"

---

## STEP 4: ADD OUTPUT MODE PRECEDENCE

**Location:** Insert in OUTPUT PROTOCOL section, after "Aspect Ratio Selection" paragraph, before CONCISE_MODE variants.

**Action:** Add new subsection.

**Insert this content:**

```markdown
### OUTPUT MODE PRECEDENCE

When multiple output modes are active, resolve conflicts using this priority order:

1. **Platform-mandatory output** (e.g., Midjourney verification lines) — CANNOT be suppressed by any mode
2. **ROUTING CORRECTION** — prints regardless of CONCISE_MODE setting
3. **TRACE check blocks** — print after slot text unless platform rules specify fixed format
4. **CONCISE_MODE** — controls planning-layer verbosity only, does not suppress platform-mandatory or TRACE output
5. **Module formatting** — changes prompt content requirements, not validation-print requirements

**Conflict resolution rule:** Platform-mandatory → TRACE → CONCISE_MODE → Module → Default

**Explicit interactions:**
| CONCISE_MODE | TRACE | Output |
|--------------|-------|--------|
| omitted | false | Decision Block + prompts |
| omitted | true | Decision Block + CHECK blocks + prompts |
| true | false | Routing Summary + prompts only |
| true | true | Routing Summary + CHECK blocks + prompts |
| false | false | Full Diagnostic + Decision Block + prompts |
| false | true | Full Diagnostic + Decision Block + CHECK blocks + prompts |

### ROUTING CONFLICT RESOLUTION

If during prompt writing a routing decision proves incorrect:
1. STOP current slot immediately — do not complete with wrong routing
2. Print: `[ROUTING CORRECTION: [field] [X]→[Y] — [reason]]`
3. Restart affected slot with corrected value
4. If earlier completed slots affected → flag for user review after series

ROUTING CORRECTION prints regardless of CONCISE_MODE setting.
```

---

## STEP 5: REORDER HARD CHECKS

**Location:** HARD CHECKS section

**Action:** Restructure priority levels to place module checks before platform suffix.

**Replace current HARD CHECKS content with:**

```markdown
## HARD CHECKS (MANDATORY — RUN PER SLOT)

For detailed check procedures → see SLOT VALIDATION STACK.

### PRIORITY 0
0. Decision Block present (if CONCISE_MODE ≠ true)

### PRIORITY 1-A: Content
1. BAN REGISTRY: ZERO TOLERANCE scan
2. Final Sentence Content — visible physical detail only, no COM market terms
3. Rendering Tail Scan → see BAN REGISTRY: BANNED FINAL PATTERNS
4. BAN REGISTRY: ABSTRACT NOUNS scan
5. BAN REGISTRY: TIER 1 ADJECTIVES scan
6. Length Check — sentence count proxy; Midjourney limits override

### PRIORITY 1-B: Modules (if active)
7. Module A minimums: format + 2 text zones + copy line
8. Module B minimums: form + closure + label
9. Module D arc integrity: lifecycle stage matches slot position

### PRIORITY 1-C: Platform
10. Platform Suffix Check (Midjourney: verify 5/5 parameters)
10a. Rendering Phrase Check (non-photo only): ≥3/5 slots contain rendering vocabulary, placed in 2nd/3rd-to-last sentence
11. Setting Fidelity: enforce GEO/ERA/MUST_INCLUDE/MUST_AVOID/VISUAL_VOCABULARY

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

---

## STEP 6: RENAME TEXT → TEXTURAL

**Location:** A.4 Creative Lenses table

**Action:** Find and replace lens name.

**Change in table:**

FROM:
```
| TEXT | Macro | Tactile, magnified | ≤10cm field. Shallow DOF. |
```

TO:
```
| TEXTURAL | Macro | Tactile, magnified | ≤10cm field. Shallow DOF. |
```

**Verify:** Search entire document for "TEXT" as lens reference. The only occurrence should be in A.4 table. Other "text" references (Module A text zones, copy text, etc.) are unrelated.

---

## STEP 7: FIX S5 TRACE VERIFICATION LOGIC

**Location:** Phase 4.2, S5 TRACE VERIFICATION

**Action:** Rewrite with unified logic direction.

**Change:**

FROM:
```
**S5 TRACE VERIFICATION:** 1. Carrying Image visible? → REWRITE. 2. Shows absent elements? → REWRITE. 3. Theme identifiable from evidence alone? → NO → REWRITE. Silent.
```

TO:
```
**S5 TRACE VERIFICATION (silent):**
REWRITE if ANY condition is true:
□ Carrying image is visible in scene
□ Prompt states what is absent (violates Narrated Absence Ban)
□ Theme NOT identifiable from physical evidence within 30 seconds

All conditions use same logic: true → rewrite.
```

---

## STEP 8: ADD SESSION_HISTORY AND RUNTIME NOTE

**Location:** INPUTS section, after TRACE parameter

**Action:** Add new optional input field and modify stateful rules.

**Insert after TRACE:**

```markdown
- SESSION_HISTORY: [optional — enables cross-session tracking]
  Format: `{ S1_ANCHORS: "[lens,lens,lens,lens]", SEED2_CATEGORIES: "[cat,cat,cat,cat]" }`
  Example: `{ S1_ANCHORS: "PHOTO,PHOTO,CINE,PHOTO", SEED2_CATEGORIES: "DOMESTIC,TRANSIT,DOMESTIC,WORKSHOP" }`
  
  If omitted → stateful rules (ANTI-ANCHOR, SEED 2 CATEGORY TRACKING, VEHICLE-WITNESS CEILING) apply within current output set only (5 slots = 1 unit, no cross-run memory).
  If provided → cross-session enforcement active using provided history.
```

**Add runtime note in Phase 4.1 after SEED 2 CATEGORY TRACKING:**

```markdown
**Cross-session tracking note:** SEED 2 DIVERSITY, VEHICLE-WITNESS CEILING, SEED 2 CATEGORY TRACKING, and ANTI-ANCHOR rules require memory of previous runs. If SESSION_HISTORY is not provided, these rules apply only within the current 5-slot output. Do not print historical compliance claims without SESSION_HISTORY data. If printing ceiling checks, note: `[SESSION_HISTORY not provided — within-set only]`
```

**Modify ANTI-ANCHOR print statement in A.3:**

FROM:
```
Print: `Anti-Anchor: [X]/4 PHOTO S1 in last 4 → S1=[lens] [OK/FORCED]`
```

TO:
```
Print: `Anti-Anchor: [X]/4 PHOTO S1 in last 4 → S1=[lens] [OK/FORCED]` (requires SESSION_HISTORY; if not provided, print: `[within-set only]`)
```

---

## STEP 9: ADD FINAL-SENTENCE VARIATION RULE

**Location:** A.2.9, after "Final Clause/Sentence Test"

**Action:** Add variation requirement.

**Insert after the existing final sentence rule:**

```markdown
**Final Sentence Variation:** The physical-detail requirement must be met, but vary closing syntax across the 5-slot set. Do not use the construction "ending on [element]" more than twice per set.

Allowed final sentence patterns:
- Direct physical statement: "Copper strands catch the rim light at the temple."
- List with state verb: "Grit, glass, and paper share the shallow focal plane."
- Spatial-material clause: "A single hair crosses the weave near the blanket fold."
- Focal residue: "The sharpest detail remains the dust on the soil edge."

Banned overuse: "...ending on [X]" appears in >2 slots → rewrite alternates.
```

---

## STEP 10: CLARIFY ADJECTIVE EXCEPTION

**Location:** Already addressed in STEP 1 (BAN REGISTRY: TIER 1 ADJECTIVES exception rule)

**Verification:** Ensure the exception rule in BAN REGISTRY reads:

```markdown
**Exception rule:** A banned adjective may remain ONLY when paired with a measurable or technically specific material qualifier. Examples:
- ✅ KEEP: "soft clay Shore A 20" / "soft wool 120gsm" / "fine mesh 400-count"
- ❌ REPLACE: "soft knit" / "soft fabric" / "fine detail" / "gentle curve"
```

If this was included in Step 1, no additional action needed. If not, add it now.

---

## STEP 11: ADD MODULE A+D CONFLICT RESOLUTION

**Location:** ZONE C — MODULES, after Module D description

**Action:** Add new MODULE COMBINATIONS subsection.

**Insert this content:**

```markdown
### MODULE COMBINATIONS

**A+B (Packaging with graphics):**
B provides form and closure; A provides surface graphics and text zones.
Both checklists apply. B physical constraints take precedence over A layout preferences.

**A+D (Poster/artwork lifecycle):**
S1-S4: A format (flat front-facing artwork) with D condition progression:
- S1: Pristine poster/artwork
- S2: Displayed/mounted/in use
- S3: Wear begins (faded, corner torn, sticker added, dust)
- S4: Heavy wear (water damage, graffiti, partial covering, peeling)

S5 Resolution — two options:
- **CONCEPTUAL TRACE (default):** Space where artwork WAS — wall with adhesive residue, unfaded rectangle, mounting holes, removed frame marks. Artwork NOT visible.
- **PHYSICAL RUPTURE:** Destroyed artwork as artifact — burned edges, torn pieces, crumpled, scraped remnants. Artwork visible but destroyed.

Default: CONCEPTUAL TRACE (aligns with standard S5 ABSENCE logic).
To use PHYSICAL RUPTURE: user must specify "A+D physical" in CONSTRAINTS.

**B+D (Packaging lifecycle):**
B form persists S1-S4; D affects condition and contents.
S5: Empty/discarded packaging with use evidence.

**A+B+D (Full packaging narrative with graphics):**
Not recommended — high complexity. If required:
1. Consult user for priority order before generation
2. Default precedence: B form constraints → A graphics/text → D wear state
3. S5: Follow B+D logic (empty packaging), A elements show wear per D state
```

---

## STEP 12: CONVERT FEEDBACK PROTOCOL TO TABLE

**Location:** FEEDBACK ADJUSTMENT PROTOCOL section

**Action:** Replace prose format with table.

**Replace current content with:**

```markdown
## FEEDBACK ADJUSTMENT PROTOCOL

Revise ONLY affected slots. Preserve Decision Block unless planning fields change. If feedback conflicts with core rules → prioritize carrying image fidelity.

| Signal | Action | Scope |
|--------|--------|-------|
| Too dark | Increase key light intensity, add fill source | Affected slot |
| Too light/bright | Reduce exposure language, deepen shadow description | Affected slot |
| Unreadable text (Module A) | Increase text size, add contrast backing, simplify hierarchy | Module A slots |
| Too abstract | Add physical anchor object, increase material specificity | Affected slot |
| Boring / lacks interest | Add surprise element, shift lens type, increase contrast | Affected slot |
| Wrong mood | Adjust palette temperature + light quality | Series-wide review |
| Style mismatch | Check reference, adjust rendering vocabulary | Affected slot |
| Too cluttered | Remove background elements, increase negative space | Affected slot |
| Composition off | Change camera angle, focal length, or subject placement | Affected slot |
| Theme drift | Re-anchor to carrying image, verify seed binding | Typically S3-S5 |
| Product not visible (COM) | Increase subject size, improve lighting, reduce background | Affected slot |
| Low contrast / flat | Increase light ratio, add specular highlights or deep shadows | Affected slot |
| Violence / gore visible | Apply aftermath rule, remove bodies, show environmental damage only | Affected slot |
| Real person resemblance | Shift to archetype features, change distinguishing characteristics | Affected slot |
| Entry Angle in S3-S5 | Verify S1-S2 first sentences, remove angle language from S3-S5 | S3-S5 |
| "Ending on" overused | Apply final sentence variation rule, use alternate constructions | Slots with repetition |
| Generic adjective escaped | Apply BAN REGISTRY: TIER 1, qualify or replace | Affected slot |
```

---

## STEP 13: ADD ARCHITECTURE SECTION

**Location:** Insert immediately after SYSTEM ROLE, before INPUTS

**Action:** Add new section explaining structural organization.

**Insert this content:**

```markdown
## ARCHITECTURE

### Zones (functional domains)
| Zone | Purpose | When active |
|------|---------|-------------|
| Zone A | Writing Standards — rules for prompt composition | During prompt writing (Phase 5) |
| Zone B | Preprocessing — decisions, enrichment, planning | Before writing (Phases 1-4) |
| Zone C | Modules — conditional extensions A/B/C/D | When triggered by input |

### Phases (pipeline stages)
| Phase | Name | Primary Zone |
|-------|------|--------------|
| 1 | Safety Scan | B.0 |
| 2 | Decisions | B.1 |
| 3 | Enrichment & Entry Angle | B.2 |
| 4 | Seeds & Slot Mapping | Phase 4 |
| 5 | Prompt Writing | Zone A |
| 6 | Validation | SLOT VALIDATION STACK / HARD CHECKS |

### Execution model
Phases execute sequentially (1→6). Zones provide rules that activate as needed within phases. A rule from Zone A may be referenced during Phase 4 planning but is primarily enforced during Phase 5 writing and Phase 6 validation.

### Key reference points
- **BAN REGISTRY:** Canonical source for all prohibited terms/patterns
- **ENTRY ANGLE SYSTEM:** Consolidated rules for S1/S2 first-sentence framing
- **SLOT VALIDATION STACK:** Ordered per-slot check procedure
- **OUTPUT MODE PRECEDENCE:** Resolves conflicts between TRACE/CONCISE_MODE/Platform
```

---

## STEP 14: CLARIFY RERUN TRIGGER

**Location:** RERUN HANDLING section

**Action:** Replace vague detection with explicit criteria.

**Change first paragraph:**

FROM:
```
Detection: Same subject/situation → RERUN.
```

TO:
```
**RERUN Detection:**
- Explicit: User states "ещё раз" / "another set" / "RERUN" / "again"
- Implicit: THEME string identical to previous theme in conversation
- Implicit: Core noun + Medium + Context ALL match previous run in conversation

If detection uncertain → assume RERUN, apply diversity checks. User corrects if false positive.
Do not ask user for clarification — maintain silent processing.
```

---

## STEP 15: ADD STRUCTURED THEME INPUT DOCUMENTATION

**Location:** INPUTS section, after SESSION_HISTORY

**Action:** Add documentation for Checklist integration.

**Insert this content:**

```markdown
- STRUCTURED THEME INPUT: If user provides theme as a code block matching Checklist v1.4 THEME TEMPLATE format (contains SETTING, SEEDS, VISUAL_VOCABULARY, ARC_PLANNING, TECHNICAL fields):
  → Parse all fields directly as authoritative input
  → Skip enrichment phase (B.2 STEP 2) — already done
  → Skip seed generation (Phase 4.1) — seeds provided
  → Proceed to seed verification → slot mapping → prompt writing
  
  UPG does not contain interview mode. For guided theme development, use Checklist v1.4 in a separate session, then paste the resulting THEME TEMPLATE as structured input to UPG.
  
  **Workflow options:**
  - Two-session: Session 1 (Checklist) produces THEME TEMPLATE → Session 2 (UPG) consumes it
  - Single-session manual: User fills THEME TEMPLATE fields manually → pastes to UPG
  - Direct: User provides simple THEME string → UPG runs full pipeline including enrichment
```

---

## STEP 16: SIMPLIFY DECISION BLOCK FORMAT

**Location:** OUTPUT PROTOCOL, CONCISE_MODE omitted section

**Action:** Remove numeric line limits, add format guidance.

**Change:**

FROM:
```
Output a Decision Block (≤35 lines for FULL ARC, or ≤40 lines if RERUN block present; ≤20 for SHALLOW ARC; group single-value fields onto shared lines separated by pipes)
```

TO:
```
Output a Decision Block in compact format. Group single-value fields onto shared lines separated by pipes. Multi-sentence fields (Enriched theme, Seeds) occupy own lines. No essays — planning serves prompts, not vice versa.

Required fields: Scope | Context | Medium | Arc | Creative latitude | Safety note | Carrying image | Enriched theme (2-4 sentences) | Cliché blacklist (3 items) | Palette summary | Aspect ratio | Entry Angle (Slots 1-2) | Modules | Slot plan (S1-S5)

For FULL ARC, also include: Seeds 1-3 (one sentence each) | Seed-to-Slot mapping | S1/Seed1 separation check
```

---

## STEP 17: UPDATE A.2.9 REFERENCES

**Location:** A.2.9 Camera-Visible Prose section

**Action:** Replace inline ban lists with BAN REGISTRY references. Retain S5-specific rules.

**Change the section to:**

```markdown
9. **Camera-Visible Prose:** Every sentence describes something a camera sees in one frame. Meta-language (intent, emotion, causality, instruction) → delete/replace with visual detail. Test: Can this be storyboarded?

   **Ban enforcement:** → Apply BAN REGISTRY: ZERO TOLERANCE, TIER 1 ADJECTIVES, ABSTRACT NOUNS, BANNED FINAL PATTERNS. Run scans simultaneously. Fix silently. Print only if Zero Tolerance caught: `[ZERO TOLERANCE FIXED: "[orig]" → "[new]" in S[n]]`
   
   **FIRST-LINE SCAN:** Check first sentence for "as if" / "as though" → rewrite to visible evidence.
   
   **TIER 1 MICRO-SCAN:** → see BAN REGISTRY: TIER 1 ADJECTIVES. Qualify or replace.
   
   **Priority scan for "fine":** This adjective has the highest escape rate. Common violations:
   - "fine dust" → "ite powder" or "particulate dust"
   - "fine lines" → "hairline" or "narrow"
   - "fine detail" → "granular detail" or [specific description]
   If "fine" appears without physical qualifier → REWRITE before output.

   **Narrated Absence Ban (S5):** Do not state element is absent/invisible. Describe visible residue, damage, altered light, contamination, physical emptiness. Module A: do not state text absent — describe what IS on surface. Technique: 1. Name evidence 2. Describe properties 3. Anchor spatially. No cause explanation.

   **SENSORY Exception:** Synaesthetic qualities implied via visible markers (frost, condensation, vibration marks, heat haze). Never name the sensation directly. Negated sensations ("no sound," "without warmth") violate camera-visible rule.

   **Final Sentence Variation:** → see addition in Step 9. Physical detail required, but vary syntax. "Ending on" ≤2× per set.
```

---

## STEP 18: UPDATE VISUAL_VOCABULARY PRE-SCAN

**Location:** INPUTS section, VISUAL_VOCABULARY Pre-Scan

**Action:** Replace inline ban list with BAN REGISTRY reference.

**Change:**

FROM:
```
**VISUAL_VOCABULARY Pre-Scan:** Before processing, scan all VISUAL_VOCABULARY entries for metaphorical language that will trigger Zero Tolerance bans when transferred to prompts:

BANNED in VV source text:
- "as if" / "as though" / "like [verb-ing]" / "seems to"
- "будто" / "словно" / "как будто" / "как если бы"
- Any simile describing process or perception
[examples follow]
```

TO:
```
**VISUAL_VOCABULARY Pre-Scan:** Before processing, scan all VISUAL_VOCABULARY entries against BAN REGISTRY: ZERO TOLERANCE and LOCALIZED BANS. If metaphorical language found → rewrite as physical property BEFORE generation.

Examples of required rewrites:
- ❌ "as if dipped in rusty water" → ✅ "with oxide-brown edges and iron-dark veins"
- ❌ "like living tissue" → ✅ "with blurred boundary and fibrous texture"
- ❌ "resembles breathing" → ✅ "with expansion marks and pressure ridges"

This scan prevents VV content from multiplying Zero Tolerance violations across all slots.
```

---

## VERIFICATION CHECKLIST

After completing all steps, verify:

### Structure
- [ ] BAN REGISTRY exists after INPUTS, before MIDJOURNEY MODE
- [ ] ARCHITECTURE exists after SYSTEM ROLE, before INPUTS
- [ ] SLOT VALIDATION STACK exists after PHASE 5, before ZONE C
- [ ] ENTRY ANGLE SYSTEM exists in B.2 (replacing old Step 6)
- [ ] OUTPUT MODE PRECEDENCE exists in OUTPUT PROTOCOL
- [ ] MODULE COMBINATIONS exists in ZONE C

### References
- [ ] A.2.9 references BAN REGISTRY (not inline lists)
- [ ] VV Pre-Scan references BAN REGISTRY
- [ ] HARD CHECKS reference SLOT VALIDATION STACK where appropriate
- [ ] Entry Angle cross-references in A.2.1, Phase 4.2, HARD CHECKS, Phase 5 all point to ENTRY ANGLE SYSTEM

### Renames
- [ ] TEXT lens renamed to TEXTURAL in A.4 table
- [ ] No remaining references to TEXT as lens name

### New content
- [ ] SESSION_HISTORY in INPUTS
- [ ] STRUCTURED THEME INPUT in INPUTS
- [ ] Final-sentence variation rule in A.2.9
- [ ] RERUN trigger clarification
- [ ] Feedback Protocol is table format

### Removals
- [ ] Old Step 6 Entry Angle content removed (replaced by ENTRY ANGLE SYSTEM)
- [ ] Inline ban lists in A.2.9 removed (replaced by BAN REGISTRY references)
- [ ] Numeric line limits removed from Decision Block description
- [ ] Old 7a position cleared (moved to 10a)

### Logic fixes
- [ ] S5 TRACE VERIFICATION uses unified "rewrite if ANY true" format
- [ ] Adjective exception includes measurable/technical qualifier requirement
- [ ] Portrait SCALE guidance included in ENTRY ANGLE SYSTEM

---

## CHANGELOG FOR v9.13

Include this changelog at the top of the refactored document or in a separate version note:

```markdown
## v9.13 CHANGELOG

### ADDITIONS
- BAN REGISTRY: Consolidated canonical source for all prohibited terms/patterns
- ARCHITECTURE: Section explaining Zone/Phase relationship
- SLOT VALIDATION STACK: Unified per-slot validation procedure
- ENTRY ANGLE SYSTEM: Consolidated from 4 locations with full type guidance
- OUTPUT MODE PRECEDENCE: Explicit conflict resolution for TRACE/CONCISE_MODE/Platform
- SESSION_HISTORY: Optional input for cross-session stateful rule enforcement
- STRUCTURED THEME INPUT: Documentation for Checklist v1.4 integration
- ROUTING CONFLICT RESOLUTION: Stop-correct-restart protocol
- MODULE COMBINATIONS: Explicit A+D S5 resolution, A+B+D guidance
- Final-sentence variation rule: "ending on" limited to ≤2× per set
- Portrait SCALE guidance: Framing descriptors valid for human subjects
- Entry Angle types: Added MATERIAL, PERSPECTIVE, ACTIVITY with examples

### CONSOLIDATIONS
- Entry Angle logic moved from A.2.1, Phase 4.2, HARD CHECKS #10, Phase 5 #1 → ENTRY ANGLE SYSTEM
- Ban lists moved from A.2.9, VV Pre-Scan → BAN REGISTRY
- Per-slot checks documented in SLOT VALIDATION STACK

### REORDERS
- HARD CHECKS Priority 1 split: 1-A (content) → 1-B (modules) → 1-C (platform)
- Former 7a (Rendering Phrase Check) moved to 10a

### RENAMES
- TEXT lens → TEXTURAL (A.4 table)

### FIXES
- S5 TRACE VERIFICATION: Unified "rewrite if ANY true" logic
- RERUN detection: "if uncertain → assume RERUN" (no user query)
- Adjective exception: Now requires measurable/technical qualifier

### FORMATS
- Feedback Adjustment Protocol converted to table
- Decision Block: Numeric line limits replaced with "compact format" guidance

### CLARIFICATIONS
- Cross-session tracking requires SESSION_HISTORY; otherwise within-set only
- ROUTING CORRECTION exempt from CONCISE_MODE suppression
- Module A+D default S5 = CONCEPTUAL TRACE; PHYSICAL RUPTURE requires explicit request
```

---

## POST-IMPLEMENTATION TESTING

After refactoring, test with these scenarios:

### Test 1: Basic FULL ARC
```
THEME: abandoned lighthouse
GOAL: artistic
```
Verify: Entry Angles applied, lens diversity, S5 trace logic, no "ending on" >2×

### Test 2: Stateful rules without SESSION_HISTORY
```
THEME: vintage compass
GOAL: artistic
```
Verify: Prints `[within-set only]` for stateful checks, no false historical claims

### Test 3: Mode interaction
```
THEME: ceramic teacup
GOAL: artistic
PLATFORM: Midjourney
CONCISE_MODE: true
TRACE: true
```
Verify: Routing Summary + CHECK blocks + MJ verification lines all present

### Test 4: Module A+D
```
THEME: concert poster
GOAL: artistic
MODE: 2
```
Verify: S5 defaults to CONCEPTUAL TRACE (wall where poster was), not destroyed poster

### Test 5: Portrait SCALE
```
THEME: tired barista, early morning
GOAL: artistic
```
Verify: S1 with SCALE uses framing descriptor ("shoulder-up crop"), not forced measurement

---

**END OF REFACTORING INSTRUCTION**