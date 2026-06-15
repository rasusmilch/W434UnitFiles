# TestZDiodes

## Declaration

```ats
function TestZDiodes(StartRow: tnetlistrow = NETLIST_FirstRow; EndRow: tnetlistrow = NETLIST_LastRow): void; tests zdiodes;
```

## Call pattern

```ats
TestZDiodes();
```

## Description

Tests the z-diodes of the netlist.

Start and end rows can optionally be passed to the function.

All z-diodes will be tested if no rows are passed.

Notice: If a project has modules with identical Zener diode lists, which call this function, the warning "No adequate component found in net list" will be shown for one of those function calls when compiling the project.

## Metadata

- Category: Electrical testing
- Code: 270341
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
TestZDiodes();
TestZDiodes(1, 10);

//The following two lines are equal
TestZDiodes(11, NETLIST_LastRow);
TestZDiodes(11);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `TestAttenuators`, `TestCapacitors`, `TestCTwistsAC`, `TestDiodes`, `TestResistors`, `TestSwitches`, `TestWires`, `ZDiodeTest`
