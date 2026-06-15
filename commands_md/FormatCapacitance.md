# FormatCapacitance

## Declaration

```ats
function FormatCapacitance(Value: real): string;
```

## Call pattern

```ats
FormatCapacitance(Value);
```

## Description

Returns the capacitance value in "Value" (in farad) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263427
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatCapacitance(0.000001);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
