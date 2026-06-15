# PowerMPinSetOff

## Declaration

```ats
function PowerMPinSetOff(PowerPin: tpowermpin): void;
```

## Call pattern

```ats
PowerMPinSetOff("PowerPin");
```

## Description

Disconnects the power M - pin "PowerPin" from high and low potential.

## Metadata

- Category: Powerpin Access
- Code: 264245
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PowerPin`: `tpowermpin`

## Example

```ats
PowerMPinSetLow(EXTIO_M1, "PowerPin1");
PowerMPinSetHigh(EXTIO_M1, "PowerPin2");
//...
PowerMPinSetOff("PowerPin1");
PowerMPinSetOff("PowerPin2");
```

## See also

`PowerMPinSetHigh`, `PowerMPinSetLow`, `PowerMPinSetTPOff`, `PowerPinResetAll`
