# FormatFrequency

## Declaration

```ats
function FormatFrequency(Value: real): string;
```

## Call pattern

```ats
FormatFrequency(Value);
```

## Description

Returns the frequency value in "Value" (in hertz) in a readable format with unit.

## Metadata

- Category: Formatting
- Code: 263443
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Output = FormatFrequency(1500000);
UIWriteNormal(Output);
```

## See also

`FormatAttenuation`, `FormatCapacitance`, `FormatConductance`, `FormatCurrent`, `FormatInductance`, `FormatPower`, `FormatPowerLevel`, `FormatResistance`, `FormatTime`, `FormatVoltage`, `FormatVoltageRamp`
