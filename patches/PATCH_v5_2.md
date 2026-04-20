You will receive a long system prompt called “UNIVERSAL PROMPT GENERATOR v5.2”.  
Your task is to surgically revise this prompt, NOT to rewrite it from scratch.  
Preserve its overall structure, phases, terminology, and style, but implement the following improvements as explicit, concise additions or modifications inside the existing sections.

WORKING STYLE
- Keep the tone, formatting, and phase structure of the original text.
- Make only targeted edits: add paragraphs, clarifications, or short submodules where needed.
- Do not shorten or simplify the framework conceptually; focus on safety, clarity, and edge‑case handling.
- Do not invent platform policies; only express generic, model‑agnostic safety and abstraction rules.

GOALS OF REVISION
1. **Real people, brands, copyrighted characters**
   - In Phase 1.3 (Safety Check), expand the “Real personalities / Copyright / AI-generated likeness” line into a clearer rule:
     - Real political figures, celebrities, or identifiable private individuals must be replaced by archetypes or generic roles.
     - Famous brands and copyrighted characters must be replaced by non-infringing, original equivalents.
   - Add an explicit mechanism that carries these replacements through all later phases:
     - Introduce a small data structure (e.g., `safety_transform`) that records original term → safe replacement.
     - In Phase 2.4 (Theme Enrichment), Phase 2.6 (Boundary Check), Phase 4.3 (Seeds), and Phase 5 (Slot Generation), explicitly state that only the replacement, not the original real name/brand/character, may appear in ENRICHED THEME, SPECIALIZED VARIANTS, seeds, and final slot prompts.
   - In the MANDATORY VALIDATION STATE JSON, add a `"safety_transform"` field under `"routing"` or `"processing"` and ensure Phase 6.2 (Cascade Check) mentions re-verifying that replacements are consistently used.

2. **Abstract and “almost non-visual” themes**
   - Add a dedicated rule for extremely abstract themes (e.g., “the meaning of life”, “emptiness without emptiness”, “the inexpressible”) which:
     - Detects when THEME_RAW has BROAD width and contains no concrete physical objects, locations, or actions.
     - Activates a special mode (you can name it e.g. `ABSTRACT-HARD`):
       - ENRICHED THEME must be expressed as one or two very simple, embodied metaphor scenes, each with a small number of concrete visual elements (e.g., a single object in a simple environment).
       - Limit metaphor density: no more than 1–2 symbolic elements per scene in ENRICHED THEME.
       - In Spectrum Axis (Phase 4.1), require a gradient “from embodied metaphor toward pure color/light/structure”, not from “abstract word to another abstract word”.
   - In Phase 4.4 and Phase 7, explicitly state that this mode exists to preserve visual executability for highly abstract concepts.

3. **Violence, trauma, and graphic content**
   - Extend the Safety Check (Phase 1.3) with a dedicated trigger for graphic violence, murder, torture, and extreme gore.
   - Create a short “violence redirect toolkit” similar in spirit to Module C (REDIRECT-EXPLICIT), but focused on violence rather than sexual content. You may:
     - Place it as a small subsection under Safety Check, or as a new optional module (e.g., `Module V — REDIRECT-VIOLENCE`).
   - This toolkit should:
     - Forbid glorified, glamorized depictions of violence.
     - Encourage documentary, aftermath, or silhouette-based framings:
       - Silhouette or shadow of an action instead of explicit detail.
       - Aftermath scenes (police tape, ambulances, empty street with traces of an event).
       - For artistic context: allow symbolic imagery (shattered objects, abstract red shapes) with clear limits on abstraction as per Phase 4.4.
   - Ensure this redirect preserves subject count and basic relational dynamics (who is victim, who is aggressor) without explicit gore.
   - Mention in Phase 5.4 (Cinematic Enhancement) or Validation that such violent themes must use these safe cinematic framings where applicable.

4. **Hate, discrimination, and harmful stereotypes**
   - Extend Phase 1.3 (Safety Check) with an explicit line for:
     - Hate speech, discriminatory stereotypes, or slurs targeting protected groups (e.g., ethnic, religious, racial, gender, sexual orientation).
   - State clearly:
     - Such input either must be refused or redirected by:
       - Removing the protected characteristic and replacing it with a neutral, non-stereotyped role (e.g., “wealthy collector” instead of “wealthy [ethnicity]”),
       - Or, if the user’s intent is clearly hateful or inciting, the system should not attempt visual realization (just refuse).
   - Ensure that Ideology & Segmentation Integrity Check (Phase 5.3) mentions not only “manifesto / radical / anti-*” language but also harmful group stereotypes and their removal/neutralization.

5. **Scientific but non-visible phenomena**
   - In Phase 3.2 (Register Rules) or Phase 4.4 (Executability Filter), add a clear rule for SCIENTIFIC context when dealing with invisible or highly abstract phenomena (quantum effects, radioactive decay, fields):
     - Prefer visually clear, diagrammatic, or laboratory-based representations (equipment, graphs, schematics, inferred visualizations) rather than generic sci-fi “neon waves in space”.
     - Encourage visual metaphors that preserve scientific honesty (e.g., detector readouts, cloud chamber tracks, simulated field lines) over purely mystical cosmic imagery.
   - Make this a guideline to avoid pseudo-scientific clichés and to strengthen clarity.

6. **Synesthesia and cross-sensory themes**
   - For themes that explicitly combine different senses (e.g., “taste of blue”, “sound of silence”, “synesthesia of pain”), add a special note in Phase 4.3/4.4:
     - Allow a higher metaphor ratio (up to 40%) even outside pure ARTISTIC context, as long as:
       - There is always at least one concrete visual carrier (object, environment, body part) that “holds” the sensation.
       - The cross-sensory mapping is made visually concrete (e.g., blue expressed as icy metallic surfaces, taste represented as frost on lips, etc.), not just linguistic.
   - Clarify that this is a controlled exception to the default metaphor limits for better handling of synesthetic themes.

7. **INTENT_SIGNAL vs. abstract breadth**
   - In Phase 0, refine the INTENT_SIGNAL rule:
     - If INTENT_SIGNAL = LITERAL but THEME_WIDTH = BROAD and the theme is highly abstract with no concrete physical anchors, treat it as EXPANSIVE for the purposes of enrichment and spectrum, while keeping Drift Evaluation (Phase 2.7) stricter.
   - Explicitly state this as a safeguard: do not over-promise literal visualization when the subject is conceptually non-literal.

8. **Propagation and bookkeeping of safety decisions**
   - In Phase 6 (Validation), under the JSON “routing” or “processing” sections, add:
     - `"safety_transform": { "original": null, "replacement": null }` (or an array of such mappings).
   - In 6.2 (Cascade Error Propagation Check), explicitly mention that:
     - Any correction in Safety Check or safety_transform must trigger re-verification that all slots and seeds use only the safe replacements, never the original sensitive terms.

DELIVERABLE
- Return the full revised “UNIVERSAL PROMPT GENERATOR v5.2” text with your additions integrated.
- Preserve headings, sections, and numbering as much as possible.
- Mark any major new optional module (e.g., violence toolkit) with the same style as existing optional modules (Module A, B, C, D), keeping naming consistent.