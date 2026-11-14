# Google Slides → YouTube Uploader

## What this skill does

Turn a finished Google Slides deck into a YouTube video. The deck's speaker notes become the narration: the deck is converted to a video in Google Vids, AI narration is inserted on every scene, the video is exported to YouTube, and the title, thumbnail, description, audience setting and visibility are set in YouTube Studio.

Typical instruction from the user: a Google Slides URL, plus words like 「YouTubeにアップして」.

Source procedure: the user's own standard workflow for publishing slide decks as narrated videos.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start an upload, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not run any connection check or open any deck.
  - **B — actually use it:** Tell them 「ブラウザのログイン状態を確認してから説明します」, then check that the browser to be used is signed in to Google (if it is signed out, the sign-in itself is the user's own step — see Step 2), identify the deck the operator names, and explain using the sheet together with that deck's title and the settings to be confirmed before starting.

## Ground rules

- The deck itself is never edited by this skill. Converting it to a video creates a separate Vids document; the slides stay as they are.
- Passwords, verification codes: never ask the user to send them in chat. Sign-in happens in the browser, operated by the user; 2FA is approved on the user's phone.
- Browser work follows the skip rule: if a screen makes no progress, do not grind on it — skip that item and report it at the end, together with the reason. Items that depend on a skipped item are skipped and reported too. Exception: steps whose submitted state could become unknown (the YouTube export, the final save) — verify the outcome first and never repeat an action that may already have taken effect.
- Menu and button labels in Slides / Vids / Studio may differ slightly from the wording below; choose the item with the same meaning.

## Preparation (before opening the browser)

1. **Thumbnail:** save the image of the deck's first page — that image becomes the YouTube thumbnail. If the deck was built with a designed thumbnail page first, use that page's image; otherwise export the first page as an image.
2. **Description （概要欄）:** read the deck's content (slide text and speaker notes) and draft the description text that summarizes it. Show the draft when confirming the settings in Step 1.
3. Nothing else is prepared in advance. The title defaults to the deck's own title.

## Step 1: Confirm the items with the user

Before converting anything, confirm the items below with the user, asking for every missing one in a single message:

- **スライドのURL** (required — the deck to publish)
- **タイトル** (default: the deck's title, used as-is; confirm, and never invent a different one silently)
- **公開範囲** (required: 公開 / 限定公開 / 非公開. If the user has no preference, propose 限定公開 — it is the safe default and can be widened later)
- **子ども向けかどうか** (default in the user's workflow: 「いいえ、子ども向けではありません」; confirm)
- **説明文** (the draft from the preparation; show it before use)
- **サムネイル** (the first-page image from the preparation)
- **使うブラウザ** (Muse's built-in browser, or the Chrome extension "muse from meta" — follow the user's designation; if not designated, ask)

Do not start the conversion until at least the deck, the title and the visibility are fixed. Settings confirmed here count as the approval for the final save in Step 5; if anything was left undecided, show the final settings and get an explicit OK before saving.

## Step 2: Check the Google sign-in in the browser

- Open the browser to be used. It must be signed in to Google with the working account that owns the deck and the YouTube channel.
- If it is signed out, stop and hand the browser to the user to sign in themselves (the `muse_login_google_account` skill covers this). Never receive a password or a code in chat.
- Confirm which account is signed in before going on; the wrong account will not see the deck or the channel.

## Step 3: Convert the deck to a video in Google Vids

1. Open the deck in Google Slides.
2. ファイルメニュー → 「動画に変換」 をクリックする。しばらく待つ。
3. On the Vids slide-selection screen, turn OFF 「AIナレーション、スクリプト、バックグラウンドミュージック、アニメーションを含める」, then click 「次へ」 at the bottom right. (OFF matters: the narration comes from the deck's own speaker notes, inserted in the next step — not from an auto-generated script.)

## Step 4: Insert the AI narration

1. In the right-hand vertical menu, click 「ナレーション」.
2. Under AIナレーション, click 「すべてのシーン」.
3. Click the blue 「すべてのナレーションを挿入」 below it.
4. Wait until the insertion finishes on every scene and the video is complete. This can take a while; report honestly if it stalls.

## Step 5: Export to YouTube and set the details

1. ファイルメニュー → 「YouTubeにエクスポート」 をクリックする。
2. When 「エクスポートが完了しました」 appears, click 「YouTubeを開く」. YouTube Studio opens on the video's details page.
3. Set the items confirmed in Step 1:
   - タイトル (usually already filled with the deck's title — check it)
   - サムネイル： upload the prepared first-page image as the custom thumbnail
   - 説明： enter the confirmed description text
   - 視聴者： 「いいえ、子ども向けではありません」 (or as confirmed)
   - 公開設定： set the confirmed visibility and click 「完了」
4. Click 「保存」 at the top right, and confirm the saved state (e.g. the "changes saved" message, and the visibility shown on the page).

## Step 6: Verify and report

- Take the video URL from Studio and report to the user: the video URL, the title, the visibility actually set, and the video length if shown.
- Report separately anything that could not be done, with the reason (see the thumbnail caution below). Never present a partially finished upload as fully done.

## Cautions

- **Custom thumbnails need the channel's phone verification.** If Studio shows 「カスタム サムネイルを追加するには、電話番号を確認してください」, do not attempt the verification — it is a step only the user can do (their phone number, their code). Save the video with the auto-generated thumbnail, and report that the prepared thumbnail can be set later from the video's edit page once the user has completed the verification in YouTube Studio. Once verified, the setting works for every later video too.
- Conversion and narration insertion take time. Long decks take longer; say so plainly instead of retrying silently.
- Keep the user's confirmations verbatim: deck, title, visibility and audience come from the user and from this run's confirmation — never from an earlier video's settings.
