# NWRemoveDiode

## Declaration

```ats
function NWRemoveDiode(Name: string; Pin1: tpin; Pin2: tpin): boolean; removes_from_net_list diodes;
```

## Call pattern

```ats
NWRemoveDiode('Name', "Pin1", "Pin2");
```

## Description

Removes the diode between Pin1 and Pin2 from the network.

## Metadata

- Category: Network Access
- Code: 266001
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
NWAddDiode('Temporary diode', "Pin1", "Pin2", 0.5V, 1V, 4V, 10mA);
DiodeTest('Temporary diode', "Pin1", "Pin2");
NWRemoveDiode('Temporary diode', "Pin1", "Pin2");
```

## See also

`NWAddDiode`, `NWRemoveAllDiodes`, `NWRemoveCapacitor`, `NWRemoveResistor`, `NWRemoveSwitch`, `NWRemoveWire`
