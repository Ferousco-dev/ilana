# Changelog Convention

`CHANGELOG.md` is written for humans who use the software, not for machines that parse commits.
Keep a Changelog format, semantic versioning.

```markdown
# Changelog

All notable changes to this project are documented in this file.
Format: Keep a Changelog. Versioning: Semantic Versioning.

## [Unreleased]

## [1.3.0] - 2026-08-25
### Added
- Overdue fine calculation for late returns (REQ-007).

### Changed
- Search now matches on author as well as title (CR-011).

### Deprecated
- The `/v1/search` endpoint. Removal planned for 2.0.0. Use `/v2/search`.

### Removed
- Bulk spreadsheet import, withdrawn by CR-003.

### Fixed
- Fines were computed as zero for returns exactly on the due date (DEF-007).

### Security
- Session tokens are now rotated on privilege change (DEF-012).
```

## Rules

1. **Written for users**, in their vocabulary. "Refactored the DAO layer" belongs in commit
   history, not here.
2. **Every entry traces** to a `REQ`, `CR` or `DEF` identifier.
3. **Security fixes get their own section**, always, even when the detail must stay vague until
   users have upgraded.
4. **Deprecations announce the removal version.** Removing something with no prior deprecation
   entry is a broken promise to your users.
5. **Unreleased section is maintained continuously**, not assembled in a panic at release time.

## Version numbering

| Change | Bump |
| --- | --- |
| Incompatible interface change | major |
| Backwards-compatible functionality | minor |
| Backwards-compatible fix | patch |

Emergency releases still take a version number. "Hotfix" is not a version.
