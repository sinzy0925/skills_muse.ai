# Google Account Login in the Built-in Browser

Get Muse's built-in browser signed in to a Google account, so that other work (Gemini, YouTube Studio, Drive, Slides and similar) can use Google services in that browser. The sign-in itself is always done by the human. Muse opens the way, hands the browser over, and verifies the result.

## Configuration

- The target account is designated by the user at run time. Never write a specific account name, email address or password into this skill.
- Signing in to an existing account is in scope. Creating a new Google account is out of scope: Google may block account creation from this browser, and creation needs the human's own device and phone.

## Usage sheet (show it when asked)

- This skill ships with `使い方シート.md`, a plain-language explanation of how to use it, written for the operator and for anyone they hand the skill to.
- Whenever anyone asks how to use or explain this skill （使い方を教えて, 説明して, how does this work, and similar), start with the one-line summary from the top of the usage sheet (what the skill does, in one sentence), then ask which of the two they want. Never ask A or B before that summary: the listener cannot choose before knowing what the skill is. Downloading and extracting this repository's ZIP and registering the skill are prerequisites shared by every skill in the collection, so do not explain them here. Many people only want to hear the explanation and will never run the skill, so never push a setup or a run on someone who only asked a question:
  - **A — explanation only:** Show the usage sheet as-is (paste its full contents or attach the file). Do not improvise a different explanation and do not shorten the sheet; the sheet is the single source for the explanation. Do not open the browser or check anything.
  - **B — actually use it:** Tell them 「内蔵ブラウザでログイン状態を確認してから説明します」, then check the sign-in state in the built-in browser against the account the operator designates, hand the browser over for sign-in when needed, verify the displayed account after they finish, and only then explain, using the sheet.

## Hard rules

- Never ask the user to send a password, verification code or recovery code in chat, and never type one yourself. The human enters every credential and code directly into the browser.
- Muse does not perform the sign-in clicks on credential screens. Open the page, then hand the browser to the user (takeover) for everything from the sign-in form onward.
- Do not start other Google work until the sign-in is verified in Step 3.
- Report the signed-in account exactly as the page displays it (name and email). Never guess which account a session belongs to.
- Browser work follows the standing skip rule: when a screen makes no progress, do not grind on it. Report what state things are in and stop.

## Step 1: Check the current sign-in state

- Open a Google service page in the built-in browser, for example https://gemini.google.com/ or https://myaccount.google.com/.
- If an account is shown as signed in, read the displayed name and email from the account menu.
- If that is the account the user designated, you are done: report it and stop.
- If nobody is signed in, or a different account is signed in, go to Step 2. When a different account is signed in, do not sign it out on your own judgment: tell the user and ask whether to switch.

## Step 2: Hand the browser to the user to sign in

- Tell the user, in one short message, that the built-in browser is waiting at the Google sign-in screen and that they can take over the browser to sign in themselves.
- The user completes the whole sign-in themselves: email address, password, and any second factor such as a phone prompt or a code.
- Wait for the user to say they are done. Do not poll the page in a loop while they are signing in.

## Step 3: Verify and report

- After the user says they are done, reload the service page and open the account menu again.
- Confirm that the displayed name and email match the account the user designated.
- Report: which account is now signed in (exactly as displayed), and that Google services in the built-in browser are ready to use.
- If the sign-in did not complete or a different account is shown, say so plainly, with what the page shows, and ask the user how to proceed.

## Pitfalls

- The browser's sign-in state can lapse between sessions even after a successful sign-in. Always check the state at the start of work that needs it, instead of assuming a past sign-in still holds.
- A sign-in can trigger a security confirmation on the user's own phone. That confirmation is the user's to approve on their device; Muse cannot approve it.
- Signing in on one Google service signs the browser in for the others. Verify on the service you actually checked, and name that service in the report.
