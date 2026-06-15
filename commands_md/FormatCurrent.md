# FormatCurrent

## Declaration

```ats
function FormatCurrent(Value: real): string;
```

## Call pattern

```ats
FormatCurrent(Value);
```

## Description

Returns the current value in "Value" (in ampere) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263425
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatCurrent(0.001);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
