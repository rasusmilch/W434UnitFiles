# LV_PowerU1PinSetLow

## Declaration

```ats
function LV_PowerU1PinSetLow(PowerU1Pin: tlvpoweru1pin): void;
```

## Call pattern

```ats
LV_PowerU1PinSetLow("PowerU1Pin");
```

## Description

Sets a power U1 pin of the LV matrix to the low potential of the LV U1 bus.
The pin must be tagged in the pin table to be used as power U1 pin.

## Metadata

- Category: Powerpin Access
- Code: 264401
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PowerU1Pin`: `tlvpoweru1pin`

## Example

```ats
LV_PowerU1PinSetHigh("PowerU1Pin");
```

## See also

`LV_PowerPinResetAll`, `LV_PowerU1PinSetHigh`, `LV_PowerU1PinSetOff`
