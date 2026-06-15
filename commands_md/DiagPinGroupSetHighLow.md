# DiagPinGroupSetHighLow

## Declaration

```ats
function DiagPinGroupSetHighLow(HighGroup: tpinarray; LowGroup: tpinarray): void;
```

## Call pattern

```ats
DiagPinGroupSetHighLow(HighGroup, LowGroup);
```

## Description

Sets the Pins in "HighGroup" to the high- and the pins in "LowGroup" to the low-side of the matrix.

## Metadata

- Category: Diagnostics
- Code: 269313
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `HighGroup`: `tpinarray`
- `LowGroup`: `tpinarray`

## Example

```ats
DiagPinGroupSetHighLow(["Pin1","Pin3"],["Pin2","Pin4"]);
```

## See also

`PinGroupSetHighLow`
