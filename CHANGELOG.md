# Changelog

## Unreleased

### Added

- Added literal pin-name HV/DB exclusion helpers that honor native CEETIS per-pin test exclusions, provide optional selection-audit debug output, deduplicate complete modeled networks, and abort when exclusion results in zero attempted tests.
- Added a compact, content-sized TXT-oriented CEETIS manual-reading table builder with begin/add/finish lifecycle, atomic numeric row prompts, ATS-compatible state handling and function-call argument evaluation, exact once failure counting for failed rows and cancellation, cancellation-aware group results, continuous outer borders above titled tables, column-aligned segmented structural borders, deterministic word-boundary title and Reading wrapping with hard-split fallback for oversized unbroken tokens, 86-character maximum rendering, and user documentation for the required CEETIS validation checkpoint.
