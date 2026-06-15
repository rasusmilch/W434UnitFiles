# ParamIDD

## Declaration

```ats
function ParamIDD(UseBandWidthFilter: boolean; UseNoiseFilter: boolean = PARAM_DontChange): void;
```

## Call pattern

```ats
ParamIDD(ON|OFF);
```

## Description

Sets general measurement parameters for the intermittent defect detection

## Metadata

- Category: Parameters
- Code: 2317
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `UseBandWidthFilter`: `boolean` — A filter can be acitvated to reduce interferences. The filter is automatically enabled when the Short Identification is used.; Allowed values: ON, OFF
- `UseNoiseFilter`: `boolean = PARAM_DontChange` — Allowed values: ON, OFF

## Example

```ats
ParamStopOnFail(COMMANDS_IDD, ON);

ParamIDD(OFF);
ParamIDDStaticContinuity(20, 80, 2ms, 100ms, IDD_RxAmplification_On, 200ns);
ParamIDDContinuityMonitoring(100, 80, ON, IDD_RxAmplification_On, ON, 200ns);
ParamIDDIsolationMonitoring(200, 160, PARAM_DontChange, ON, 200ns);

IDDEnableManualTrigger('Activate the shaker and click to start the test');

NWCreatePinlist(TransmitterList, COMPONENT_Wire, COMPONENTDATA_Information , '*IDD*', COMPONENTPINS_Primary, FALSE);

IDDRun('Intermittent Defect Detection', TransmitterList, 30s);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_UseFilter` | `boolean` | Filter activated or deactivated |
| `RES_UseFilterChanged` | `boolean` | TRUE, if the the filter was changed, otherwise FALSE |

## See also

`ParamIDDStaticContinuity`, `ParamIDDContinuityMonitoring`, `ParamIDDIsolationMonitoring`, `IDDRun`, `IDDEnableManualTrigger`
