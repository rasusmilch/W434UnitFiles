# PinExcludeIsolationLVRange

## Declaration

```ats
function PinExcludeIsolationLVRange(FromPin: tpin; ToPin: tpin): void;
```

## Call pattern

```ats
PinExcludeIsolationLVRange("FromPin", "ToPin");
```

## Description

Excludes a range of pins from testing when executing the function IsolationTestLV().

## Metadata

- Category: Pin Access
- Code: 268551
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
PinExcludeIsolationLVRange("Pin1", "Pin3");
IsolationtestLV();
```

## See also

`IsolationTestLV`, `PinExcludeDielectricBreakdownRange`, `PinExcludeIsolationHVRange`, `PinExcludeIsolationLV`
