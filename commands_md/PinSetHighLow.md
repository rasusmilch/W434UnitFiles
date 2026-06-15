# PinSetHighLow

## Declaration

```ats
function PinSetHighLow(HighPin: tpin; LowPin: tpin; DCVoltage: boolean = TRUE; Umax: tvoltage = 0V): void;
```

## Call pattern

```ats
PinSetHighLow("HighPin", "LowPin");
```

## Description

Sets one pin of the matrix to high and one to low.

If a voltage value is passed, it will be checkt whether that voltage is allowed on the pins.
If the Feature "Voltage levels" is enabled, the passed voltage value has also impact on the matrix switching.

## Metadata

- Category: Pin Access
- Code: 268556
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `HighPin`: `tpin`
- `LowPin`: `tpin`
- `DCVoltage`: `boolean = TRUE` — TRUE, if the passed voltage is a DC voltage, otherwise FALSE; Allowed values: TRUE, FALSE
- `Umax`: `tvoltage = 0V` — Voltage that will be connected to the pins

## Example

```ats
PinSetHighLow("HighPin", "LowPin");
```

## See also

`PinGetMaximumVoltage`, `PinGroupSetHighLow`, `PinSetLowAll`, `PinSetOffAll`
