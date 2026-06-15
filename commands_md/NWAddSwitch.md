# NWAddSwitch

## Declaration

```ats
function NWAddSwitch(Name: string; Pin1: tpin; Pin2: tpin; State: integer): boolean; adds_to_net_list switches;
```

## Call pattern

```ats
NWAddSwitch('Name', "Pin1", "Pin2", OPEN|CLOSED);
```

## Description

Adds a switch to the network.

If there already exists a component between the specified pins the new component will not be added.

## Metadata

- Category: Network Access
- Code: 266006
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `State`: `integer` — Allowed values: OPEN, CLOSED

## Return value

The function returns TRUE if the component was successfully added, otherwise FALSE.

## Example

```ats
NWAddSwitch('Temporary switch', "Pin1", "Pin2", CLOSED);
SwitchTest('Temporary switch', "Pin1", "Pin2");
NWRemoveSwitch('Temporary switch', "Pin1", "Pin2");
```

## See also

`NWAddCapacitor`, `NWAddDiode`, `NWAddResistor`, `NWAddWire`, `NWRemoveAllSwitches`, `NWRemoveSwitch`, `SwitchTest`
