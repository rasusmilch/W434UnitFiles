# PowerUPinGroupSetTPHighLow

## Declaration

```ats
function PowerUPinGroupSetTPHighLow(ExternalIO: integer; HighPins: tpinarray; LowPins: tpinarray): void;
```

## Call pattern

```ats
PowerUPinGroupSetTPHighLow(EXTIO_U?, ["Pin1", "Pin2", ...], ["Pin3", "Pin4", ...]);
```

## Description

Connects the power U - pins which are assigned to the specified pins to the High respectively Low potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264220
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_U1, EXTIO_U2, EXTIO_U3, EXTIO_U4, EXTIO_U5, EXTIO_U6, EXTIO_U7, EXTIO_U8, EXTIO_U9, EXTIO_U10
- `HighPins`: `tpinarray`
- `LowPins`: `tpinarray`

## Example

```ats
PowerUPinGroupSetTPHighLow(EXTIO_U2, ["Pin1", "Pin2"], ["Pin3", "Pin4"]);
//...
PowerUPinGroupSetTPOff(EXTIO_U2, ["Pin1", "Pin2", "Pin3", "Pin4"]);
```

## See also

`PowerUPinGroupSetTPHigh`, `PowerUPinGroupSetTPLow`, `PowerUPinGroupSetTPOff`, `PowerUPinSetLow`, `PowerUPinSetTPHigh`, `PowerUPinSetTPLow`, `PowerUPinSetTPOff`
