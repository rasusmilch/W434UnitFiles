# TestInitSetComplete

## Declaration

```ats
function TestInitSetComplete(Complete: boolean): void;
```

## Call pattern

```ats
TestInitSetComplete(TRUE|FALSE);
```

## Description

Specifies whether the test initialization terminated correctly.

## Metadata

- Category: Test Initialization
- Code: 265216
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program
- Count result: no
- Archive allowed: no

## Parameters

- `Complete`: `boolean` — Allowed values: TRUE, FALSE

## Example

```ats
TestInitSetComplete(TRUE);
```

## See also

`TestInitSetNextStep`, `TestInitSetTestAllowed`
