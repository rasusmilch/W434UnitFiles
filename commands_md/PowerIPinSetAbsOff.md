# PowerIPinSetAbsOff

## Declaration

```ats
function PowerIPinSetAbsOff(PowerPin: tpoweripinabs): void;
```

## Call pattern

```ats
PowerIPinSetAbsOff("X.Y");
```

## Description

This function is deprecated. Please use PowerIPinSetOff or PowerIPinSetTPOff instead.

## Metadata

- Category: Powerpin Access
- Code: 264232
- Visible in alphabetical index: yes
- Deprecated: yes
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `PowerPin`: `tpoweripinabs`

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
PowerIPinSetAbsLow(EXTIO_I1, "12.a1");
PowerIPinSetAbsHigh(EXTIO_I1, "12.a2");
//...
PowerIPinSetAbsOff("12.a1");
PowerIPinSetAbsOff("12.a2");
```

## See also

`PowerPinResetAll`, `PowerIPinSetOff`, `PowerIPinSetTPOff`
