# PowerUPinGroupSetHighLow

## Declaration

```ats
function PowerUPinGroupSetHighLow(ExternalIO: integer; HighPowerUPins: tpowerupinarray; LowPowerUPins: tpowerupinarray): void;
```

## Call pattern

```ats
PowerUPinGroupSetHighLow(EXTIO_U?, ["PowerUPin1", "PowerUPin2", ...], ["PowerUPin3", "PowerUPin4", ...]);
```

## Description

Connects the specified power U pins to the High respectively Low potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264256
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer`
- `HighPowerUPins`: `tpowerupinarray`
- `LowPowerUPins`: `tpowerupinarray`

## Example

```ats
PowerUPinGroupSetHighLow(EXTIO_U2, ["PowerUPin1", "PowerUPin2"], ["PowerUPin3", "PowerUPin4"]);
//...
PowerUPinGroupSetOff(["PowerUPin1", "PowerUPin2", "PowerUPin3", "PowerUPin4"]);
```

## See also

`PowerUPinGroupSetHigh`, `PowerUPinGroupSetLow`, `PowerUPinGroupSetOff`, `PowerUPinGroupSetTPHighLow`, `PowerUPinSetHigh`, `PowerUPinSetLow`
