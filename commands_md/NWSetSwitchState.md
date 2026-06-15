# NWSetSwitchState

## Declaration

```ats
function NWSetSwitchState(Name: string; Pin1: tpin; Pin2: tpin; State: integer): void;
```

## Call pattern

```ats
NWSetSwitchState('Name', "Pin1", "Pin2", OPEN|CLOSED);
```

## Description

Sets the state of the switch between Pin1 and Pin2.

The function always refers to a switch in the netlist.


## Metadata

- Category: Network Access
- Code: 265984
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `State`: `integer` — Allowed values: OPEN, CLOSED, INVERT

## Example

```ats
SwitchTest('Switch1', "Pin1", "Pin2");
NWSetSwitchState('Switch1', "Pin1", "Pin2", INVERT);
SwitchTest('Switch1', "Pin1", "Pin2");
```

## See also

`NWResetSwitchStates`, `SwitchTest`
