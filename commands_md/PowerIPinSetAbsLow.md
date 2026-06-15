# PowerIPinSetAbsLow

## Declaration

```ats
function PowerIPinSetAbsLow(ExternalIO: integer; PowerPin: tpoweripinabs): void;
```

## Call pattern

```ats
PowerIPinSetAbsLow(EXTIO_I?, "X.Y");
```

## Description

This function is deprecated. Please use PowerIPinSetLow or PowerIPinSetTPLow instead.

## Metadata

- Category: Powerpin Access
- Code: 264230
- Visible in alphabetical index: yes
- Deprecated: yes
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_I1, EXTIO_I2, EXTIO_I3, EXTIO_I4, EXTIO_I5, EXTIO_I6, EXTIO_I7, EXTIO_I8, EXTIO_I9, EXTIO_I10
- `PowerPin`: `tpoweripinabs`

## Example

```ats
PowerIPinSetAbsLow(EXTIO_I1, "12.a1");
PowerIPinSetAbsHigh(EXTIO_I1, "12.a2");
//...
PowerIPinSetAbsOff("12.a1");
PowerIPinSetAbsOff("12.a2");
```

## See also

`PowerIPinSetLow`, `PowerIPinSetTPLow`
