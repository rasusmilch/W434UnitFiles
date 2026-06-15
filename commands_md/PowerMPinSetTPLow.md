# PowerMPinSetTPLow

## Declaration

```ats
function PowerMPinSetTPLow(ExternalIO: integer; Pin: tpin): void;
```

## Call pattern

```ats
PowerMPinSetTPLow(EXTIO_M?, "Pin");
```

## Description

Connects the power M - pin that is assigned to "Pin" to the low potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264240
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_M1, EXTIO_M2, EXTIO_M3, EXTIO_M4, EXTIO_M5, EXTIO_M6, EXTIO_M7, EXTIO_M8, EXTIO_M9, EXTIO_M10
- `Pin`: `tpin`

## Example

```ats
PowerMPinSetTPLow(EXTIO_M1, "Pin1");
PowerMPinSetTPHigh(EXTIO_M1, "Pin2");
//...
PowerMPinSetTPOff(EXTIO_M1, "Pin1");
PowerMPinSetTPOff(EXTIO_M1, "Pin2");
```

## See also

`PowerMPinSetLow`, `PowerMPinSetTPHigh`, `PowerMPinSetTPOff`
