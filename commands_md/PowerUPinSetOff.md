# PowerUPinSetOff

## Declaration

```ats
function PowerUPinSetOff(PowerPin: tpowerupin): void;
```

## Call pattern

```ats
PowerUPinSetOff("PowerPin");
```

## Description

Disconnects the power U - pin "PowerPin" from high and low potential.

## Metadata

- Category: Powerpin Access
- Code: 264213
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PowerPin`: `tpowerupin`

## Example

```ats
PowerUPinSetLow(EXTIO_U1, "PowerPin1");
PowerUPinSetHigh(EXTIO_U1, "PowerPin2");
//...
PowerUPinSetOff("PowerPin1");
PowerUPinSetOff("PowerPin2");
```

## See also

`PowerPinResetAll`, `PowerUPinGroupSetTPOff`, `PowerUPinSetHigh`, `PowerUPinSetLow`, `PowerUPinSetTPOff`
