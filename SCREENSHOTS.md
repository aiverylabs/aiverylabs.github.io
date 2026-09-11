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

**And it happened twice, which is why it is a pattern and not bad luck.** The second was
`11-activate`, cleared by the same audit on the same day. The app was titled **"CSAT Surveys"** in it;
it is **"Surveys"** in every capture taken since. Nobody comparing it knew the product had been
renamed, so the title read as correct — the same failure as `17-response-detail` with a different
missing fact. One was a feature the comparer had not met; the other was a rename nobody had
mentioned. Neither is a lapse of care, and no amount of looking harder would have caught either.

This is the week's failure one level up. Not a record nobody checked — a check nobody could have
passed. The defence is to compare against *what changed since the capture*, named from the code or
the release, and to re-audit anything whose feature area has moved since it was last looked at, even
when it has a clean verdict against it.

**Both instances are now resolved** — `17-response-detail` recaptured 2026-09-10, `11-activate`
2026-09-11. They stay written up because the pattern is what is worth keeping, not the two files. A
resolved instance is still evidence; deleting it would leave the rule sounding like a precaution
rather than a description of something that happened here, twice, four weeks into a product.

⚠️ **Cheapest check first, before opening anything.** A collapsed section cannot carry stale copy; an
expanded one can. `39-config-groups` survived the labelling copy change for exactly that reason, with
its Act-on sections showing only summary lines. Sort captures by what is expanded in frame, and open
those. It is the one test here that costs nothing and rules things out rather than in.

---

## ⚠️ Outstanding — 1

### `01-marketplace-install.png` — blocked, not your fault
The only broken image on the published page. Blocked until the app is listed on the marketplace,
because the listing is the subject. Nothing else is waiting on anything.

⚠️ `11-activate` and `22-low-rating-alert` were both recaptured on 2026-09-11 and checked by opening
them. `11` now reads **Surveys** with a Live badge, the master toggle On, the Saved button at rest
and the confirmation line — no *Unsaved changes*. `22` is reshot with a different account. Alt text
and captions were rewritten for both rather than carried over: `22` had been out of the page for two
commits, and `11`'s old alt said only "the configuration switched to active", which describes less
than a third of what is now in frame.

---

## Landed and wired — 16 of 17

All of these are uncommented in the page, with alt text and captions checked against the image
itself rather than against what was requested. Where they differed, the words were changed.

| File | Lands in | Alt text |
| --- | --- | --- |
| `36-survey-thread` | §5, *It is a conversation* | rewritten — it is mode 3, so the opening question is AI written, and two answers are already sent |
| `37-next-vs-send` | §5, *Next and Send* | rewritten — names both states and the typed word, after a recapture |
| `38-band-change-warning` | §5, *Changing the rating* | as written; the dialog names "the three answers you have given" |
| `39-config-groups` | §3, after the three groups are named | **placed** — no restructuring needed, it sits with the paragraph describing the groups |
| `41`+`42-mode1` | §3, *Let AI write some of the questions* | rewritten — 42 shows a Choose one question, which the old alt did not mention |
| `43`+`44-mode2` | same | rewritten — 43 also shows topics to avoid and the one-or-two setting |
| `45`+`46-mode3` | same | rewritten — 45 shows the fallback questions, which changed the prose too |
| `40-question-editor` | §3, *Show a question only to some raters* | **placed** — the type dropdown and the bands are in one frame, as asked |
| `31-connect-admin-only` | §2, *Only an admin can connect* | rewritten — the frame also carries a readiness checklist |
| `32-outstanding-card` | §7, *Create them automatically* | rewritten, renamed, and moved — see below |
| `17-response-detail` | §6 | **both rewritten**; the figure was already live and described the old frame |
| `33-followup-item` | §7, *Follow up items* | as written |
| `35-sidekick-skills` | §8 | as written — both skills visible and toggled on |
| `11-activate` | §3, *Test once, then switch it on* | rewritten after recapture — the old alt covered under a third of the frame |
| `22-low-rating-alert` | §3, *Get told about unhappy customers* | rewritten after reshoot; see the note on its address below |

