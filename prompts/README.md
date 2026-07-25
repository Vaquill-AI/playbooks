# Prompts

Ready-to-use prompts for in-house and corporate counsel working with a legal AI assistant.
These are the same starter prompts that ship inside [Vaquill](https://vaquill.ai), lightly reformatted for reuse anywhere.

There are two sets:

- **[composer-prompts.md](composer-prompts.md)** - fully written, ready-to-run prompts grouped by task (triage, review, drafting, negotiation, research, compliance, corporate, disputes). Paste one in, attach your document, and go.
- **[research-templates.md](research-templates.md)** - fill-in-the-blank templates with `{{placeholders}}` for research and analysis questions.

## How they are written

Every prompt follows the same discipline that makes legal AI output trustworthy:

1. **Assign your side.** State whether you are the customer, vendor, employer, licensee, and so on, so the analysis is framed for you.
2. **Ground in the document.** Prompts ask the model to quote and cite the clause it is talking about, not to paraphrase from memory.
3. **Forbid invention.** Placeholders in `[BRACKETS]` mark facts you must supply. The model is told to leave them as placeholders rather than guess commercial terms.
4. **Ask for structure.** Tables, ranked lists, and tiered positions make the output usable instead of a wall of text.

## A note on placeholders

- `[BRACKETED]` values are facts **you** fill in (a party name, a jurisdiction, a dollar cap).
- `{{double-braced}}` values in the templates are the same idea, with an example inside to guide you.
- "the @-mentioned document" refers to whatever contract or file you attach or pin in your tool.

## Disclaimer

General reference for US commercial practice, not legal advice.
See [../DISCLAIMER.md](../DISCLAIMER.md).
Licensed under [CC BY 4.0](../LICENSE).
