# Muse カスタムスキル集

Muse（MetaのパーソナルAIエージェント）で使う、カスタムスキルの置き場です。
1フォルダ＝1スキルになっていて、フォルダの中に手順書（SKILL.md）と、人のための説明（README.md）が入っています。

## スキル一覧

### スライド作成

| スキル | 入力 | 出来上がるもの |
|---|---|---|
| `muse_make_slides_with_narration_from_texts_to_youtube` | 殴り書きメモ・会話ログ | ナレーション原稿入りのYouTube用スライド一式 |
| `muse_make_slides_with_narration_from_screenshots_to_youtube` | スクリーンショット／画面録画の動画 | 画像にマスクと番号注釈を載せた、ナレーション付きYouTube用スライド |
| `muse_make_slides_without_narration_from_screenshots` | スクリーンショット／画面録画の動画 | 作業内容をスライド上に大きく書いた、プレゼン用スライド（ノート無し） |

### 動画アップロード

| スキル | 内容 |
|---|---|
| `muse_up_youtube_from_google_drive_mp4` | Googleドライブに置いたmp4を、設定を確認してからYouTubeへアップロードする |

### 議事録

| スキル | 内容 |
|---|---|
| `muse_make_gijiroku_ai-output` | オンラインコミュニティの雑談会の議事録と開催報告を作り、下書き確認のうえDiscordの指定スレッドへ投稿する（特定のコミュニティ向けに作ったものです） |

## 使い方

1. このリポジトリを clone します。

   ```bash
   git clone https://github.com/sinzy0925/skills_muse.ai.git
   ```

2. 使いたいスキルのフォルダを、Museのカスタムスキル置き場（`custom-skills/`）に入れます。

3. Museのチャットで、スキル名で呼び出して使います（例：「muse_up_youtube_from_google_drive_mp4 を使って」）。

各スキルの詳しい使い方・前提・注意は、それぞれのフォルダ内の README.md を見てください。

## ルールのメモも入っています

リポジトリの直下には `常時参照して欲しいメモ.md` があります。これはスキルではなく、Museにいつも守ってほしいルール（投稿前に下書き確認する、固まったら見切って報告する、など）をまとめたメモです。

clone したあと、自分のClaudeに次のように指示すれば、スキルの保存とメモの保存が一度で済みます。

> このリポジトリのスキルを全部、custom-skills に保存して。あと、常時参照して欲しいメモ.md の内容を、常時参照するメモに保存して。

## 前提

- Museのアカウントが必要です。
- スキルによっては、Googleアカウントの連携や、Museの内蔵ブラウザでのログイン（YouTube Studio、Discordなど）が必要です。
- 投稿や公開のような外向きの操作は、いきなり実行せず、下書きを見せて本人のOKをもらってから行う作りになっています。

## 中身の約束事

- スキルを作るときは、SKILL.md と skill.yaml に加えて、人間向けの README.md を必ず付けます。
- スクショ系スキルのスライドでは、元の画像自体は編集しません。個人情報のマスクや注釈は、スライド上の図形として載せます。
