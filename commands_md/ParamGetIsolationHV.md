# ParamGetIsolationHV

## Declaration

```ats
function ParamGetIsolationHV(DataIdentifier: integer): real;
```

## Call pattern

```ats
ParamGetIsolationHV(PARAM_IsolationHV?);
```

## Description

Returns the value of the HV-isolation-test-parameter specified by "DataIdentifier".

## Metadata

- Category: Parameters
- Code: 266244
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program
- Count result: no
- Archive allowed: no

## Parameters

- `DataIdentifier`: `integer` — Allowed values: PARAM_IsolationHVVoltage, PARAM_IsolationHVThreshold, PARAM_IsolationHVTrise, PARAM_IsolationHVTwait, PARAM_IsolationHVTmeas, PARAM_IsolationHVAutoRange, PARAM_IsolationHVTmeasReduction, PARAM_IsolationHVCurrentLimit, PARAM_IsolationHVTmeasFactor, PARAM_IsolationHVVoltageRamp, PARAM_IsolationHVCurrentLimitValid, PARAM_IsolationHVValid, PARAM_IsolationHVIThreshold, PARAM_IsolationHVUseIThreshold, PARAM_IsolationHVdIdtEnabled, PARAM_IsolationHVdIdtCurrentThreshold, PARAM_IsolationHVdIdtTimeThreshold, PARAM_IsolationHVExpectedRValue, PARAM_IsolationHVExpectedIValue

## Example

```ats
Threshold = ParamGetIsolationHV(PARAM_IsolationHVThreshold);
```

## See also

`ParamIsolationHV`
