# PinGroupGetMaximumVoltage

## Declaration

```ats
function PinGroupGetMaximumVoltage(PinGroup: tpinarray; DCVoltage: boolean): real;
```

## Call pattern

```ats
PinGroupGetMaximumVoltage(PinGroup, TRUE|FALSE);
```

## Description

Returns the maximum allowed voltage for the pins in the passed pin group.

## Metadata

- Category: Pin Access
- Code: 268559
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinGroup`: `tpinarray`
- `DCVoltage`: `boolean` — If TRUE the maximum allowed DC voltage will be returned.
; If FALSE the maximum allowed AC voltage will be returned.; Allowed values: TRUE, FALSE

## Example

```ats
MaximumVoltageDC = PinGroupGetMaximumVoltage(["Pin1", "Pin2", "Pin3"], TRUE);
MaximumVoltageAC = PinGroupGetMaximumVoltage(["Pin1", "Pin2", "Pin3"], FALSE);
```

## See also

`PinCreateList`, `PinDefineList`, `PinGetMaximumVoltage`, `PinSetHighLow`
