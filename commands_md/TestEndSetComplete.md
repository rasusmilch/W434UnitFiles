# TestEndSetComplete

## Declaration

```ats
function TestEndSetComplete(Complete: boolean): void;
```

## Call pattern

```ats
TestEndSetComplete(TRUE|FALSE);
```

## Description

Specifies whether the test end terminated correctly.

## Metadata

- Category: Test End
- Code: 265472
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Complete`: `boolean` — Allowed values: TRUE, FALSE

## Example

```ats
TestEndSetComplete(TRUE);
```

## See also

`TestEndGetTestResult`, `TestEndSetNextStep`
