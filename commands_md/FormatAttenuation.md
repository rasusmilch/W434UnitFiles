# FormatAttenuation

## Declaration

```ats
function FormatAttenuation(Value: real): real;
```

## Call pattern

```ats
FormatAttenuation(Value);
```

## Description

Returns the resistance value in "Value" (in dB) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263441
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatAttenuation(3.23265);
UIWriteNormal(Output);
```

## See also

`FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
