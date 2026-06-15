# ParamIsolation3xHV

## Declaration

```ats
function ParamIsolation3xHV(LowerTolerance: real; UpperTolerance: real; Delay1: ttime = PARAM_DontChange; Delay2: ttime = PARAM_DontChange; ExecuteHV3: boolean = PARAM_DontChange): void;
```

## Call pattern

```ats
ParamIsolation3xHV(<LowerTol%>, <UpperTol%>, <Delay1>ms, <Delay2>ms, TRUE|FALSE);
```

## Description

Sets the parameters for the triple HV isolation test.

## Metadata

- Category: Parameters
- Code: 2322
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `LowerTolerance`: `real` — Lower tolerance between the first and the third measurement.; Presetting; : 100%
- `UpperTolerance`: `real` — Upper tolerance between the first and the third measurement.; Presetting; : 100%
- `Delay1`: `ttime = PARAM_DontChange` — Delay between the first and the second measurement.; Presetting; : 0s
- `Delay2`: `ttime = PARAM_DontChange` — Delay between the second and the third measurement.; Presetting; : 0s
- `ExecuteHV3`: `boolean = PARAM_DontChange` — If TRUE is passed three measurements will be executed.; If FALSE is passed the third measurement will not be executed.; Presetting; : TRUE; Allowed values: TRUE, FALSE

## Example

```ats
ParamIsolation3xHV(30, 40, 200ms, PARAM_DontChange, TRUE);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_3xHV_Lower_1_3_Tol` | `real` | Lower tolerance for the difference between the first and the third measurement. |
| `RES_3xHV_Upper_1_3_Tol` | `real` | Upper tolerance for the difference between the first and the third measurement. |
| `RES_3xHV_Delay1` | `real` | Delay between the first and the second measurement. |
| `RES_3xHV_Delay2` | `real` | Delay between the second and the third measurement. |
| `RES_3xHV_ExecuteHV3` | `boolean` | The third mesaurement will be done if this value is TRUE |
| `RES_3xHV_Lower_1_3_Tol_Changed` | `boolean` | TRUE, if the value of the lower tolerance was changed, otherwise FALSE |
| `RES_3xHV_Upper_1_3_Tol_Changed` | `boolean` | TRUE, if the value of the upper tolerance was changed, otherwise FALSE |
| `RES_3xHV_Delay1_Changed` | `boolean` | TRUE, if the value of the first delay was changed, otherwise FALSE |
| `RES_3xHV_Delay2_Changed` | `boolean` | TRUE, if the value of the second delay was changed, otherwise FALSE |
| `RES_3xHV_ExecuteHV3_Changed` | `boolean` | TRUE, if the flag for the third measurement was changed, otherwise FALSE |

## See also

`IsolationTest3xHV`, `NoConnAll3xHV`, `NoConnection3xHV`, `NoConnGroup3xHV`, `ParamIsolation3xHV2ndMeasurement`, `ParamIsolationHV`
