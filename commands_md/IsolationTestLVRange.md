# IsolationTestLVRange

## Declaration

```ats
function IsolationTestLVRange(FromPin: tpin; ToPin: tpin): void;
```

## Call pattern

```ats
IsolationTestLVRange("FromPin", "ToPin");
```

## Description

Executes a low voltage isolation test on a pin range.

## Metadata

- Category: Electrical testing
- Code: 1034
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
IsolationTestLVRange("Pin65", "Pin128");
```

## See also

`DielectricBreakdownTest`, `IsolationTestHVRange`, `IsolationTestLVRange`
