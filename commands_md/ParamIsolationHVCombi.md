# ParamIsolationHVCombi

## Declaration

```ats
function ParamIsolationHVCombi(LowerTolerance: real; UpperTolerance: real; Delay1: ttime = PARAM_DontChange; Delay2: ttime = PARAM_DontChange; ExecuteHV2: boolean = PARAM_DontChange): void;
```

## Call pattern

```ats
ParamIsolationHVCombi(<LowerTol%>, <UpperTol%>, <Delay1>ms, <Delay2>ms, TRUE|FALSE);
```

## Description

Sets the parameters for combined high voltage tests.

## Metadata

- Category: Parameters
- Code: 2312
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `LowerTolerance`: `real` — Lower tolerance between the first and the second DC measurement.; Presetting; : 100%
- `UpperTolerance`: `real` — Upper tolerance between the first and the second DC measurement.; Presetting; : 100%
- `Delay1`: `ttime = PARAM_DontChange` — Delay between the first DC and the AC measurement.; Presetting; : 0s
- `Delay2`: `ttime = PARAM_DontChange` — Delay between the AC and the second DC measurement.; Presetting; : 0s
- `ExecuteHV2`: `boolean = PARAM_DontChange` — If TRUE is passed a DC then an AC and then again a DC measurement are executed.
; If FALSE is passed a DC and then an AC measurement are executed.; Presetting; : TRUE; Allowed values: TRUE, FALSE

## Example

```ats
ParamIsolationHVCombi(30, 40, 200ms, PARAM_DontChange, TRUE);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_HVCLowerHV2Tol` | `real` | Lower tolerance for difference between first and second HV measurement |
| `RES_HVCUpperHV2Tol` | `real` | Upper tolerance for difference between first and second HV measurement |
| `RES_HVCDelay1` | `real` | Delay between first HV measurement and DB measurement |
| `RES_HVCDelay2` | `real` | Delay between DB measurement and second HV measurement |
| `RES_HVCExecuteHV2` | `boolean` | The second HV measurement will be done if this value is TRUE |
| `RES_HVCLowerHV2TolChanged` | `boolean` | TRUE, if the value of the lower tolerance was changed, otherwise FALSE |
| `RES_HVCUpperHV2TolChanged` | `boolean` | TRUE, if the value of the upper tolerance was changed, otherwise FALSE |
| `RES_HVCDelay1Changed` | `boolean` | TRUE, if the value of the first delay was changed, otherwise FALSE |
| `RES_HVCDelay2Changed` | `boolean` | TRUE, if the value of the second delay was changed, otherwise FALSE |
| `RES_HVCExecuteHV2Changed` | `boolean` | TRUE, if the flag for the second HV measurement was changed, otherwise FALSE |

## See also

`IsolationTestHVCombi`, `NoConnAllHVCombi`, `NoConnectionHVCombi`, `NoConnGroupHVCombi`, `ParamDielectricBreakdown`, `ParamIsolationHV`
