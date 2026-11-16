# Post to X via Muse from Meta

Post to X (text, with an optional image, video or GIF attachment, plus optional follow-up replies) from the X account that is logged in on the user's own PC Chrome through the Muse from Meta extension. The built-in browser cannot log in to X, so it is never used for this skill. The post text is always confirmed by the user first, and whether an attachment is needed is always asked.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any settings or prepare anything.
  - **B — actually use it:** On first use, check the one-time prerequisites first (the Muse from Meta extension is installed in the PC's Chrome and X is logged in there — the login itself is done by the user), then explain using the sheet and the actual post being prepared. When the prerequisites are already in place, explain using the sheet and the current draft.

## Configuration

- This skill holds no account name, username, post URL or schedule. The posting account is whichever X account is logged in on the user's PC Chrome at run time; read it from the screen and tell the user if it is not the account they expect.
- The attachment file is designated by the user for each post. Nothing about past posts is stored in the skill.

## Hard rules

- **Never use the built-in (cloud) browser for X.** It cannot log in to X (the login fails there), so posting from it is impossible. Always post through the PC's Chrome via the Muse from Meta extension (the device browser), and say so explicitly when delegating the browser work, because the default browser may not be the PC Chrome.
- **Never post without the user's explicit OK for the exact final text.** Show the full text (and the attachment, when there is one) before posting. A draft, a plan, or approval of an earlier version is not approval.
- **Always ask whether an attachment is needed** (none, image, video or GIF) and which file, before posting. Never attach a file the user did not designate.
- **Never enter credentials.** If X is not logged in on the PC Chrome, stop and ask the user to log in themselves. Never ask for a password or a code in chat.
- **Verify every post.** After posting, confirm the post is actually visible and get its URL before doing anything else. If whether a post was submitted is unclear, do not post the same content again — verify the actual state first.
- **Never accept X Premium (paid plan) offers** that appear during posting. Dismiss them and continue; never sign up or pay.
- Post one item at a time: main post first, then each confirmed reply in order, verifying each before the next.

## Free-account limits to check before posting

- Text: 280 weighted characters per post. Japanese characters count as 2, a URL counts as 23. If the text is over, propose splitting it into consecutive replies (a thread) or shortening it, and get the user's OK for the split before posting.
- Video: at most 140 seconds and 512 MB, MP4 (H.264 video + AAC audio).
- GIF: at most 15 MB on the web (5 MB in the mobile apps).
- Photo: at most 5 MB.
- Report any limit problem before posting, never after.

## Flow

1. **Draft and confirm the text.** Prepare the post text, show it in full, and get the user's explicit OK. Apply any edits and re-show the final version when it changes.
2. **Ask about the attachment.** Ask whether to attach a file; if yes, have the user designate the file (or pick from files already in the workspace, with their OK).
3. **Check the limits.** Check the text length and the attachment's type, length and size against the free-account limits above. If something is over, propose the fix (split replies, trim, recompress) and confirm before proceeding.
4. **Confirm follow-up replies, if any.** When the user wants replies under the post (for example, instructions in the comments), confirm each reply's full text the same way as the main post, including any split needed for the character limit.
5. **Post via Muse from Meta.** Delegate the posting to a browser task on the PC Chrome (device browser), stating explicitly: this is the PC's Chrome through Muse from Meta, not the built-in browser; the X account is already logged in there; no credentials are to be entered. Include the exact approved texts and the designated attachment file, and instruct the browser to verify each post is visible and to return the post URL.
6. **Report.** Tell the user the main post's URL and what was posted (main post and each reply), including anything that was split or skipped and why.

## If something stalls

- If a screen makes no progress, do not force it: stop that item, say what happened, and ask the user. The exception is a post whose submission state is unknown — verifying whether it went through always comes first, and the same content is never sent twice.
- If the PC Chrome is unavailable or X is logged out there, stop and tell the user what is needed (open the PC Chrome, or log in to X there themselves). Do not fall back to the built-in browser.
