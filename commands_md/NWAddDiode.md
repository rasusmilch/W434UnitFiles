# NWAddDiode

## Declaration

```ats
function NWAddDiode(Name: string; Pin1: tpin; Pin2: tpin; Voltage1: tvoltage; Voltage2: tvoltage; Voltage3: tvoltage; Current: tcurrent): boolean; adds_to_net_list diodes;
```

## Call pattern

```ats
NWAddDiode('Name', "Pin1", "Pin2", <Voltage>V, <Voltage>V, <Voltage>V, <Current>mA);
```

## Description

Adds a diode to the network.

If there already exists a component between the specified pins the new component will not be added.

## Metadata

- Category: Network Access
- Code: 266000
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Voltage1`: `tvoltage`
- `Voltage2`: `tvoltage`
- `Voltage3`: `tvoltage`
- `Current`: `tcurrent`

## Return value

The function returns TRUE if the component was successfully added, otherwise FALSE.

## Example

```ats
NWAddDiode('Temporary diode', "Pin1", "Pin2", 0.5V, 1V, 4V, 10mA);
DiodeTest('Temporary diode', "Pin1", "Pin2");
NWRemoveDiode('Temporary diode', "Pin1", "Pin2");
```

## See also

`DiodeTest`, `NWAddCapacitor`, `NWAddResistor`, `NWAddSwitch`, `NWAddWire`, `NWRemoveAllDiodes`, `NWRemoveDiode`
