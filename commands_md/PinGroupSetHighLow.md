# PinGroupSetHighLow

## Declaration

```ats
function PinGroupSetHighLow(HighGroup: tpinarray; LowGroup: tpinarray; DCVoltage: boolean = TRUE; Umax: tvoltage = 0V): void;
```

## Call pattern

```ats
PinGroupSetHighLow(HighGroup, LowGroup);
```

## Description

Sets the Pins in "HighGroup" to the high- and the pins in "LowGroup" to the low-side of the matrix.

If a voltage value is passed, it will be checkt whether that voltage is allowed on the pins.
If the Feature "Voltage levels" is enabled, the passed voltage value has also impact on the matrix switching.


## Metadata

- Category: Pin Access
- Code: 268557
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `HighGroup`: `tpinarray`
- `LowGroup`: `tpinarray`
- `DCVoltage`: `boolean = TRUE` — TRUE, if the passed voltage is a DC voltage, otherwise FALSE; Allowed values: TRUE, FALSE
- `Umax`: `tvoltage = 0V` — Voltage that will be connected to the pins

## Example

```ats
PinGroupSetHighLow(["Pin1", "Pin3"], ["Pin2", "Pin4"]);
```

## See also

`PinCreateList`, `PinDefineList`, `PinGroupGetMaximumVoltage`, `PinSetHighLow`
