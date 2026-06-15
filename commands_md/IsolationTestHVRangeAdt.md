# IsolationTestHVRangeAdt

## Declaration

```ats
function IsolationTestHVRangeAdt(FromCable: string; ToCable: string): void;
```

## Call pattern

```ats
IsolationTestHVRangeAdt('FromCable', 'ToCable');
```

## Description

Executes a partial HV isolation test.

All adapter cables from "FromCable" to "ToCable" will be tested by the order of the cables in the pin table.
If an empty string is passed for  the test will start with the first cable in the pin table.
If an empty string is passed for  the test will end with the last cable in the pin table.

The function can only be executed if the project has a pin table with adapter cables.

## Metadata

- Category: Electrical testing
- Code: 1290
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
IsolationTestHVRangeAdt('', 'Cable 3');
FromCable = 'Cable 4';
IsolationTestHVRangeAdt(FromCable, 'Cable 5');
IsolationTestHVRangeAdt('Cable 6', '');
```

## See also

`DielectricBreakdownTestRangeAdt`, `IsolationTestHV`, `IsolationTestLVRangeAdt`
