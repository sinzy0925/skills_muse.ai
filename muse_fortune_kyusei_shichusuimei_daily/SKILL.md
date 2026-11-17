# Kyusei × Four Pillars Daily Reading

## What this skill does

Give one short **daily** fortune reading that combines two calculation-based methods with fixed roles. Nothing is drawn by lot in this skill — both sides are computed, so the same person on the same day always gets the same result.

- **四柱推命 (Four Pillars)** — the day-level flow: the person's natal chart （日主 day master and five-element balance) set against the target day's pillars, above all the day pillar.
- **九星気学 (Kyusei Kigaku)** — the month/year-level flow: the person's 本命星 and 月命星 set against the current year's star and the current month's board star （月盤中宮）.

The helper pre-computes the element relations （相生・相剋・比和・漏気・制気） between the two systems, and the reading weaves them into a compact five-part daily message (§ Step 3). The tone is gentle and encouraging; the reading never frightens.

Typical instruction from the user: a birth date (once) and words like 「今日の運勢」 — the target day defaults to today.

Design source: the operator's combined-fortune design (daily type; 日盤 and direction readings are out of scope in v1; decisions confirmed by the user on 2026-11-17). This skill is a sibling of `muse_fortune_shichusuimei_tarot` （四柱推命 × タロット) and `muse_fortune_kyusei_runes` （九星気学 × ルーン) and follows the same ground rules.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start a reading, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any birth data and do not run a reading.
  - **B — actually use it:** Tell them 「入力項目を確認してから説明します」, then collect the input items of Step 1 (birth date, birth time if known), and explain using the sheet together with how those items will be used, before starting the reading.

## Ground rules

- **Everything is computed, never remembered or guessed.** All arithmetic goes through the bundled helper `references/daily_tools.py` (which uses the sxtwl library). Its output — pillars, stars, and the element relations it prints — is used verbatim. Never compute a pillar, a star, or a relation by hand, and never "correct" the helper's output from memory.
- **Entertainment framing.** A reading is entertainment and a thinking aid. Never give definitive judgments on health, law, or money (investments, loans); if a worry the person mentions touches those, add a line suggesting a professional. Never use frightening phrasing （〜しないと不幸になる, deadlines of doom, curses). When difficult material appears, always pair it with a way forward.
- **Privacy.** Birth dates and times are personal data: use them only for that reading. Never write them into the skill files, shared materials, or any saved note.
- **Missing inputs are asked, not guessed.** If a required item is missing, stop and ask for all missing items in one message.

## Step 1: Collect the inputs

- **生年月日** (required)
- **出生時刻** (optional — if unknown, the chart is computed without the hour pillar and the reading's basis says so; the daily result itself does not depend on it)
- **対象日** (optional — default today; 明日・明後日なども可）
- **気になること** (optional — one line, e.g. 仕事の会議. If given, the lucky action and the care point lean toward it)

相談テーマ as a required item is NOT collected — this is the daily type, not the question type.

## Step 2: Compute and verify the daily materials

Run everything with a Python environment that has sxtwl installed (`pip install sxtwl` if missing; if it cannot be installed or run, stop and report — do not fall back to hand calculation).

1. **Self-test first** (once per environment, before the first real reading):
   `python references/daily_tools.py selftest`
   It checks Four Pillars anchors, Kyusei anchors, the month board, and the element-relation table. If it does not print `SELFTEST: ALL OK`, stop and report; do not produce a reading on an unverified calculation.
2. **Compute the materials:**
   `python references/daily_tools.py daily YYYY-MM-DD [HH:MM] [TARGET-DATE]`
   Use its output verbatim: the natal pillars, day master and element balance; the 本命星・月命星； the target day's pillars; the year's and month's Kyusei stars; and the three printed element relations.

## Step 3: Compose the daily reading

Write the reading in this fixed structure, compact by design (about 400–500 characters overall):

1. **今日のデータ** — the date, the day's pillar, and the person's day master / 本命星 with the month's star, in one or two lines
2. **今日の運気** — the day's flow woven from the printed relations: the day pillar vs the day master (today's main weather), grounded by the month star vs the 本命星 (this month's background)
3. **ラッキーアクション** — 1–2 small, concrete things that fit today's flow (and the 気になること, if given)
4. **気をつけること** — exactly one care point, framed as care plus a way through, never as a warning of doom
5. **締めの一言** — one short, encouraging sentence

Keep the tone gentle and encouraging throughout. A 相剋 day is read as "a day to go carefully and keep margins", never as a bad day fated to go wrong.

## Step 4: Present

- Present the reading as composed. Asking again for the same day gives the same result (it is a calculation, not a draw) — say so plainly if asked.
- A different target day is a fresh run of Step 2 with that date.

## Cautions

- **日盤 (the day-level Kyusei board) and 方位 (lucky directions) are out of scope in v1.** The daily angle comes from the Four Pillars day pillar; Kyusei covers the year and month. If asked for a lucky direction, say plainly that this version does not cover it; do not improvise one.
- The five-element balance counts only the visible stems and each branch's main element （蔵干 is not counted) — the v1 simplification inherited from the sibling skill. 大運 is also out of scope.
- Readings for a third party use only the information given; do not embellish the person's profile beyond the inputs.
