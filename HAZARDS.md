# Hazards in these documents

Ways this repository goes wrong that **nothing catches**. Every entry here has already
happened at least once and produced a published error.

The common shape: **a fact lives in two places, and nothing enforces that they agree.** No
build breaks, no test fails, no link 404s. The wrong version just sits there looking exactly
like the right one.

Screenshot-specific hazards live in [`SCREENSHOTS.md`](SCREENSHOTS.md). What a given page has
and has not been checked against lives in a `PROVENANCE` comment at the top of that file.

---

## 1 · A section number is a name two documents share

⚠️ **Renumbering is renaming. Grep the other file for the number before shifting anything.**

`terms.html` pointed at "section 4 of the privacy policy" for who can see recipient
identities, and at "section 8" for what happens at uninstall. Both were correct when written.
Then a new section 4 was inserted into `privacy.html`, every later section shifted by one, and
the two pointers silently began naming **What we send to AI** and **How long we keep it**
instead.

⚠️ **Nothing could have caught it.** Both references still resolved to a real section with a
plausible heading. There is no broken link, no missing anchor, no failing check — a reader
following the pointer simply arrives somewhere else and has no way to know.

The renumbering *within* `privacy.html` was done carefully and verified. The pointers *into*
it from another file were never considered, because they are invisible from inside the
document being edited.

**Before you insert, delete or reorder any `<h2>`:**

```
python3 check-section-refs.py
```

It resolves every `section N` in all four documents to the heading that number currently
names, and prints them all. Read the list. The script can only catch a reference that points
outside the document's range — **a reference can resolve and still be wrong**, and only a
person reading the resolved heading can see that.

Run it before the change and after, and diff the two.

**Cheaper still:** prefer a link to a named anchor over a number in prose. `<a
href="privacy.html#visibility">` survives renumbering; "section 5 of the privacy policy" does
not. Several references already do this and they are the ones that have never broken.

---

## 2 · The same commitment written in two documents, on two clocks

`terms.html` §15 promised 14 days' notice before a material change took effect.
`privacy.html` §13 said an amended policy took effect **once we had notified you** — no notice
period at all.

Both were drafted deliberately. Neither drafter was looking at the other. And because
`terms.html` §1 makes the privacy policy *part of the agreement*, the two rules covered the
same event and disagreed, with the more customer-favourable one granted by accident in the
document that did not mean to grant it.

Aligned 2026-09-13: the policy now carries the same 14 days and says so explicitly, naming the
terms.

⚠️ **The general case:** when a promise appears in more than one document, one of them will be
edited alone. Before changing any commitment — notice periods, retention, response times,
allowances — grep the other files for the same subject. A commitment is not a fact about one
page.

---

## 3 · Facts duplicated from a source nothing links to

Several published statements are copies of something maintained elsewhere, with no mechanism
tying them together:

| Published here | Actually lives in | What breaks it |
| --- | --- | --- |
| The two outstanding labels, named in prose in `user-guide.html` | the backend's label set | removing or renaming a label; there is no migration to notice |
| Plan allowances, in `pricing.html` and `user-guide.html` | the backend's plan config and the monetization submission form | a cap changing in one and not the others |
| The 2 business day support commitment, `terms.html` §10 | monday's Marketplace Listing Terms | monday changing the required SLA |
| What reaches monday's AI, `privacy.html` §4 and `terms.html` §4 | the backend call sites | a new call site, or a field added to an existing one |

⚠️ **Nothing here fails when these drift.** The page keeps serving the old number with total
confidence. `PROJECT.md` §16 in the backend repo carries the production-verified values for
some of them and records, in row 9, that nothing links the two repositories.

When you change one of these, the docs repo is a separate, manual step — and it is the one
that is visible to customers.

### ⚠️ It runs the other way too: the RECORD OF these pages can be the stale copy

Everything above assumes the published page is the copy that drifts. On **2026-09-13** the
opposite happened, and it was more convincing than a stale page would have been.

`PROJECT.md` §16 row 11 in the backend repo — a register whose whole purpose is recording what
has been verified — stated that `pricing.html` and `user-guide.html` both still described a
**Starter** trial of 25 responses, called it "customer-facing", and said both "must be edited by
hand". Both pages had said **Pro / 400** since `3d62b6e` (2026-09-12), pushed to `origin/main`
the previous day. The row was wrong on the day it was written, and stayed wrong for four days.

⚠️ **THE TELL IS THE VERBATIM QUOTATION, AND IT IS THE THING THAT MADE IT CREDIBLE.** The row
quoted the exact live strings — *"metered against Starter's allowance, so 25 responses"* — plus a
whole paragraph about the allowance running out around day four. Quoting a string reads as
though the writer had the page open. In fact the quotes were inherited from an earlier version
of the same row, written on 2026-09-11 when they *were* current, and carried forward while the
claim around them was quietly upgraded from a **warning about the future** ("whatever the form
says, both must be edited to match") into an **assertion about the present** ("are now wrong").
The words that were quoted never changed; the tense of the claim built around them did.

**A verbatim quotation is evidence of copying, never of checking.**

⚠️ **AND A CLAIM CHANGING TENSE IS A NEW CLAIM.** "This will need updating" and "this is wrong
right now" need different evidence, even when the surrounding paragraph is otherwise untouched
and the edit looks like a rewording.

⚠️ **CONCRETE COST — DO NOT TRIM THIS TO A SUMMARY. IT IS THE ENTRY.** A session read row 11,
believed it, and wrote a prompt to correct two pages that were already correct. What that prompt
instructed was, precisely, restoring the Starter / 25-response copy that `3d62b6e` had replaced.
**That is a reversion of `3d62b6e`, described as a fix** — the backend's *record of* the docs
overwriting the docs. It is not a hypothetical: the prompt existed and said so. It did not run
because a human knew the pages had already been changed and said so before it went anywhere.

⚠️ That last clause is the uncomfortable part and belongs in the entry too: **nothing mechanical
stopped it.** No test, no link, no check in either repository can see a claim in one repo about a
file in the other. The only thing standing between the record and the pages it described was
somebody's memory of a commit they had made five days earlier.

**So: before acting on a record that says a published page is wrong, open the page.** Both
repositories are checked out on the same machine; it is one `grep`. That is cheaper than every
mechanism in the table above, and it is the only one that catches this direction.

---

## 4 · A published document can be ahead of the product

On 2026-09-12 `pricing.html` was updated with new allowances before the backend enforced them,
so the page promised 400 responses on Pro while the gate still cut off at 150. The gap was
closed the next day, but nothing in the repository knew it existed.

Docs changes ship on push. Code changes ship on deploy. **When a docs change describes
behaviour that has not shipped, say so in the commit message and know the window exists.**
