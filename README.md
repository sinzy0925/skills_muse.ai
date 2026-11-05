# Muse カスタムスキル集

MetaのAIアシスタント **Muse** 用のカスタムスキル集です。

**1フォルダ = 1スキル** で、フォルダごとに Muse のカスタムスキルが入っています。
登録すると、そのスキルを Muse のチャットで名前で呼ぶだけで使えるようになります。

## スキル一覧

| フォルダ | 何ができるか |
| --- | --- |
| [muse_make_editable_google_slides](muse_make_editable_google_slides/) | メモや会話ログからYouTube動画のスライド素材一式を作り、編集可能なテキストのままGoogleスライドへ入れる |
| [muse_up_youtube_from_google_drive_mp4](muse_up_youtube_from_google_drive_mp4/) | Googleドライブのmp4を、端末に落とさずYouTubeへアップロードする |

各スキルの詳しい使い方・前提・注意点は、各フォルダの `README.md` にあります（手順本体は `SKILL.md`）。

## 使い方（登録方法）

Muse のチャットで進めるだけです。手順は3ステップ。

### 1. このリポジトリを clone してもらう

Muse のチャットで、次のように指示します。

```
このリポジトリを git clone して：
https://github.com/sinzy0925/skills_muse.ai.git
```

### 2. 使いたいスキルを登録してもらう

スキル名を指定して、登録を指示します。

```
muse_make_editable_google_slides をカスタムスキルに登録して
muse_up_youtube_from_google_drive_mp4 をカスタムスキルに登録して
```

複数のスキルをまとめて登録することもできます。

### 3. チャットで名前で呼んで使う

登録したスキルは、以降の Muse での作業で活用できます。使うときはスキル名を添えてお願いするだけです。

```
muse_up_youtube_from_google_drive_mp4 で、このドライブのmp4をYouTubeにアップして
```

> スキルは常時読み込みオフ（`include_in_prompt: false`）で登録されるため、使わないときは Muse の動作に影響しません。必要なときに名前で呼ぶ方式です。

## フォルダ構成

```
.
├── README.md                                  # このファイル
├── muse_make_editable_google_slides/
│   ├── README.md / SKILL.md / skill.yaml
│   └── references/                            # テンプレート・投入手順・実例
└── muse_up_youtube_from_google_drive_mp4/
    └── README.md / SKILL.md / skill.yaml
```

- `SKILL.md`：スキルの手順本体（Muse が読むファイル）
- `skill.yaml`：スキルの名前・説明などのメタ情報
- `README.md`：人間向けの説明（このファイルと同じ役割を各フォルダでも）
