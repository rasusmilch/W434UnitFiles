# FormatLength

## Declaration

```ats
function FormatLength(Value: real): string;
```

## Call pattern

```ats
FormatLength(Value);
```

## Description

Returns the length value in "Value" (in meters) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263445
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatLength(0.37);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatCurrent`, `FormatFrequency`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`, `FomratConductance`
