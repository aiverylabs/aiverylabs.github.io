# Screenshot checklist — Survey Flow user guide

Work through this with the app open. Files go in `images/survey-flow/`.

Most items have a `<figure>` waiting in `survey-flow/user-guide.html`, commented out with the alt text
and caption already written: drop the file in, delete the two comment markers, done. Items marked
**placeholder pending** have no figure yet — see the note on each.

**Ranked by how much the prose struggles without the picture**, following
`csat/docs/feature-behaviour.md` §6. The first three are not illustrations. They are the correction.

⚠️ **The survey page renders the customer's own words.** Use a seeded test board, never a real
response, and check the ticket title in frame — that is customer content too.

Last updated 11 September 2026.

---

## Stale means somebody looked

**A capture is stale when a person compared it against the live app and it differed. A ticket saying
the screen changed is a reason to look, and nothing more.**

The first version of this file read CFM-154 and CFM-162 — both of which say a *screen* changed — and
recorded five captures as stale. The 2026-09-10 audit compared all five. Four were fine. The fifth,
`05-board-picker`, had a correct image and wrong words around it, so the flag pointed at the wrong
artifact entirely. Four comparisons spent disproving claims this file should not have made.

⚠️ **Same shape as the rest of the week: a confident record nobody had checked.** A ticket describes
the code at the moment it was written. It is not evidence about a screenshot, a document, or anything
else downstream. **Flag from a comparison, or write "check this" and name what prompted it.**

### ⚠️ And that rule is necessary, not sufficient: the comparer has to know what changed

`17-response-detail` passed the 2026-09-10 audit and is stale anyway. The comparison genuinely
happened — but the person doing it did not yet know the outstanding labels and the create-follow-up
action existed, so they were comparing against an out-of-date idea of what the screen should contain.
Everything they were looking for was present. Nothing they were not looking for registered.

**An audit against a stale understanding returns a confident clean result**, and a clean result is
harder to revisit than no result, because the file now says somebody checked.

This is the week's failure one level up. Not a record nobody checked — a check nobody could have
passed. The defence is to compare against *what changed since the capture*, named from the code or
the release, and to re-audit anything whose feature area has moved since it was last looked at, even
when it has a clean verdict against it.

---

## ⚠️ Outstanding — 2 of 15

### `37-next-vs-send.png` — RECAPTURE, the frame does not show what it needs to
**What landed:** two panels of the same survey side by side, and **both show an empty box with the
button reading Next.** The Send state is not in the frame, so the image does not demonstrate the
distinction it exists for. Its figure is left commented out in the page rather than published.
**What it needs:** the same turn twice — empty box reading **Next**, and something typed reading
**Send**. Type a word into the composer for the second crop; that is the whole difference.
**Note:** `38-band-change-warning` and `46-mode3-survey` both happen to catch a **Send** button, so
the state is not unphotographable — it just is not in this file.
**Lands in:** §5, under *Next and Send are different buttons*.

### `01-marketplace-install.png` — blocked, not your fault
Still the only broken image on the published page, and still blocked until the app is listed on the
marketplace, because the listing is the subject.

---

## Landed and wired — 13 of 15

All of these are uncommented in the page, with alt text and captions checked against the image
itself rather than against what was requested. Where they differed, the words were changed.

| File | Lands in | Alt text |
| --- | --- | --- |
| `36-survey-thread` | §5, *It is a conversation* | rewritten — it is mode 3, so the opening question is AI written, and two answers are already sent |
| `38-band-change-warning` | §5, *Changing the rating* | as written; the dialog names "the three answers you have given" |
| `39-config-groups` | §3, after the three groups are named | **placed** — no restructuring needed, it sits with the paragraph describing the groups |
| `41`+`42-mode1` | §3, *Let AI write some of the questions* | rewritten — 42 shows a Choose one question, which the old alt did not mention |
| `43`+`44-mode2` | same | rewritten — 43 also shows topics to avoid and the one-or-two setting |
| `45`+`46-mode3` | same | rewritten — 45 shows the fallback questions, which changed the prose too |
| `40-question-editor` | §3, *Show a question only to some raters* | **placed** — the type dropdown and the bands are in one frame, as asked |
| `31-connect-admin-only` | §2, *Only an admin can connect* | rewritten — the frame also carries a readiness checklist |
| `32-followup-destination` | §3, *Where follow up items go* | rewritten — and it corrected the prose, see below |
| `17-response-detail` | §6 | **both rewritten**; the figure was already live and described the old frame |
| `33-followup-item` | §7, *Follow up items* | as written |
| `35-sidekick-skills` | §8 | as written — both skills visible and toggled on |

⚠️ **`43-mode2-setting` arrived as `43-mode2-setting .png`, with a space before the extension.** It was
renamed. A space in a filename does not fail loudly: the reference simply does not resolve and the
page shows a broken image.

## ⚠️ Three prose errors the pictures caught
Recorded here because it is the argument for taking them at all, not just for publishing them.

1. **Question types.** `feature-behaviour.md` gave the UI names as *short answer / choose one /
   choose several*. The dropdown says **Short text / Choose one / Choose multiple**.
2. **Where follow-up items go.** That file's group-3 line reads as though the destination sits inside
   *Mark what is still outstanding*. The screenshot shows it is a block of its own, above it. This
   was the fourth version of that sentence, and it settled back to the second.
3. **The How it runs strip** has five steps, not four.

**A document read from the code is closer to the product than a ticket is, and still not the
product.** Both `32` and `39` show the same thing and neither was taken to check it — the pictures
were for the reader, and they audited the prose on the way past.

---

## Lower value — prose already carries these
From `feature-behaviour.md` §6: the invitation email, the thank-you screen, and the individual end
states (expired, already rated, withdrawn, superseded, paused). Each is a short page whose words are
the content. `12-email-received` and `14-thank-you` already exist and are fine.

## Audited and correct — do not reflag
Compared against the live app on 2026-09-10: `23-ticket-columns`, `03-authorize`, `05-board-picker`
(image), `08-questions`, `04-empty-state`, `11-activate`, `16-dashboard`, `29-agent-view`.

⚠️ `17-response-detail` **was on this list and has been removed** — see item 11. It is the reason the
list carries a date: a clean verdict is only as good as what the comparer knew to look for on the day,
and these were cleared before the outstanding labels and the follow-up action were understood. If a
feature has shipped into one of these screens since 2026-09-10, that verdict does not cover it.

⚠️ `13-survey-page` was **not** in that audit and is the one existing capture most likely to be
wrong, because it is captioned as a page and the page is a thread. Compare it before trusting it; if
it shows a static form, it predates the conversation UI and item 1 replaces it rather than joining it.
