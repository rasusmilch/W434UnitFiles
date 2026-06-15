# TestAttenuators

## Declaration

```ats
function TestAttenuators(StartRow: tnetlistrow = NETLIST_FirstRow; EndRow: tnetlistrow = NETLIST_LastRow): void; tests attenuators;
```

## Call pattern

```ats
TestAttenuators();
```

## Description

Tests the attenuators of the netlist.

Start and end rows can optionally be passed to the function.

All attenuators will be tested if no rows are passed.

Notice: If a project has modules with identical optical fiber lists, which call this function, the warning "No adequate component found in net list" will be shown for one of those function calls when compiling the project.

## Metadata

- Category: Electrical testing
- Code: 270345
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `StartRow`: `tnetlistrow = NETLIST_FirstRow` — Allowed values: NETLIST_FirstRow
- `EndRow`: `tnetlistrow = NETLIST_LastRow` — Allowed values: NETLIST_LastRow

## Example

```ats
TestAttenuators();
TestAttenuators(1, 10);

//The following two lines are equal
TestAttenuators(11, NETLIST_LastRow);
TestAttenuators(11);
```

## See also

`AttenuatorTest`, `DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `TestCapacitors`, `TestCTwistsAC`, `TestDiodes`, `TestResistors`, `TestSwitches`, `TestZDiodes`
