# Skills Set Updater (muse_skills_space_update)

## What this skill does

Update the whole published skills set — every custom skill, the スキルランチャー Space, the 住民税非課税シミュレーター Space, and the always-referenced rules memo (常時参照して欲しいメモ.md) — to the latest state published in the GitHub repository below. This skill is the "update" counterpart of the first-time install: the install puts the set in place, and this skill refreshes it when the published set changes (new skills added, existing skills revised, the launcher or simulator updated, memo rules added).

The repository is the source of truth for the published set:

https://github.com/sinzy0925/skills_muse.ai.git

Typical instruction from the user:

> muse_skills_space_update を実行して

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Cloning this repository and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
- **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not fetch or update anything.
- **B — actually use it:** Fetch the latest state of the repository, show the differences (skills to add, skills to update, local-only skills left untouched), then explain using the sheet while the update is applied and reported.

## The update instruction (canonical text)

The update follows the same five steps as the install instruction, with the safeguards in the steps below:

```
https://github.com/sinzy0925/skills_muse.ai.git
1. 上記をgit cloneする。
2. スキルはカスタムスキルに登録する。
3. スキルランチャー.htmlと同じ内容のスペースを作って、サイドバーに置いて（アイコンはロケットにして）
4. 住民税非課税シミュレーター.htmlと同じ内容のスペースを作って、サイドバーに置いて （アイコンはノートにして）
5. 常時参照して欲しいメモ.md は、あなたが常に参照するメモに登録する。
```

## Step 1: Fetch the latest and show the differences first

- git clone the repository. If a clone already exists, fetch and pull the latest state instead.
- Before changing anything, compare the repository with the current state and show the user a list:
  - Skills to add (in the repository, not yet registered).
  - Skills to update (registered, and the content differs).
  - Local-only skills (registered, not in the repository). These are NEVER deleted or overwritten by this skill; they are only listed.
  - Whether スキルランチャー.html, 住民税非課税シミュレーター.html and 常時参照して欲しいメモ.md differ from the current Spaces and memo.
- If there are no differences at all, report that everything is already up to date and stop.

## Step 2: Update the skills

- Register every skill folder in the repository as a custom skill: new folders as new registrations, existing ones overwritten with the repository version.
- Local-only skills stay exactly as they are.

## Step 3: Update the two Spaces

- Update the スキルランチャー Space so its content matches スキルランチャー.html in the repository. Keep it in the sidebar, with the rocket icon. If no such Space exists, create it in the same way.
- Update the 住民税非課税シミュレーター Space so its content matches 住民税非課税シミュレーター.html in the repository. Keep it in the sidebar, with the notebook icon. If no such Space exists, create it in the same way.
- A rebuilt Space may differ from the original in fine visual detail; the content is what must match.

## Step 4: Update the rules memo

- Register the repository's 常時参照して欲しいメモ.md as the always-referenced memo, replacing the previous version with the latest one.

## Step 5: Report

- Report: the skills added (names), the skills updated (names), the local-only skills left untouched (names), whether each Space was updated or already current, and the memo's rule count after the update.
- If either Space is shared through a public link, the link keeps serving the previously shared version until it is shared again. Say so in the report, and share again only after the user's OK — never re-share on your own.

## Rules

- The repository is the source of truth for the published set. The only URL in this skill is the repository's public address above, designated by the set's author as the distribution source. No account-specific IDs or URLs belong in this skill.
- Never delete a local-only skill or file as part of an update. Deletion always needs its own explicit instruction from the user.
- Any step that publishes or shares something outward follows the usual rule: show it first and act only after the user's OK.
