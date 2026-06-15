# TestResistors

## Declaration

```ats
function TestResistors(StartRow: tnetlistrow = NETLIST_FirstRow; EndRow: tnetlistrow = NETLIST_LastRow): void; tests resistors;
```

## Call pattern

```ats
TestResistors();
```

## Description

Tests the resistors of the netlist.

Start and end rows can optionally be passed to the function.

All resistors will be tested if no rows are passed.

Notice: If a project has modules with identical resistor lists, which call this function, the warning "No adequate component found in net list" will be shown for one of those function calls when compiling the project.

## Metadata

- Category: Electrical testing
- Code: 270338
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
TestResistors();
TestResistors(1, 10);

//The following two lines are equal
TestResistors(11, NETLIST_LastRow);
TestResistors(11);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `ResistorTest`, `TestAttenuators`, `TestCapacitors`, `TestCTwistsAC`, `TestDiodes`, `TestSwitches`, `TestWires`, `TestZDiodes`
