
═══════════════════════════════════════════════════════════════
UPG v9.10 → v9.11 PATCH
Apply to: UNIVERSAL PROMPT GENERATOR v9.10
Scope: 3 targeted fixes, no structural changes
═══════════════════════════════════════════════════════════════

## PATCH 1: VISUAL_VOCABULARY METAPHOR TRAP

LOCATION: INPUTS section → VISUAL_VOCABULARY Usage paragraph

ADD after existing VISUAL_VOCABULARY paragraph:

"""
**VISUAL_VOCABULARY Pre-Scan:** Before processing, scan all 
VISUAL_VOCABULARY entries for metaphorical language that will 
trigger Zero Tolerance bans when transferred to prompts:

BANNED in VV source text:
- "as if" / "as though" / "like [verb-ing]" / "seems to"
- "будто" / "словно" / "как будто" / "как если бы"
- Any simile describing process or perception

If found → rewrite as physical property BEFORE generation:
  ❌ "as if dipped in rusty water"
  ✅ "with oxide-brown edges and iron-dark veins"
  
  ❌ "like living tissue"  
  ✅ "with blurred boundary and fibrous texture"
  
  ❌ "resembles breathing"
  ✅ "with expansion marks and pressure ridges"

This scan prevents VV content from multiplying Zero Tolerance 
violations across all slots.
"""

───────────────────────────────────────────────────────────────

## PATCH 2: TIER 1 "FINE" ENFORCEMENT

LOCATION: A.2 Mandatory Quality Rules → Banned generic adjectives

MODIFY the existing Tier 1 list:

BEFORE:
"""
soft→diffused/muted/low-contrast | clean→uncluttered/minimal | 
fresh→recently-cut/undried | fine→narrow/hairline | ...
"""

AFTER:
"""
soft→diffused/muted/low-contrast | clean→uncluttered/minimal | 
fresh→recently-cut/undried | **fine→particulate/narrow/hairline 
(MANDATORY REPLACE — high escape rate)** | smooth→polished/satin | ...
"""

ADD to TIER 1 MICRO-SCAN instruction:

"""
**Priority scan for "fine":** This adjective has the highest 
escape rate. Common violations:
- "fine dust" → "particulate dust" or "ite powder"
- "fine powder" → "ite powder" or "ite particulate"
- "fine lines" → "hairline" or "narrow"
- "fine detail" → "granular detail" or specific description

If "fine" appears without physical qualifier (measurement, 
material comparison), REWRITE before output.
"""

───────────────────────────────────────────────────────────────

## PATCH 3: ENTRY ANGLE SCALE EXECUTION

LOCATION: B.2 Theme Enrichment → Entry Angle section

ADD after Entry Angle rotation table:

"""
**Entry Angle Execution Guidance:**

SCALE angle (S1) has low natural compliance. To ensure proper 
execution:

✅ SCALE-compliant first sentences open with size/quantity:
- "A fifteen-meter granite Buddha rises..."
- "A half-meter strip of steel lies..."
- "Three hundred years of growth have..."
- "The eight-wheeled chassis spans..."

❌ Non-compliant (actually LOCATION):
- "Lunokhod-2 stands at the edge..." (location leads)
- "An abandoned forge occupies..." (location leads)
- "The sakura trunk fills..." (subject leads)

SCALE requires numerical or dimensional anchor as grammatical 
subject or first modifier. If theme lacks obvious dimensional 
hook, prefer LOCATION or TIME for S1 instead.

LOCATION angle (S2) has high natural compliance. Prepositions 
(on, within, beneath, inside, at) naturally open sentences.
No additional guidance needed.
"""

═══════════════════════════════════════════════════════════════
## PATCH SUMMARY
═══════════════════════════════════════════════════════════════

| # | Target | Change type | Risk |
|---|--------|-------------|------|
| 1 | VV metaphor scan | ADD paragraph | None |
| 2 | "fine" enforcement | MODIFY + ADD | None |
| 3 | SCALE execution | ADD paragraph | None |

No deletions. No structural changes. No parameter defaults.
All changes are guidance/enforcement, not behavioral shifts.

═══════════════════════════════════════════════════════════════
## VERIFICATION AFTER PATCH
═══════════════════════════════════════════════════════════════

Run these checks on first generation after patching:

□ VV entries contain no "as if/as though/like [verb]"
□ No "fine" appears without physical qualifier
□ S1 with SCALE angle opens with number/dimension
□ Zero Tolerance scan returns 0 violations

If any check fails → patch not fully integrated.

═══════════════════════════════════════════════════════════════
```

---