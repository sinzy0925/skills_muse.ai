# Google Drive Inbox → Muse Storage Importer

## What this skill does

Import files (mainly large videos that cannot be attached to chat) from a dedicated Google Drive inbox folder into Muse's own storage, so the user can keep them with Muse and watch them later by just asking.

The model is a pipe and a tank: Google Drive is the **pipe** (its free space is small, so files pass through one at a time), and Muse's storage is the **tank**. The user drops a file into the Drive folder named **「Muse受け取り」**, says 「取り込んで」, and Muse fetches it into the storage folder `~/workspace/your_files/videos/`, verifies it, indexes it in `保管メモ.md` in that folder, and reports completion. Only after that report does the user delete the Drive copy by hand — Muse never deletes or moves the Drive files.

Typical instructions from the user: 「取り込んで」/「ドライブに入れたよ」 for an import, and 「○○見せて」 for playing a stored file.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run an import, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not run any connection check or fetch any file.
  - **B — actually use it:** Tell them 「Googleドライブに接続してから説明します」, then run the Google Drive connection check (share a connect link and wait if it is not connected), run the first-time setup below if it has not been done, and explain using the sheet together with the actual inbox folder and storage folder.

## Ground rules

- **Muse never deletes, moves, or renames the files in Google Drive.** Cleanup on the Drive side is always the user's own hand, after they have seen the completion report. This is a deliberate design decision （手動で確実）.
- Folder and file references are resolved **by name** at run time. No folder IDs, file IDs, or account-specific URLs are written into this skill; if an ID is resolved during a run and is worth keeping, it goes to the operator's own records (memory), never into the skill files.
- Muse's storage is a **copy**, not the only copy and not a backup service. The original stays on the user's PC. Say this once at setup, not on every run.
- Passwords and verification codes are never asked for in chat. Drive access is through the connector's own authorization.

## First-time setup (once)

1. Check the Google Drive connection. If it is not connected, share the connect link and wait.
2. Find the inbox folder by the name 「Muse受け取り」:
   - If exactly one exists, use it.
   - If several exist, ask the user which one — do not guess.
   - If none exists, create it with that name and tell the user it is ready.
3. Make sure the storage folder `~/workspace/your_files/videos/` exists, and that it contains `保管メモ.md` (create it with a header and an empty index if missing).
4. Tell the user, in one short message: put files into the 「Muse受け取り」 folder (on a PC, the Drive desktop app makes this a plain drag & drop), say 「取り込んで」 when ready, and delete the Drive copies by hand only after the completion report.

## Step 1: List the inbox

- Resolve the inbox folder by name (per setup) and list its contents with names and sizes.
- If the folder is empty, say so and stop — do not invent work.
- Report the list briefly before downloading, so the user can spot a mistake (wrong folder, wrong file).

## Step 2: Fetch and verify each file

For each file, in order:

- Download it into `~/workspace/your_files/videos/` with the Google Drive connector.
- If a stored file with the **same name** already exists:
  - Same name and same size → treat it as already imported: skip the download and note it in the report.
  - Same name but different size → do not overwrite; ask the user how to handle it.
- Verify the copy: the local file size must match the size reported by Drive. For video files, also read the duration (e.g., with ffprobe) and keep it for the index.
- If a download fails or the sizes do not match, stop that file, report it plainly, and continue with the next file only if the user agrees. Never report an unverified file as imported.

## Step 3: Index and report

- Append one line per newly imported file to `保管メモ.md`: file name, size, duration (for videos), import date, and a short description. The description comes from the user when they gave one; otherwise use the file name and let the user rename it later.
- Report completion to the user: for each file, its name, size, and duration. End with the reminder that the Drive copies can now be deleted by hand.
- The report is the user's signal to clean the pipe. Do not delete anything yourself, and do not chase the user about deleting.

## Showing a stored file （「○○見せて」)

- When the user asks to see a stored file, find it in `保管メモ.md` / the storage folder. If the name is vague and several files could match, ask which one — do not guess.
- Reply with one short line and the file attached. Watching/playing the file in the app uses no tokens on the user's side; keep the reply itself short for the same reason.
- Renaming a stored file (「○○を△△に変えて」) is done on request: rename the file and update `保管メモ.md` to match.

## Cautions

- Very large files take time to upload to Drive and to fetch; say so plainly instead of promising speed. One file at a time is the normal rhythm because of Drive's free quota.
- A missing inbox folder after setup usually means the user put the file somewhere else or under a different account; ask, do not search the whole Drive silently.
- Never present this storage as a professional backup. If the user is about to delete the only other copy, remind them once of the copy-not-backup rule above.