⚠️ **Two files have now arrived with a space before the extension** — `43-mode2-setting .png` and
then `35-sidekick-skills .png`. Both renamed. This one does not fail loudly: the reference stops
resolving, git reports a delete plus an untracked file, and the page shows a broken image. Twice is
enough to check for it on every drop: `ls images/survey-flow | grep " "` costs nothing.

## ✅ The copy change landed — both recaptures checked by looking

`32` and `35` were retaken on 2026-09-11 and the pending item is cleared. The card now reads "The
rating is sent to the AI with the comment and answers, but it does not decide which get marked: a
five-star response can be marked, and an angry one-star may not be", and "are not labelled" in place
of "are not read". `35` has scrolled past the card entirely.

**I checked every other capture shot on the configuration screen rather than reasoning about which
could be affected**, since reasoning is how `35` was nearly missed the first time:

- `39-config-groups` — **clean, and for a reason worth recording.** Its Act-on-what-comes-back
  sections are collapsed to summary lines ("On, suggesting"), so no card description is in frame.
  Collapsed sections are immune to copy changes; expanded ones are not. That is the test to apply
  next time rather than opening every file.
- `22-low-rating-alert`, `11-activate` — no labelling card in frame. Both turned up something else.

## `32-outstanding-card` — renamed, and moved to match what it shows

The recapture was cropped to the **labelling card alone**. The *Where follow-up items go* block, which
was the point of the original and the reason for the old filename, is out of frame — so the file is
now `32-outstanding-card.png`, and `32-followup-destination` is free for a real destination crop.

- The figure has been **moved** out of §3's *Where follow up items go* and into §7's *Create them
  automatically*, where its content — the rule box — is exactly the subject. Alt text and caption
  rewritten to the card.
- §3's *Where follow up items go* now carries no figure of its own. Not urgent: `39-config-groups`
  is in the same section and frames the destination block in context. A tighter crop would be better
  but nothing is broken.
- ⚠️ **The old name was a stale record of the same kind this file exists to catch**, just wearing a
  filename instead of a sentence. A name that sounds accurate is worse than one that sounds vague,
  because nobody opens the file to check it.

## `22-low-rating-alert` — the address in it is deliberate

⚠️ **The email address visible in this capture is a disused account belonging to the author, published
on purpose. It is not a leak and does not need reporting.** Recorded here because it is exactly the
kind of thing someone doing the right thing re-flags in three months, and the reflex to flag it is
correct — the answer just already exists.

The first version of this capture carried a different, live personal address and was pulled. What
follows is that history, kept because the reasoning is worth more than the incident.

### Why it was pulled the first time

It published a live personal email address as the notify target, legible at full size. The figure was
removed from §3 and **the file deleted from the repository**, not merely unreferenced: GitHub Pages
serves any file in the folder at its own URL whether or not a page links to it, so unreferencing alone
would have left the address fetchable.

⚠️ **It remains in git history**, which this cannot fix. If that matters, it needs a history rewrite,
and that is a decision rather than a cleanup.

⚠️ The old file **remains in git history**, which this does not fix. If that matters it needs a history
rewrite, which is a decision rather than a cleanup.

The section ran without a figure for two commits, which cost a reader very little — the right trade
when the alternative is leaving a real address on a public page until a reshoot arrives.

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
(image), `08-questions`, `04-empty-state`, `16-dashboard`, `29-agent-view`.

⚠️ Two of that day's clean verdicts have since been overturned, so read the date as the limit it is:
these were compared against what was known on 2026-09-10 and nothing since.

⚠️ `17-response-detail` **was on this list and has been removed** — see item 11. It is the reason the
list carries a date: a clean verdict is only as good as what the comparer knew to look for on the day,
and these were cleared before the outstanding labels and the follow-up action were understood. If a
feature has shipped into one of these screens since 2026-09-10, that verdict does not cover it.

⚠️ `13-survey-page` **has been deleted**, image and reference both. It was never in that audit, it
showed the old static form, and `36-survey-thread` covers the ground. It was removed from disk rather
than just unreferenced: a capture of a UI that no longer exists, sitting in the folder under a name
that sounds current, is the next person's stale source — and this folder is the kind of place someone
goes looking for "the survey page".
