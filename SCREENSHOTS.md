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

## 1. `36-survey-thread.png` — NEW, highest value
**Shows:** the survey mid conversation — one answer already sent and sitting in the thread, the next
question arriving below it. Take it in **mode 2 or 3** so an AI-written question is visible.
**Why first:** the guide's biggest error was describing a form. No sentence conveys "it is a
conversation" as fast as this frame does.
**Lands in:** §5, under *It is a conversation, not a form*.

## 2. `37-next-vs-send.png` — NEW
**Shows:** the same turn twice — empty answer box with the button reading **Next**, and a filled box
with it reading **Send**. Two crops in one image is fine.
**Why:** the distinction is behavioural (Next skips the question) and completely invisible in prose.
**Lands in:** §5, under *Next and Send are different buttons*.

## 3. `38-band-change-warning.png` — NEW
**Shows:** the confirmation dialog when a customer re-rates across a band, **with the count of answers
about to be lost visible**. The count is the part nobody believes without seeing it.
**Setup:** answer two or three questions at 5 stars, then change the rating to 2.
**Lands in:** §5, under *Changing the rating can discard answers*.

## 4. `39-config-groups.png` — NEW, ⚠️ placeholder pending
**Shows:** the configuration screen with all three group headings visible — *Set up*, *Refine your
survey*, *Act on what comes back* — sections collapsed. One frame, whole shape.
**Why:** it is the only way to convey the screen's structure, and it fixes the two placements people
get wrong: the AI modes live under *The opening question*, and Score/Comment live under *Show on the
ticket* rather than in *Set up* with the other columns.
**Lands in:** §3, near the top. **No figure in the page yet** — it goes in with the §3 corrections
still to be agreed.

## 5–7. The three mode pairs — NEW, replacing `34-ai-question-mode`
Six files, taken as three pairs. Each pair is **the setting, then the survey a customer gets under
it**, so the connection is visible rather than asserted. `34-ai-question-mode.png` is retired: it
showed only the off state, which is the one mode that needs no picture.

**5.** `41-mode1-setting.png` + `42-mode1-survey.png` — *Fixed questions*. The survey shows the
comment question then your configured questions, nothing generated.
**6.** `43-mode2-setting.png` + `44-mode2-survey.png` — *Ask more when needed*. The survey shows a
generated question following the customer's comment, then your questions. Capture the setting with
its credit-cost line in frame.
**7.** `45-mode3-setting.png` + `46-mode3-survey.png` — *Questions per ticket*. The survey shows an
AI-written opening question, then the conversation, then your questions.

⚠️ In all three survey frames, **your configured questions must be visible at the end.** That is the
fact the pairs exist to prove, and the one the guide got backwards.
**Land in:** §3, under *Let AI write some of the questions*.

## 8. `40-question-editor.png` — NEW, ⚠️ placeholder pending
**Shows:** the follow-up question editor with one question expanded — the type selector and the three
band toggles together in one frame.
**Why:** three question types and three bands, described in prose, read as six unrelated facts.
**Lands in:** §3, under *Show a question only to some raters*. **No figure in the page yet** — it goes
in with the §3 corrections.

## 9. `31-connect-admin-only.png` — NEW
**Shows:** the welcome screen as someone who is *not* an account admin sees it — no Connect button,
and the line saying an admin needs to connect the account. Sign in as a board owner who is not an
admin; an admin's own screen is the wrong picture.
**Lands in:** §2, under *Only an admin can connect the account*.

## 10. `32-followup-destination.png` — NEW
**Shows:** the follow-up item destination — board and optional group. ⚠️ It sits **inside the *Mark
what is still outstanding* section**, in the *Act on what comes back* group, alongside the labelling
feature. Frame enough of that section to show where it lives.
**Lands in:** §3, under *Where follow up items go*.

## 11. `17-response-detail.png` — ⚠️ RECAPTURE, was wrongly cleared
**Shows:** one response with **the rating, the comment, the outstanding label, and the
create-follow-up action, all in one frame**. The label and the action are what the existing capture
is missing; a crop showing only the rating and comment reproduces the error.
⚠️ Fabricated comment.
**Why it is here again:** it was in *audited and correct* until 2026-09-11. See the note above — the
comparison ran against an understanding that predated both features.
**Lands in:** §6 Read your results. The figure is live in the page rather than commented, so the file
drops straight in — but **update its alt text and caption when it does**, since both currently
describe a frame with no label and no action in it.

## 12. `33-followup-item.png` — NEW
**Shows:** one follow up item on a board with its update open — rating and date, the outstanding
label, the comment, the answers. The item name too, since it carries the ticket title.
⚠️ Fabricated comment. This is the frame most likely to publish a real customer's words.
**Lands in:** §7, under *Follow up items*.

## 13. `35-sidekick-skills.png` — NEW
**Shows:** the two Survey Flow skills in monday's Sidekick tools list, named as a user sees them.
**Lands in:** §8.

## 14. `01-marketplace-install.png` — NEW, blocked
Referenced by §1 and not on disk, so the page carries one broken image today. It cannot be taken
until the app is listed on the marketplace, because the listing is the subject. Unlike every item
above, this `<img>` is live rather than commented, which is why the gap shows on the published page.

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
