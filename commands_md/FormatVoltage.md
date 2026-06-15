# FormatVoltage

## Declaration

```ats
function FormatVoltage(Value: real): string;
```

## Call pattern

```ats
FormatVoltage(Value);
```

## Description

Returns the voltage value in "Value" (in volt) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263428
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatVoltage(2250);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltageRamp`
