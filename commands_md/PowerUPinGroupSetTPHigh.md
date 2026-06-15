# PowerUPinGroupSetTPHigh

## Declaration

```ats
function PowerUPinGroupSetTPHigh(ExternalIO: integer; Pins: tpinarray): void;
```

## Call pattern

```ats
PowerUPinGroupSetTPHigh(EXTIO_U?, ["Pin1", "Pin2", ...]);
```

## Description

Connects the power U - pins which are assigned to the specified pins to the High potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264218
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_U1, EXTIO_U2, EXTIO_U3, EXTIO_U4, EXTIO_U5, EXTIO_U6, EXTIO_U7, EXTIO_U8, EXTIO_U9, EXTIO_U10
- `Pins`: `tpinarray`

## See also

`PowerUPinGroupSetTPHighLow`, `PowerUPinGroupSetTPLow`, `PowerUPinGroupSetTPOff`, `PowerUPinSetLow`, `PowerUPinSetTPHigh`, `PowerUPinSetTPLow`, `PowerUPinSetTPOff`
