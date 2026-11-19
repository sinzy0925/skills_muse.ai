# Verify an artifact fix on the real device

This amendment adds to the base skill for a Muse artifact or Space that the user opens on their own device. It applies after any edit or repair to such an artifact or Space, and it does not replace the base skill.

## Check the edited content first

- After an edit, read the edited file or use `artifact.inspect` to confirm the change is present in the content that will run.

- Treat a build completion widget or a successful edit call as proof that a change was applied, not as proof that the fault is gone.

- When the earlier report said a change was done and the user later shows it had no effect, recheck the content before trying another repair.

## Treat the audit environment as non reproducing

- When your check environment cannot reproduce the display on the user device, say that plainly in the same report.

- Do not claim the fault is fixed from a check in an environment that cannot reproduce it.

- Report the work as changed and awaiting a test on the real device, and ask the user to try the exact action that failed before.

## Report the state honestly

- Use the word fixed only after the edited content was checked and the user confirms the action works on their device.

- When the user reports that the fault is still present, start from their exact report and change the repair angle instead of repeating the same repair.

- When a second repair of the same kind also fails on the real device, simplify the artifact or rebuild it in a plainer form instead of adding another layer to the same approach.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Remove a fragile input or interaction when removing it also removes the fault, as removing the launcher inputs removed the lost input fault.

- Rebuild with no script and a plain link when scripted navigation keeps failing on the real device.

- Keep the user report and the exact failing action in the next repair attempt so the same untested claim is not repeated.
