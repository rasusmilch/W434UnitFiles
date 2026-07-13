# CEETIS manual reading table builder

## Purpose

`report_manual_table_begin`, `report_manual_table_add`, and
`report_manual_table_finish` let a test script collect any practical number of
numeric manual readings and print the completed readings as one compact TXT
report table.

The caller defines each row with one `report_manual_table_add` call. The caller
does not create arrays, track row indexes, provide a row count, or coordinate
parallel lists.

This facility is TXT-oriented only. HTML report rendering is not part of this
feature.

## Public API

- `report_manual_table_begin(Title: string = ''; Debug: boolean = FALSE): void`
- `report_manual_table_add(Reading: string; MinValue: real; MaxValue: real; Units: string = ''): void`
- `report_manual_table_finish(): void`

Only one table may be active at a time. Call `begin`, then one or more `add`
calls, then `finish`.

## Complete caller example

    report_manual_table_begin('Insertion Loss Readings');

    report_manual_table_add(
       'C-C Insertion Loss at 850nm',
       0.01,
       2.0,
       'dB'
    );

    report_manual_table_add(
       'C-C Insertion Loss at 1300nm',
       0.01,
       2.0,
       'dB'
    );

    report_manual_table_add(
       'D-D Insertion Loss at 850nm',
       0.01,
       2.0,
       'dB'
    );

    report_manual_table_finish();

## Example TXT report output

The exact numeric formatting comes from CEETIS ATS real-to-string conversion.
Units remain attached to the Min, Max, and Measured cells.

    +------------------------------+---------+------+----------+--------+
    |                      Insertion Loss Readings                      |
    +------------------------------+---------+------+----------+--------+
    | Reading                      |     Min |  Max | Measured | Result |
    +------------------------------+---------+------+----------+--------+
    | C-C Insertion Loss at 850nm  | 0.01 dB | 2 dB |  1.67 dB |  PASS  |
    | C-C Insertion Loss at 1300nm | 0.01 dB | 2 dB |  1.80 dB |  PASS  |
    | D-D Insertion Loss at 850nm  | 0.01 dB | 2 dB |  2.15 dB |  FAIL  |
    +------------------------------+---------+------+----------+--------+
    |                         GROUP RESULT: FAIL                        |
    +------------------------------+---------+------+----------+--------+

Tables are content-sized and stay compact up to the 86-character maximum. The
optional title does not force table expansion; long titles wrap inside the
calculated table width. Reading descriptions expand the Reading column only up
to the maximum permitted width and then wrap at word boundaries. Borders are
segmented so each `+` aligns with the corresponding `|` in standard rows. Hard
splitting is used only as a fallback for an unbroken sequence longer than the
available width, and content is not truncated.

## Input behavior

### In-range numeric input

- The value is accepted.
- The normalized real value is stored.
- The row is marked `PASS`.
- The Others failure counter is not incremented.

### Nonnumeric input

- Input is trimmed before numeric validation.
- Validation uses `FormatIsInteger` or `FormatIsReal`.
- If validation fails, the operator sees an immediate `UIErrorDialog` containing
  the Reading description, the raw invalid input, and an instruction to enter a
  numeric value.
- The same reading is reprompted.
- The malformed attempt is not stored.
- The malformed attempt is not written to the permanent report.
- Correcting malformed input does not increment the failure counter.

### Accepted out-of-range numeric input

- The value is accepted without reprompting.
- The operator sees an immediate `UIErrorDialog` showing the Reading, entered
  value, units, minimum, and maximum.
- The Others failure counter increments exactly once for that reading.
- The completed row is stored and marked `FAIL`.
- Later readings continue.
- No duplicate permanent report error line is written; the table row is the
  permanent failure record.

### Cancellation

- Canceling a prompt stops gathering later readings for that table.
- Cancellation increments the Others failure counter exactly once total.
- The canceled prompt does not create a fake measured row.
- Previously completed rows are preserved.
- Later `report_manual_table_add` calls for the same table are silent no-ops.
- `report_manual_table_finish` still renders completed rows and the group result.
- The overall CEETIS test continues after `finish`.

## Group result meanings

- `GROUP RESULT: PASS`: all completed rows passed and the table was not canceled.
- `GROUP RESULT: FAIL`: one or more completed rows failed and the table was not canceled.
- `GROUP RESULT: CANCELED (FAIL)`: the table was canceled before any failed row.
- `GROUP RESULT: FAIL + CANCELED`: a failed row occurred before cancellation.

Completed row statuses are only `PASS` and `FAIL`.

## Programming and configuration errors

The following are script or configuration defects rather than product failures:

- Calling `begin` while a table is already active.
- Calling `add` before `begin`.
- Calling `finish` before `begin`.
- Calling `finish` with no completed rows when the table was not canceled.
- Empty or whitespace-only Reading text.
- `MinValue` greater than `MaxValue`.
- Internal state corruption.
- Fixed value columns that make an 86-character table impossible.
- Any generated physical table line longer than 86 characters.

These errors write a permanent report error, show an operator error, abort the
test with `MiscAbortTest`, and do not increment the product failure counter.

## CEETIS compile and tester validation status

This repository change has not been compiled in CEETIS during local Codex work.
The next required checkpoint is CEETIS 4.10-08 compilation, `.cats` generation,
representative script execution, and TXT report review under
`Nortech_Default_TXT`.

## Mandatory CEETIS checkpoint matrix

Validate these cases in the CEETIS editor/tester before releasing the feature:

1. One passing row.
2. Multiple passing rows.
3. Different units across rows.
4. Unitless reading.
5. Negative minimum, maximum, and measured values.
6. Minimum equal to maximum.
7. Value exactly at minimum.
8. Value exactly at maximum.
9. Below-minimum value.
10. Above-maximum value.
11. Multiple failed rows, each counted once.
12. One nonnumeric entry followed by valid input.
13. Multiple nonnumeric entries followed by valid input.
14. Raw malformed input shown to the operator.
15. Corrected malformed input producing no failure increment and no report entry.
16. Cancel on the first prompt.
17. Cancel after completed passing rows.
18. Cancel after a completed failed row.
19. Cancellation counted once.
20. Later add calls after cancellation producing no prompts or failures.
21. Title present.
22. Empty title.
23. Long Reading text requiring wrapping.
24. Long unbroken Reading text.
25. Long units and numeric display strings.
26. Every physical table line no longer than 86 characters.
27. Two tables executed sequentially.
28. `begin` called twice.
29. `add` called before `begin`.
30. `finish` called before `begin`.
31. `finish` called with no rows and no cancellation.
32. Empty Reading.
33. `MinValue` greater than `MaxValue`.
34. Rerunning a test after a prior abrupt abort to detect stale Global Data.
35. Real CEETIS 4.10-08 compilation.
36. Resulting `.cats` generation and loading.
37. Generated TXT report alignment under `Nortech_Default_TXT`.
38. Actual Others failure-counter changes.
