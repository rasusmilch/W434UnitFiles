# NWRemoveWire

## Declaration

```ats
function NWRemoveWire(Name: string; Pin1: tpin; Pin2: tpin): boolean; removes_from_net_list wires;
```

## Call pattern

```ats
NWRemoveWire('Name', "Pin1", "Pin2");
```

## Description

Removes the wire between Pin1 and Pin2 from the network.

## Metadata

- Category: Network Access
- Code: 265992
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
NWAddWire('Temporary wire', "Pin1", "Pin2", [COLOR_Red,  COLOR_Yellow]);
WireTest('Temporary wire', "Pin1", "Pin2");
NWRemoveWire('Temporary wire', "Pin1", "Pin2");
```

## See also

`NWAddWire`, `NWRemoveAllWires`, `NWRemoveCapacitor`, `NWRemoveDiode`, `NWRemoveResistor`, `NWRemoveSwitch`
