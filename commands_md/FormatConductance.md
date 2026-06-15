# FormatConductance

## Declaration

```ats
function FormatConductance(Value: real): string;
```

## Call pattern

```ats
FormatConductance(Value);
```

## Description

Returns the conductance value in "Value" (in siemens) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263444
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatConductance(0.001);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
