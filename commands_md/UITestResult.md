# UITestResult

## Declaration

```ats
function UITestResult(Pass: boolean; UserBreak: boolean; ShowSummary: boolean; DisplayTime: ttime = 0s): void;
```

## Call pattern

```ats
UITestResult(Pass, UserBreak, ShowSummary, <DisplayTime>s);
```

## Description

Shows the test result window for the test.

## Metadata

- Category: Userinterface Access
- Code: 263963
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Pass`: `boolean` — Allowed values: TRUE, FALSE
- `UserBreak`: `boolean` — Allowed values: TRUE, FALSE
- `ShowSummary`: `boolean` — Allowed values: TRUE, FALSE
- `DisplayTime`: `ttime = 0s`

## Example

```ats
Pass = FALSE;
UserBreak = FALSE;
TestEndGetTestResult(UserBreak, Pass);
UITestResult(Pass, UserBreak, TRUE, 3s);
```
