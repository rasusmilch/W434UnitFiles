# PowerIPinSetTPLow

## Declaration

```ats
function PowerIPinSetTPLow(ExternalIO: integer; Pin: tpin): void;
```

## Call pattern

```ats
PowerIPinSetTPLow(EXTIO_I?, "Pin");
```

## Description

Connects the power I - pin that is assigned to "Pin" to the low potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264224
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_I1, EXTIO_I2, EXTIO_I3, EXTIO_I4, EXTIO_I5, EXTIO_I6, EXTIO_I7, EXTIO_I8, EXTIO_I9, EXTIO_I10
- `Pin`: `tpin`

## Example

```ats
PowerIPinSetTPLow(EXTIO_I1, "Pin1");
PowerIPinSetTPHigh(EXTIO_I1, "Pin2");
//...
PowerIPinSetTPOff(EXTIO_I1, "Pin1");
PowerIPinSetTPOff(EXTIO_I1, "Pin2");
```

## See also

`PowerIPinSetLow`, `PowerIPinSetTPHigh`, `PowerIPinSetTPOff`
