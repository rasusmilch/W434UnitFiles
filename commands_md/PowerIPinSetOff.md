# PowerIPinSetOff

## Declaration

```ats
function PowerIPinSetOff(PowerPin: tpoweripin): void;
```

## Call pattern

```ats
PowerIPinSetOff("PowerPin");
```

## Description

Disconnects the power I - pin "PowerPin" from high and low potential.

## Metadata

- Category: Powerpin Access
- Code: 264229
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PowerPin`: `tpoweripin`

## Example

```ats
PowerIPinSetLow(EXTIO_I1, "PowerPin1");
PowerIPinSetHigh(EXTIO_I1, "PowerPin2");
//...
PowerIPinSetOff("PowerPin1");
PowerIPinSetOff("PowerPin2");
```

## See also

`PowerPinResetAll`, `PowerIPinSetHigh`, `PowerIPinSetLow`, `PowerIPinSetTPOff`
