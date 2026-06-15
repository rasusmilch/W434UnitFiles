# NWSetResistorValues

## Declaration

```ats
function NWSetResistorValues(Name: string; Pin1: tpin; Pin2: tpin; Resistance: tresistance; LowerTol: tresistance; UpperTol: tresistance; MaxPower: tpower = PARAM_DontChange): void;
```

## Call pattern

```ats
NWSetResistorValues('Name', "Pin1", "Pin2", <Value>Ohm, <LowerTol>Ohm, <UpperTol>Ohm, <MaxPower>W);
```

## Description

Changes the resistance value and the tolerances for the resistor between Pin1 and Pin2.

The function always refers to a resistor in the netlist.

## Metadata

- Category: Network Access
- Code: 265985
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
- `LowerTol`: `tresistance` — Allowed values: PARAM_DontChange
- `UpperTol`: `tresistance` — Allowed values: PARAM_DontChange
- `MaxPower`: `tpower = PARAM_DontChange`

## Example

```ats
ResistorTest('Resistor1', "Pin1", "Pin2");
NWSetResistorValues('Resistor1', "Pin1", "Pin2", 100Ohm, 10Ohm, 10Ohm);
ResistorTest('Resistor1', "Pin1", "Pin2");
```

## See also

`ResistorTest`, `ResistorTestCustom`
