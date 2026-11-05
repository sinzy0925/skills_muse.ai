# Worked examples

Adapted from the examples of the source skill, with the Muse phrasing for questions and options.

## Example 1, minimal input, all four parameters asked

User input:

```text
I want a video about the Cursor skill feature.

- Skills are written in SKILL.md
- The agent loads them automatically
- There are personal and project skills
- Roughly, this is how you make one
```

Agent response at the parameter check, with the format and checkpoint offered as reply options and the rest as plain text in the same message:

```text
I will make the video materials. Please tell me:
1. Length and slide count, for example about 3 minutes and 8 slides, or ask me to propose
2. Image style, for example flat illustration or anime style
```

After the user answers "presentation form, about 3 minutes, flat illustration, checkpoint B", the flow runs structure, stops for approval, then content, stops for approval, then narration, images and packaging run automatically.

## Example 2, format named in the request

User input:

```text
In manga form, draw a day in the life of someone who started programming as a side job.
Waking up and writing code, fighting a bug at midday, finishing and celebrating at night.
About 5 minutes. Watercolour style. Run everything automatically.
```

Agent response at the parameter check:

```text
Confirmed from your message:
- Format: manga (named)
- Length: 5 minutes, so about 15 to 18 panels proposed
- Image style: watercolour
- Checkpoint: D (fully automatic)

Starting now.
```

No questions are asked and the structure phase begins.

## Example 3, revision at checkpoint B

User feedback after the structure:

```text
Change slide 3 from benefits to who this suits.
Delete slide 5. Add a channel subscribe prompt to the ending.
```

The agent edits structure.md, shows the revised structure again, and moves to content only after approval.

## Example 4, completion report

```text
The materials are ready.

~/workspace/youtube-videos/cursor-skill-intro/
- brief.md: recorded parameters
- structure.md: structure, 10 slides including the thumbnail
- content.md: final slide text
- narrations.md: narration script, about 3 minutes in total
- upload.json: machine readable package for the Google Slides upload
- youtube-meta.md: title ideas, description and tags
- images/: thumbnail.png and slide-01.png to slide-09.png
- manual-steps.md: Google Slides to Vids to YouTube steps

Next step: ask me to put the deck into Google Slides, or follow manual-steps.md after the deck URL is in slides-result.json.
```

## Example 5, conversation log input

User input:

```text
Make a how-to video from this Cursor conversation log.
```

The agent reads the attached jsonl in chunks, writes source-notes.md, and shows the summary first. Only after the user approves the summary does the parameter check begin, and the raw log is never used as the source for the structure.
