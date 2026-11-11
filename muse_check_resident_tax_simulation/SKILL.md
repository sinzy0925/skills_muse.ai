# Resident Tax Simulation Checker

Take the result text of the 住民税非課税シミュレーター (a Space the operator uses), pasted into chat, and check it in detail: restate what was entered, independently recompute the decisive figures, look for missed items, verify the latest pension and tax information on the web, and report everything in plain Japanese.

## Configuration

- This skill works on the text the operator pastes. It never opens, edits or re-runs the simulator itself.
- The simulator's figures are an estimate based on the fiscal year stated inside the simulator （令和8年度前提）. Always name that premise in the report, and compare it against the latest information found in Step 4.
- No specific person's name, address, municipality or amounts are written into this skill. Everything comes from the pasted text at run time.

## Input

The standard input is the text produced by the simulator's 「結果をコピー（AI確認用）」 button. Its first line invokes this skill, followed by sections for the person's inputs, the spouse's inputs, dependents, and the verdicts (person / household / spouse, plus the future scenario when present).

- If some sections are missing, work with what is there and say plainly what could not be checked. Ask for the missing part only when it changes the conclusion.
- If the operator pastes a screenshot or free-form text instead, read what can be read and mark the rest as unread — never fill gaps by guessing.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Cloning this repository and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not run any check.
  - **B — actually use it:** Ask them to run the simulator in the Space, press its 「結果をコピー（AI確認用）」 button, and paste the copied text here. Then run the check below and explain the result together with the sheet.

## Hard rules

- Never invent a figure, a threshold or a rule. Every number in the report comes from the pasted text, from your own recomputation shown step by step, or from a cited source.
- For the latest-information check, prefer official sources （厚生労働省， 国税庁， 日本年金機構， the municipality). Give the source name and the date you checked for every item. If something cannot be confirmed, write 「未確認」 — do not present a guess as current fact.
- This is a check of an estimate, not tax advice. Always close by saying the final judgment belongs to the municipality / tax office, and that individual circumstances can change the result.
- Do not modify the simulator, do not file any tax return, and do not send anything to anyone. The only output is the report in chat.

## Step 1: Restate the inputs and the verdict

- Rebuild the pasted content into a short table: person (birth date, pension amounts at the stated ages, other income, district class （級地）, special-status checks: disability pension, widow(er)/single parent, care-certificate status), spouse (same items), dependents.
- Restate the simulator's verdicts next to it: person, household, spouse, and how much room （あといくら余裕があるか) the simulator showed, when present.
- This restatement is the operator's chance to spot a paste or input error before the check begins. Do not skip it.

## Step 2: Recompute the decisive figures

Independently recompute, showing the steps:

- 雑所得 ＝ 年金額 − 公的年金等控除額 (use the deduction table for the person's age band and pension size; the simulator's notes carry the table it used — recompute from the rules, do not just copy its intermediate values).
- 合計所得金額 ＝ 雑所得 ＋ その他の所得.
- The exemption limits for 均等割 and 所得割 from the district class （級地）, household size and dependent additions, and the special-case limit (合計所得金額1,350,000円以下） when a special status applies.
- Compare each recomputed figure with the simulator's result. If they agree, say so in one line. If they differ, name the exact figure, both values, and the most likely reason (for example a different age band or a missed addition) — never silently adopt one side.

## Step 3: Missed-item checklist

Check each of these against the pasted inputs and report only what is relevant:

- **Spouse and household**: the spouse's own pension and other income were entered, and the household verdict （世帯全員が非課税か) was looked at — many benefits depend on the household, not the person.
- **Public-pension additions**: 企業年金・企業型DC・iDeCoの老齢給付 count as 公的年金等 but do not appear in the ねんきん定期便 estimate; check whether they are missing from the pension amount.
- **Other income**: 個人年金保険 (not 公的年金等）, パート収入, 不動産所得, シルバー人材センターの配分金 — entered as その他の所得？
- **Non-taxable income**: 障害年金・遺族年金 are non-taxable and must not be inside the pension amount.
- **Care certificate**: 障害者控除対象者認定書 — already obtained, expected （見込み）, or not considered? Its criteria differ by municipality; never treat 要介護度 alone as proof.
- **District and municipality**: the 級地 matches the municipality where the person lived on January 1 of that year.
- **Filing note**: even when exempt, a 住民税の申告 may still be needed （非課税証明書, 国民健康保険料の算定）.

## Step 4: Latest-information check

- Search the web for the newest official information that could change the result: 年金額の改定 (latest 年度）, changes to 公的年金等控除 or the resident-tax exemption limits, and any change to the 障害者控除対象者認定書 system.
- Compare with the simulator's stated premise （令和8年度前提）. Report each checked item as: still valid / changed (with the new figure and source) / could not be confirmed.
- Keep this to items that affect this person's result. Do not dump general pension news.

## Step 5: Report

Write the report in Japanese, in this order:

1. 判定の要約 — the verdict in one or two lines, including the household view.
2. 検算の結果 — agree / differ (details from Step 2).
3. 見落とし・注意点 — only the relevant items from Step 3.
4. 最新情報との差分 — from Step 4, with sources and the check date.
5. 次のアクション — concrete next steps when there are any (for example: apply for the certificate, file the resident-tax return, re-run the simulator with corrected inputs).
6. Closing line: this is a check of an estimate; the final judgment is the municipality's / tax office's.

## Pitfalls

- The exemption verdict is based on 合計所得金額 before deductions: increasing 医療費控除 or other deductions does not change it. Do not suggest deduction strategies as a way to become exempt.
- Pension amounts in the simulator may be estimates at ages 65/70/75. Keep estimate and confirmed amounts clearly separated in the report.
- A result for one year does not carry to the next: resident tax is based on the previous year's income.
