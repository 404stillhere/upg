# TASK

You are given the full text of UNIVERSAL PROMPT GENERATOR v7.9.
Perform ONLY the 4 edits described below.
Make NO other changes.
Do not fix grammar, do not rephrase, do not "improve".
If an instruction does not cover a fragment — do not touch it.

---

# EDIT 1: VERSION NUMBER

FIND: v7.9 (in the title)
REPLACE WITH: v8.0

This is the ONLY place where v7.9 appears. Change it once.

---

# EDIT 2: A.5 COMPOSITION INSTRUCTION (section A.5, Universal Prompt Structure)

FIND this exact bullet point:

- **Composition:** Subject placement in frame, visual weight distribution, and
  compositional balance or geometry when relevant to the scene — expressed through
  spatial description, not academic formula

REPLACE WITH:

- **Composition:** Subject placement in frame (positioned left/right/center, upper/lower third, offset against negative space), visual weight distribution (anchored to, balanced against, weighted toward), depth layers (foreground/midground/background relationship), and compositional geometry when relevant. Use spatial prepositions: positioned against, anchored to, offset from, balanced with, receding toward, crowded into, isolated within. Express through spatial description, not academic formula. Each prompt must include at least one explicit placement phrase describing WHERE in the frame the subject sits relative to surrounding space.

Do not modify any text before or after this bullet point.

---

# EDIT 3: A.5 EMOTIONAL QUALITY INSTRUCTION (section A.5, Universal Prompt Structure)

FIND this exact bullet point:

- **Emotional quality:** Expressed through visual detail, not adjectives

REPLACE WITH:

- **Emotional quality:** Expressed through visible physical states, not mood labels. Use: posture tension (hunched, rigid, slack), surface wear (handled, neglected, polished raw), temperature markers (frost, condensation, heat shimmer), spatial indicators (emptiness around, crowding against, isolation between, proximity to), object arrangement (abandoned mid-task, prepared but untouched, mid-use, stacked for storage). The emotion should be inferrable from physical evidence, never stated directly.

Do not modify any text before or after this bullet point.

---

# EDIT 4: FULL ARC TABLE — ADD S1-S2 DIFFERENTIATION RULE (section A.3)

FIND the FULL ARC table. It currently reads:

| Slot | Role | Interpretation | Anchor | Legibility |
|------|------|----------------|--------|------------|
| S1 ANCHOR | Pure literal + Entry Angle | LITERAL | Enriched Theme | Instant |
| S2 TILT | Shift in scale or context + Entry Angle | LITERAL | Enriched Theme | Instant + ≥2 diffs |
| S3 COLLISION | Theme + creative lens, obvious expansion | ADJACENT | Seed 1 | <5 sec + ≥2 diffs |
| S4 DRIFT | Unexpected angle on theme | OBLIQUE | Seed 2 | <15 sec + ≥2 diffs |
| S5 RUPTURE | Theme as physical consequence only | TRACE | Seed 3 | <30 sec + ≥2 diffs |

Do NOT modify this table.

IMMEDIATELY AFTER this table, BEFORE the next paragraph that starts with "**PALETTE EVOLUTION RULE", INSERT:

**S1–S2 VISUAL DIFFERENTIATION RULE (FULL ARC):** S1 and S2 both derive from Enriched Theme, but must emphasize DIFFERENT visual aspects of that theme. They must not share dominant texture, dominant weather element, or dominant organic/mechanical motif. If the Enriched Theme spans multiple material categories, S1 uses one, S2 uses another. If it spans multiple scales, S1 uses one, S2 uses another. If it implies both indoor and outdoor contexts, S1 uses one, S2 uses the other.

Test: describe S1 and S2 each in 5 words. If the descriptions share more than 2 words (excluding the carrying image name), rewrite S2 with a different visual emphasis.

Do not modify the PALETTE EVOLUTION RULE or any other text after the insertion.

---

# PROHIBITIONS

- Do NOT change any text other than the 4 locations specified above
- Do NOT add comments like "changed", "updated", or "modified"
- Do NOT rephrase surrounding text "for consistency"
- Do NOT touch examples (matchbox, ceramic mug, etc.)
- Do NOT touch modules (A, B, C, D, V)
- Do NOT delete or add sections
- Do NOT reorder anything
- Do NOT touch any rules, definitions, or explanations outside the 4 edit locations
- Do NOT renumber existing items in any list or checklist

Output the COMPLETE prompt text with all 4 edits applied.