# NWAddWire

## Declaration

```ats
function NWAddWire(Name: string; Pin1: tpin; Pin2: tpin; Colors: tintegerarray): boolean; adds_to_net_list wires;
```

## Call pattern

```ats
NWAddWire('Name', "Pin1", "Pin2", [COLOR_?]);
```

## Description

Adds a wire to the network.

If there already exists a component between the specified pins the new component will not be added.

## Metadata

- Category: Network Access
- Code: 265991
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Colors`: `tintegerarray`

## Return value

The function returns TRUE if the component was successfully added, otherwise FALSE.

## Example

```ats
NWAddWire('Temporary wire', "Pin1", "Pin2", [COLOR_Red,  COLOR_Yellow]);
WireTest('Temporary wire', "Pin1", "Pin2");
NWRemoveWire('Temporary wire', "Pin1", "Pin2");
```

## See also

`NWAddCapacitor`, `NWAddDiode`, `NWAddResistor`, `NWAddSwitch`, `NWRemoveAllResistors`, `NWRemoveResistor`, `WireTest`
