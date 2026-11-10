# Receipt PDFs to Google Sheets Ledger

Organize receipts for a Japanese tax return （確定申告）: read the receipt PDFs and images waiting in a Google Drive inbox folder, append them to a Google Sheets expense ledger in a fixed format, report anything that needs the operator's confirmation, then move the processed files to a done folder.

## Configuration

- This skill is shareable: it contains no folder IDs, spreadsheet IDs, URLs or account details. Resolve everything by name at runtime. The operator keeps the resolved IDs and any personal settings in their own records, not in this file.
- Drive folders, found by name: `領収書整理_実行前` (inbox) and `領収書整理_実行後` (done). Create either one if it does not exist.
- Ledger spreadsheet, found by title from the operator's records (for example `領収書整理<year>`). Create it with the format below on first use.
- Use the Google Workspace CLI (`/opt/hatch/bin/hatch_gws_cli`) for both Drive and Sheets. Read the google_drive and google_sheets connector docs for exact commands.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Cloning this repository and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a connection or setup on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not run any connection check or setup. Where the three URLs would appear, they stay as the placeholder 「ここに実際のURLが入ります」 — no real URLs in explanation mode.
  - **B — actually use it:** Tell them 「Googleドライブとスプレッドシートに接続してから説明します」, then run the connection checks under "Connect first" (share a connect link and wait if either service is not connected), resolve the two folders and the ledger by name (creating any that are missing), and only then explain, using the sheet plus the three real URLs.
- In mode B, always finish by telling the operator the three URLs they will actually use: the inbox folder （領収書整理_実行前）, the done folder （領収書整理_実行後）, and the ledger spreadsheet. Those URLs come from the operator's own environment at runtime; never write them into the skill. An explanation without the concrete URLs does not get the operator started, so in mode B this step is part of answering "how do I use it".

## Connect first

- Check Google Drive: `hatch_gws_cli drive status`. If it is `not_connected`, share the returned connect link as `[Connect Google Drive](<connect_url>)` and wait for the operator to connect before continuing.
- Check Google Sheets the same way: `hatch_gws_cli sheets status`, sharing `[Connect Google Sheets](<connect_url>)` when needed.
- Never ask for passwords or credentials in chat; connection always goes through the connect link.

## Hard rules

- Never invent or guess text, amounts or tax figures that cannot be read. Write what is printed, and mark anything uncertain as 要確認 in the 備考 column and in the final report.
- Amounts and consumption tax are taken exactly as written on the receipt.
- Count each receipt once. The same receipt often appears both as a PDF scan and as a photo; match on store, date, total and receipt number, merge duplicates into one row, and name every source file in the 証憑ファイル column.
- Keep template or sample images out of the ledger (fictitious payees such as サンプル株式会社， placeholder amounts or dates). List excluded files in the final report instead.
- Handwritten receipts: if the issuer's name, address, registration number or tax breakdown is missing, say so in 備考 and in the report. Never fill the gaps.
- 勘定科目 is a proposal. Append （仮） whenever business versus personal use is not clear from the receipt itself.
- Move a file to the done folder only after its row has been written to the ledger and read back verified.

## Ledger format

Workbook sheets: `領収書一覧` (the ledger), `集計` (totals), `項目の説明` (column guide and cautions).

`領収書一覧` columns A–O, first row frozen, with one 合計 row at the bottom:

| Column | Content |
|---|---|
| A No. | Running number, continuing across runs |
| B 日付 | Receipt date |
| C 支払先・発行者 | Store or issuer name |
| D 内容（品目・但し書き） | Items bought, or the 但し書き wording |
| E 勘定科目 | Expense category, with （仮） when provisional |
| F 金額（税込） | Total paid, tax included |
| G 税率区分 | `10%`, `8%（軽減）`, mixed, or `記載なし` |
| H 消費税額 | Tax amount exactly as printed; blank when not stated |
| I 税抜金額 | Formula `=F-H` |
| J 支払方法 | 現金 / クレジット / etc., blank or （記載なし） when unknown |
| K インボイス登録番号 | `T` + 13 digits when printed, otherwise `なし` |
| L 事業割合（%) | Business-use share for 家事按分； default 100 |
| M 経費計上額 | Formula `=ROUND(F*L/100,0)` |
| N 証憑ファイル | Source file name(s) in Drive |
| O 備考・要確認 | Reading caveats and points to confirm |

`集計` holds SUMIF totals by 勘定科目 (of M) and by 税率区分 (of F), and a SUMIFS total per month (of M). When appending rows, write the new data rows first, then rewrite the 合計 row so its SUM ranges cover all data rows, and extend the 集計 formula ranges to match.

`項目の説明` explains each column's purpose and carries the standing cautions (invoice-system notes, the duplicate/sample handling, and the handwritten-receipt warning). Write it when the workbook is created.

## Procedure

1. Run the connection checks above; stop and share a connect link if either service is not connected.
2. Find the two folders by name (`drive files list` with a name query); create any that are missing. Find the ledger spreadsheet by title; create it in the format above if missing.
3. List the files in `領収書整理_実行前`. If it is empty, report that there is nothing to organize and stop.
4. Download each file (`drive files get` with `alt: media`) to a local working folder. Receipt PDFs are scanned images: render each page to PNG (for example `pdftoppm -png -r 130`) and read every receipt as an image, including handwritten ones. Do not rely on embedded PDF text.
5. Extract per receipt: date, payee/issuer, items or 但し書き, total （税込）, 税率区分， 消費税額 as printed, payment method, and the invoice registration number when present.
6. Apply the hard rules: merge duplicates, set samples aside, flag handwritten gaps, mark unclear 勘定科目 with （仮）.
7. Sort by date, assign continuing No. values (continue after the ledger's last number), and append the rows with the I and M formulas. Write with `valueInputOption=USER_ENTERED` so dates and formulas parse.
8. Read the written range back and check the row values and the 合計 row against the receipts before going on.
9. Report to the operator: rows added, the new totals, and every 要確認 point (unreadable parts, missing issuer information, provisional 勘定科目， duplicates merged, samples excluded).
10. Move each processed file from `領収書整理_実行前` to `領収書整理_実行後` (`drive files update` with `addParents` / `removeParents`). Verify by listing both folders: the inbox should hold only unprocessed files and the done folder should contain the moved ones. Files outside the inbox are never touched.

## Reading notes

- Some receipts are printed tax-exclusive （外税）: the subtotal is 税抜 and the tax is printed separately. Record F as the final total paid and H as the printed tax.
- Drugstore receipts may mark items with ★ as eligible for the セルフメディケーション tax scheme. Such an item may belong to 医療費控除 rather than business expenses; flag it in 備考 and never count it in both.
- Receipts belong to the calendar year of their dates. If that year's filing deadline has already passed, tell the operator to confirm late or amended filing handling with the tax office or their accountant. Do not assert tax conclusions yourself.
