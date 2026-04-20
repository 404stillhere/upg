Below is a strict **Visual Correspondence Protocol v1.0** audit of your S4 image.

---

# STAGE 0: PROMPT DECOMPOSITION

### 0.1 Element Inventory

| #  | Element                         | Category | Specificity | Priority   |
| -- | ------------------------------- | -------- | ----------- | ---------- |
| 1  | magnified oblique view          | COMP     | EXACT       | ANCHOR     |
| 2  | one edge of processor microchip | SUBJ     | EXACT       | ANCHOR     |
| 3  | layered substrate visible       | MAT      | EXACT       | ANCHOR     |
| 4  | micro-scratches on metal cap    | TEX      | EXACT       | ANCHOR     |
| 5  | contact wear at pad border      | COND     | EXACT       | ANCHOR     |
| 6  | adhesive seam tolerance visible | MAT      | EXACT       | ANCHOR     |
| 7  | raking light                    | LIGHT    | DIRECTIONAL | ANCHOR     |
| 8  | narrow bright specular bands    | LIGHT    | EXACT       | SUPPORTING |
| 9  | deep shadow between layers      | LIGHT    | EXACT       | SUPPORTING |
| 10 | 100mm macro                     | TECH     | EXACT       | SUPPORTING |
| 11 | f10                             | TECH     | EXACT       | SUPPORTING |
| 12 | inspection-oriented framing     | COMP     | DIRECTIONAL | ANCHOR     |
| 13 | layered laminate                | MAT      | EXACT       | SUPPORTING |
| 14 | worn gold pad edges             | COND     | EXACT       | ANCHOR     |
| 15 | hairline scratches              | TEX      | EXACT       | SUPPORTING |
| 16 | adhesive residue at cap seam    | COND     | EXACT       | ANCHOR     |

**Total elements extracted: 16**

---

### 0.2 Structural Expectations

| Parameter               | Value                        |
| ----------------------- | ---------------------------- |
| Medium/style            | macro technical photography  |
| Camera/lens             | 100mm macro                  |
| Dominant subject        | microchip edge               |
| Setting                 | neutral/isolated inspection  |
| Light direction         | raking / grazing             |
| Palette                 | metallic gray, gold, green   |
| Entry angle realization | S4 (oblique, detail-focused) |

---

# STAGE 1: IMAGE SCAN

### 1.1 Objective Description

A close macro image shows the corner edge of a microchip with stacked layers. The top metal cap has visible scratches, and beneath it are multiple layered materials including a green substrate and gold-toned edges. There are visible adhesive-like residues near the seam between layers. Lighting is directional and grazing, creating strong highlights on edges and shadows between stacked layers.

---

### 1.2 Image Element Inventory

| #  | Visible element                  | Category | Confidence |
| -- | -------------------------------- | -------- | ---------- |
| 1  | microchip corner edge            | SUBJ     | CLEAR      |
| 2  | layered stack (substrate layers) | MAT      | CLEAR      |
| 3  | scratched metal cap surface      | TEX      | CLEAR      |
| 4  | gold contact/pad edges           | MAT      | CLEAR      |
| 5  | worn edges on gold pads          | COND     | PROBABLE   |
| 6  | adhesive residue blobs           | COND     | CLEAR      |
| 7  | seam between cap and substrate   | MAT      | CLEAR      |
| 8  | raking directional light         | LIGHT    | CLEAR      |
| 9  | specular highlights along edges  | LIGHT    | CLEAR      |
| 10 | deep shadow between layers       | LIGHT    | CLEAR      |
| 11 | macro shallow framing            | COMP     | CLEAR      |
| 12 | inspection-like composition      | COMP     | CLEAR      |

---

# STAGE 2: CORRESPONDENCE MAP

### 2.1 Element-by-Element Comparison

| #  | Prompt element               | Priority | Image match                                   | Status | Delta                                |
| -- | ---------------------------- | -------- | --------------------------------------------- | ------ | ------------------------------------ |
| 1  | magnified oblique view       | A        | macro angled view                             | ✅      | —                                    |
| 2  | processor microchip edge     | A        | chip corner visible                           | ✅      | —                                    |
| 3  | layered substrate            | A        | stacked layers visible                        | ✅      | —                                    |
| 4  | micro-scratches on metal cap | A        | scratches clearly visible                     | ✅      | —                                    |
| 5  | contact wear at pad border   | A        | slight edge wear visible                      | 🔶     | not strongly emphasized              |
| 6  | adhesive seam tolerance      | A        | adhesive present but not “tolerance-specific” | 🔶     | more residue than tolerance detail   |
| 7  | raking light                 | A        | grazing light confirmed                       | ✅      | —                                    |
| 8  | narrow specular bands        | S        | highlights present                            | ✅      | —                                    |
| 9  | deep shadow between layers   | S        | strong separation shadows                     | ✅      | —                                    |
| 10 | 100mm macro                  | S        | macro look achieved                           | 🔶     | focal length not verifiable          |
| 11 | f10                          | S        | moderate depth                                | 🔶     | DOF slightly shallower than expected |
| 12 | inspection-oriented framing  | A        | technical framing                             | ✅      | —                                    |
| 13 | layered laminate             | S        | visible composite layers                      | ✅      | —                                    |
| 14 | worn gold pad edges          | A        | gold edges visible, mild wear                 | 🔶     | wear subtle                          |
| 15 | hairline scratches           | S        | scratches visible                             | ✅      | —                                    |
| 16 | adhesive residue at seam     | A        | visible adhesive blobs                        | ✅      | —                                    |

