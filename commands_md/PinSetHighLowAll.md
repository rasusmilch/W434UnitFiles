# PinSetHighLowAll

## Declaration

```ats
function PinSetHighLowAll(HighPin: tpin; DCVoltage: boolean = TRUE; Umax: tvoltage = 0V):void;
```

## Call pattern

```ats
PinSetHighLowAll("HighPin");
```

## Description

Sets one pin of the matrix to high and all other to low.

## Metadata

- Category: Pin Access
- Code: 268563
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `HighPin`: `tpin`
- `DCVoltage`: `boolean = TRUE`
- `Umax`: `tvoltage = 0V`

## Example

```ats
PinSetHighLowAll("HighPin");
```

## See also

`PinGroupSetHighLow`, `PinSetHighLow`, `PinSetLowAll`, `PinSetOffAll`
