# TestWires

## Declaration

```ats
function TestWires(StartRow: tnetlistrow = NETLIST_FirstRow; EndRow: tnetlistrow = NETLIST_LastRow): void; tests wires;
```

## Call pattern

```ats
TestWires();
```

## Description

Tests the wires of the netlist.

Start and end rows can optionally be passed to the function.

All wires will be tested if no rows are passed.

Notice: If a project has modules with identical wire lists, which call this function, the warning "No adequate component found in net list" will be shown for one of those function calls when compiling the project.

## Metadata

- Category: Electrical testing
- Code: 270336
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
TestWires();
TestWires(1, 10);

//The following two lines are equal
TestWires(11, NETLIST_LastRow);
TestWires(11);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `TestAttenuators`, `TestCapacitors`, `TestCTwistsAC`, `TestDiodes`, `TestResistors`, `TestSwitches`, `TestZDiodes`, `WireTest`
