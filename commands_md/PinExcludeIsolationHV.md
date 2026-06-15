# PinExcludeIsolationHV

## Declaration

```ats
function PinExcludeIsolationHV(Pins: tpinarray): void;
```

## Call pattern

```ats
PinExcludeIsolationHV(["Pin1", "Pin2", ...]);
```

## Description

Excludes pins from testing when executing the function IsolationTestHV().

## Metadata

- Category: Pin Access
- Code: 268549
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pins`: `tpinarray`

## Example

```ats
PinExcludeIsolationHV(["Pin1", "Pin2", "Pin3"]);
IsolationTestHV();
```

## See also

`IsolationTestHV`, `PinExcludeDielectricBreakdown`, `PinExcludeIsolationLV`
