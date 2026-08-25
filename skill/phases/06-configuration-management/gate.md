# PHASE 06 GATE

Full criteria: `gates/G6-release.md`.

Quick form for `RIGOUR` 1 to 2:

1. Everything is committed; nothing important is local-only.
2. The release is built from a tagged commit.
3. There is a rollback, and someone has actually tried it.
4. The changelog says what changed, in words a user could read.

The rollback rehearsal is the criterion people skip and later regret. At `RIGOUR` 1 it can be as
small as "we checked that deploying the previous tag works". It cannot be nothing.
