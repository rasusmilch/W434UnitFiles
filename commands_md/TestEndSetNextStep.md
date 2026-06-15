# TestEndSetNextStep

## Declaration

```ats
function TestEndSetNextStep(NextStep: integer): void;
```

## Call pattern

```ats
TestEndSetNextStep(STEP_?);
```

## Description

Specifies what must be executed after the test end.

## Metadata

- Category: Test End
- Code: 265473
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `NextStep`: `integer` — Allowed values: STEP_ProjectSelection, STEP_TestInitialization, STEP_WaitForTeststart, STEP_Test

## Example

```ats
TestEndSetNextStep(STEP_Test);
```

## See also

`ProjectSelectionSetAutostartTest`, `TestEndGetTestResult`, `TestEndSetComplete`, `TestIniSetNextStep`
