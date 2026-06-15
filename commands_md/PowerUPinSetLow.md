# PowerUPinSetLow

## Declaration

```ats
function PowerUPinSetLow(ExternalIO: integer; PowerPin: tpowerupin): void;
```

## Call pattern

```ats
PowerUPinSetLow(EXTIO_U?, "PowerPin");
```

## Description

Connects the power U - pin "PowerPin" to the low potential of "ExternalIO".

## Metadata

- Category: Powerpin Access
- Code: 264211
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `ExternalIO`: `integer` — Allowed values: EXTIO_U1, EXTIO_U2, EXTIO_U3, EXTIO_U4, EXTIO_U5, EXTIO_U6, EXTIO_U7, EXTIO_U8, EXTIO_U9, EXTIO_U10
- `PowerPin`: `tpowerupin`

## Example

```ats
PowerUPinSetLow(EXTIO_U1, "PowerPin1");
PowerUPinSetHigh(EXTIO_U1, "PowerPin2");
//...
PowerUPinSetOff("PowerPin1");
PowerUPinSetOff("PowerPin2");
```

## See also

`PowerUPinGroupSetTPHighLow`, `PowerUPinGroupSetTPLow`, `PowerUPinSetHigh`, `PowerUPinSetOff`, `PowerUPinSetTPLow`
