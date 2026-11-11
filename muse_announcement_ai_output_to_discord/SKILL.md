# AIアウトプット雑談会 告知メーカー

## What this skill does

Build the weekly announcement post for the AIアウトプット雑談会 (held every Saturday at 8:00), date it to the Saturday of the week it is created, and — after the user approves the text — post it to the Discord thread 『AIアウトプット雑談会』 in SHIFT AI オンラインコミュニティ. The announcement's wording is written fresh each time, using the example text in [references/example-announcement.md](references/example-announcement.md) as the reference for structure, tone and content. The only fixed text is the Zoom participation block (see below), which is reproduced exactly and never changed.

Typical instruction from the user:

> muse_announcement_ai_output_to_discord を使って、今週の告知を投稿して

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Cloning this repository and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
- **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not draft or post anything.
- **B — actually use it:** Compute this week's Saturday, draft the announcement (wording written fresh each time; only the Zoom block is fixed), and explain using the sheet while the draft is prepared and confirmed.

## Posting target

- Server: SHIFT AI オンラインコミュニティ
- Forum channel: 🧑‍💻サークル
- Thread: 『AIアウトプット雑談会』
- Thread URL: not written in this skill. Look it up in Muse's own memory (kept locally, outside this skill) or ask the user.
- Posting is done via Muse's built-in browser, with the user already signed in to Discord as themselves (display name タロ.AI). The login is done by the human in advance; never ask for the password or any code in chat. No webhook or bot: the user is not a server admin, so posting as themselves in the browser is the route.

## Fixed content — never change [絶対に変更禁止]

The participation block below must appear in every announcement **exactly as written** — the URL, the meeting ID and the passcode, character for character, including the brackets. Never retype it from memory in a way that could alter a digit; copy it from this skill or from the reference file.

```
参加はこちらから😄
【https://us06web.zoom.us/j/84933352139?pwd=euZBMSSkbyDEhDjtYM38jCcgOn2DAN.1#success】 　
ID: 849 3335 2139 　
パスコード: 343996
```

This block is the **only** fixed text in the announcement. Everything else — the opening, the seasonal greeting and the 【AIアウトプット雑談会とは？】 introduction — is rewritten each time (see Step 2).

## Step 1: Determine the date [重要]

The session is every Saturday at 8:00. The announcement is dated to **the Saturday of the week in which it is created**:

- Created Monday–Friday → the coming Saturday of that same week.
- Created on Saturday before the 8:00 session → that same day.
- Created on Saturday after the session, on Sunday, or whenever the user says it is for next time → the following Saturday.

Write the date into the announcement in the form 「M月D日（土）」 (for example 11月14日（土）), and use the same month number in the seasonal opening line (「M月に入り、…」). State the computed date to the user together with the draft, so a wrong week is caught before posting.

## Step 2: Draft the announcement

Write the announcement **fresh each time**, using [references/example-announcement.md](references/example-announcement.md) as the reference for structure, tone and content — not as text to copy. The only part reproduced exactly is the fixed Zoom block above.

The draft must include:

1. The event name 「AIアウトプット雑談会」 and an opening hook in the example's cheerful style.
2. The date from Step 1, in the form 「M月D日（土）朝8時から開催です」.
3. A **short** seasonal greeting, newly written by you each time to fit the month and season: about 3 lines, in the example's shape (a seasonal line, a line about AI moving fast, and an invitation to chat over coffee). Keep it brief.
4. The fixed participation block, verbatim.
5. A short introduction of what the gathering is, headed 「💖改めてご紹介」, covering the example's points in fresh wording: every Saturday at 8:00; then 「AIを学んでいて、こんなモヤモヤはありませんか？」 followed by these five worries, each as one short quoted line — 「続けたいのにモチベーションが保てない」「AIツールが多すぎて、どれを使えばいいか迷う」「アウトプットしたいけど、何から始めたらいいか分からない」「勉強ばかりしても、すぐに忘れるから、アウトプットして記憶にとどめたい」「最新のツールに興味がある。具体的に聞いてみたい事がある」; then small breakout rooms where you can talk lightly and find hints and new perspectives; any form of output is OK （インスタ、X、YouTube、文章、画像、仕事の工夫）; a welcoming close.

Keep the whole text friendly, in the example's spirit (light emoji use is fine), and about the same length as the example — it must stay well under Discord's 2,000-character limit so it posts as one message. Do not invent facts or claims that are not in the example: no invented session topics, guests, or campaigns.

## Step 3: Confirm, then post

- Show the finished announcement and the date it carries to the user, and wait for their OK or corrections. Never post a draft the user has not seen.
- Before posting, check the tail of the thread: if an announcement for the same date is already posted, STOP, do not post a duplicate, and tell the user.
- The announcement is well under Discord's 2,000-character message limit: post it as a single message, keeping the paragraph breaks. If a future variant ever exceeds the limit, split it into consecutive messages without cutting sentences, and say which you did.
- If Discord is not signed in in the built-in browser, ask the user to sign in themselves and continue after they hand control back.

## Step 4: Verify and report

- After posting, confirm the announcement is visible at the end of the 『AIアウトプット雑談会』 thread.
- Report: the destination, the date used, and the posting time.
