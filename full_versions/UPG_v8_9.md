You are a technical editor for prompt specifications. Task: apply six targeted changes to Universal Prompt Generator v8.9 to create version v9.0.

## CONTEXT

Analysis of @gunebak4n's JSON collection (26 prompts) identified parameters that improve generation quality but are absent or underspecified in UPG v8.9. This patch addresses real gaps without adding bloat.

## CHANGES

---

### CHANGE #1: Expand Light Requirement (add Intensity + Contrast)

**Location:** A.5 Universal Prompt Structure, the "Light (REQUIRED)" bullet point

**Find:**

- **Light (REQUIRED):** Source, direction, quality, color, and what it DOES (casts, catches, rakes, pools, filters). Every slot must name a light source. For flat graphics or product sheets, describe studio lighting or ambient source explicitly.

**Replace with:**

- **Light (REQUIRED):** Source, direction, intensity, contrast, quality, color, and behavior (casts, catches, rakes, pools, filters). Every slot must name a light source. For flat graphics or product sheets, describe studio lighting or ambient source explicitly.

  **Intensity** (energy level):
  - HARSH/INTENSE: strong shadows, high energy, potentially clipped highlights
  - MODERATE: balanced exposure, naturalistic, readable shadows
  - SOFT/DIM: diffused, gentle gradients, low energy, intimate

  **Contrast** (tonal range):
  - HIGH: dramatic separation, deep blacks, bright highlights
  - MEDIUM: balanced, naturalistic tonal range
  - LOW: compressed, atmospheric, hazy

  Integrate into description: "harsh side light creating high contrast against deep shadow" — not just "dramatic lighting."

---

### CHANGE #2: Add Surface Texture

**Location:** A.5 Universal Prompt Structure, after "Palette" bullet point

**Add new bullet:**

- **Surface texture (stylized media):** When Medium is painting, illustration, or vintage photography, specify the visible texture of the medium itself, not subject materials.

  Painting: brushstroke visibility, canvas weave, impasto, palette knife texture
  Illustration: paper tooth, ink bleed, halftone dots, risograph grain, vector-clean
  Vintage photography: film grain (fine/heavy), dust, scratches, light leaks

  State when defining the aesthetic: "heavy impasto with visible palette knife marks" or "fine 35mm film grain with subtle vignette." Default (unstated) = clean contemporary render. Optional for standard digital photography.

---

### CHANGE #3: Expand Style Reference Beyond PAINTERLY

**Location:** A.4 Creative Lenses, after the "Non-Photographic Execution" paragraph

**Add:**

**STYLE REFERENCE (all lenses):**

Naming a specific artist, photographer, or movement anchors aesthetic precisely. Available for any lens, not only PAINTERLY.

Examples by medium:
- Photography: William Eggleston (democratic color), Gregory Crewdson (suburban uncanny), Sebastião Salgado (epic documentary), Düsseldorf School (typological)
- Cinematography: Roger Deakins lighting, Wong Kar-wai palette, Terrence Malick naturalism
- Illustration: Charley Harper (geometric), Ryo Takemasa (minimalist), Mary Blair (stylized color)
- Concept art: Syd Mead (retro-futurism), Simon Stålenhag (Nordic melancholy), Moebius (ligne claire)

Use when specific tradition serves the theme. Prefer movements (New Topographics, Bauhaus, Memphis) over living artists for controversial subjects. Optional — do not force when generic description suffices.

---

### CHANGE #4: Add Aspect Ratio to Decision Block

**Location:** OUTPUT PROTOCOL, "CONCISE_MODE omitted (default)" section

**Find this line in the field list:**

Carrying image | Enriched theme (2–4 sentences) | Cliché blacklist (3 items) | Palette summary |

**Replace with:**

Carrying image | Enriched theme (2–4 sentences) | Cliché blacklist (3 items) | Palette summary | Aspect ratio |

**Then find "Decision Block Completeness Check (silent)" and in the "Always required" list, add:**

Aspect ratio

**After the Completeness Check, add new paragraph:**

**Aspect Ratio Selection:**
Derive from composition:
- Vertical subject (portrait, standing figure, product hero): 4:5 or 3:4
- Horizontal scene (landscape, environmental, tabletop): 3:2 or 16:9
- Square (social media, album, symmetrical): 1:1
- Cinematic (narrative, widescreen): 2.39:1
- Module A: match format spec
- Module B: match container proportions

Format: `Aspect: [ratio]`

---

### CHANGE #5: Add Negative Prompt Generation

**Location:** PHASE 5 — PROMPT WRITING, after section "5.2 Platform Suffixes"

**Add new section:**

### 5.3 Negative Prompt

**For SD / SDXL / Flux:** Generate negative prompt from layers.

**Base (always):**
blurry, deformed, disfigured, bad anatomy, low quality, jpeg artifacts, watermark, signature, cropped, out of frame, duplicate, ugly

**If humans present:**
extra fingers, missing fingers, fused fingers, malformed hands, extra limbs, distorted face, asymmetrical eyes

**Medium mismatch:**
- Photography: cartoon, illustration, painting, anime, 3D render
- Painting/Illustration: photograph, photorealistic, 3D render
- Concept art: photograph, amateur sketch

**Context:**
- COMMERCIAL: amateur, unprofessional, cluttered, messy
- ARTISTIC: generic, stock photo, corporate, bland

**Modules:**
- Module A: illegible text, broken letters, misaligned type
- Module B: warped container, impossible geometry

Print after Decision Block:
`Negative: [assembled from applicable layers]`

**For Midjourney / Aurora:** Negative prompts not supported — omit entirely.

---

### CHANGE #6: Update Version

**Location:** Document title

**Change:**
`# UNIVERSAL PROMPT GENERATOR v8.9`

**To:**
`# UNIVERSAL PROMPT GENERATOR v9.0`

---

## SUMMARY

| # | Change | Location | Words |
|---|--------|----------|-------|
| 1 | Light: +intensity, +contrast | A.5 | ~90 |
| 2 | Surface texture | A.5 | ~80 |
| 3 | Style reference expansion | A.4 | ~110 |
| 4 | Aspect ratio | OUTPUT PROTOCOL | ~80 |
| 5 | Negative prompt | 5.3 new | ~130 |
| 6 | Version update | Title | — |

**Total: ~490 words added**

---

## INSTRUCTIONS

1. Apply all six changes in order
2. Preserve all existing content not explicitly modified
3. Maintain original formatting and structure
4. Output complete UPG v9.0 document with no commentary