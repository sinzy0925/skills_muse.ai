# Short Movie Maker (60-second narrated shorts)

## What this skill does

Make one vertical short movie (about 60 seconds) about a theme the user gives — for example introducing a skill, a product, or an announcement:

- **Picture:** AI-generated video clips, one per scene. A single generated clip is about 10 seconds and its length cannot be chosen, so the movie is always built at the maximum length one request can produce: **6 scenes × about 10 seconds = about 60 seconds**.
- **Sound:** the generated clips' own audio is never used (it often comes out strange — odd voices and noises). Instead, a spoken narration is synthesized for each scene and laid over the picture, replacing the original audio entirely.

Two rules define this skill and are never skipped:

1. **Maximum length, always.** The movie is 6 scenes, about 60 seconds. Do not make a shorter version unless the user explicitly asks for one.
2. **Confirm the content first.** The scene plan and every narration script are shown to the user in full, and nothing is generated until the user says OK.

Longer stories are made as **multi-part productions**: the story is split into parts of 6 scenes (about 60 seconds) each, every part is produced with the same flow in its own request, and the finished parts are concatenated at the end (two parts ≈ 120 seconds, and so on). When a character appears, one reference image (a character sheet) and one fixed character description are decided before part 1 and reused for every scene of every part, so the same character carries through the whole story — see "Multi-part productions" below.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never start a production, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not collect any theme and do not generate anything.
  - **B — actually use it:** Tell them 「入力項目を確認してから説明します」, then collect the input items of Step 1 (the theme, and the mood/style if they have one), and explain using the sheet together with how those items will be used, before starting production.

## Ground rules

