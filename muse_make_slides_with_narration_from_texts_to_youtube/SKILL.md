# YouTube Video Slide Maker

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not run any connection check or setup.
  - **B — actually use it:** Tell them 「接続を確認してから説明します」, then run the Google Drive and Google Slides connection checks (share a connect link and wait if a service is not connected), and explain using the sheet while collecting the material for the first video.

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

- Ask about every missing item among the format, the length, the image style, the image generation source and the checkpoint in one message before starting work. Ask all of these questions together at the start, never one at a time later, and write how to answer inside the question block: number the questions, show the choices or a one-line answer example for each, and state the default that applies when an item is left unanswered, so the user can reply in a single message.

- Accept the manga format only when the user names it with words such as manga, flip style, panels or image only.

- Accept the presentation format only when the user names it with words such as presentation, slides or an explainer with images.

- Offer the four checkpoints A to D from the templates file and record the chosen one instead of guessing it.

- Offer the image style as a choice from a fixed list instead of asking for free text: 1. cool and stylish (the standing default, recommended), 2. flat and clear, 3. photo-like, 4. warm hand-drawn, 5. minimal, 6. manga style. Record the chosen style in brief.md; when the user does not choose, use the cool and stylish default. Apply the chosen style to every image in the package, the thumbnail included.

- Apply the Japanese language, a 16 to 9 frame, a casual and clear tone and a general beginner audience when the user leaves those open.

- Record the format, the slide count, the image style, the image source, the checkpoint, the tone, the audience and a short slug in brief.md once the answers arrive.

- Offer the two image generation sources inside the same opening question block and record the chosen one as the image source: Muse (the built-in image generation) or Gemini (through the built-in browser). When the user chooses Gemini, proceed to the Google sign-in step in the image generation section before any image work, because Gemini is used only while the built-in browser is signed in to Google.

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

- Write every image prompt in English and submit it in English, whichever image source is used. Only the text that must appear inside an image (for example the thumbnail title) stays in the content's language, quoted inside the English prompt.

- Generate the body images first. Do NOT generate the thumbnail in this phase: the thumbnail is made last, in the thumbnail phase after packaging, once the finished content and the body images can be reviewed as a whole.

- When the image source is Muse, generate the images with `media.generate_image`, set the output folder to the images folder inside the video folder, and name the files thumbnail.png, slide-01.png onward for presentation form or scene-01.png onward for manga form.

- Skip generation for a slide already covered by a supplied image used as-is and point that slide entry in upload.json at the supplied file.

- Keep one image style across every image and record a fixed character description in brief.md for a recurring manga character, then reuse that description in every prompt.

- Apply the image style chosen at the parameter check to every prompt, in the style's English wording. The standing default is a cool and stylish look: sharp composition, strong confident subjects, clean modern color contrast and a polished, high-end finish. A style the user chose for this package always replaces the default for that package.

- Put large title text only in the thumbnail image and keep text and speech bubbles out of body images unless the user asked for dialogue inside the images.

- Write detailed image prompts into content.md and ask the user to generate the images when image generation is unavailable in the session.

- When the image source is Gemini, generate the images with Gemini in the built-in browser instead of `media.generate_image`:

  - Use Gemini only while the built-in browser is signed in to Google. Check the sign-in state first with a read-only open of https://myaccount.google.com/ and continue only when the account page shows a signed-in account.
  - When the browser is not signed in, open the Google sign-in page in the built-in browser and have the user sign in themselves through the secure entry. Never ask the user to send a password or a sign-in code in chat. Verify the signed-in state on the account page before generating anything.
  - When the user stops, declines or cannot complete the sign-in, do not generate with Gemini. Stop and ask whether to switch the image source to Muse or pause the build; never switch silently.
  - Generate one image per new Gemini chat with the exact image prompt from content.md, download each generated image at full size, convert it to PNG when needed, and save it into the images folder under the same standard names as the Muse route.
  - Inspect every downloaded image before packaging: the subject matches the prompt, the style stays consistent across the set, and the thumbnail title text is legible and spelled exactly as written. Regenerate an off-brief image once with the same prompt before reporting a problem.

## Package the deliverables

- Build upload.json at version 1 from content.md, narrations.md and the image paths. Reserve the thumbnail as the first slide entry, pointing at images/thumbnail.png, even though the thumbnail image itself is generated afterwards in the thumbnail phase.

- Write youtube-meta.md with three title ideas, a description, tag ideas and an audience note.

- Write manual-steps.md with the delivery template from the references file.

## Make the thumbnail last

- Only after the content, the narration, the body images and the package drafts exist, design the thumbnail with the whole package in view: the final title wording, the strongest visual among the finished slides, and the hook of the opening narration. A thumbnail designed with the whole package in view is consistently stronger than one made first.
- Write the thumbnail prompt in English (the in-image title text stays in the content's language) and apply the same chosen image style as the body images, so the thumbnail matches the deck.
- Generate the thumbnail with the same image source as the body images and save it as images/thumbnail.png.
- Afterwards, validate upload.json with `muse.exec` by parsing it and checking that every referenced image file exists, the thumbnail included, before calling the package complete.

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
