# Kyusei Kigaku × Runes Reading

## What this skill does

Give one integrated fortune reading that combines two methods with fixed roles:

- **九星気学 (Kyusei Kigaku)** — the foundation: the person's inborn tendencies from their 本命星 (honmeisei, the star of their birth year) and 月命星 (getsumeisei, the star of their birth month), and the broad flow of the current year, all from their birth date alone. No birth time is needed.
- **ルーン (Runes)** — the answer for right now: three runes drawn by random lot for the person's actual question — 現状 (present), 課題 (challenge), 助言 (advice).

The two are woven into a single reading in a fixed seven-part structure (§ Step 4). The tone is gentle and encouraging; the reading never frightens.

Typical instruction from the user: a birth date and a question or theme, plus words like 「占って」.

Design source: the operator's combined-fortune design (roles fixed as above; 方位 readings are out of scope in v1; decisions confirmed by the user on 2026-11-17). This skill is the sibling of `muse_fortune_shichusuimei_tarot` (四柱推命 × タロット) and follows the same ground rules.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start a reading, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any birth data and do not draw any runes.
  - **B — actually use it:** Tell them 「入力項目を確認してから説明します」, then collect the input items of Step 1 (birth date, the question/theme), and explain using the sheet together with how those items will be used, before starting the reading.

## Ground rules

- **The stars are computed, never remembered or guessed.** All Kyusei arithmetic goes through the bundled helper `references/kyusei_rune_tools.py` (which uses the sxtwl library for the solar-term boundaries). Its output is used verbatim. Never compute a star by hand, never "correct" the helper's output from memory, and never invent a star.
- **Entertainment framing.** A reading is entertainment and a thinking aid. Never give definitive judgments on health, law, or money (investments, loans); if the question touches those, add a line suggesting a professional. Never use frightening phrasing （〜しないと不幸になる, deadlines of doom, curses). When difficult material appears, always pair it with a way forward.
- **Privacy.** Birth dates are personal data: use them only for that reading. Never write them into the skill files, shared materials, or any saved note.
- **No re-draws.** The rune draw happens once per question. If the person asks a genuinely new question, that is a new reading with a new draw; the same question is never re-drawn to get a "better" result.
- **Missing inputs are asked, not guessed.** If a required item is missing, stop and ask for all missing items in one message.

## Step 1: Collect the inputs

- **生年月日** (required — the only personal input; no birth time, no birthplace)
- **相談テーマ／質問** (required — a theme such as 仕事・恋愛・お金・人間関係, or a free-form question)
- **鑑定の長さ** (optional — default 標準； 短め / じっくり also possible)

## Step 2: Build and verify the Kyusei chart

Run everything with a Python environment that has sxtwl installed (`pip install sxtwl` if missing; if it cannot be installed or run, stop and report — do not fall back to hand calculation).

1. **Self-test first** (once per environment, before the first real chart):
   `python references/kyusei_rune_tools.py selftest`
   It checks published anchor stars （本命星 7 cases including the 立春 boundary, 月命星 4 cases) and the rune deck's integrity. If it does not print `SELFTEST: ALL OK`, stop and report; do not produce a reading on an unverified calculation.
2. **Compute the chart:**
   `python references/kyusei_rune_tools.py chart YYYY-MM-DD`
   Use its output verbatim: the 本命星， the 月命星， and the current year's star (all on the 立春-based Kyusei year).
3. Note silently for the reading: the 本命星's element (the person's basic tone), the 月命星 (read in v1 as the inner, less visible side), and how the current year's star relates to the 本命星 (same element, generating, controlling, etc.).

## Step 3: Draw the runes

- Run once: `python references/kyusei_rune_tools.py draw` (3 runes: 現状 / 課題 / 助言， each upright or reversed; the eight symmetric runes have no reversed position and the helper says so).
- If the question is a two-choice question (AかBか), still draw 3 and read them as: the flow of the choice the person leans toward / the flow of the other choice / advice — and say that mapping in the output.
- Record the drawn runes exactly as output; they are named in the reading so the draw can be checked later.

## Step 4: Compose the integrated reading

Write the reading in this fixed structure, default length 標準 (about 1,000 characters overall; 短め ≈ half, じっくり ≈ double):

1. **命盤サマリー** — the 本命星， 月命星 and the current year's star, briefly
2. **生まれ持った傾向** — the 本命星 as the visible, basic tendencies; the 月命星 as the inner side that shows in private or under stress, in non-deterministic wording （〜な傾向があります)
3. **今の運気の流れ** — the current year's star against the 本命星： where the wind is favorable, where care helps
4. **ルーン3つ** — 現状 / 課題 / 助言， each with the rune name and orientation, read against the actual question (general rune meanings tied to the person's situation — not a list of memorized keywords)
5. **統合メッセージ** — the heart of this skill: where the Kyusei view and the rune view agree, where they differ, and what that means for the question
6. **行動ヒント** — 1–3 small steps the person can take this week
7. **締めの一言** — one short, encouraging sentence

Keep the tone gentle and encouraging throughout. Difficult runes or stars are framed as "where to take care" plus a concrete way forward, never as fate.

## Step 5: Present and adjust

- Present the reading as composed. If the person wants a different length or a softer/ firmer tone, adjust the wording — the chart and the runes do not change.
- A new theme or question starts a fresh reading (new draw); say so plainly.

## Cautions

- Births near a solar-term boundary （立春 in early February for the year, 節入り for the month) are exactly where hand calculations go wrong — another reason the helper's output is final. If the person disputes a star, show the inputs used and the self-test result rather than improvising an alternative.
- **方位 (direction readings — 吉方位, 日盤・月盤） is out of scope in v1.** If asked for a lucky direction, say plainly that this version does not cover it; do not improvise one from the stars.
- The eight symmetric runes （ゲボ, ハガラズ, ナウシズ, イサ, ジェラ, エイワズ, ソウィロ, ダガズ) have no reversed position; never report one as reversed.
- Readings for a third party use only the information given; do not embellish the person's profile beyond the inputs.
