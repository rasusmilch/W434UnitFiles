# ParamGetDielectricBreakdown

## Declaration

```ats
function ParamGetDielectricBreakdown(DataIdentifier: integer): real;
```

## Call pattern

```ats
ParamGetDielectricBreakdown(PARAM_DielectricBreakdown?);
```

## Description

Returns the value of the dielectric-breakdown-test-parameter specified by "DataIdentifier".

## Metadata

- Category: Parameters
- Code: 266245
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program
- Count result: no
- Archive allowed: no

## Parameters

- `DataIdentifier`: `integer` — Allowed values: PARAM_DielectricBreakdownVoltage, PARAM_DielectricBreakdownTrise, PARAM_DielectricBreakdownTwait, PARAM_DielectricBreakdownTmeas, PARAM_DielectricBreakdownTmeasFactor, PARAM_DielectricBreakdownVoltageRamp, PARAM_DielectricBreakdownThresholdIr, PARAM_DielectricBreakdownThresholdIi, PARAM_DielectricBreakdownFrequency, PARAM_DielectricBreakdownCurrentThresholdsValid, PARAM_DielectricBreakdownValid, PARAM_DielectricBreakdownAutoRange

## Example

```ats
Voltage = ParamGetDielectricBreakdown(PARAM_DielectricBreakdownVoltage);
```

## See also

`ParamDielectricBreakdown`
