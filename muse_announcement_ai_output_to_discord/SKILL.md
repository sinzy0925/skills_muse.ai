# AIアウトプット雑談会 告知メーカー

## What this skill does

Build the weekly announcement post for the AIアウトプット雑談会 (held every Saturday at 8:00) from the fixed example text in [references/example-announcement.md](references/example-announcement.md), date it to the Saturday of the week it is created, and — after the user approves the text — post it to the Discord thread 『AIアウトプット雑談会』 in SHIFT AI オンラインコミュニティ.

Typical instruction from the user:

> muse_announcement_ai_output_to_discord を使って、今週の告知を投稿して

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Cloning this repository and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
- **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not draft or post anything.
- **B — actually use it:** Compute this week's Saturday, draft the announcement from the template, and explain using the sheet while the draft is prepared and confirmed.

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

The closing section 「💖改めてご紹介 」 and everything after it is also fixed text: reproduce it verbatim from the reference file.

## Step 1: Determine the date [重要]

The session is every Saturday at 8:00. The announcement is dated to **the Saturday of the week in which it is created**:

- Created Monday–Friday → the coming Saturday of that same week.
- Created on Saturday before the 8:00 session → that same day.
- Created on Saturday after the session, on Sunday, or whenever the user says it is for next time → the following Saturday.

Write the date into the announcement in the form 「M月D日（土）」 (for example 11月14日（土）), and use the same month number in the seasonal opening line (「M月に入り、…」). State the computed date to the user together with the draft, so a wrong week is caught before posting.

## Step 2: Draft the announcement

Start from [references/example-announcement.md](references/example-announcement.md) and change only these parts:

1. **The date**: replace 「??月??日（土）」 with the date from Step 1.
2. **The seasonal opening**: replace 「??月」 in 「??月に入り、…」 with the month number, and adapt the seasonal wording of that one paragraph to the actual season (the example text is written for November/autumn). Keep the following two lines of that paragraph as they are: 「今週も生成AIの進化が止まりません！🚀」 and 「AIで試したことや気になったことを、コーヒー片手に楽しくお話ししましょう☕️」.

Everything else — the opening lines, the fixed participation block, and the section — is reproduced verbatim. Do not add new sections, new facts or new claims to the announcement.

## Step 3: Confirm, then post

- Show the finished announcement and the date it carries to the user, and wait for their OK or corrections. Never post a draft the user has not seen.
- Before posting, check the tail of the thread: if an announcement for the same date is already posted, STOP, do not post a duplicate, and tell the user.
- The announcement is well under Discord's 2,000-character message limit: post it as a single message, keeping the paragraph breaks. If a future variant ever exceeds the limit, split it into consecutive messages without cutting sentences, and say which you did.
- If Discord is not signed in in the built-in browser, ask the user to sign in themselves and continue after they hand control back.

## Step 4: Verify and report

- After posting, confirm the announcement is visible at the end of the 『AIアウトプット雑談会』 thread.
- Report: the destination, the date used, and the posting time.
