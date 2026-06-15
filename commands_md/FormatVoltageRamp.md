# FormatVoltageRamp

## Declaration

```ats
function FormatVoltageRamp(Value: real): string;
```

## Call pattern

```ats
FormatVoltageRamp(Value);
```

## Description

Returns the voltage ramp value in "Value" (in volts per second) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263435
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatVoltageRamp(2000000);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`
