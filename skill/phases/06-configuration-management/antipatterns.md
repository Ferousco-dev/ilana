# PHASE 06 ANTI-PATTERNS

## The Snowflake Environment
Production was configured by hand over three years. Nobody can reproduce it. The source material
names environment inconsistency as the classic cause of deployment failure.
**Fix:** infrastructure as code. The G6 environment-drift question, asked every release.

## The Untagged Release
Deployed from `main` at whatever commit it happened to be. Now nobody can say precisely what is
running, and rollback means guessing.
**Fix:** tag every release. Deploy from the tag, never from a branch.

## The Rehearsed-Never Rollback
A rollback plan exists in a document. It has never been executed. On the night it is needed, it
turns out step 4 does not work.
**Fix:** rehearse it. Record the date. Re-rehearse when the architecture changes.

## The Secret in History
Removed from the working tree, still in the commit history, still in every clone.
**Fix:** rotate the secret; removal is cosmetic. Add secret scanning to CI so the next one is
caught before it lands.

## Change Approved Then Analysed
The change is approved because someone senior wants it. Impact analysis happens during
implementation, when the cost is discovered rather than estimated.
**Fix:** Article 11. Impact analysis is an input to the approval decision, not an output.

## The Long-Lived Branch
A feature branch open for three months. Merging it is now a project of its own, and every
conflict is resolved by whoever is least tired.
**Fix:** short-lived branches, feature flags, and merge frequency as a tracked metric.

## Commit Messages That Say Nothing
"fix", "update", "wip", "changes". The history is the only permanent record of *why*, and this
throws it away.
**Fix:** one line stating the change, one paragraph stating why, and the `CR` or `REQ` ID.

## Direct Push to Main
No review, no CI, no record. Every control in phases 04, 05 and 07 is bypassed in one command.
**Fix:** branch protection above RIGOUR 2.

## The Emergency Change That Skips Everything
Production is down, so the fix goes straight in. That is often correct. The failure is not
writing the `CR` afterwards.
**Fix:** emergency changes get a retrospective `CR` within one working day, with the emergency
justification recorded.

## Documentation Not Under Control
Code is versioned. The SRS lives in a shared drive with filenames ending `_final_v3_REAL`.
**Fix:** documentation is a configuration item. It goes in the repository.
