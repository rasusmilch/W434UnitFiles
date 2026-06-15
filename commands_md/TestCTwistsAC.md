# TestCTwistsAC

## Declaration

```ats
function TestCTwistsAC(StartRow: tnetlistrow = NETLIST_FirstRow; EndRow: tnetlistrow = NETLIST_LastRow): void; tests ctwists;
```

## Call pattern

```ats
TestCTwistsAC();
```

## Description

Tests the c-twists of the netlist.

Start and end rows can optionally be passed to the function.

All c-twists will be tested if no rows are passed.

Notice: If a project has modules with identical C-Twist lists, which call this function, the warning "No adequate component found in net list" will be shown for one of those function calls when compiling the project.

## Metadata

- Category: Electrical testing
- Code: 270343
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `StartRow`: `tnetlistrow = NETLIST_FirstRow` — Row of the netlist where the test starts.; Allowed values: NETLIST_FirstRow
- `EndRow`: `tnetlistrow = NETLIST_LastRow` — Row of the netlist where the test ends.; Allowed values: NETLIST_EndRow

## Example

```ats
TestCTwistsAC();
TestCTwistsAC(1, 10);

//The following two lines are equal
TestCTwistsAC(11, NETLIST_LastRow);
TestCTwistsAC(11);
```

## See also

`CTwistTestAC`, `DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `TestAttenuators`, `TestCapacitors`, `TestDiodes`, `TestResistors`, `TestSwitches`, `TestWires`, `TestZDiodes`
