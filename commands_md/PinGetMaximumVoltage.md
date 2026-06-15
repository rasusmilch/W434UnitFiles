# PinGetMaximumVoltage

## Declaration

```ats
function PinGetMaximumVoltage(Pin: tpin; DCVoltage: boolean): real;
```

## Call pattern

```ats
PinGetMaximumVoltage("Pin", TRUE|FALSE);
```

## Description

Returns the maximum allowed voltage for the passed pin.

## Metadata

- Category: Pin Access
- Code: 268558
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pin`: `tpin`
- `DCVoltage`: `boolean` — If TRUE the maximum allowed DC voltage will be returned.
; If FALSE the maximum allowed AC voltage will be returned.; Allowed values: TRUE, FALSE

## Example

```ats
MaximumDCVoltage = PinGetMaximumVoltage("Pin", TRUE);
MaximumACVoltage = PinGetMaximumVoltage("Pin", FALSE);
```

## See also

`PinGroupGetMaximumVoltage`, `PinSetHighLow`
