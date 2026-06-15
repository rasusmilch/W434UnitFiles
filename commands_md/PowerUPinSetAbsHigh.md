# PowerUPinSetAbsHigh

## Declaration

```ats
function PowerUPinSetAbsHigh(ExternalIO: integer; PowerPin: tpowerupinabs): void;
```

## Call pattern

```ats
PowerUPinSetAbsHigh(EXTIO_U?, "X.Y");
```

## Description

This function is deprecated. Please use PowerUPinSetHigh or PowerUPinSetTPHigh instead.

## Metadata

- Category: Powerpin Access
- Code: 264215
- Visible in alphabetical index: yes
- Deprecated: yes
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_U1, EXTIO_U2, EXTIO_U3, EXTIO_U4, EXTIO_U5, EXTIO_U6, EXTIO_U7, EXTIO_U8, EXTIO_U9, EXTIO_U10
- `PowerPin`: `tpowerupinabs`

## Example

```ats
PowerUPinSetAbsLow(EXTIO_U1, "12.a1");
PowerUPinSetAbsHigh(EXTIO_U1, "12.a2");
//...
PowerUPinSetAbsOff("12.a1");
PowerUPinSetAbsOff("12.a2");
```

## See also

`PowerUPinSetHigh`, `PowerUPinSetTPHigh`
