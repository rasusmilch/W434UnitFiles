# DielectricBreakdownTestRange

## Declaration

```ats
function DielectricBreakdownTestRange(FromPin: tpin; ToPin: tpin): void;
```

## Call pattern

```ats
DielectricBreakdownTestRange("FromPin", "ToPin");
```

## Description

Executes a dielectric breakdown test on a pin range.

## Metadata

- Category: Electrical testing
- Code: 1545
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
DielectricBreakdownTest("Pin65", "Pin128");
```

## See also

`DielectricBreakdownTest`, `IsolationTestHVRange`, `IsolationTestLVRange`
