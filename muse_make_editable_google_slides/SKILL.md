# YouTube Video Slide Maker

## Route the input

- Start from rough notes or bullet text the user pastes or attaches and go straight to the parameter check.

- Accept image files supplied with the notes or the log as video material and route them through the supplied image rules below.

- Start from a conversation log file, such as a Cursor transcript in jsonl form, and run the log summary phase before anything else.

- Treat one video as one folder and one chat so the context stays small across a series of videos.

- Read [templates and schemas](references/templates.md) before writing deliverables, read [delivery into Google Slides](references/delivery.md) before putting a deck into Google Slides, and read [worked examples](references/examples.md) when a request is ambiguous.

## Preserve the user's exact names

- Copy product, service and other proper names exactly as the user writes them, in every deliverable: titles, bullets, narration, metadata, image prompts and deck text.

- If the user writes Muse, write Muse everywhere. Never substitute a similar-looking name such as Claude, and never "correct" the user's spelling of a name, even when another product with a similar name exists.

- When a request does not name the product or service, use the spelling the user has used for it before; do not introduce a look-alike variant of your own.

- Before calling the package complete, search the deliverable texts for look-alike variants of the key names (for example Claude when the user wrote Muse) and unify every occurrence to the user's spelling.

## Confirm the parameters before building

- Ask about every missing item among the format, the length, the image style and the checkpoint in one message before starting work.

- Accept the manga format only when the user names it with words such as manga, flip style, panels or image only.

- Accept the presentation format only when the user names it with words such as presentation, slides or an explainer with images.

- Offer the four checkpoints A to D from the templates file and record the chosen one instead of guessing it.

- Apply the Japanese language, a 16 to 9 frame, a casual and clear tone and a general beginner audience when the user leaves those open.

- Record the format, the slide count, the image style, the checkpoint, the tone, the audience and a short slug in brief.md once the answers arrive.

- Use `muse.create_options` for the format and checkpoint choices in the main chat and keep any remaining questions in that same message as plain text.

## Set up the video folder

- Create the output folder under ~/workspace/youtube-videos/ with the slug as its name unless the user names another place.

- Keep deliverables out of the source repository at ~/workspace/skills-youtube-make and out of this skill folder.

- Track the phases with `todo.write` and tell the user the current phase at each checkpoint.

## Summarize a conversation log first

- Read a large log in chunks with `muse.exec` instead of loading the whole file into the chat.

- Extract the theme, the goal, the prerequisites, the steps in time order, the pitfalls, the key commands or screens and the parts a video can skip into source-notes.md with the template in the references file.

- Remove tokens, passwords, env file values and personal identifiers from the summary and from every later deliverable.

- Present the summary to the user and wait for approval or corrections before any structure work.

- Treat the approved source-notes.md as the only source for the later phases and never promote the raw log back into that role.

## Build the structure

- Write structure.md with the thumbnail as the first row and the opening, the body and the ending after it.

- Count a requested slide total as body slides and add the thumbnail on top of that count.

- Keep body bullets to three lines or fewer on each presentation slide and keep one scene in each manga panel.

- Stop after the structure when the chosen checkpoint includes that stop and fold user feedback into structure.md before moving on.

## Place supplied images

- Inspect every image the user supplied and identify what it shows before the structure phase.

- Record each supplied image in brief.md with what it shows, the planned slide, the role and the reason, using the register form in the templates file.

- Decide the placement from the image content and the flow of the notes, and state the placement with its reason in structure.md so the user can move it at the structure checkpoint.

- Ask the user what an image shows when its content cannot be identified and never place an unidentified image by guessing.

- Write the title, the bullets and the narration of a page around the supplied image placed on it, including what the narration says while that image is on screen.

- Copy a supplied image used as-is into the images folder with a clear file name and keep the supplied original unchanged.

- Warn the user when a supplied image resolution is too low for a full slide and offer a smaller placement or a generated alternative.

- Use a supplied image as a reference for generated images only when the user asks and mark that use in the register.

## Write the content and the narration

- Write content.md in the presentation or manga form from the templates file, with a title, bullets, speaker notes and an image direction for each slide or scene.

- Write narrations.md as natural spoken text instead of reading the slide text aloud word for word.

- Give the thumbnail narration a short hook of about 8 to 15 seconds and give each body slide about 15 to 30 seconds in presentation form or 10 to 20 seconds in manga form.

- Stop after the content at checkpoint B and after the narration at checkpoint C, then continue automatically at the stops a checkpoint marks as automatic.

## Generate the images

- Generate the images with `media.generate_image`, set the output folder to the images folder inside the video folder, and name the files thumbnail.png, slide-01.png onward for presentation form or scene-01.png onward for manga form.

- Skip generation for a slide already covered by a supplied image used as-is and point that slide entry in upload.json at the supplied file.

- Generate the thumbnail in the same batch as the body images and never leave it to a later round.

- Keep one image style across every image and record a fixed character description in brief.md for a recurring manga character, then reuse that description in every prompt.

- Put large title text only in the thumbnail image and keep text and speech bubbles out of body images unless the user asked for dialogue inside the images.

- Write detailed image prompts into content.md and ask the user to generate the images when image generation is unavailable in the session.

## Package the deliverables

- Build upload.json at version 1 from content.md, narrations.md and the image paths, with the thumbnail as the first slide entry.

- Write youtube-meta.md with three title ideas, a description, tag ideas and an audience note.

- Write manual-steps.md with the delivery template from the references file.

- Validate upload.json with `muse.exec` by parsing it and checking that every referenced image file exists before calling the package complete.

- In the same pass, grep every deliverable file for look-alike variants of the proper names in the user's request and fix any mismatch to the user's exact spelling before delivery.

- Refuse to call the package complete when the thumbnail is missing from upload.json or from the images folder.

## Put the deck into Google Slides

- Build every deck for Google Slides with titles, body text, tables and speaker notes as editable text objects, for example by assembling the presentation file with native text shapes through python-pptx, and never render slide text into images.

- Keep the thumbnail, manga panels, illustrations and other image assets as images inside that text native deck, because pictures stay pictures by design.

- Follow the Google Slides connector doc to create the empty destination presentation and put the text native file into it through Drive, which converts the file in place and keeps the text editable.

- Read the deck back after the upload and check both the page count and that text is present as text on each page before reporting success.

- Use a rendered image deck only when the user asks for design fidelity over editability and tell the user before that upload that the slides land as images with uneditable text.

- Follow [delivery into Google Slides](references/delivery.md) for the upload steps and record the resulting presentation URL in slides-result.json inside the video folder.

## Hand off the manual steps

- Leave the Google Vids conversion, the voiceover work inside Vids and the YouTube publishing to the user, with the steps written into manual-steps.md.

- Never operate the Vids or YouTube interface on the user behalf in this workflow.

## Available connectors

- [Google Slides](/opt/hatch/connectors/google_slides/CONNECTOR.md) for creating the destination presentation and putting a finished deck into the user Google Slides account.

- [Google Drive](/opt/hatch/connectors/google_drive/CONNECTOR.md) for finding staged image folders and presentation files in the user Drive.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Websites

- [YouTube](https://www.youtube.com/) for the final manual publishing step, where the user enters the title, description and tags from youtube-meta.md.

## Alternatives for better results

- Open a fresh chat for the next video in a series and carry over only the style and character settings from brief.md, which keeps the working context small.

- Split an overlong structure into a part one and a part two at a natural break instead of packing more bullets onto each slide.
