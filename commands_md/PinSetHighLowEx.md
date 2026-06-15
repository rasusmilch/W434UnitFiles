# PinSetHighLowEx

## Declaration

```ats
function PinSetHighLowEx(HighPin: tpin; LowPin: tpin; DCVoltage: boolean = TRUE; Umax: tvoltage = 0V; ResetGenerators: boolean = TRUE; SettleTimeModifier: ttime = 0s): void;
```

## Call pattern

```ats
PinSetHighLowEx("HighPin", "LowPin");
```

## Description

Sets one pin of the matrix to high and one to low.

If a voltage value is passed, it will be checkt whether that voltage is allowed on the pins.
If the Feature "Voltage levels" is enabled, the passed voltage value has also impact on the matrix switching.

The command makes it possible to switch a pin to high and low at the same time.
This can be used for diagnostics purposes.

## Metadata

- Category: Pin Access
- Code: 268569
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
- `ResetGenerators`: `boolean = TRUE` — If FALSE is passed for ResetGenerators the generators will not be switched off and disconnected from the measurement bus before the matrix is switched.
- `SettleTimeModifier`: `ttime = 0s` — The time, which is waited until a relay of the matrix has switched, can be extended with this parameter.

## Example

```ats
PinSetHighLowEx("HighPin", "LowPin");
```

## See also

`PinGetMaximumVoltage`, `PinGroupSetHighLow`, `PinSetHighLow`, `PinSetLowAll`, `PinSetOffAll`
