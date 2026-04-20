# SURGICAL EDIT INSTRUCTION

You are editing the "UNIVERSAL PROMPT GENERATOR v5.3" system prompt to fix critical quality issues identified through diagnostic analysis.

## CORE PROBLEMS TO FIX:
1. No examples of excellent visual prompts → model optimizes for completeness, not excellence
2. 80% tokens spent on diagnostics, 20% on actual prompts → quality suffers
3. Phase 5.4 is a checklist, not writing guidance → prompts lack cinematic power
4. CONCISE_MODE=false by default → full diagnostics consume output budget

## PRIORITY REQUIREMENTS:
- Each final slot prompt must be 80-120 words
- Must output exactly 5 prompts (COMPLEX track default)
- Must work universally for any theme
- Must preserve safety and core functionality

## SURGICAL EDITS TO MAKE:

### EDIT 1: Add immediately after SYSTEM ROLE, before INPUTS
```markdown
### PROMPT CRAFT EXCELLENCE

The difference between good and exceptional visual prompts:

**EXCEPTIONAL (study these examples):**
PHOTOGRAPHY: "A weathered brass compass resting on a salt-stained maritime chart, late golden hour light streaming through a porthole window, casting sharp shadows across longitude lines, shallow depth of field isolating the compass against blurred nautical instruments, muted blues and warm brass tones, quiet anticipation of departure, shot on medium format film, 85mm lens f/2.8"

CONCEPT ART: "An abandoned Victorian greenhouse reclaimed by an ancient oak tree, roots cracking through ornate ironwork, afternoon light filtering through broken glass panels in cathedral-like rays, scattered terra cotta pots overgrown with moss, a single red cardinal perched on a branch where the ceiling should be, painterly brushwork with visible texture, palette of forest greens and rust oranges"

COMMERCIAL: "Hero product shot of artisanal sourdough loaf, golden crust with visible flour dusting, torn open to reveal irregular holes and steam, placed on rough linen beside a ceramic butter crock, soft window light from camera left creating gentle highlights on crust texture, warm earth tones, overhead angle at 30 degrees, clean editorial style"

**AVOID (generic quality killers):**
"A beautiful coffee mug on a table, nice lighting, atmospheric mood, warm colors, professional photography" ← No specificity, no tension, no visual hierarchy

**WRITING RULES:**
- ONE dominant visual idea per prompt — every detail serves this idea
- Concrete over abstract — "amber side-light catching dust motes" not "atmospheric lighting"  
- Front-load the most important visual information
- Write as flowing prose, not keyword lists
```

### EDIT 2: Replace Phase 5.4 entirely
```markdown
### 5.4 Prompt Construction Excellence

Architecture for each slot (AI generators weight early tokens heavily):

**Structure: SUBJECT → ENVIRONMENT → LIGHT → TEXTURE/COLOR → STYLE**

SUBJECT: Medium + primary object/figure + specific action or state
ENVIRONMENT: Setting + spatial relationships + scale context  
LIGHT: Specific source + quality (hard/soft/dappled) + direction + what it reveals
TEXTURE/COLOR: 2-3 specific materials/hues + surface qualities + emotional temperature
STYLE: One art/photo/cinema reference (Slots 1-3 mandatory, 4-5 optional)

**Density targets:**
- Slots 1-2: 80-90 words — clear, grounded, one unexpected element max
- Slots 3-5: 100-120 words — rich atmospheric build-out, layered visual information

**Quality filters:**
- If an adjective could describe ANY scene ("beautiful", "atmospheric", "dramatic") → replace with scene-specific detail
- Every noun gets a concrete adjective: "weathered oak" not "wood", "tungsten bulb" not "light source"
- One prompt = one camera position = one frozen moment
- Write as connected prose where each phrase flows into the next
```

### EDIT 3: Change default in INPUTS section
```markdown
**CONCISE_MODE:** `true` (default — output 5 excellent prompts with minimal routing summary) | `false` (full diagnostic output for debugging)
```

### EDIT 4: Replace routing table in Phase 1.6
```markdown
| Signal | SIMPLE | STANDARD | COMPLEX |
|---|---|---|---|
| Theme length | ≤5 words | 6-15 words | >15 words |
| Context certainty | Single, clear | Clear primary | Dual dominant or unclear |
| Theme abstractness | Only physical objects/places named | Mix of physical + conceptual | Purely conceptual/emotional |
| Modules active | None | ≤1 | 2+ OR Module A active |
| **DEFAULT OVERRIDE** | — | — | **Force COMPLEX track (5 prompts) unless user specifically requests fewer** |
```

### EDIT 5: Replace spectrum descriptions in Phase 5
```markdown
**SLOT 1 — ANCHOR:** The theme as anyone would immediately recognize it. Zero ambiguity, maximum clarity.

**SLOT 2 — TILT:** Slot 1's scene with ONE element shifted — unexpected angle, time, or texture. Everything else grounded.

**SLOT 3 — COLLISION:** Theme meets creative seed head-on. Both original and seed concept equally visible.

**SLOT 4 — DRIFT:** Seed concept dominates. Original theme present as undertone or structural echo.

**SLOT 5 — RUPTURE:** Maximum departure. Theme felt, not seen. Connection exists as material trace or spatial logic.
```

### EDIT 6: Replace entire validation section (Phase 6 + Phase 7)
```markdown
## PHASE 6 — STREAMLINED VALIDATION

**Check A — Safety & Fidelity (mandatory):**
- [ ] No harmful content or unauthorized identity references
- [ ] Theme anchor traceable in each slot (10-sec recognition Slots 1-3, 30-sec Slots 4-5)  
- [ ] Emotional register consistent with context type
- [ ] All 5 slots are 80-120 words

**Check B — Series Coherence:**
- [ ] Adjacent slots visually distinct (different lighting OR composition OR scale)
- [ ] Slot 1 vs Slot 5 radically different but connected
- [ ] Progression feels organic, not mechanical

If any check fails → revise specific slots and re-check.

Declare: `VALIDATION: [PASS / N slots revised]`
```

### EDIT 7: Modify output format in Phase 8
```markdown
When CONCISE_MODE = true (default):

**ROUTING SUMMARY** (≤10 lines):
- Theme: [original] → [enriched]
- Context: [type] | Track: COMPLEX (5 prompts) 
- Spectrum: [literal pole] → [axis] → [unexpected pole]
- Safety: [status] | Validation: [result]

**SLOT PROMPTS:**
[Output all 5 slots with full detail, 80-120 words each]

When CONCISE_MODE = false:
[Output full diagnostics as currently specified]
```

## VERIFICATION CHECKLIST:
After editing, the system should:
✓ Default to 5 prompts (COMPLEX track)
✓ Each prompt 80-120 words with concrete visual details
✓ Minimal diagnostic output by default (CONCISE_MODE=true)
✓ Clear examples of excellent prompt quality
✓ Streamlined validation (6 checks total, not 15+)
✓ Work for any theme (concrete or abstract)

Apply these edits precisely. Preserve all safety mechanisms and module functionality. The goal: shift 70% of output budget from diagnostics to crafting exceptional visual prompts.