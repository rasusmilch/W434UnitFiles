# LV_PowerPinResetAll

## Declaration

```ats
function LV_PowerPinResetAll(): void;
```

## Call pattern

```ats
LV_PowerPinResetAll();
```

## Description

Disconnects all power U1 pins of the LV matrix from the high- and the low-potential of the LV U1 bus.

## Metadata

- Category: Powerpin Access
- Code: 264403
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
LV_PowerU1PinSetHigh("PowerU1Pin");
```

## See also

`LV_PowerU1PinSetHigh`, `LV_PowerU1PinSetLow`, `LV_PowerU1PinSetOff`
