# AIアウトプット雑談会 議事録メーカー

## What this skill does

Turn the transcript （議事内容の文字起こし） of an AIアウトプット雑談会 session into two deliverables and post each to its own destination, after the user approves the texts:

1. **新議事録** (short meeting minutes) **with the supplied image** → the Discord thread 『AIアウトプット雑談会』
2. **超簡単議事録** (super-simple report) **as text only** → 『サークル開催報告』 in the #サークルリーダー交流 channel

Typical instruction from the user:

> 議事内容を要約した上で、添付の画像と一緒に
> 1. SHIFT AIの🧑‍💻サークルにある『AIアウトプット雑談会』に新議事録と画像を投稿して
> 2. SHIFT AIの＃サークルリーダー交流にある『サークル開催報告』に超簡単議事録を文章のみ投稿して

## Posting targets

Both are in the server SHIFT AI オンラインコミュニティ, posted via Muse's built-in browser with the user already signed in to Discord as themselves (display name タロ.AI). The login is done by the human in advance; never ask for the password or any code in chat.

1. **Minutes + image**
   - Forum channel: 🧑‍💻サークル
   - Thread: 『AIアウトプット雑談会』
   - Thread URL: https://discord.com/channels/1390567808148045907/1498124068845654168
2. **Super-simple report, text only (no image)**
   - Channel: ＃サークルリーダー交流
   - Thread/topic: 『サークル開催報告』
   - Thread URL: https://discord.com/channels/1390567808148045907/1541255290467389450 (confirmed 2026-11-04: the only thread with this name in ＃サークルリーダー交流)

## Step 1: Validate the input before writing anything [重要]

Check that the user's input (the transcript or the accompanying message) contains all four of these:

1. 今日の日付 (the date of this session)
2. 来週の日付 (the date of the next session)
3. 今日の参加人数 (today's participant count)
4. 新規参加人数 (the number of first-time participants)

If any one of them is missing, STOP. Do not draft anything and do not post. Tell the user exactly which item is missing and ask them to supply it.

## Step 2: Write the new minutes （新議事録）

- Base the new minutes on the transcript, using the previous minutes in [references/previous-minutes.md](references/previous-minutes.md) only as a reference for structure and tone.
- **Keep it short and simple.** The previous minutes are long; the new one must be much shorter and plainer than that example. Cut detail aggressively: topics and conclusions, not a retelling.
- End the minutes with the next meeting schedule （次回予定）.
- Never invent facts, names, numbers or topics that are not in the transcript.
- Destination: the 『AIアウトプット雑談会』 thread, posted together with the image the user supplied.

## Step 3: Write the super-simple report （超簡単議事録）

Always produce this second format as well, filled from the same material:

```
━━━━━━━━━━━━━━━━━━━━
📝サークル開催報告
■サークル名：ＡＩアウトプット雑談会
■開催日： YYYY/MM/DD
■参加者数： ？？人
■新規参加者数：？人
■内容：
■感想：
■特に報告したい目新しい内容：
■次回予定：YYYY/MM/DD
━━━━━━━━━━━━━━━━━━━━
```

- ■特に報告したい目新しい内容： do NOT force an entry. Fill it only when the session contained something genuinely novel — a topic that sounds first-of-its-kind or innovative, or something with especially wide practical use. Otherwise leave it blank or write なし.
- Destination: 『サークル開催報告』 in #サークルリーダー交流, posted as **text only — never attach the image to this one**.

## Step 4: Confirm, then post

- Show the finished minutes and the super-simple report to the user and wait for their OK or corrections before posting. Never post a draft the user has not seen.
- After the OK, post in this order:
  1. Minutes **with the supplied image attached** → 『AIアウトプット雑談会』 thread (🧑‍💻サークル)
  2. Super-simple report, **text only** → 『サークル開催報告』 (#サークルリーダー交流)
- Discord messages are limited to 2,000 characters: if a text is longer, split it into consecutive messages without cutting sentences, or attach it as a file — and say which you did.
- After posting, confirm each post is visible at the end of its destination and report the result (both destinations, times, and that the image went only to the minutes post).
