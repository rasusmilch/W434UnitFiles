# TestStartSetNextStep

## Declaration

```ats
function TestStartSetNextStep(NextStep: integer): void;
```

## Call pattern

```ats
TestStartSetNextStep(STEP_?);
```

## Description

Specifies what must be executed after the test start program.

If this function is not called in the test start program, the test will be executed.

## Metadata

- Category: Test Start
- Code: 274432
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test start program
- Count result: no
- Archive allowed: no

## Parameters

- `NextStep`: `integer` — Allowed values: STEP_WaitForTeststart, STEP_ProjectSelection, STEP_TestInitialization

## Example

```ats
TestStartSetNextStep(STEP_WaitForTeststart);
```

## See also

`ProjectSelectionSetAutostartTest`, `TestEndSetNextStep`, `TestInitSetNextStep`
