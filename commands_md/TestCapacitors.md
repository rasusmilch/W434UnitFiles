# TestCapacitors

## Declaration

```ats
function TestCapacitors(StartRow: tnetlistrow = NETLIST_FirstRow; EndRow: tnetlistrow = NETLIST_LastRow): void; tests capacitors;
```

## Call pattern

```ats
TestCapacitors();
```

## Description

Tests the capacitors of the netlist.

Start and end rows can optionally be passed to the function.

All capacitors will be tested if no rows are passed.

Notice: If a project has modules with identical capacitor lists, which call this function, the warning "No adequate component found in net list" will be shown for one of those function calls when compiling the project.

## Metadata

- Category: Electrical testing
- Code: 270339
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
TestCapacitors();
TestCapacitors(1, 10);

//The following two lines are equal
TestCapacitors(11, NETLIST_LastRow);
TestCapacitors(11);
```

## See also

`CapacitorTest`, `DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `TestAttenuators`, `TestCTwistsAC`, `TestDiodes`, `TestResistors`, `TestSwitches`, `TestWires`, `TestZDiodes`
