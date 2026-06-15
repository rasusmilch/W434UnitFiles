# PinExcludeIsolationLV

## Declaration

```ats
function PinExcludeIsolationLV(Pins: tpinarray): void;
```

## Call pattern

```ats
PinExcludeIsolationLV(["Pin1", "Pin2", ...]);
```

## Description

Excludes pins from testing when executing the function IsolationTestLV().

## Metadata

- Category: Pin Access
- Code: 268548
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pins`: `tpinarray`

## Example

```ats
PinExcludeIsolationLV(["Pin1", "Pin2", "Pin3"]);
IsolationTestLV();
```

## See also

`IsolationTeslLV`, `PinExcludeDielectricBreakdown`, `PinExcludeIsolationHV`
