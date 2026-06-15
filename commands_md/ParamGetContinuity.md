# ParamGetContinuity

## Declaration

```ats
function ParamGetContinuity(DataIdentifier: integer): real;
```

## Call pattern

```ats
ParamGetContinuity(PARAM_Continuity?);
```

## Description

Returns the value of the continuity-test-parameter specified by "DataIdentifier".

## Metadata

- Category: Parameters
- Code: 266242
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program
- Count result: no
- Archive allowed: no

## Parameters

- `DataIdentifier`: `integer` — Allowed values: PARAM_ContinuityCurrent, PARAM_ContinuityThreshold, PARAM_ContinuityTrise, PARAM_ContinuityTwait, PARAM_ContinuityTmeas, PARAM_ContinuityAutoRange, PARAM_ContinuityVoltageLimit, PARAM_ContinuityVoltageLimitValid

## Example

```ats
Threshold = ParamGetContinuity(PARAM_ContinuityThreshold);
```

## See also

`ParamContinuity`
