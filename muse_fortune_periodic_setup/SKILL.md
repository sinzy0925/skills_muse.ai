# Fortune Periodic Setup

## What this skill does

Set up, change, or stop a **recurring (periodic) run** of the five combined fortune-telling skills:

- `muse_fortune_shichusuimei_tarot` （四柱推命 × タロット）
- `muse_fortune_kyusei_runes` （九星気学 × ルーン）
- `muse_fortune_numerology_tarot` （数秘術 × タロット）
- `muse_fortune_astrology_oracle` （西洋占星術 × オラクルカード）
- `muse_fortune_kyusei_shichusuimei_daily` （九星気学 × 四柱推命・デイリー）

This skill does **not** perform any reading itself. It only handles the scheduling: proposing the setup items, collecting the person's answers, registering the recurring job after their OK, and later updating or removing that same job. Each actual reading is done by the fortune skill named for that day, following that skill's own SKILL.md.

Typical instruction from the user: words like 「占いを定期実行したい」「毎朝占いを届けて」 — or the execution sentence copied from the fortune launcher （占いランチャー）, whose only role for scheduling is to call this skill.

Design source: the operator's design confirmed on 2026-11-17 — the launcher keeps only the choice of fortune; all scheduling setup moves into this skill's dialogue, because form input on a static launcher page is not preserved.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start a setup, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any setup items and do not register anything.
  - **B — actually use it:** Tell them 「入力項目を確認してから説明します」, then collect the setup items of Step 1 (execution pattern, timing, image option, birth information, destination chat), and explain using the sheet together with how those items will be used, before starting the setup.

## Ground rules

- **No reading in this skill.** Never draw cards, runes or oracle cards, and never compute a chart here. This skill only schedules the skills that do.
- **OK before registration.** Never create, update, or delete a recurring job before showing the setup summary and getting the person's explicit OK (Step 2).
- **One job, no duplicates.** Before registering, list the existing scheduled jobs and check for an existing fortune periodic run. If one exists, adopt it under this skill's management and update that job — never create a second overlapping job.
- **Privacy.** Birth dates, birth times and birth places are personal data. They are held only inside the person's own recurring job body, where the daily runs need them. Never write them into the skill files, shared materials, the fortune launcher, or any saved note.
- **No specific identifiers in this skill.** This skill text contains no chat IDs, job IDs, folder IDs, personal names, or personal dates. At setup time, resolve the destination chat and the job from the live conversation and the job list, never from this file.
- **No outward sending.** A recurring fortune run never sends anything to LINE (that integration is on hold), and never posts to social media without the person's approval for that post. Readings are delivered only to the destination chat of Step 1-E.
- **Launcher scope.** This skill is not registered in the general skill launcher; it belongs to the fortune launcher （占いランチャー） set, like its sibling fortune skills.

## Step 1: Present the setup proposal and collect the answers

Present all of the following items together as one proposal, with the standard defaults shown, and ask the person to answer them in one go. If anything is missing afterwards, ask for all missing items in one message — never guess.

**A. Execution pattern （実行パターン）**
Standard proposal — weekday rotation （曜日ローテーション）:
- 月曜：西洋占星術 × オラクル (`muse_fortune_astrology_oracle`)
- 火曜：九星気学 × ルーン (`muse_fortune_kyusei_runes`)
- 水曜：数秘術 × タロット (`muse_fortune_numerology_tarot`)
- 木曜：四柱推命 × タロット (`muse_fortune_shichusuimei_tarot`)
- 金曜：九星 × 四柱デイリー (`muse_fortune_kyusei_shichusuimei_daily`)
- 土曜：全部まとめて (all five, woven into one weekly summary — not five full texts in a row)
- 日曜：九星 × 四柱デイリー (`muse_fortune_kyusei_shichusuimei_daily`, light version)

The consultation theme for skills that need one is fixed to 「今日の全体運」 as the standard. Say that a single fixed fortune, or swapping individual weekdays, is also possible.

