# FormatResistance

## Declaration

```ats
function FormatResistance(Value: real): string;
```

## Call pattern

```ats
FormatResistance(Value);
```

## Description

Returns the resistance value in "Value" (in ohm) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263426
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatResistance(1000000);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
