# UPG v9.13 PATCH INSTRUCTION

**Document type:** Post-implementation patches
**Target:** UPG v9.13 (current)
**Result:** UPG v9.13.1

---

## PATCH 1: A.2.2 — Shorten inline list, reference BAN REGISTRY

**Priority:** Medium
**Location:** A.2 Mandatory Quality Rules, rule 2

**Rationale:** BAN REGISTRY is now canonical source. A.2.2 should provide inline writing aid but not duplicate the full list. Shortened version keeps immediate context for writers while establishing BAN REGISTRY as authority.

**FIND:**
```
2. **Specificity Test:** If adjective could describe any scene → replace.
   **Banned generic adjectives (replace on sight):**
   soft→diffused/muted/low-contrast | clean→uncluttered/minimal | fresh→recently-cut/undried | **fine→particulate/narrow/hairline (MANDATORY REPLACE — high escape rate)** | smooth→polished/satin | gentle→gradual/low-angle | subtle→understated/hint-of | elegant→proportioned/balanced | delicate→thin-walled/lightweight | simple→single-element/unadorned.
   Tier 2: nice, beautiful, lovely, pure, clear, calm, quiet, refined, pretty, pleasant → replace materially.
   → For exception rule see BAN REGISTRY: TIER 1 ADJECTIVES.
```

**REPLACE WITH:**
```
2. **Specificity Test:** If adjective could describe any scene → replace.
   → Full list and exception rule: BAN REGISTRY: TIER 1 ADJECTIVES.
   Key replacements for quick reference:
   soft→diffused/muted | clean→uncluttered | fresh→recently-cut | **fine→particulate/narrow/hairline (highest escape rate)** | smooth→polished/satin
   Tier 2: nice, beautiful, lovely, pure, clear, calm, quiet, refined, pretty, pleasant → replace materially.
```

**Why this works:**
- Keeps immediate inline utility when writing prompts
- Reduces duplication from 10 items to 5 key items
- Establishes BAN REGISTRY as canonical source
- Retains "fine" priority warning
- Retains Tier 2 list (not in BAN REGISTRY table format)

---

## PATCH 2: A.1 — Fix banned adjectives in examples (OPTIONAL)

**Priority:** Low
**Location:** A.1 Reference Quality Examples, COMMERCIAL example

**Rationale:** "Soft" and "clean" are Tier 1 banned adjectives. While A.0 states examples are not canonical, having banned words in reference examples sends conflicting signal. Patch is optional but improves consistency.

**FIND:**
```
**COMMERCIAL:** Hero sourdough loaf, golden crust with flour, torn open revealing steam/holes, rough linen beside ceramic crock, soft window light, warm earth tones, overhead 30°, clean editorial, shallow DOF f/2.0.
```

**REPLACE WITH:**
```
**COMMERCIAL:** Hero sourdough loaf, golden crust with flour, torn open revealing steam/holes, rough linen beside ceramic crock, diffused window light, warm earth tones, overhead 30°, uncluttered editorial, shallow DOF f/2.0.
```

**Changes:**
- "soft window light" → "diffused window light"
- "clean editorial" → "uncluttered editorial"

---

## PATCH 3: Phase 3 COM BAN — Clarify relationship to BAN REGISTRY

**Priority:** Low
**Location:** PHASE 3 — REGISTER VALIDATION & AUTO-GOAL

**Rationale:** COM BAN contains words that overlap with BAN REGISTRY: ABSTRACT NOUNS (silence, absence, memory) plus context-specific terms (sublime, echo, breath, dissolving, rupture). Adding clarification note explains relationship without removing any words from the list.

**FIND:**
```
**COM BAN:** sublime, echo, memory, silence, absence, breath, dissolving, rupture, void.
```

**REPLACE WITH:**
```
**COM BAN (extends BAN REGISTRY: ABSTRACT NOUNS for commercial context):** sublime, echo, memory, silence, absence, breath, dissolving, rupture, void.
```

**Why this works:**
- Full list preserved (no words removed)
- Relationship to BAN REGISTRY clarified
- Reader understands COM BAN is context-specific extension, not separate system

---

## VERIFICATION AFTER PATCHES

After applying patches, verify:

- [ ] A.2.2 contains shortened list (5 key items, not 10)
- [ ] A.2.2 references BAN REGISTRY as full source
- [ ] A.2.2 retains "fine" priority warning
- [ ] A.2.2 retains Tier 2 list
- [ ] A.1 COMMERCIAL example contains "diffused window light" (if Patch 2 applied)
- [ ] A.1 COMMERCIAL example contains "uncluttered editorial" (if Patch 2 applied)
- [ ] Phase 3 COM BAN has parenthetical clarification
- [ ] Phase 3 COM BAN retains all 9 words in list

---
