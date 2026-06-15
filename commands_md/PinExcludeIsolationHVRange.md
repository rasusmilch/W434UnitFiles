# PinExcludeIsolationHVRange

## Declaration

```ats
function PinExcludeIsolationHVRange(FromPin: tpin; ToPin: tpin): void;
```

## Call pattern

```ats
PinExcludeIsolationHVRange("FromPin", "ToPin");
```

## Description

Excludes a range of pins from testing when executing the function IsolationTestHV().

## Metadata

- Category: Pin Access
- Code: 268552
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
PinExcludeIsolationHVRange("Pin1", "Pin3");
IsolationtestHV();
```

## See also

`IsolationTestHV`, `PinExcludeDielectricBreakdownRange`, `PinExcludeIsolationHV`, `PinExcludeIsolationLVRange`
