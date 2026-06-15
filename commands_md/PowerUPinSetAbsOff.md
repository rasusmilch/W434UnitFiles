# PowerUPinSetAbsOff

## Declaration

```ats
function PowerUPinSetAbsOff(PowerPin: tpowerupinabs): void;
```

## Call pattern

```ats
PowerUPinSetAbsOff("X.Y");
```

## Description

This function is deprecated. Please use PowerUPinSetOff or PowerUPinSetTPOff instead.

## Metadata

- Category: Powerpin Access
- Code: 264216
- Visible in alphabetical index: yes
- Deprecated: yes
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

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

`PowerPinResetAll`, `PowerUPinGroupSetTPOff`, `PowerUPinSetOff`, `PowerUPinSetTPOff`
