# NWRemoveResistor

## Declaration

```ats
function NWRemoveResistor(Name: string; Pin1: tpin; Pin2: tpin): boolean; removes_from_net_list resistors;
```

## Call pattern

```ats
NWRemoveResistor('Name', "Pin1", "Pin2");
```

## Description

Removes the resistor between Pin1 and Pin2 from the network.

## Metadata

- Category: Network Access
- Code: 265989
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`

## Return value

The function returns TRUE if the component was successfully removed, otherwise FALSE.

## Example

```ats
NWAddResistor('Temporary resistor', "Pin1", "Pin2", 100Ohm, 10Ohm, 10Ohm);
ResistorTest('Temporary resistor', "Pin1", "Pin2");
NWRemoveResistor('Temporary resistor', "Pin1", "Pin2");
```

## See also

`NWAddResistor`, `NWRemoveAllResistors`, `NWRemoveCapacitor`, `NWRemoveDiode`, `NWRemoveSwitch`, `NWRemoveWire`
