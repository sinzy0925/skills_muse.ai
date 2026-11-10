# Google Drive mp4 → YouTube Uploader

## What this skill does

Upload an mp4 that lives in the user's Google Drive to YouTube, without the file ever being downloaded to the user's own device. The file travels: Google Drive → Muse (a working copy) → YouTube Studio in Muse's built-in browser → YouTube.

Typical instruction from the user: a Google Drive file name or link/URL for the mp4, plus words like 「YouTubeにアップして」.

Source procedure: the user's deck 「Googleドライブのmp4をYouTubeにアップする方法」 (Google Slides, 14 pages).

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Cloning this repository and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start an upload, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not run any connection check or fetch any file.
  - **B — actually use it:** Tell them 「Googleドライブに接続してから説明します」, then run the Google Drive connection check (share a connect link and wait if it is not connected), identify the mp4 the operator names, and explain using the sheet together with that file's details before confirming the upload settings.

## Ground rules

- The Drive original is never modified or deleted. Work on a copy fetched into the workspace.
- Passwords, verification codes: never ask the user to send them in chat. Sign-in happens in the built-in browser through the secure entry, operated by the user; 2FA is approved on the user's phone.
- The Drive connection and the browser's YouTube login are separate things. The first run needs both.
- No CDP or scripting of the browser is needed; use the normal built-in browser flow.

## Step 1: Identify and fetch the mp4

- From a Drive link, identify the file; from a file name, search Drive. If several files match, ask the user which one — do not guess.
- Download a copy into the workspace with the Google Drive connector (`files get` with `alt: media` to a local path).
- Check the copy: duration, format, file size. Report them briefly.
- If the file is very large, warn before continuing: browser uploads can take a long time or fail midway.

## Step 2: Confirm the required items with the user

Before uploading anything, confirm the items below with the user, asking for every missing one in a single message:

- **タイトル** (required — never invent one silently; a draft suggestion is fine)
- **公開範囲** (required: 公開 / 限定公開 / 非公開, or 予約公開 with a date and time)
- **投稿先チャンネル** (the default channel, or a named one if the user has several)
- **子ども向けかどうか** (required by YouTube's audience setting)
- 説明文 (optional — if the user wants one and provides material, draft it and show it before use)
- サムネイル (optional — an image the user supplies or approves)

Do not start the upload until at least the title and visibility are fixed.

## Step 3: Open YouTube Studio and sign in

- Open YouTube Studio in Muse's built-in browser (it is separate from the user's own browser).
- If sign-in is needed, hand the browser to the user to sign in through the secure entry. If a verification code, a "no channel yet" situation, or an identity check appears, only the step that needs the user is theirs (e.g., creating a channel is the user's action); explain briefly and wait.

## Step 4: Upload the mp4

- In Studio, choose 作成 → 動画をアップロード and send the working copy fetched in Step 1.
- Wait for the upload and processing to finish; report progress honestly if it stalls or fails.

## Step 5: Set the details and publish

- Enter the title, description and thumbnail confirmed in Step 2.
- Answer the audience setting （子ども向けかどうか） and set the visibility exactly as confirmed.
- **Before pressing publish, show the user the final settings (title, channel, visibility) and get an explicit OK.** Publishing is the one step that must never happen unconfirmed.

## Step 6: Verify and clean up

- After publishing, take the video URL and check that the video opens (or confirm its state in Studio's video list).
- Report to the user: the video URL, the channel, the title and the visibility actually set.
- Ask whether to delete the working copy of the mp4 from the workspace; delete it only if the user says yes. The Drive original stays untouched either way.

## Cautions

- Very large files may take long or fail over a browser upload; say so plainly and offer alternatives (e.g., splitting, or a manual upload) instead of retrying silently.
- Keep the user's confirmations verbatim: title, visibility and channel come from the user, not from assumptions or from an earlier video's settings.
