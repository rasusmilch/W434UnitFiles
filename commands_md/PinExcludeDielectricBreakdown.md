# PinExcludeDielectricBreakdown

## Declaration

```ats
function PinExcludeDielectricBreakdown(Pins: tpinarray): void;
```

## Call pattern

```ats
PinExcludeDielectricBreakdown(["Pin1", "Pin2", ...]);
```

## Description

Excludes pins from testing when executing the function DielectricBreakdownTest().

## Metadata

- Category: Pin Access
- Code: 268550
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pins`: `tpinarray`

## Example

```ats
PinExcludeDielectricBreakdown(["Pin1", "Pin2", "Pin3"]);
DielectricBreakdownTest();
```

## See also

`DielectricBreakdownTest`, `PinExcludeIsolationHV`, `PinExcludeIsolationLV`