**B. Execution timing （実行タイミング）**
Daily, at what time? Show 8:00 as the standard candidate.

**C. Image （イメージ化）**
Ask whether they want an image. When asking, always show this warning exactly as written:
「画像を毎日生成するとトークンを多めに消費しますよ！」
Only if they say yes: the image is one per day (on Saturday's all-together run, one representative image), generated by the Muse that runs that day's reading, and ask the mood — クール・かっこいい／かわいい／静か. If they say no, the runs are text only.

**D. Required information （必要情報）**
- **生年月日** (required)
- **出生時刻** (optional — if unknown, the skills that use it run their simplified version)
- **出生地** (optional — used by the astrology skill; if unknown, it runs its simplified version)

**E. Destination （届け先）**
The chat where this setup conversation is happening (expected to be the fortune chat). Readings are delivered there and nowhere else.

## Step 2: Summarize and get the OK

Show a compact summary of the chosen pattern, timing, image setting, birth information as entered, and destination chat. Register nothing until the person gives an explicit OK. If they change an item at this point, update the summary and confirm again.

## Step 3: Check for an existing fortune periodic run

List the existing scheduled jobs. If a fortune periodic run already exists (for example, a weekday rotation registered before this skill existed), adopt that job under this skill's management: from now on it is the job this skill updates or removes, and Step 4 updates it instead of creating a new one. Tell the person plainly that the existing run was adopted rather than duplicated.

## Step 4: Register the recurring job

After the OK, create (or update, if adopted) one recurring job that fires daily at the chosen time in the person's timezone. Write the job body so that each run:

- Determines the weekday in the person's timezone and runs the fortune skill named for that weekday in the chosen pattern (Saturday: all five, integrated into one weekly summary).
- Uses the fixed theme 「今日の全体運」 for the skills that take a theme (unless a different fixed theme was chosen in Step 1).
- Carries the birth information from Step 1-D **in the job body only**, marked as private to that job, with an instruction not to copy it into skill files, shared materials, or saved notes.
- First reads the SKILL.md of the skill it is about to run and follows it, including its bundled helper: if that helper's self-test does not print `SELFTEST: ALL OK`, that day's reading is not produced and the failure is reported briefly instead. No hand calculation and no guessing.
- Draws lots (tarot / runes / oracle) only once per question, with no re-draws.
- Keeps the tone gentle and encouraging （優しく背中を押す）, and never gives definitive judgments on health, law, or money.
- If images were chosen in Step 1-C: generates exactly one image for that day, in the chosen mood, made by the Muse running the reading.
- Sends nothing to LINE, and posts nothing to social media without approval.
- Delivers the reading to the destination chat from Step 1-E, opening with the date, the weekday, and the name of the fortune that ran.

## Step 5: Verify, refresh the task meter, and report

- Read the saved job back and confirm its schedule matches the OK'd summary.
- Trigger a re-measurement of the task meter space （タスクメーター） so the new or updated job appears there, following the standing rule that every new or changed scheduled task goes into the task meter.
- Report to the person: that the setup is registered (or adopted), the daily time, and the **next run** — its date, weekday, and which fortune will run.

## Step 6: Change or stop

- **Change** (time, rotation, image setting, theme, destination): show the changed summary, get the OK, then update the *same* job — never add a second one — refresh the task meter, and report the next run under the new settings.
- **Stop**: after confirmation, delete (or disable) that same job, refresh the task meter, and report that the periodic run has stopped and nothing further will be delivered.

## Cautions

- The Saturday all-together run is the heaviest of the week (five skills in one run). If the person is concerned about consumption, propose the image only for Saturday, or dropping Saturday to a single fortune, as lighter alternatives — but change nothing without their answer.
- A recurring run cannot ask questions each morning; that is why the theme is fixed in Step 1. If the person wants a different theme on a given day, that is a separate one-off reading in chat, not a change to the job, unless they ask to change the fixed theme itself.
- If the destination chat cannot be resolved at setup time, stop and ask rather than registering a job that delivers nowhere.
