# Delivery into Google Slides

Put a packaged video folder into Google Slides with editable text on each slide. Follow the steps below unless the user asks for design fidelity over editability (see the exception).

## Muse Google Slides connector with a text native build

Use the user own Google account through the Google Slides connector. Follow the connector doc linked from SKILL.md for the exact commands.

1. Assemble the presentation file with native text shapes, for example with python-pptx, placing titles, bullets, tables and speaker notes as real text and the generated pictures as image elements.
2. Create the empty destination presentation through the connector with the video title.
3. Upload the built presentation file into that destination through Drive, which converts it in place and keeps the text editable.
4. Read the deck back and confirm both the page count and that text is present as text on each page.
5. Write the presentation URL into slides-result.json in the video folder.

Verified on 2026-11-01 with the skill guide deck: a text native build uploaded this way gave 7 pages with editable text on every page, while an image rendered build of the same content gave 7 pages with no editable text at all.

Exception: a rendered image build, such as the presentation artifact builder output, is allowed only when the user asks for design fidelity over editability. State before that upload that the slides land as images and their text cannot be edited in Google Slides, and that text changes then mean editing the source files, rebuilding and uploading again to the same presentation, which replaces every slide and discards edits made inside Google Slides since the last upload. Read the live deck back before a re-upload and warn the user when it changed.

## manual-steps.md template

Write this file into every video folder, filled with that video values.

```markdown
# Manual steps

## Setup
- Video folder: ~/workspace/youtube-videos/{slug}/
- Format: {presentation or manga}
- Slides: {N} including the thumbnail

## Step 1: Check the Google Slides deck
Open the deck URL recorded in slides-result.json and check the order, the images and the speaker notes against content.md and narrations.md.

## Step 2: Convert to video in Google Vids
1. In Google Slides, use the convert to video button to send the deck to Google Vids.
2. In Vids, set the voiceover for each page following narrations.md.
3. Preview the whole video once for timing and volume balance.

## Step 3: Publish on YouTube
1. In Vids, use the convert to YouTube action.
2. Enter the title, description and tags from youtube-meta.md.
3. Set images/thumbnail.png from the video folder as the thumbnail when YouTube asks for one.
4. Adjust the visibility settings and publish.
```