- **Pre-confirmation is a hard gate.** Scene plan + narration scripts first, user OK, then generation. If the user asks for changes at the gate, revise the plan/scripts and show them again; the chart of what will be generated is what the user approved.
- **Never use a generated clip's audio.** The final movie's only sound is the narration (plus the silence padding it to each scene's length). Do not "keep the music a little" — generated audio is exactly what this skill exists to avoid.
- **One voice for the whole movie.** All scenes use the same narration voice. If any scene's narration does not fit its 10 seconds with the first voice, switch voices and re-synthesize **all** scenes with the new voice; never mix voices scene by scene.
- **Measure, don't estimate.** Every narration file's duration is measured before assembly. A scene is ready only when its narration is 10 seconds or shorter.
- **Generation limits.** At most 6 video clips per user request — that is why the movie is 6 scenes. If a clip fails, only the failed clip may be regenerated; successful clips are kept.
- **Fixed references for continuing characters.** When a production has a character, the character sheet (reference image), the fixed character description and the narration voice are decided once, confirmed at the first gate, stored with the production's files, and reused unchanged in every part. Never redesign the character midway.
- **No fixed URLs or IDs.** Themes, titles and end-card text come from the user at run time and are never baked into this skill.

## Step 1: Collect the inputs

- **テーマ／題材** (required — what the movie is about: a skill name, a product, an event, an announcement…)
- **雰囲気** (optional — default: クールでかっこいい感じ. If the user names a different mood, use that)
- **締めの文言** (optional — end-card text such as where the thing is available; if the user gives none, propose one at the confirmation gate)

If the theme is missing, stop and ask. Do not guess a theme.

## Step 2: Write the plan (6 scenes + narration scripts)

- Split the theme into **6 scenes**: hook → what goes in / the setup → the key steps (2–3 scenes) → the finish → closing/end card. Adapt the middle to the theme, but keep the count at 6.
- For each scene write two things:
  - **映像イメージ**: what the clip shows, in one or two lines. All six share one style description (vertical 9:16, the chosen mood, one consistent visual world) so the clips look like one movie.
  - **ナレーション原稿**: what is said over that scene. Guide: about 40–60 Japanese characters per scene — at a normal reading pace that fits inside 10 seconds. The script is what will be read word for word, so write it as it should sound (numbers and abbreviations spelled as spoken).

## Step 3: Pre-confirmation gate

- Show the user the full plan: all 6 scenes with their picture ideas and narration scripts, the total length (about 60 seconds), and the end-card text.
- Generate **nothing** until the user says OK. Apply requested edits and re-show the changed parts.
- **Destination check (only when the total exceeds 60 seconds).** If the planned total length is over 60 seconds (any multi-part production), also ask where the finished movie will be posted, and check the plan against that destination's video-length limit before anything is generated:
  - YouTube Shorts: up to 3 minutes
  - Instagram Reels: up to 3 minutes
  - Instagram Stories: 60 seconds per video — anything longer cannot be posted as one Story
  - X (Twitter): 140 seconds on free accounts; longer videos need a paid plan
  - TikTok: up to 60 minutes for uploaded files
  If the plan exceeds the chosen destination's limit, say so at the gate and propose adjusting the number of parts (or splitting the post). If the user has not decided the destination yet, asking is enough — do not block production on it. A single about-60-second movie fits all of the above, so this check is skipped for one-part productions.

## Step 4: Generate the 6 clips

- Generate one clip per scene (6 in total), vertical 9:16, each with its scene-specific request plus a shared context block (the movie's theme, the scene's role, the shared style, and any on-screen text for that scene — text to appear on screen is written in Japanese).
- If the production has a character sheet, pass the reference image as an image input to every clip generation, and include the fixed character description verbatim in every scene's context block.
- Keep the successful clips; regenerate only a failed one.

## Step 5: Synthesize and measure the narration

- Synthesize one narration audio per scene from the approved scripts, all with the same voice, in the scripts' language.
- Measure every file's duration. All must be ≤ 10 seconds.
- If any scene is over 10 seconds: choose a faster-paced voice and re-synthesize **all six** scenes with it, then measure again. (Reading pace differs a lot by voice; the default voice can be far too slow for a fixed sentence.) Repeat until all six fit. Never speed up audio with tempo processing as a first resort, and never trim an approved script without telling the user.

## Step 6: Assemble

- For each scene: take the clip's picture only, lay its narration over it, and pad the audio with silence to exactly the clip's length (10 seconds).
- Concatenate the 6 scenes in order into one file (ffmpeg concat; re-encode only if the clips' parameters differ).

## Step 7: Verify and deliver

- Verify before delivering: total duration is about 60 seconds, and audio is actually present in every scene (check the sound level of a few seconds inside each scene — a silent scene means a failed mix, fix it before delivering).
- Deliver the movie attached in the chat, with a one-line summary of the scene flow. Mention honestly anything that came out imperfect (for example, decorative on-screen text in generated clips can be garbled in places).
- If the user wants changes afterwards: picture changes mean regenerating that scene's clip; wording changes mean re-synthesizing that scene's narration (same voice as the rest) and re-assembling. The other scenes stay untouched.

## Multi-part productions (longer stories)

- Split the story into parts of 6 scenes each (part 1, part 2, …). Each part runs the normal flow (Steps 1–7) in its own request, because one request can generate at most 6 clips. Keep each part's finished file; the parts are the building blocks of the full movie.
- **Before part 1 — fix the character.** Generate one character sheet: a single reference image showing the character full-body, front view, with the design features clearly visible. Write the fixed character description (hair, outfit, colors, distinguishing features) as one exact text. Show both at part 1's pre-confirmation gate; once approved, store them with the production's files and never change them for the rest of the story.
- **Every scene, every part:** pass the character sheet as an image input to the clip generation and include the fixed character description word for word in the scene's context. Use the same narration voice across all parts.
- **Assembly:** when all parts are done, concatenate the part files in story order into one full movie. Verify the total duration (parts × about 60 seconds) and that every part has its narration, then deliver the combined movie (the individual parts stay available too).
- The destination check in Step 3 applies to the whole story's total length; run it once, at part 1's gate.
- **Honest limit:** generated video cannot promise a pixel-identical character. The reference image plus the fixed description make the character recognizably the same across parts; fine details (facial details, small accessories) may still drift slightly. Say this at the gate when a character is involved, not after delivery.

## Cautions

- The generated clips may contain on-screen text that is decorative rather than exact; the narration carries the real information. If exact on-screen text matters (names, prices), say so at the gate and prefer short, large text in the scene request.
- This skill makes the movie only. Posting it anywhere (Instagram, YouTube, …) is a separate step that needs its own confirmation.
