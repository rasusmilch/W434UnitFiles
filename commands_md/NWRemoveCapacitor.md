# NWRemoveCapacitor

## Declaration

```ats
function NWRemoveCapacitor(Name: string; Pin1: tpin; Pin2: tpin): boolean; removes_from_net_list capacitors;
```

## Call pattern

```ats
NWRemoveCapacitor('Name', "Pin1", "Pin2");
```

## Description

Removes the capacitor between Pin1 and Pin2 from the network.

## Metadata

- Category: Network Access
- Code: 265999
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
NWAddCapacitor('Temporary capacitor', "Pin1", "Pin2", 100uF, 10uF, 10uF, 4V);
CapacitorTest('Temporary capacitor', "Pin1", "Pin2");
NWRemoveCapacitor('Temporary capacitor', "Pin1", "Pin2");
```

## See also

`NWAddCapacitor`, `NWRemoveAllCapacitors`, `NWRemoveDiode`, `NWRemoveResistor`, `NWRemoveSwitch`, `NWRemoveWire`
