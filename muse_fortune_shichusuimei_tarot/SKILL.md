# Four Pillars × Tarot Reading

## What this skill does

Give one integrated fortune reading that combines two methods with fixed roles:

- **四柱推命 (Four Pillars)** — the foundation: the person's inborn tendencies, five-element balance, and the broad flow of the current year, from their birth date (and birth time, if known).
- **タロット (Tarot)** — the answer for right now: three cards drawn by random lot for the person's actual question — 現状 (present), 課題 (challenge), 助言 (advice).

The two are woven into a single reading in a fixed seven-part structure (§ Step 4). The tone is gentle and encouraging; the reading never frightens.

Typical instruction from the user: a birth date (birth time if known) and a question or theme, plus words like 「占って」.

Design source: the operator's design memo for this combined reading (roles fixed as above; no 大運 in v1; decisions confirmed by the user on 2026-11-14).

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start a reading, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any birth data and do not draw any cards.
  - **B — actually use it:** Tell them 「入力項目を確認してから説明します」, then collect the input items of Step 1 (birth date, birth time if known, the question/theme), and explain using the sheet together with how those items will be used, before starting the reading.

## Ground rules

- **The pillars are computed, never remembered or guessed.** All pillar arithmetic goes through the bundled helper `references/fortune_tools.py` (which uses the sxtwl library). Its output is used verbatim. Never compute a day pillar by hand, never "correct" the helper's output from memory, and never invent a pillar.
- **Entertainment framing.** A reading is entertainment and a thinking aid. Never give definitive judgments on health, law, or money (investments, loans); if the question touches those, add a line suggesting a professional. Never use frightening phrasing （〜しないと不幸になる, deadlines of doom, curses). When difficult material appears, always pair it with a way forward.
- **Privacy.** Birth dates and times are personal data: use them only for that reading. Never write them into the skill files, shared materials, or any saved note.
- **No re-draws.** The tarot draw happens once per question. If the person asks a genuinely new question, that is a new reading with a new draw; the same question is never re-drawn to get a "better" result.
- **Missing inputs are asked, not guessed.** If a required item is missing, stop and ask for all missing items in one message.

## Step 1: Collect the inputs

- **生年月日** (required)
- **出生時刻** (optional — if unknown, the reading runs as a simplified three-pillar version without the hour pillar, and says so in the output)
- **相談テーマ／質問** (required — a theme such as 仕事・恋愛・お金・人間関係, or a free-form question)
- **鑑定の長さ** (optional — default 標準； 短め / じっくり also possible)

出生地 and 性別 are not collected in v1 （大運 and true-solar-time correction are out of scope).

## Step 2: Build and verify the Four Pillars chart

Run everything with a Python environment that has sxtwl installed (`pip install sxtwl` if missing; if it cannot be installed or run, stop and report — do not fall back to hand calculation).

1. **Self-test first** (once per environment, before the first real chart):
   `python references/fortune_tools.py selftest`
   It checks 12 published anchor charts, including the 立春 year/month boundaries. If it does not print `SELFTEST: ALL OK`, stop and report; do not produce a reading on an unverified calculation.
2. **Compute the chart:**
   `python references/fortune_tools.py meishiki YYYY-MM-DD [HH:MM]`
   (omit the time if unknown). Use its output verbatim: the pillars, the 日主 (day master), the five-element balance (counted from the heavenly stems and the main element of each earthly branch), and the current year's pillar.
3. Note silently for the reading: the day master and its element, which elements are strong/absent, and how the current year's pillar relates to the chart (same element, generating, controlling, etc.). v1 reads the year only — no 大運.

## Step 3: Draw the tarot cards

- Run once: `python references/fortune_tools.py draw` (3 cards: 現状 / 課題 / 助言， each upright or reversed).
- If the question is a two-choice question (AかBか), still draw 3 and read them as: the flow of the choice the person leans toward / the flow of the other choice / advice — and say that mapping in the output.
- Record the drawn cards exactly as output; they are named in the reading so the draw can be checked later.

## Step 4: Compose the integrated reading

Write the reading in this fixed structure, default length 標準 (about 1,000 characters overall; 短め ≈ half, じっくり ≈ double):

1. **命式サマリー** — the pillars, day master and five-element balance, briefly (a small table is fine)
2. **生まれ持った傾向** — strengths and habits from the day master and the element balance, in non-deterministic wording （〜な傾向があります)
3. **今の運気の流れ** — the current year against the chart: where the wind is favorable, where care helps
4. **タロット3枚** — 現状 / 課題 / 助言， each with the card name and orientation, read against the actual question (general card meanings tied to the person's situation — not a list of memorized keywords)
5. **統合メッセージ** — the heart of this skill: where the Four Pillars view and the tarot view agree, where they differ, and what that means for the question
6. **行動ヒント** — 1–3 small steps the person can take this week
7. **締めの一言** — one short, encouraging sentence

Keep the tone gentle and encouraging throughout. Difficult cards or elements are framed as "where to take care" plus a concrete way forward, never as fate.

## Step 5: Present and adjust

- Present the reading as composed. If the person wants a different length or a softer/ firmer tone, adjust the wording — the chart and the cards do not change.
- A new theme or question starts a fresh reading (new draw); say so plainly.

## Cautions

- Births near a solar-term boundary （節入り, especially 立春 in early February) are exactly where hand calculations go wrong — another reason the helper's output is final. If the person disputes a pillar, show the inputs used and the self-test result rather than improvising an alternative.
- The five-element balance in v1 counts only the visible stems and each branch's main element （蔵干 is not counted). If asked, explain this as the v1 simplification.
- Readings for a third party use only the information given; do not embellish the person's profile beyond the inputs.
