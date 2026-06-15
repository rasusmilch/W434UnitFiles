# NWAddCapacitor

## Declaration

```ats
function NWAddCapacitor(Name: string; Pin1: tpin; Pin2: tpin; Capacitance: tcapacitance; LowerTol: tcapacitance; UpperTol: tcapacitance; Voltage: tvoltage): boolean; adds_to_net_list capacitors;
```

## Call pattern

```ats
NWAddCapacitor('Name', "Pin1", "Pin2", <Capacitance>uF, <LowerTol>uF, <UpperTol>uF, <Voltage>V);
```

## Description

Adds a capacitor to the network.

If there already exists a component between the specified pins the new component will not be added.

## Metadata

- Category: Network Access
- Code: 265998
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Capacitance`: `tcapacitance`
- `LowerTol`: `tcapacitance`
- `UpperTol`: `tcapacitance`
- `Voltage`: `tvoltage`

## Return value

The function returns TRUE if the component was successfully added, otherwise FALSE.

## Example

```ats
NWAddCapacitor('Temporary capacitor', "Pin1", "Pin2", 100uF, 10uF, 10uF, 4V);
CapacitorTest('Temporary capacitor', "Pin1", "Pin2");
NWRemoveCapacitor('Temporary capacitor', "Pin1", "Pin2");
```

## See also

`CapacitorTest`, `NWAddDiode`, `NWAddResistor`, `NWAddSwitch`, `NWAddWire`, `NWRemoveAllCapacitors`, `NWRemoveCapacitor`
