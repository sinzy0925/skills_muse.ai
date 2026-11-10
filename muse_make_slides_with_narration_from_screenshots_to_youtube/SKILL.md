# スクショから手順スライド作成 (Slides from Screenshots)

## What this skill does

Turn the user's screenshots of a procedure (PC screens, app screens, photos of steps) into an editable Google Slides how-to deck:

- Original images are pasted onto slides **unedited**.
- Privacy masks and click annotations are placed **as slide shapes on top of the images** (rectangles, ellipse outlines, numbered badges), so the user can drag and fine-tune them in Google Slides.
- Every slide's speaker notes carry a narration script describing the work done on that page, ready for a YouTube walkthrough.
- Slide body text stays editable text (never flattened into images).

First run: 2026-11-08, a Google-account creation guide from 8 PC screenshots (10 slides). The user explicitly rejected baking annotations into the image files; slide-shape overlays are the point of this skill.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Cloning this repository and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not run any connection check or setup.
  - **B — actually use it:** Tell them 「接続を確認してから説明します」, then run the Google Drive and Google Slides connection checks (share a connect link and wait if a service is not connected), and explain using the sheet while collecting the screenshots or video and the one-line brief.

## Inputs (validate first)

1. The screenshots, with a known order. Default order: filename timestamps ascending, when filenames carry them.
2. A one-line brief from the user, three parts. If any part is missing, ask using exactly these prompts:
   - 何の写真か（試作品？ 完成品？ いただきもの？）
   - 目的は何か（宣伝したい／記録したい／感謝を伝えたい）
   - 誰・どこなのか、強調したい点は何か
3. Whether real names / email addresses / other personal information visible in the screenshots should be masked. Default: mask them; confirm with the user when unsure what counts.

If the brief is missing, STOP and ask before building anything. A one-line brief dramatically improves captions and narration; do not guess the purpose.

## If the input is a video file instead of screenshots

The same workflow applies, with one added front step:

1. Accept the video (mp4). Large files come via Google Drive, because chat attachments have a size cap.
2. Extract frames with ffmpeg — at scene changes, at fixed intervals, or at timestamps the user names. Frame resolution is the video's resolution.
3. Present the candidate frames and agree the selection with the user. With screenshots the user has already curated the key scenes; with a video, this selection step replaces that curation.
4. Treat the selected frames as the screenshots. Order is by timestamp. Everything from Step 1 of the Workflow onward (structure, coordinates, overlays) is unchanged.
5. If the video has narration audio, transcribe it (faster-whisper) and use the transcript as the draft source for the speaker-note narration, aligned to the steps. This is a head start the screenshot route does not have; still show the user the resulting narration with the deck.

## Workflow

### Step 1: Structure proposal [checkpoint]

Propose the deck structure first (title slide + one slide per step + a summary/notes slide) and wait for the user's OK before building. Note anything in the screenshots that needs a decision (visible personal info, unclear click targets, steps that seem out of order).

### Step 2: Locate elements and verify coordinates locally

For each screenshot:

1. Use visual grounding to locate every element that needs a mask or a mark (click targets, input fields, buttons, personal information). Work in normalized 0–1000 coordinates per image.
2. Render a **private local preview** (e.g. PIL) with the masks and marks drawn at those coordinates and **look at every preview image**. Grounding coordinates are often slightly off; masks especially must be checked and widened until the personal information is completely covered, including on screens where the same information appears again in the background (e.g. address suggestions still visible on the next screen).
3. Only after the previews are clean, carry the same coordinates into the deck build.

Never ship a mask you have not visually verified on the preview.

### Step 3: Build the deck

- 16:9. House style: background #F7FAFF, orange #E87A2E accent, blue #2E6BE6 hairline, Arial.
- Title slide: deck title, one-line subtitle, what to prepare if relevant.
- Step slides: step chip + heading, the original screenshot fitted large, a short caption under it that references the annotation numbers (①②③).
- Summary slide: the key points / cautions as bullets.
- Speaker notes on **every** slide: a narration script in spoken style describing the work on that page (what to click, what to type, what to watch out for), so the user can read it as-is for a YouTube video.
- Overlays per screenshot, in this order: image, mask rectangles (dark fill #2D2D2D, no line), ellipse outlines (no fill, red #E21E1E, ~3pt), numbered badges (red filled circles, white bold numbers) placed at the ellipse's top-left, nudged outside so the circled text stays readable.
- Number marks in click order per page. If a page has several click points, number all of them. Visible buttons the user names (e.g. a 「次へ」 that is not on the main path) get a number too when the user asks; explain such exceptions in the narration.

Build with python-pptx, upload the .pptx to Google Drive with conversion to Google Slides (mimeType application/vnd.google-apps.presentation).

### Step 4: Verify and report

Read the presentation back and check: slide count, one image per step slide, overlay shapes present (element counts), speaker notes present on all slides. Report the Slides URL and what was masked/annotated.

### Revisions

- The user will fine-tune shapes themselves; that is expected and is why overlays are shapes.
- When the user asks Muse to fix a slide, rebuild and re-upload **to the same file** (drive files update) so the link does not change — but tell the user plainly that a whole-deck re-upload overwrites any manual adjustments they already made, and ask them to flag if that is a problem.
- Numbering corrections from the user (e.g. "ステップ2は、次へが③") are applied exactly as stated; adjust the caption/narration to match.

## Rules

- Never edit the original image files. All annotation lives on the slides.
- Never record or reveal personal information found in the screenshots; mask it in the deliverable and do not repeat it in chat.
- Do not upload or publish anything beyond the agreed deck without the user's OK.
- This skill is local only unless the user says otherwise: do not add it to the GitHub README (the README lists only the two skills the user chose on 2026-11-05).
