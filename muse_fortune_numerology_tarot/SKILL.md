# Numerology × Tarot Reading

## What this skill does

Give one integrated fortune reading that combines two methods with fixed roles:

- **数秘術 (Numerology)** — the foundation: the person's life theme from their ライフパス (life path number), their inborn talent from their バースデー (birthday number), and this year's theme from their パーソナルイヤー (personal year number) — all computed from the birth date alone. No name and no birth time are needed (this skill uses birth-date numbers only).
- **タロット (Tarot)** — the answer for right now: three cards drawn by random lot for the person's actual question — 現状 (present), 課題 (challenge), 助言 (advice).

The two are woven into a single reading in a fixed seven-part structure (§ Step 4). The tone is gentle and encouraging; the reading never frightens.

Typical instruction from the user: a birth date and a question or theme, plus words like 「占って」.

Design source: the operator's combined-fortune design (roles fixed as above; name-based numbers are out of scope in v1; decisions confirmed by the user on 2026-11-17). This skill is a sibling of `muse_fortune_shichusuimei_tarot` （四柱推命 × タロット) and `muse_fortune_kyusei_runes` （九星気学 × ルーン) and follows the same ground rules.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start a reading, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any birth data and do not draw any cards.
  - **B — actually use it:** Tell them 「入力項目を確認してから説明します」, then collect the input items of Step 1 (birth date, the question/theme), and explain using the sheet together with how those items will be used, before starting the reading.

## Ground rules

- **The numbers are computed, never remembered or guessed.** All numerology arithmetic goes through the bundled helper `references/numerology_tools.py`. Its output is used verbatim. Never compute a number by hand in the reading, never "correct" the helper's output from memory, and never invent a number.
- **Entertainment framing.** A reading is entertainment and a thinking aid. Never give definitive judgments on health, law, or money (investments, loans); if the question touches those, add a line suggesting a professional. Never use frightening phrasing （〜しないと不幸になる, deadlines of doom, curses). When difficult material appears, always pair it with a way forward.
- **Privacy.** Birth dates are personal data: use them only for that reading. Never write them into the skill files, shared materials, or any saved note.
- **No re-draws.** The tarot draw happens once per question. If the person asks a genuinely new question, that is a new reading with a new draw; the same question is never re-drawn to get a "better" result.
- **Missing inputs are asked, not guessed.** If a required item is missing, stop and ask for all missing items in one message.

## Step 1: Collect the inputs

- **生年月日** (required — the only personal input; no name, no birth time, no birthplace)
- **相談テーマ／質問** (required — a theme such as 仕事・恋愛・お金・人間関係, or a free-form question)
- **鑑定の長さ** (optional — default 標準； 短め / じっくり also possible)

## Step 2: Compute and verify the numbers

The helper is pure arithmetic (no external library needed), but the numbers still always come from the helper, never from mental arithmetic in the reply.

1. **Self-test first** (once per environment, before the first real reading):
   `python references/numerology_tools.py selftest`
   It checks anchor calculations （ライフパス 5 cases including both master numbers, バースデー 6 cases, パーソナルイヤー 3 cases) and the tarot deck's integrity. If it does not print `SELFTEST: ALL OK`, stop and report; do not produce a reading on an unverified calculation.
2. **Compute the numbers:**
   `python references/numerology_tools.py numbers YYYY-MM-DD`
   Use its output verbatim: the ライフパス, the バースデー, and the パーソナルイヤー for the current year.
3. Note silently for the reading: the life path as the person's long-running theme, the birthday number as the handy, inborn tool they use without thinking, and the personal year as where they are in the 9-year cycle right now.

The v1 conventions, fixed here so every reading is consistent: digits are reduced to 1–9 **except 11 and 22, which are kept as master numbers**; the personal year is **calendar-based** (January–December of the current year). Name-based numbers （デスティニー, ソウル, パーソナリティ) are out of scope in v1.

## Step 3: Draw the tarot cards

- Run once: `python references/numerology_tools.py draw` (3 cards: 現状 / 課題 / 助言， each upright or reversed).
- If the question is a two-choice question (AかBか), still draw 3 and read them as: the flow of the choice the person leans toward / the flow of the other choice / advice — and say that mapping in the output.
- Record the drawn cards exactly as output; they are named in the reading so the draw can be checked later.

## Step 4: Compose the integrated reading

Write the reading in this fixed structure, default length 標準 (about 1,000 characters overall; 短め ≈ half, じっくり ≈ double):

1. **数字サマリー** — the ライフパス, バースデー and パーソナルイヤー, briefly
2. **生まれ持った傾向** — the life path as the life-long theme and the birthday number as the inborn talent, in non-deterministic wording （〜な傾向があります)
3. **今の運気の流れ** — the personal year: what kind of year this is in the 9-year cycle, where the wind is favorable, where care helps
4. **タロット3枚** — 現状 / 課題 / 助言， each with the card name and orientation, read against the actual question (general card meanings tied to the person's situation — not a list of memorized keywords)
5. **統合メッセージ** — the heart of this skill: where the numerology view and the tarot view agree, where they differ, and what that means for the question
6. **行動ヒント** — 1–3 small steps the person can take this week
7. **締めの一言** — one short, encouraging sentence

Keep the tone gentle and encouraging throughout. Difficult cards or numbers are framed as "where to take care" plus a concrete way forward, never as fate.

## Step 5: Present and adjust

- Present the reading as composed. If the person wants a different length or a softer/ firmer tone, adjust the wording — the numbers and the cards do not change.
- A new theme or question starts a fresh reading (new draw); say so plainly.

## Cautions

- Master numbers (11, 22) are read as a stronger, more sensitive version of their reduced value (2, 4) — mention both faces briefly rather than treating them as simply "luckier".
- If the person disputes a number, show the digit sum and the self-test result rather than improvising an alternative; schools differ on master numbers and on the personal-year start, and this skill's conventions are the ones in Step 2.
- Readings for a third party use only the information given; do not embellish the person's profile beyond the inputs.
