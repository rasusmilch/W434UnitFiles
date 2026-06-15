# NWAddResistor

## Declaration

```ats
function NWAddResistor(Name: string; Pin1: tpin; Pin2: tpin; Resistance: tresistance; LowerTol: tresistance; UpperTol: tresistance; Power: tpower = 1W): boolean; adds_to_net_list resistors;
```

## Call pattern

```ats
NWAddResistor('Name', "Pin1", "Pin2", <Resistance>Ohm, <LowerTol>Ohm, <UpperTol>Ohm, <Power>W);
```

## Description

Adds a resistor to the network.

If there already exists a component between the specified pins the new component will not be added.

## Metadata

- Category: Network Access
- Code: 265988
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Resistance`: `tresistance`
- `LowerTol`: `tresistance`
- `UpperTol`: `tresistance`
- `Power`: `tpower = 1W`

## Return value

The function returns TRUE if the component was successfully added, otherwise FALSE.

## Example

```ats
NWAddResistor('Temporary resistor', "Pin1", "Pin2", 100Ohm, 10Ohm, 10Ohm);
ResistorTest('Temporary resistor', "Pin1", "Pin2");
NWRemoveResistor('Temporary resistor', "Pin1", "Pin2");
```

## See also

`NWAddCapacitor`, `NWAddDiode`, `NWAddSwitch`, `NWAddWire`, `NWRemoveAllResistors`, `NWRemoveResistor`, `ResistorTest`
