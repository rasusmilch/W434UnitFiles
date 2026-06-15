# FormatPower

## Declaration

```ats
function FormatPower(Value: real): string;
```

## Call pattern

```ats
FormatPower(Value);
```

## Description

Returns the power value in "Value" (in watt) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263429
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatPower(0.001);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
