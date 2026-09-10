# Screenshot checklist — Survey Flow user guide

Work through this with the app open. Files go in `images/survey-flow/`.

Every item below has a `<figure>` waiting for it in `survey-flow/user-guide.html`, commented out with
the alt text and caption already written. Drop the file in, delete the two comment markers around the
figure, done — no prose to write.

⚠️ **Anything a customer wrote is published the moment the file lands.** Use fabricated comments and
fabricated names in every frame that shows feedback — item 3 especially.

Last updated 11 September 2026.

---

## ⚠️ Stale means somebody looked

**A capture is stale when a person compared it against the live app and it differed. A ticket saying
the screen changed is a reason to look, and nothing more.** Those are different claims, and this file
made the wrong one four times.

The first version of this checklist read CFM-154 and CFM-162 — both of which say a *screen* was
restructured — and recorded five captures as stale. The 2026-09-10 audit compared all five. Four were
fine: `23-ticket-columns` was cropped tightly enough that whatever moved beside it was out of frame,
`03-authorize` is monday's own screen and CFM-162 changed who reaches it rather than what it shows,
and `08-questions` and `17-response-detail` were unchanged. Four comparisons spent disproving claims
this file should never have made.

The fifth, `05-board-picker`, was a real defect — but not the one recorded. **The image was correct
and the words around it were wrong**, describing a board picker that does not exist. The stale flag
pointed at the wrong artifact entirely.

⚠️ **This is the same shape as the errors this codebase kept turning up all week: a confident record
that nobody had checked.** A ticket describing a change is evidence about the code at the moment it
was written. It is not evidence about a screenshot, a document, or anything else downstream — and
writing it down as though it were converts a reason to look into a fact that gets acted on.

**So: flag from a comparison, or write "check this" and say what prompted it.** Never write "stale"
from a ticket alone.

---

## The captures

### 1. `31-connect-admin-only.png` — NEW
**Shows:** the Survey Flow welcome screen as someone who is *not* an account admin sees it — no
Connect button, and the line saying an admin needs to connect this account before surveys can be set
up. Sign in as a board owner who is not an admin; an admin's own screen is the wrong picture.
**Lands in:** §2 Authorize access, under *Only an admin can connect the account* (last thing in the
section).

### 2. `32-followup-destination.png` — NEW
**Shows:** the *Where follow up items go* block, under **Act on what comes back** on the configuration
screen. Frame the whole block including its heading, so someone hunting for it on screen recognises
where it sits. Both fields visible: destination board, and the optional group.
**Lands in:** §3 Build your first survey, under *Where follow up items go* (between the low rating
alert and *Test once, then switch it on*).

### 3. `33-followup-item.png` — NEW
**Shows:** one follow up item on a monday board with its update open — the rating and date, the
outstanding label, the customer's comment, and the answers. The item name should be visible too, since
it carries the ticket title.
⚠️ Fabricated comment. This is the frame most likely to publish a real customer's words.
**Lands in:** §7 Act on what comes back, under *Follow up items*.

### 4. `34-ai-question-mode.png` — NEW
**Shows:** the AI question setting **in its off state**. Off-by-default is the claim the picture is
there to support, so capture it before switching anything on. If the setting names its three modes,
frame them — the guide now lists all three and a reader will look for them here.
**Lands in:** §3 Build your first survey, under *Add an AI question*.

### 5. `35-sidekick-skills.png` — NEW
**Shows:** the two Survey Flow skills in monday's Sidekick tools list, named as a user sees them.
**Lands in:** §8 Ask Sidekick about your feedback.

### 6. `01-marketplace-install.png` — NEW, blocked
Referenced by §1 and **not on disk**, so the page carries one broken image today. It cannot be taken
until the app is listed on the marketplace, because the listing is the subject. Unlike the five above,
this `<img>` is live rather than commented, which is why the gap is visible on the published page.
Leave it until the listing exists, or comment the figure out if a broken image is worse than no image.

---

## Audited and correct — do not reflag

Compared against the live app on 2026-09-10: `23-ticket-columns`, `03-authorize`, `05-board-picker`
(image), `08-questions`, `17-response-detail`, `04-empty-state`, `11-activate`, `16-dashboard`,
`29-agent-view`. The four prose errors that audit turned up are fixed in the guide as of
11 September 2026.

The remaining captures in the guide were never in question: no ticket names them and none of the text
around them has changed.
