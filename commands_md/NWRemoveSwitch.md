# NWRemoveSwitch

## Declaration

```ats
function NWRemoveSwitch(Name: string; Pin1: tpin; Pin2: tpin): boolean; removes_from_net_list switches;
```

## Call pattern

```ats
NWRemoveSwitch('Name', "Pin1", "Pin2");
```

## Description

Removes the switch between Pin1 and Pin2 from the network.

## Metadata

- Category: Network Access
- Code: 266007
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
NWAddSwitch('Temporary switch', "Pin1", "Pin2", CLOSED);
SwitchTest('Temporary switch', "Pin1", "Pin2");
NWRemoveSwitch('Temporary switch', "Pin1", "Pin2");
```

## See also

`NWAddSwitch`, `NWRemoveAllSwitches`, `NWRemoveCapacitor`, `NWRemoveDiode`, `NWRemoveResistor`, `NWRemoveWire`
