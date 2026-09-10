# Screenshot checklist — Survey Flow user guide

Work through this with the app open. Files go in `images/survey-flow/`.

**New captures** already have a `<figure>` waiting for them in `survey-flow/user-guide.html`, commented
out with the alt text and caption written. Drop the file in, delete the two comment markers around the
figure, done — no prose to write.

**Recaptures** overwrite the existing file at the same name. Nothing in the page needs editing, but
check the caption still describes what you captured.

⚠️ **Anything a customer wrote is published the moment the file lands.** Use fabricated comments and
fabricated names in every frame that shows feedback — items 9, 10 and 11 especially.

Last updated 10 September 2026.

---

## New captures

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
there to support, so capture it before switching anything on.
**Lands in:** §3 Build your first survey, under *Or let AI ask them*.

### 5. `35-sidekick-skills.png` — NEW
**Shows:** the two Survey Flow skills in monday's Sidekick tools list, named as a user sees them.
**Lands in:** §8 Ask Sidekick about your feedback.

---

## Recaptures — known stale

### 6. `03-authorize.png` — RECAPTURE (CFM-162)
**Why:** the connect flow is now admin gated, so the route to this screen changed and a non-admin
never reaches it.
**Shows:** the authorization screen with the full scope list, as an admin now reaches it.
**Lands in:** §2 Authorize access.

### 7. `23-ticket-columns.png` — RECAPTURE (CFM-154)
**Why:** inside the region restructured on 2026-09-10; the outstanding section beside it moved.
**Shows:** the columns that receive the score and the comment.
**Lands in:** §3, under *Choose what appears on the ticket*.

### 8. `05-board-picker.png` — RECAPTURE (CFM-154)
**Why:** the configuration screen was restructured on the same date and this capture predates it.
**Shows:** board selection. Check what else is now in frame before reshooting the old crop.
**Lands in:** §3, under *Pick the board*.

### 9. `08-questions.png` — RECAPTURE
**Why:** not in the ticket. The text around it was rewritten for the AI question modes, and the capture
predates them.
**Shows:** the question editor — fixed star rating, one follow up question. If the AI toggle is
visible in this region, decide whether it belongs here or only in item 4.
**Lands in:** §3, under *Write the questions*.

### 10. `17-response-detail.png` — RECAPTURE
**Why:** not in the ticket. A response now carries outstanding labels and the action that creates a
follow up item; neither is in the existing capture.
**Shows:** one response with its rating, comment, label, and the create-follow-up action.
⚠️ Fabricated comment.
**Lands in:** §6 Read your results.

---

## Worth checking while you are in there

No evidence these are stale — flagged because they show surfaces that have moved at least once since
capture, and nobody has audited them. Open each, compare, reshoot only if it differs.

### 11. `04-empty-state.png`
The empty state is the screen the connect gate changed. If an admin now sees something different
before the first configuration exists, this is stale.
⚠️ If it shows any real feedback, fabricate it.

### 12. `11-activate.png`
The configuration switched to active, on a screen that was restructured on 2026-09-10.

### 13. `16-dashboard.png`
The dashboard, which gained the labels and the follow up action elsewhere in the same release.

### 14. `29-agent-view.png`
The agent view. Same reason as the dashboard.

---

## Not yet possible

### 15. `01-marketplace-install.png`
Referenced by §1 and **not on disk**, so the page has one broken image today. It cannot be taken until
the app is listed on the marketplace, because the listing is the subject. The `<img>` is live rather
than commented, so this is the only item here that is visibly missing on the published page. Leave it
until the listing exists, or comment the figure out if the broken image is worse than the gap.

---

The other 20 captures in the guide are not listed here on purpose: no ticket names them, and none of
the text around them changed. If you are auditing everything anyway, they are the remainder.
