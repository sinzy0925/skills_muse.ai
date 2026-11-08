# Templates and schemas

Adapted from the youtube-video-make skill in the skills-youtube-make repository for use inside Muse. Keep the Markdown files as the human readable copy and upload.json as the machine readable copy of the same content.

## Checkpoints

| Choice | After structure | After content | After narration | Images and package |
|--------|-----------------|---------------|-----------------|--------------------|
| A | stop | automatic | automatic | automatic |
| B | stop | stop | automatic | automatic |
| C | stop | stop | stop | automatic |
| D | automatic | automatic | automatic | automatic |

A stop means presenting the file and waiting for approval or corrections. Automatic means continuing without approval.

## Slide counts from video length

| Video length | Presentation | Manga |
|--------------|--------------|-------|
| 1 to 2 min | 5 to 7 slides | 6 to 8 panels |
| 3 min | 8 to 10 slides | 10 to 12 panels |
| 5 min | 12 to 15 slides | 15 to 18 panels |
| 10 min | 20 to 25 slides | 25 to 30 panels |

Counts are body slides or panels. Add one thumbnail slide on top. When the user says to propose a count, estimate from the amount of material in the notes using this table.

## source-notes.md

Created in the log summary phase when the input is a conversation log. Later phases treat this file as the only source.

```markdown
# Video notes from a conversation log

## Theme
{what app or procedure the log is about}

## Goal
{what the viewer will be able to do}

## Prerequisites
{accounts, tools and environment}

## Steps in time order
1. ...
2. ...

## Pitfalls and cautions
- ...

## Key commands, APIs or screens
- ...

## Parts a video can skip
- ...

## Source log
- File: {log path or id}
- Summary date: {date}
```

Never write secrets such as tokens or passwords into this file.

## Supplied images register

Record supplied images in brief.md in this form. The structure and content phases follow this register.

```markdown
## Supplied images
- file: screenshot-settings.png
  shows: the settings screen with the API key field
  planned slide: 4 (body, procedure step 2)
  role: procedure screenshot, used as-is
  reason: the notes explain this exact screen at step 2
```

Roles in use: procedure screenshot, product photo, evidence or result, cover or thumbnail material, character or style reference, before and after pair.

## structure.md

### Presentation form

```markdown
# Structure: {title}

## Summary
{one or two sentences on the point of the video}

## Slides
| # | Type | Title | Key point |
|---|------|-------|-----------|
| 1 | thumbnail | {video title, large} | doubles as the YouTube thumbnail, short hook narration |
| 2 | opening | {hook or question} | |
| 3 | body | | |
| N | ending | summary plus call to action | |
```

### Manga form

```markdown
# Structure: {title}

## Summary
{one or two sentences on the point of the video}

## Scenes
| # | Scene | Narration outline | What the image shows |
|---|-------|-------------------|----------------------|
| 1 | thumbnail | short hook | YouTube thumbnail, title text allowed |
| 2 | opening | | |
| N | ending | | |
```

## content.md

### Presentation form

```markdown
# Final content: {title}

## Slide 1, thumbnail
**Title**: {video title}
**Bullets**: none, the image leads
**Speaker notes**: doubles as the YouTube thumbnail, narration hook goes here
**Image direction**: 16 to 9 thumbnail, large title text allowed, style per brief.md

---

## Slide 2, opening
**Title**: {heading}
**Bullets**:
- {point 1}
- {point 2}

**Speaker notes**: {production notes and extra explanation}
**Image direction**: {what to draw, style per brief.md}
```

### Manga form

```markdown
# Final content: {title}

## Scene 1, opening
**Scene**: {what is happening}
**Narration outline**: {what this panel talks about}

**Image prompt elements**:
- Character: {fixed description, reused across scenes}
- Action: {what the character is doing}
- Setting: {place and mood}
- Style: {image style from brief.md}
- Text: none by default

---
```

For a recurring character, record the fixed description under a character settings section in brief.md and start every image prompt with it.

## narrations.md

```markdown
# Narration script

## Slide 1 / Scene 1
**Target time**: 15 seconds
**Script**:
{spoken text}

---
```

Keep one tone throughout. Write spoken language rather than a reading of the slide text.

## upload.json

Schema version 1. The thumbnail entry comes first in every file, created at package time and never appended later.

### Presentation form

```json
{
  "version": 1,
  "title": "Video title",
  "format": "presentation",
  "aspect_ratio": "16:9",
  "slides": [
    {
      "index": 1,
      "slide_type": "thumbnail",
      "title": "Video title",
      "bullets": [],
      "narration": "Short hook, about 8 to 15 seconds",
      "image": "images/thumbnail.png"
    },
    {
      "index": 2,
      "slide_type": "body",
      "title": "Slide title",
      "bullets": ["point 1", "point 2", "point 3"],
      "narration": "Spoken script, written into the speaker notes",
      "image": "images/slide-01.png"
    }
  ]
}
```

### Manga form

```json
{
  "version": 1,
  "title": "Video title",
  "format": "manga",
  "aspect_ratio": "16:9",
  "slides": [
    {
      "index": 1,
      "slide_type": "thumbnail",
      "title": "Video title",
      "narration": "Short hook, about 8 to 15 seconds",
      "image": "images/thumbnail.png"
    },
    {
      "index": 2,
      "slide_type": "body",
      "scene": "Scene memo for humans",
      "narration": "Spoken script, written into the speaker notes",
      "image": "images/scene-01.png"
    }
  ]
}
```

Field rules:

- version is always 1 and title is the Google Slides title.
- format is presentation or manga and aspect_ratio is 16:9.
- index values run from 1 with no gaps.
- slide_type is one of thumbnail, opening, body or ending.
- narration is required on every entry and becomes the speaker notes text.
- image is a relative path from the video folder with forward slashes.
- title and bullets are required in presentation form, and bullets may be an empty array on the thumbnail entry.
- scene is a human memo in manga form and is not used by an upload.

## Image prompts

### Presentation support image

```text
{style} style illustration, 16:9 aspect ratio.
Subject: {concept or diagram content}.
Simple, clean, no text, no watermark.
Colors: {palette direction}.
Purpose: supplementary visual for a presentation slide about {topic}.
```

### Manga scene image

```text
{style} style scene illustration, 16:9 aspect ratio.
Character: {character settings from brief.md}.
Action: {action and expression}.
Setting: {background and place}.
No text, no speech bubbles, no watermark.
Consistent character design across scenes.
```

### Thumbnail

Use the same style family as the body images, add the video title as large text inside the image, and favour a composition with contrast and clear empty space that stops the eye in a feed.
