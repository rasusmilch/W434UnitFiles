# FormatTime

## Declaration

```ats
function FormatTime(Value: real): string;
```

## Call pattern

```ats
FormatTime(Time);
```

## Description

Returns the time value in "Value" (in seconds) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263424
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatTime(0.001);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatVoltage`, `FormatVoltageRamp`
