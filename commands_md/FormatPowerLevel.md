# FormatPowerLevel

## Declaration

```ats
function FormatPowerLevel(Value: real): string;
```

## Call pattern

```ats
FormatPowerLevel(Value);
```

## Description

Returns the power level value in "Value" (in dBm) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263442
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatPowerLevel(3.23265);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
