# IsolationTestLVRangeAdt

## Declaration

```ats
function IsolationTestLVRangeAdt(FromCable: string; ToCable: string): void;
```

## Call pattern

```ats
IsolationTestLVRangeAdt('FromCable', 'ToCable');
```

## Description

Executes a partial LV isolation test.

All adapter cables from "FromCable" to "ToCable" will be tested by the order of the cables in the pin table.

If an empty string is passed for  the test will start with the first cable in the pin table.
If an empty string is passed for  the test will end with the last cable in the pin table.

The function can only be executed if the project has a pin table with adapter cables.

## Metadata

- Category: Electrical testing
- Code: 1035
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `FromCable`: `string`
- `ToCable`: `string`

## Example

```ats
IsolationTestLVRangeAdt('', 'Cable 3');
FromCable = 'Cable 4';
IsolationTestLVRangeAdt(FromCable, 'Cable 5');
IsolationTestLVRangeAdt('Cable 6', '');
```

## See also

`DielectricBreakdownTestRangeAdt`, `IsolationTestHVRangeAdt`, `IsolationTestLV`
