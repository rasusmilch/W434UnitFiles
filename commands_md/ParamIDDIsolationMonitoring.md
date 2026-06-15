# ParamIDDIsolationMonitoring

## Declaration

```ats
function ParamIDDIsolationMonitoring(RxThreshold: integer; NWThreshold: integer = PARAM_DontChange; RxAmplification: integer = PARAM_DontChange; StaticCounting: boolean = PARAM_DontChange; CountingInterval: ttime = PARAM_DontChange; GapWidth: ttime = PARAM_DontChange): void;
```

## Call pattern

```ats
ParamIDDIsolationMonitoring(<RxThreshold>, <NWThreshold>, PARAM_DontChange, ON|OFF, <CountingInterval>ns);
```

## Description

Sets the parameters for the isolation monitoring during the intermittent defect detection.

## Metadata

- Category: Parameters
- Code: 2320
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `RxThreshold`: `integer` — If the number of detected shorts of one receiver is above this value, a fail will be counted.
- `NWThreshold`: `integer = PARAM_DontChange` — The test of a network counts as failed if the sum of all errors within the network exceeds this value multipied with the number of receivers within the network. (Default = 0)
- `RxAmplification`: `integer = PARAM_DontChange` — Receiver amplification
; Not yet supported by the hardware.; The value which was is set with ParamIDDContinuityMonitoring will be used.; Allowed values: IDD_RxAmplification_On, IDD_RxAmplification_Off
- `StaticCounting`: `boolean = PARAM_DontChange` — Enabled and disables a static counter.
; The static counter counts, in addition to the number of the shorts, the duration of the shorts.; Allowed values: ON, OFF
- `CountingInterval`: `ttime = PARAM_DontChange` — nterval, in which the static counter for shorts will be increased. (Default: 200 ns)
- `GapWidth`: `ttime = PARAM_DontChange` — Minimum duration of the shorts that shall be detected (Default: 100ns)
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
| `RES_GapWidthChanged` | `boolean` | TRUE, if the minimum duration of the gaps that shall be detected was changed, otherwise FALSE |
| `RES_StaticCountingChanged` | `boolean` | TRUE, if the Static Counting was changed, otherwise FALSE |
| `RES_CountingIntervalChanged` | `boolean` | TRUE, if the counting interval was changed, otherwise FALSE |
| `RES_RxThresholdChanged` | `boolean` | TRUE, if the threshold per receiver was changed, otherwise FALSE |
| `RES_NWThresholdChanged` | `boolean` | TRUE, if the threshold per network was changed, otherwise FALSE |
| `RES_RxAmplificationChanged` | `boolean` | TRUE, if the receiver amplification was changed, otherwise FALSE |
| `RES_IM_GapWidth` | `real` | Minimum duration of the gaps that shall be detected |
| `RES_IM_RxAmplification` | `boolean` | Receiver amplification |
| `RES_IM_NWThreshold` | `integer` | Threshold per receiver in a network |
| `RES_IM_RxThreshold` | `integer` | Threshold per receiver |
| `RES_IM_CountingInterval` | `real` | Counting interval for static counting |
| `RES_IM_StaticCounting` | `real` | Static Counting |

## See also

`ParamIDD`, `ParamIDDStaticContinuity`, `ParamIDDContinuityMonitoring`, `IDDRun`, `IDDEnableManualTrigger`
