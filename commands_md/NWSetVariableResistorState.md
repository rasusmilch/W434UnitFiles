# NWSetVariableResistorState

## Declaration

```ats
function NWSetVariableResistorState(Name: string; Pin1: tpin; Pin2: tpin; State: string): void;
```

## Call pattern

```ats
NWSetVariableResistorState('Name', "Pin1", "Pin2", 'State');
```

## Description

Sets the state of the variable resistor between Pin1 and Pin2.
The function always refers to a variable resistor in the netlist.


## Metadata

- Category: Network Access
- Code: 266010
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `State`: `string`

## Example

```ats
UIInfoDialog('Set potentiometer Poti_01 to Minimum');
NWSetVariableResistorState('Poti_01', "Pin1", "Pin2", 'Minimum');
VariableResistorTest('Poti_01', "Pin1", "Pin2");
UIInfoDialog('Set potentiometer Poti_01 to Maximum');
NWSetVariableResistorState('Poti_01', "Pin1", "Pin2", 'Maximum');
VariableResistorTest('Poti_01', "Pin1", "Pin2");
```

## See also

`VariableResistorTest`
