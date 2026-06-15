# PowerUPinSetTPOff

## Declaration

```ats
function PowerUPinSetTPOff(ExternalIO: integer; Pin: tpin): void;
```

## Call pattern

```ats
PowerUPinSetTPOff(EXTIO_U?, "Pin");
```

## Description

Disconnects the power U - pin that is assigned to "Pin" from high and low potential of ExternalIO.

## Metadata

- Category: Powerpin Access
- Code: 264210
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_U1, EXTIO_U2, EXTIO_U3, EXTIO_U4, EXTIO_U5, EXTIO_U6, EXTIO_U7, EXTIO_U8, EXTIO_U9, EXTIO_U10
- `Pin`: `tpin`

## Example

```ats
PowerUPinSetTPLow(EXTIO_U1, "Pin1");
PowerUPinSetTPHigh(EXTIO_U1, "Pin2");
//...
PowerUPinSetTPOff(EXTIO_U1, "Pin1");
PowerUPinSetTPOff(EXTIO_U1, "Pin2");
```

## See also

`PowerPinResetAll`, `PowerUPinGroupSetTPOff`, `PowerUPinSetOff`, `PowerUPinSetTPHigh`, `PowerUPinSetTPLow`
