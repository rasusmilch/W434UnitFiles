# TestDiodes

## Declaration

```ats
function TestDiodes(StartRow: tnetlistrow = NETLIST_FirstRow; EndRow: tnetlistrow = NETLIST_LastRow): void; tests diodes;
```

## Call pattern

```ats
TestDiodes();
```

## Description

Tests the diodes of the netlist.

Start and end rows can optionally be passed to the function.

All diodes will be tested if no rows are passed.

Notice: If a project has modules with identical diode lists, which call this function, the warning "No adequate component found in net list" will be shown for one of those function calls when compiling the project.

## Metadata

- Category: Electrical testing
- Code: 270340
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
TestDiodes();
TestDiodes(1, 10);

//The following two lines are equal
TestDiodes(11, NETLIST_LastRow);
TestDiodes(11);
```

## See also

`DielectricBreakdownTest`, `DiodeTest`, `IsolationTestHV`, `IsolationTestLV`, `TestAttenuators`, `TestCapacitors`, `TestCTwistsAC`, `TestResistors`, `TestSwitches`, `TestWires`, `TestZDiodes`
