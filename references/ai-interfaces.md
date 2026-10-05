# AI interaction checks (only for AI-enabled features)

Do not add AI controls to a product that has no AI feature. When one does, use Microsoft's HAX guidance as the base and translate it to the product's real capabilities. Carbon's AI components are a useful reference where the project uses Carbon.

## Checks

- **Capability and limits.** Say what the AI can do, where it is limited, and when output needs verification. Never show fabricated confidence percentages or assurances of correctness.
- **Origin.** Distinguish generated suggestions, user-written edits, and confirmed system outcomes whenever that distinction affects a decision. Give access to sources when evidence matters, and never invent citations or imply a citation proves accuracy.
- **Control.** Support correction, dismissal, editing, retry, and cancellation where the capability allows. Preserve user work, and never overwrite edits during regeneration or streaming.
- **Draft versus action.** Separate generating a draft from executing or sending it. Define the permitted action scope from the user's or project's authorisation. Before an irreversible or consequential action, show the real content, destination, and consequences, unless valid prior authorisation already covers it. Avoid repeated approvals for authorised low-risk actions.
- **Agentic features.** Make consequential action scope, access and outcomes understandable. Provide stop/cancel and undo where the capability exists; do not promise reversibility for irreversible actions. Keep a readable action record when relevant. Scale preview and review to risk and existing authorisation; do not require repeated plan approval for authorised routine actions.
- **States.** Show generating, cancelled, failed, saved, and completed states honestly. Never report success before confirmation, and resolve concurrent edit and regeneration conflicts visibly.
- **Testing.** Test wrong or incomplete output, missing evidence, interruption, and recovery.
