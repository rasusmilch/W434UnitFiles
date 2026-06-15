# MiscProbe

## Declaration

```ats
function MiscProbe(ShowWarning: boolean = TRUE): void;
```

## Call pattern

```ats
MiscProbe();
```

## Description

Runs the probe during a test.

## Metadata

- Category: Miscellaneous
- Code: 266514
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ShowWarning`: `boolean = TRUE` — If TRUE is passed a warning will be displayed before the start of the probe to protect your test system.; If FALSE is passed the warning is omitted.; Allowed values: TRUE, FALSE

## Example

```ats
MiscProbe(TRUE);
MiscProbe(FALSE);
```

## See also

`ProbeTest`
