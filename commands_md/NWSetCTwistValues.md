# NWSetCTwistValues

## Declaration

```ats
function NWSetCTwistValues(Name: string; Pin1: tpin; Pin2: tpin; Capacitance: tcapacitance; LowerTol: tcapacitance; UpperTol: tcapacitance): void;
```

## Call pattern

```ats
NWSetCTwistValues('Name', "Pin1", "Pin2", <Value>nF, <LowerTol>nF, <UpperTol>nF);
```

## Description

Changes the capacitance value and the tolerances for the C-Twist between Pin1 and Pin2.

The function always refers to a C-Twist in the netlist.

## Metadata

- Category: Network Access
- Code: 266012
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

## Example

```ats
CTwistTest('C-Twist 1', "Pin1", "Pin2");
NWSetCTwistValues('C-Twist 1', "Pin1", "Pin2", 100nF, 10nF, 10nF);
CTwistTest('C-Twist 1', "Pin1", "Pin2");
```

## See also

`CTwistTestAC`
