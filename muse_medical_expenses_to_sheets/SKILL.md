# Medical Expenses to Google Sheets Ledger

Organize the records needed for the Japanese medical expense deduction （医療費控除）: read the hospital and pharmacy receipts waiting in a Google Drive inbox folder, combine them with transport-to-hospital memos (train, bus and taxi fares usually have no receipts, so a dated memo is the record), append everything to a yearly Google Sheets ledger, report anything that needs the operator's confirmation, then move the processed files to a done folder. At filing time the ledger can be reshaped into the official 明細書 layout (grouped by person and by hospital or pharmacy).

## Configuration

- This skill is shareable: it contains no folder IDs, spreadsheet IDs, URLs or account details. Resolve everything by name at runtime. The operator keeps the resolved IDs and any personal settings in their own records, not in this file.
- Drive folders, found by name: `医療費整理_実行前` (inbox) and `医療費整理_実行後` (done). Create either one if it does not exist.
- Ledger spreadsheet, found by title from the operator's records (for example `医療費台帳<year>`). Create it with the format below on first use.
- Use the Google Workspace CLI (`/opt/hatch/bin/hatch_gws_cli`) for both Drive and Sheets. Read the google_drive and google_sheets connector docs for exact commands.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Cloning this repository and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a connection or setup on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not run any connection check or setup. Where the three URLs would appear, they stay as the placeholder 「ここに実際のURLが入ります」 — no real URLs in explanation mode.
  - **B — actually use it:** Tell them 「Googleドライブとスプレッドシートに接続してから説明します」, then run the connection checks under "Connect first" (share a connect link and wait if either service is not connected), resolve the two folders and the ledger by name (creating any that are missing), and only then explain, using the sheet plus the three real URLs.
- In mode B, always finish by telling the operator the three URLs they will actually use: the inbox folder （医療費整理_実行前）, the done folder （医療費整理_実行後）, and the ledger spreadsheet. Those URLs come from the operator's own environment at runtime; never write them into the skill. An explanation without the concrete URLs does not get the operator started, so in mode B this step is part of answering "how do I use it".

## Connect first

- Check Google Drive: `hatch_gws_cli drive status`. If it is `not_connected`, share the returned connect link as `[Connect Google Drive](<connect_url>)` and wait for the operator to connect before continuing.
- Check Google Sheets the same way: `hatch_gws_cli sheets status`, sharing `[Connect Google Sheets](<connect_url>)` when needed.
- Never ask for passwords or credentials in chat; connection always goes through the connect link.

## Hard rules

