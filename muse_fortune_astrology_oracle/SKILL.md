# Western Astrology × Oracle Cards Reading

## What this skill does

Give one integrated fortune reading that combines two methods with fixed roles:

- **西洋占星術 (Western astrology)** — the foundation: the person's core from their 太陽星座 (sun sign), their emotional, unguarded side from their 月星座 (moon sign, needs the birth time), and how they come across from their 上昇宮 (ascendant, needs the birth time and place) — computed from the birth data with a real ephemeris.
- **オラクルカード (Oracle cards)** — the answer for right now: three cards drawn by random lot from this skill's original 36-card deck for the person's actual question — 現状 (present), 課題 (challenge), 助言 (advice).

The two are woven into a single reading in a fixed seven-part structure (§ Step 4). The tone is gentle and encouraging; the reading never frightens.

Typical instruction from the user: a birth date (birth time and birthplace if known) and a question or theme, plus words like 「占って」.

Design source: the operator's combined-fortune design (roles fixed as above; houses are out of scope in v1; decisions confirmed by the user on 2026-11-17). This skill is a sibling of `muse_fortune_shichusuimei_tarot` （四柱推命 × タロット), `muse_fortune_kyusei_runes` （九星気学 × ルーン) and `muse_fortune_numerology_tarot` （数秘術 × タロット) and follows the same ground rules.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start a reading, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any birth data and do not draw any cards.
  - **B — actually use it:** Tell them 「入力項目を確認してから説明します」, then collect the input items of Step 1 (birth date, birth time and birthplace if known, the question/theme), and explain using the sheet together with how those items will be used, before starting the reading.

## Ground rules

- **The chart is computed, never remembered or guessed.** All positions go through the bundled helper `references/astrology_tools.py` (which uses the Swiss Ephemeris via pyswisseph). Its output is used verbatim. Never state a sign from the calendar alone, never "correct" the helper's output from memory, and never invent a position.
- **Entertainment framing.** A reading is entertainment and a thinking aid. Never give definitive judgments on health, law, or money (investments, loans); if the question touches those, add a line suggesting a professional. Never use frightening phrasing （〜しないと不幸になる, deadlines of doom, curses). When difficult material appears, always pair it with a way forward.
- **Privacy.** Birth dates, times and places are personal data: use them only for that reading. Never write them into the skill files, shared materials, or any saved note.
- **No re-draws.** The oracle draw happens once per question. If the person asks a genuinely new question, that is a new reading with a new draw; the same question is never re-drawn to get a "better" result.
- **Missing inputs are asked, not guessed.** If a required item is missing, stop and ask for all missing items in one message. Optional items (birth time, birthplace) are simply left out — never invented — and the reading says what was left out.

## Step 1: Collect the inputs

- **生年月日** (required)
- **出生時刻** (optional — without it, the reading is a simplified sun-sign-only version and says so in the output)
- **出生地** (optional — a Japanese prefectural capital name, e.g. 大阪, or `lat,lon[,utc_offset_hours]`; without it, no ascendant is given. Japanese places use the capital's coordinates and JST)
- **相談テーマ／質問** (required — a theme such as 仕事・恋愛・お金・人間関係, or a free-form question)
- **鑑定の長さ** (optional — default 標準； 短め / じっくり also possible)

## Step 2: Build and verify the natal chart

Run everything with a Python environment that has pyswisseph installed (`pip install pyswisseph` if missing; if it cannot be installed or run, stop and report — do not fall back to calendar-based guesses).

1. **Self-test first** (once per environment, before the first real chart):
   `python references/astrology_tools.py selftest`
   It checks sun-sign anchors and a full published chart (Einstein: sun Pisces, moon Sagittarius, ascendant Cancer), the place table, and the oracle deck. If it does not print `SELFTEST: ALL OK`, stop and report; do not produce a reading on an unverified calculation.
2. **Compute the chart:**
   `python references/astrology_tools.py chart YYYY-MM-DD [HH:MM] [PLACE]`
   Use its output verbatim: the sun sign, the moon sign (with birth time), the ascendant (with time and place), and today's Jupiter and Saturn signs.
3. Note silently for the reading: the sun as the person's core direction, the moon as the emotional, private side, the ascendant as the outer impression and way of starting things, the elements involved, and how today's Jupiter (expansion, tailwind) and Saturn (the current lesson) relate to the natal sun.

## Step 3: Draw the oracle cards

- Run once: `python references/astrology_tools.py draw` (3 cards: 現状 / 課題 / 助言. This skill's deck is an original 36-card set; oracle cards have no reversed position.)
- If the question is a two-choice question (AかBか), still draw 3 and read them as: the flow of the choice the person leans toward / the flow of the other choice / advice — and say that mapping in the output.
- Record the drawn cards exactly as output; they are named in the reading so the draw can be checked later.

## Step 4: Compose the integrated reading

Write the reading in this fixed structure, default length 標準 (about 1,000 characters overall; 短め ≈ half, じっくり ≈ double):

1. **ホロスコープ・サマリー** — the sun, moon and ascendant signs with their elements, briefly (in the simplified version, the sun sign only, marked as such)
2. **生まれ持った傾向** — the sun as the core and life direction, the moon as the emotional, unguarded side, the ascendant as the outer impression, in non-deterministic wording （〜な傾向があります)
3. **今の運気の流れ** — today's Jupiter and Saturn against the natal chart: where expansion is favored this year, what the current lesson is, where care helps
4. **オラクル3枚** — 現状 / 課題 / 助言， each with the card name, read against the actual question (the card's theme tied to the person's situation — not a list of memorized keywords)
5. **統合メッセージ** — the heart of this skill: where the astrology view and the oracle view agree, where they differ, and what that means for the question
6. **行動ヒント** — 1–3 small steps the person can take this week
7. **締めの一言** — one short, encouraging sentence

Keep the tone gentle and encouraging throughout. Difficult cards or placements are framed as "where to take care" plus a concrete way forward, never as fate.

## Step 5: Present and adjust

- Present the reading as composed. If the person wants a different length or a softer/ firmer tone, adjust the wording — the chart and the cards do not change.
- A new theme or question starts a fresh reading (new draw); say so plainly.

## Cautions

- Births near a sign boundary (a cusp) are exactly where calendar-based guesses go wrong — another reason the helper's output is final. If the person disputes a sign, show the inputs used and the self-test result rather than improvising an alternative.
- **Houses and detailed aspects are out of scope in v1** — the chart covers the sun, moon, ascendant, and the current Jupiter/Saturn signs only. If asked for more, say plainly that this version does not cover it.
- Birth times recorded as 「朝」「夜」 etc. are not precise enough for the moon or ascendant; if only a vague time is given, treat the time as unknown (sun-only version) rather than guessing an hour.
- Readings for a third party use only the information given; do not embellish the person's profile beyond the inputs.
