# PowerUPinGroupSetLow

## Declaration

```ats
function PowerUPinGroupSetLow(ExternalIO: integer; PowerUPins: tpowerupinarray): void;
```

## Call pattern

```ats
PowerUPinGroupSetLow(EXTIO_U?, ["PowerUPin1", "PowerUPin2", ...]);
```

## Description

Connects the specified power U pins to the Low potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264221
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer`
- `PowerUPins`: `tpowerupinarray`

## Example

```ats
PowerUPinGroupSetLow(EXTIO_U2, ["PowerUPin1", "PowerUPin2"]);
PowerUPinGroupSetHigh(EXTIO_U2, ["PowerUPin3", "PowerUPin4"]);
//...
PowerUPinGroupSetOff(["PowerUPin1", "PowerUPin2", "PowerUPin3", "PowerUPin4"]);
```

## See also

`PowerUPinGroupSetHigh`, `PowerUPinGroupSetHighLow`, `PowerUPinGroupSetOff`, `PowerUPinGroupSetTPLow`, `PowerUPinSetLow`