- Never invent or guess text, amounts or dates that cannot be read. Write what is printed, and mark anything uncertain as 要確認 in the 備考 column and in the final report.
- The person treated （受診した人） is often not printed on a receipt. If it cannot be determined, leave it blank and flag it as 要確認. Never guess which family member it was.
- Count each receipt once. The same receipt often appears both as a PDF scan and as a photo; match on facility, date, total and receipt number, merge duplicates into one row, and name every source file in the 証憑・メモ column.
- Keep template or sample images out of the ledger (fictitious names such as サンプル株式会社， placeholder amounts or dates). List excluded files in the final report instead.
- Transport fares are recorded from memos, not receipts. A transport memo is usable only when it states: date, person, hospital or clinic, transport type (train, bus or taxi), departure station or stop, arrival station or stop, one-way or round trip, and the amount. Record chat memos in the `通院交通費メモ` sheet first, then reflect them into the ledger. If an element is missing, ask for exactly that element or mark the memo 要確認; never fill the gaps.
- Taxis are the exception, not the rule: a taxi fare is includable only when public transport could not be used (injury, sudden illness, and similar). Always flag taxi rows as 要確認（タクシー） and require the reason in the memo. A taxi memo without a reason is not entered into the ledger; list it in the final report instead.
- Private-car costs (gasoline, parking) are never entered; they are outside the deduction.
- Pharmacy items marked ★ are eligible for the セルフメディケーション tax scheme. Track them in a separate subtotal in `集計`. The medical expense deduction and the self-medication scheme are alternatives that cannot be combined; never count a ★ item in both.
- 補填される金額 (insurance payouts, 高額療養費 refunds, and similar) reduces the deductible total. It is usually unknown when the receipt is recorded, so leave it blank at first and fill it in when the operator provides it (for example from the insurer's 医療費のお知らせ）.
- Borderline items (health checkups such as 人間ドック, vaccinations, cosmetic treatment, supplements) are not decided by this skill. Enter them with 要確認 and let the operator confirm with the tax office or their accountant. Do not assert tax conclusions yourself.
- Paper originals must be kept by the operator for five years after filing. The scans in Drive are for organization only and never replace the originals. Say this in the final report of the first run of each year.
- Move a file to the done folder only after its row has been written to the ledger and read back verified.

## Ledger format

Workbook sheets: `医療費一覧` (the ledger), `通院交通費メモ` (transport memos), `集計` (totals).

`医療費一覧` columns A–K, first row frozen, with one 合計 row at the bottom:

| Column | Content |
|---|---|
| A No. | Running number, continuing across runs |
| B 日付 | Date of treatment, purchase or transport |
| C 受診した人 | Person treated; blank + 要確認 when unknown |
| D 病院・薬局 | Hospital, clinic or pharmacy name; for transport rows, the destination hospital |
| E 区分 | `診療・治療`, `医薬品`, `交通費` or `その他` |
| F 内容 | Treatment or items bought; for transport, route and one-way/round trip |
| G 金額 | Amount paid |
| H 補填される金額 | Insurance or refunds; blank until known |
| I 差引額 | Formula `=G-H` |
| J 証憑・メモ | Source file name(s) in Drive, or the transport memo it came from |
| K 備考・要確認 | Reading caveats and points to confirm |

`通院交通費メモ` columns A–J: 日付 / 受診した人 / 病院 / 交通手段 / 出発駅・バス停 / 到着駅・バス停 / 片道・往復 / 金額 / メモ / 反映 (`済` once the memo has been copied into `医療費一覧`). One hospital visit is one row; for a round trip, 金額 is the round-trip total.

`集計` holds: SUMIF totals by 受診した人 (of I), by 区分 (of I), and a SUMIFS total per month (of I); the grand total of I; the remaining amount to the deduction threshold (reference only: 原則10万円, or 5% of income when total income is under 2,000,000 yen — the operator confirms which applies); and the ★ self-medication subtotal kept separately. When appending rows, write the new data rows first, then rewrite the 合計 row so its SUM ranges cover all data rows, and extend the 集計 formula ranges to match.

## Procedure

1. Run the connection checks above; stop and share a connect link if either service is not connected.
2. Find the two folders by name (`drive files list` with a name query); create any that are missing. Find the ledger spreadsheet by title; create it in the format above if missing.
3. If transport memos were given in chat, append them to `通院交通費メモ` first (checking the required elements above), so they are processed together with the receipts.
4. List the files in `医療費整理_実行前` and the unreflected memos in `通院交通費メモ`. If both are empty, report that there is nothing to organize and stop.
5. Download each file (`drive files get` with `alt: media`) to a local working folder. Receipt PDFs are scanned images: render each page to PNG (for example `pdftoppm -png -r 130`) and read every receipt as an image, including handwritten ones. Do not rely on embedded PDF text.
6. Extract per receipt: date, person (only when determinable), facility, 区分， items, amount, and any ★ marks. Apply the hard rules: merge duplicates, set samples aside, flag taxis and borderline items.
7. Sort everything by date, assign continuing No. values (continue after the ledger's last number), and append the rows with the I formula. Write with `valueInputOption=USER_ENTERED` so dates and formulas parse.
8. Read the written range back and check the row values and the 合計 row against the sources before going on. Mark the processed memos as 反映 `済`.
9. Report to the operator: rows added, the new totals (including the remaining amount to the threshold as a reference), and every 要確認 point (unreadable parts, unknown person, taxi reasons, borderline items, duplicates merged, samples excluded, memos not entered and why).
10. Move each processed file from `医療費整理_実行前` to `医療費整理_実行後` (`drive files update` with `addParents` / `removeParents`). Verify by listing both folders. Files outside the inbox are never touched.

## Filing-time output (on request)

When the operator asks for the filing summary, produce a 明細書-ready view from `医療費一覧`: group rows by 受診した人 and then by 病院・薬局， with each group's 区分， 金額 total, 補填 total and 差引 total, plus the grand total. Put it in a new sheet named `明細書用集計` in the same workbook (or an exported file if asked). The official form layout changes; match the current year's 医療費控除の明細書 columns and say so if they cannot be verified.
