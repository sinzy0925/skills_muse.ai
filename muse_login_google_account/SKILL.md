# Google Account Login in the Built-in Browser

Get Muse's built-in browser signed in to a Google account, so that other work (Gemini, YouTube Studio, Drive, Slides and similar) can use Google services in that browser. The sign-in itself is always done by the human. Muse opens the way, hands the browser over, and verifies the result.

## Configuration

- The target account is designated by the user at run time. Never write a specific account name, email address or password into this skill.
- Signing in to an existing account is in scope. Creating a new Google account is out of scope: Google may block account creation from this browser, and creation needs the human's own device and phone.

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
