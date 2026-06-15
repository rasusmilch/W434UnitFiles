# TestInitSetTestAllowed

## Declaration

```ats
function TestInitSetTestAllowed(TestAllowed: boolean): void;
```

## Call pattern

```ats
TestInitSetTestAllowed(TRUE|FALSE);
```

## Description

Specifies whether a test run is allowed or not.

## Metadata

- Category: Test Initialization
- Code: 265217
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program
- Count result: no
- Archive allowed: no

## Parameters

- `TestAllowed`: `boolean` — Allowed values: TRUE, FALSE

## Example

```ats
TestInitSetTestAllowed(TRUE);
```

## See also

`TestInitSetComplete`, `TestInitSetNextStep`
