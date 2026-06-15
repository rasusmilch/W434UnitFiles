# TestInitSetNextStep

## Declaration

```ats
function TestInitSetNextStep(NextStep: integer): void;
```

## Call pattern

```ats
TestInitSetNextStep(STEP_?);
```

## Description

Specifies what must be executed after the initialization.

## Metadata

- Category: Test Initialization
- Code: 265218
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program
- Count result: no
- Archive allowed: no

## Parameters

- `NextStep`: `integer` — Allowed values: STEP_WaitForTeststart, STEP_Test, STEP_ProjectSelection

## Example

```ats
TestInitSetNextStep(STEP_Test);
```

## See also

`ProjectSelectionSetAutostartTest`, `TestEndSetNextStep`, `TestInitSetComplete`, `TestInitSetTestAllowed`, `TestStartSetNextStep`
