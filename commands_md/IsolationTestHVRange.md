# IsolationTestHVRange

## Declaration

```ats
function IsolationTestHVRange(FromPin: tpin; ToPin: tpin): void;
```

## Call pattern

```ats
IsolationTestHVRange("FromPin", "ToPin");
```

## Description

Executes a high voltage isolation test on a pin range.

## Metadata

- Category: Electrical testing
- Code: 1289
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `FromPin`: `tpin`
- `ToPin`: `tpin`

## Example

```ats
IsolationTestHVRange("Pin65", "Pin128");
```

## See also

`DielectricBreakdownTest`, `IsolationTestHVRange`, `IsolationTestLVRange`
