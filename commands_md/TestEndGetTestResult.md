# TestEndGetTestResult

## Declaration

```ats
function TestEndGetTestResult(var UserBreak: boolean; var Pass: boolean): void;
```

## Call pattern

```ats
TestEndGetTestResult(UserBreak, Pass);
```

## Description

Returns the result of the test.

## Metadata

- Category: Test End
- Code: 265474
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `var UserBreak`: `boolean`
- `var Pass`: `boolean`

## Example

```ats
Pass = FALSE;
UserBreak = FALSE;
TestEndGetTestResult(UserBreak, Pass);
UITestResult(Pass, UserBreak, TRUE, 3s);
```