---

### 2.2 Uninstructed Elements

| # | Element                               | Category | Impact  | Source        |
| - | ------------------------------------- | -------- | ------- | ------------- |
| 1 | liquid-like adhesive pooling          | COND     | HELPFUL | interpolation |
| 2 | slightly glossy moisture-like texture | TEX      | NEUTRAL | model default |

---

# STAGE 3: DIAGNOSIS

### 3.1 Score Card

| Metric                | Value    |
| --------------------- | -------- |
| Total elements        | 16       |
| ✅ MATCH               | 10 (62%) |
| 🔶 PARTIAL            | 6 (38%)  |
| ❌ LOST                | 0        |
| 🔀 MUTATED            | 0        |
| 👻 GHOST              | 0        |
| Uninstructed elements | 2        |
| — HARMFUL             | 0        |

---

### 3.2 Anchor Integrity

| Anchor element     | Status |
| ------------------ | ------ |
| oblique macro view | ✅      |
| microchip edge     | ✅      |
| layered substrate  | ✅      |
| scratches          | ✅      |
| pad wear           | 🔶     |
| adhesive seam      | 🔶     |
| raking light       | ✅      |
| inspection framing | ✅      |
| gold pad edges     | 🔶     |
| adhesive residue   | ✅      |

**Anchor Integrity Score: 7 / 10 fully matched**

**Verdict:**
Image is clearly correct but lacks precision in **wear/tolerance specificity**

---

### 3.3 Loss Pattern Analysis

| Loss                        | Cause                | Evidence                        |
| --------------------------- | -------------------- | ------------------------------- |
| pad border wear subtle      | UNDERSPECIFICATION   | wear not emphasized visually    |
| seam tolerance not explicit | GENERATOR LIMITATION | tolerance vs residue indistinct |
| f10 depth not exact         | GENERATOR LIMITATION | DOF stylistic variation         |
| gold edge wear mild         | GENERATOR BIAS       | prefers clean metallic edges    |

---

### 3.4 Gain Pattern Analysis

No harmful additions.

---

# STAGE 5: ACTIONABLE FINDINGS

### 5.1 Prompt-Side Fixes

| Problem                | Fix     | Suggestion                                                     |
| ---------------------- | ------- | -------------------------------------------------------------- |
| Wear too subtle        | SPECIFY | “clearly abraded, visibly eroded gold pad edges”               |
| Seam tolerance unclear | REWORD  | “visible uneven adhesive gap and measurable seam misalignment” |
| Adhesive ambiguity     | SPECIFY | “thin adhesive line, not pooled or liquid-like”                |
| DOF mismatch           | SPECIFY | “deep focus across all layers, minimal falloff”                |

---

### 5.2 Generator-Side Notes

| Limitation                              | Workaround                                              |
| --------------------------------------- | ------------------------------------------------------- |
| Cannot express “tolerance” concept well | translate to visible misalignment or uneven gap         |
| Wear tends to be understated            | exaggerate physically (“chipped,” “frayed,” “oxidized”) |

---

### 5.3 UPG Rule Effectiveness

| Rule                 | Visible | Notes                               |
| -------------------- | ------- | ----------------------------------- |
| Material specificity | yes     | metals, laminate accurate           |
| Lighting control     | yes     | strong raking achieved              |
| Realism anchor       | yes     | residue + scratches grounded        |
| Lens instruction     | partial | macro achieved, f-stop less precise |
| Spatial zones        | yes     | clear layering                      |
| Density              | yes     | high detail                         |

**Key insight:**
Material + lighting instructions dominate accuracy; **micro-condition descriptors need exaggeration to survive generation.**

---

# STAGE 6: VERDICT

### 6.1 Scores

| Metric                 | Score                 |
| ---------------------- | --------------------- |
| Anchor Fidelity        | 70%                   |
| Element Coverage       | 100% (incl. partials) |
| Purity                 | 100%                  |
| Overall Correspondence | **8 / 10**            |

---

### 6.3 One-Line Summary

`Microchip inspection macro on Flux: 8/10 — strong structural fidelity, wear and tolerance details under-expressed`

---

If you want, I can tune this into a **perfect 9–10/10 prompt revision** that forces visible tolerance + edge wear (this is a known weak spot in generators).
