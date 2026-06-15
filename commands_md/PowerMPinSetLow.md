# PowerMPinSetLow

## Declaration

```ats
function PowerMPinSetLow(ExternalIO: integer; PowerPin: tpowermpin): void;
```

## Call pattern

```ats
PowerMPinSetLow(EXTIO_M?, "PowerPin");
```

## Description

Connects the power M - pin "PowerPin" to the low potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264243
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_M1, EXTIO_M2, EXTIO_M3, EXTIO_M4, EXTIO_M5, EXTIO_M6, EXTIO_M7, EXTIO_M8, EXTIO_M9, EXTIO_M10
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

`PowerMPinSetHigh`, `PowerMPinSetOff`, `PowerMPinSetTPLow`
