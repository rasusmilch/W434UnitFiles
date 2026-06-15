# ParamGetIsolationLV

## Declaration

```ats
function ParamGetIsolationLV(DataIdentifier: integer): real;
```

## Call pattern

```ats
ParamGetIsolationLV(PARAM_IsolationLV?);
```

## Description

Returns the value of the LV-isolation-test-parameter specified by "DataIdentifier".

## Metadata

- Category: Parameters
- Code: 266243
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program
- Count result: no
- Archive allowed: no

## Parameters

- `DataIdentifier`: `integer` — Allowed values: PARAM_IsolationLVVoltage, PARAM_IsolationLVThreshold, PARAM_IsolationLVTrise, PARAM_IsolationLVTwait, PARAM_IsolationLVTmeas, PARAM_IsolationLVAutoRange, PARAM_IsolationLVTmeasReduction, PARAM_IsolationLVCurrentLimit, PARAM_IsolationLVCurrentLimitValid

## Example

```ats
Threshold = ParamGetIsolationLV(PARAM_IsolationLVThreshold);
```

## See also

`ParamIsolationLV`
