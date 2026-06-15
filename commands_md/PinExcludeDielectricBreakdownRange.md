# PinExcludeDielectricBreakdownRange

## Declaration

```ats
function PinExcludeDielectricBreakdownRange(FromPin: tpin; ToPin: tpin): void;
```

## Call pattern

```ats
PinExcludeDielectricBreakdownRange("FromPin", "ToPin");
```

## Description

Excludes a range of pins from testing when executing the function DielectricBreakdownTest().

## Metadata

- Category: Pin Access
- Code: 268553
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Not listed
- Count result: no
- Archive allowed: no

## Parameters

- `FromPin`: `tpin`
- `ToPin`: `tpin`

## Example

```ats
PinExcludeDielectricBreakdownRange("Pin1", "Pin3");
DielectricBreakdownTest();
```

## See also

`DielectricBreakdownTest`, `PinExcludeDielectricBreakdown`, `PinExcludeIsolationHVRange`, `PinExcludeIsolationLVRange`
