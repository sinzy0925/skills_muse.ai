# Daily SNS Posting Workflow

Run one posting cycle for a brand account on Instagram and Threads from a stock of ready-made materials: prepare the next Instagram item and the next Threads text, present a final confirmation, and publish only after the user approves.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any settings or prepare anything.
  - **B — actually use it:** On first use, collect the one-time operator settings first (the target Instagram and Threads accounts, the material source folder, the posting order and progress record, and the output folders), then explain using the sheet. When settings already exist, explain using the sheet and the current progress state.

## Configuration

- Read the operator settings before starting: the target Instagram and Threads accounts, the source folder that holds the materials, the posting order, the progress record, and the folders where prepared files are saved. The operator supplies these values from their own records.
- Keep this file free of account names, post URLs and schedules when sharing it. Those values belong in the operator's own records, not in the skill.
- Treat any schedule as external to this skill. A scheduler may invoke this workflow, and the skill itself carries no time or frequency.

## Hard rules

- Publish only after showing the user a preview and receiving their explicit approval for that exact content. Never publish on preparation alone.
- Post only to the designated brand account from the configuration. Never post this material to a personal account.
- Use Threads texts verbatim from the source file. Never reword, shorten or decorate them.
- Never invent specifics that are not in the material, such as tool names, app names, prices or earnings figures, in a caption or anywhere else.
- Never prepare or publish the same item twice. Decide what is next from the live published state, not from the plan alone.

## Determine the next pair

- Check the actual published posts on both platforms first, using the Instagram and Threads connector docs for the exact commands.
- Compare the published state with the recorded posting order and progress to pick the next Instagram item and the next Threads text.
- Follow the configured default variant when a video has several versions, such as a female and a male version. When the default variant is missing for the next item, prepare with the available variant only if the user agrees, and ask before substituting.
- Skip preparation and report briefly when today's pair is already published.

## Prepare the Instagram item

- Download the target video or images from the configured source folder in Google Drive.
- Compress a reel to at most 100 MB with `muse.exec` and ffmpeg, keeping 1080x1920 and the original length. Use a video bitrate near 10.5 Mbps as the starting point, with AAC audio at 128k and faststart enabled.
  - A proven recipe: `ffmpeg -i <input> -c:v libx264 -preset slow -b:v 10500k -maxrate 12000k -bufsize 24000k -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart <output>`
  - Skip compression when the source file is already at most 100 MB.
- Use the material's own title image as the cover. Every posted video needs a cover image.
- Extract frames from the prepared video and confirm the burned-in subtitles stay readable after compression.
- Order a carousel as cover, introduction, numbered content slides, then closing slide. Make every slide the same aspect ratio and pixel size before posting.
- Save prepared files in the configured output folders, following the naming pattern already used there.

## Write the caption

- Follow the established caption pattern used by earlier posts on the account:
  - Open with a short hook that introduces the item's title.
  - Say what the reel or carousel collects, in one line.
  - Add three check-marked bullet points drawn only from what the material actually shows.
  - Recommend saving the post to look back later.
  - Introduce the account with three short lines: what the account posts about, its practical topics, and the offer or community it guides readers to.
  - Invite the reader to follow for the next post.
  - Invite questions by comment or DM.
  - Close with about ten hashtags that match the material's theme.

## Present the final confirmation

- Show the destination accounts, what the video or images contain, the compression result and file size, the cover image, the full caption, and the full Threads text.
- Attach reply options for: publish both as shown, Instagram only, Threads only, or do not publish yet.
- State clearly that nothing has been published yet.

## Publish and verify

- Publish only the parts the user approved, using the Instagram and Threads connector docs for the exact commands, flags and approval behavior.
- Read the published items back from each platform's post list and confirm they are public.
- Report the result briefly with the two post URLs, and record the progress in the operator's records so the next cycle picks the following pair.
- Stop the affected kind of write for the day when a platform returns a 429 rate limit, and report what remains unpublished.

## Pitfalls

- Judge the Threads published count from the actual post list. A profile post count can read higher than the real number of posts.
- Check the live account state again before publishing when approval arrives much later than the preparation, because the plan may have shifted.
- Treat connector documentation updates as authoritative. Reread the current Instagram and Threads connector docs before publishing when they have changed.

## Available connectors

- Instagram: read `/opt/hatch/connectors/instagram/CONNECTOR.md` for accounts, reads and publishing.
- Threads: read `/opt/hatch/connectors/threads/CONNECTOR.md` for accounts, reads and publishing.
- Google Drive: read `/opt/hatch/connectors/google_drive/CONNECTOR.md` for finding and downloading source materials.
