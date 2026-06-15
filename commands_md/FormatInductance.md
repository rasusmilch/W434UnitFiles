# FormatInductance

## Declaration

```ats
function FormatInductance(Value: real): string;
```

## Call pattern

```ats
FormatInductance(Value);
```

## Description

Returns the inductance value in "Value" (in henry) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263438
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatInductance(0.001);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatFrequency`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
