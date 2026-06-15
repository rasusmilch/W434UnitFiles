# ParamIDDStaticContinuity

## Declaration

```ats
function ParamIDDStaticContinuity(LowerThreshold: integer; UpperThreshold: integer = PARAM_DontChange; Ttest: ttime = PARAM_DontChange; Delay: ttime = PARAM_DontChange; RxAmplification: integer = PARAM_DontChange; CountingInterval: ttime = PARAM_DontChange; GapWidth: ttime = PARAM_DontChange): void;
```

## Call pattern

```ats
ParamIDDStaticContinuity(<LowerThreshold>, <UpperThreshold>, <Ttest>ms, <Delay>ms, IDD_RxAmplification_On|IDD_RxAmplification_Off, <TimeSlice>ns);
```

## Description

Sets the measurement parameters for the IDD Pretest and IDD Finalization.

## Metadata

- Category: Parameters
- Code: 2318
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `LowerThreshold`: `integer` — This must be a percentage which has to be less than 100 and less than UpperThreshold. (Default = 40)
; If the duration of the connection is below this value during the continuity test, the test will fail.
- `UpperThreshold`: `integer = PARAM_DontChange` — This must be a percentage which has to be less than 100 and greater than LowerThreshold. (Default = 60)
; If the duration of the connection is longer than this value during the continuity test, the test will pass.
- `Ttest`: `ttime = PARAM_DontChange` — Duration of the test of a network (Default: 2 ms)
- `Delay`: `ttime = PARAM_DontChange` — Delay between the tests of two networks (Default: 100 ms; at least 50 ms)
- `RxAmplification`: `integer = PARAM_DontChange` — Receiver amplification; Allowed values: IDD_RxAmplification_On, IDD_RxAmplification_Off
- `CountingInterval`: `ttime = PARAM_DontChange` — Interval, in which the static counter for disconnections will be increased. (Default: 200 ns)
- `GapWidth`: `ttime = PARAM_DontChange` — Minimum duration of the gaps that shall be detected (Default 100ns)
; Not yet supported by the hardware.

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
| `RES_TtestChanged` | `boolean` | TRUE, if the duration of the test of a network was changed, otherwise FALSE |
| `RES_GapWidthChanged` | `boolean` | TRUE, if the minimum duration of the gaps that shall be detected was changed, otherwise FALSE |
| `RES_CountingIntervalChanged` | `boolean` | TRUE, if the time slice for counting was changed, otherwise FALSE |
| `RES_DelayChanged` | `boolean` | TRUE; if the delay between the tests of two networks was changed, otherwise FALSE |
| `RES_LowerThresholdChanged` | `boolean` | TRUE, if the lower threshold for the static continuity tests was changed, otherwise FALSE |
| `RES_UpperThresholdChanged` | `boolean` | TRUE, if the upper threshold for continuity and isolation tests was changed, otherwise FALSE |
| `RES_RxAmplificationChanged` | `boolean` | TRUE, if the receiver amplification was changed, otherwise FALSE |
| `RES_SC_Ttest` | `real` | Duration of the test of a network |
| `RES_SC_LowerThreshold` | `integer` | Lower threshold for continuity and isolation tests |
| `RES_SC_UpperThreshold` | `integer` | Upper threshold for continuity and isolation tests |
| `RES_SC_GapWidth` | `real` | Minimum duration of the gaps that shall be detected |
| `RES_SC_CountingInterval` | `real` | Time slice for counting |
| `RES_SC_Delay` | `real` | Delay between the tests of two networks |
| `RES_SC_RxAmplification` | `integer` | Receiver amplification |

## See also

`ParamIDD`, `ParamIDDContinuityMonitoring`, `ParamIDDIsolationMonitoring`, `IDDRun`, `IDDEnableManualTrigger`
