# PowerIPinSetHigh

## Declaration

```ats
function PowerIPinSetHigh(ExternalIO: integer; PowerPin: tpoweripin): void;
```

## Call pattern

```ats
PowerIPinSetHigh(EXTIO_I?, "PowerPin");
```

## Description

Connects the power I - pin "PowerPin" to the high potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264228
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_I1, EXTIO_I2, EXTIO_I3, EXTIO_I4, EXTIO_I5, EXTIO_I6, EXTIO_I7, EXTIO_I8, EXTIO_I9, EXTIO_I10
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

`PowerIPinSetLow`, `PowerIPinSetOff`, `PowerIPinSetTPHigh`, ``
