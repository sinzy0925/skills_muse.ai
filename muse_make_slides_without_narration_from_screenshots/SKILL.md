# スクショからプレゼン資料作成（ノート無し）(Slides without Narration from Screenshots)

## What this skill does

Turn the user's screenshots of a procedure into a **finished presentation deck** in Google Slides:

- **No speaker notes.** The deck must stand on its own as presentation material.
- The work to do on each page is written **on the slide itself, in large text** (a bold instruction line, ~22pt, in a highlighted band under the screenshot), so the audience can follow the procedure from the slides alone.
- Original images are pasted onto slides **unedited**. Privacy masks and click annotations are placed **as slide shapes on top of the images**, so the user can drag and fine-tune them in Google Slides.

Sibling skill: `muse_make_slides_with_narration_from_screenshots_to_youtube` is the YouTube version (speaker notes carry the narration). Use THIS skill when the user asks for プレゼン資料, ノート無し, or large on-slide text instead of narration.

First run: 2026-11-08, a Chrome-profile guide (7 screenshots → 9 slides) built as the presentation counterpart of the narration deck made the same morning.

## Inputs (validate first)

1. The screenshots, with a known order. Default order: filename timestamps ascending.
2. A one-line brief from the user, three parts. If any part is missing, ask using exactly these prompts:
- 何の写真か（試作品？ 完成品？ いただきもの？）
- 目的は何か（宣伝したい／記録したい／感謝を伝えたい）
- 誰・どこなのか、強調したい点は何か
3. Whether real names / email addresses / other personal information visible in the screenshots should be masked. Default: mask them; confirm with the user when unsure what counts.

If the brief is missing, STOP and ask before building anything.

## If the input is a video file instead of screenshots

The same workflow applies, with one added front step:

1. Accept the video (mp4). Large files come via Google Drive, because chat attachments have a size cap.
2. Extract frames with ffmpeg — at scene changes, at fixed intervals, or at timestamps the user names. Frame resolution is the video's resolution.
3. Present the candidate frames and agree the selection with the user. With screenshots the user has already curated the key scenes; with a video, this selection step replaces that curation.
4. Treat the selected frames as the screenshots. Order is by timestamp. Everything from Step 1 of the Workflow onward (structure, coordinates, overlays, large on-slide instruction text, no notes) is unchanged. If the video has audio, a transcript may help phrase the step titles and instruction lines, but the deck still gets no speaker notes.

## Workflow

### Step 1: Structure proposal [checkpoint]

Unless the user has already fixed the structure, propose it first (title slide + one slide per step + a summary slide) and wait for the user's OK.

### Step 2: Locate elements and verify coordinates locally

For each screenshot:

1. Use visual grounding to locate every element that needs a mask or a mark, in normalized 0–1000 coordinates per image.
2. Render a **private local preview** (e.g. PIL) with the masks and marks drawn at those coordinates and **look at every preview image**. Masks especially must be widened until personal information is completely covered, including where the same information appears again in the background of a later screen.
3. Only after the previews are clean, carry the same coordinates into the deck build.

Never ship a mask you have not visually verified on the preview.

### Step 3: Build the deck

- 16:9. House style: background #F7FAFF, orange #E87A2E accent, blue #2E6BE6 hairline, Arial.
- Title slide: deck title, one-line subtitle, relation to any previous deck if it is a sequel.
- Step slides: step chip + heading (~29pt), the original screenshot fitted large, and below it an **instruction band**: a light-orange rounded band with the page's action in **large bold text (~22pt)** referencing the annotation numbers (e.g. 「作ったアカウントのメールアドレス（①）を入力して、『次へ』（②）を押す」). Add a small sub-line (~13pt) only for notes like 「※他のプロファイル名は、資料では隠しています」.
- Summary slide: the key points as large bullets (~22pt).
- **Do not write speaker notes.** If the build path creates notes pages, leave them empty and verify emptiness on read-back.
- Overlays per screenshot, in this order: image, mask rectangles (dark fill #2D2D2D, no line), ellipse outlines (no fill, red #E21E1E, ~3.5pt), numbered badges (red filled circles, white bold numbers, slightly larger than the narration version — the audience reads them at a distance) placed at the ellipse's top-left, nudged outside so the circled text stays readable.
- Number marks in click order per page; number every click point when a page has several.

Build with python-pptx, upload the.pptx to Google Drive with conversion to Google Slides (mimeType application/vnd.google-apps.presentation). When a narration version of the same content already exists, name the deck distinctly (e.g.) so the two are not confused in Drive.

### Step 4: Verify and report

Read the presentation back and check: slide count, one image per step slide, overlay shapes present (element counts), and **speaker notes empty on every slide**. Report the Slides URL and what was masked/annotated.

### Revisions

- The user will fine-tune shapes themselves; that is expected and is why overlays are shapes.
- When the user asks Muse to fix a slide, rebuild and re-upload **to the same file** (drive files update) so the link does not change — but tell the user plainly that a whole-deck re-upload overwrites any manual adjustments they already made.
- Numbering corrections from the user are applied exactly as stated; adjust the instruction text to match.

## Rules

- Never edit the original image files. All annotation lives on the slides.
- Never record or reveal personal information found in the screenshots; mask it in the deliverable and do not repeat it in chat.
- Do not upload or publish anything beyond the agreed deck without the user's OK.
- This skill is local only unless the user says otherwise: do not add it to the GitHub README (the README lists only the two skills the user chose on 2026-11-05).
