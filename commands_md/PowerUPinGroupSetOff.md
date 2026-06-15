# PowerUPinGroupSetOff

## Declaration

```ats
function PowerUPinGroupSetOff(PowerUPins: tpowerupinarray): void;
```

## Call pattern

```ats
PowerUPinGroupSetOff(["PowerUPin1", "PowerUPin2", ...]);
```

## Description

Switches the specified power U pins off.

## Metadata

- Category: Powerpin Access
- Code: 264223
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PowerUPins`: `tpowerupinarray`

## Example

```ats
PowerUPinGroupSetLow(EXTIO_U2, ["PowerUPin1", "PowerUPin2"]);
PowerUPinGroupSetHigh(EXTIO_U2, ["PowerUPin3", "PowerUPin4"]);
//...
PowerUPinGroupSetOff(["PowerUPin1", "PowerUPin2", "PowerUPin3", "PowerUPin4"]);
```

## See also

`PowerUPinGroupSetHigh`, `PowerUPinGroupSetHighLow`, `PowerUPinGroupSetLow`, `PowerUPinGroupSetTPOff`, `PowerUPinSetOff`
