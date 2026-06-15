# TestOpticalFibers

## Declaration

```ats
function TestOpticalFibers(StartRow: tnetlistrow = NETLIST_FirstRow; EndRow: tnetlistrow = NETLIST_LastRow): void; tests opticalfibers;
```

## Call pattern

```ats
TestOpticalFibers();
```

## Description

Tests the optical fibers of the netlist.

Start and end rows can optionally be passed to the function.

All optical fibers will be tested if no rows are passed.

Notice: If a project has modules with identical attenuator lists, which call this function, the warning "No adequate component found in net list" will be shown for one of those function calls when compiling the project.

## Metadata

- Category: Optical fibers
- Code: 270344
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `StartRow`: `tnetlistrow = NETLIST_FirstRow` — Row of the netlist where the test starts.; Allowed values: NETLIST_FirstRow
- `EndRow`: `tnetlistrow = NETLIST_LastRow` — Row of the netlist where the test ends.; Allowed values: NETLIST_LastRow

## Example

```ats
TestOpticalFibers();
TestOpticalFibers(1, 10);

//The following two lines are equal
TestOpticalFibers(11, NETLIST_LastRow);
TestOpticalFibers(11);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `OFAttenuationTest`, `TestAttenuators`, `TestCapacitors`, `TestCTwistsAC`, `TestDiodes`, `TestResistors`, `TestSwitches`, `TestWires`, `TestZDiodes`
