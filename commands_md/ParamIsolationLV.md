# ParamIsolationLV

## Declaration

```ats
function ParamIsolationLV(Voltage: tvoltage=PARAM_DontChange; Threshold: tresistance=PARAM_DontChange; Trise: ttime=PARAM_DontChange; Twait: ttime=PARAM_DontChange; Tmeas: ttime=PARAM_DontChange; AutoRange: boolean=PARAM_DontChange; TmeasReduction: boolean=PARAM_DontChange; ILimit: tcurrent=PARAM_DontChange): void;
```

## Call pattern

```ats
ParamIsolationLV(<Voltage>V, <Threshold>Ohm, <Trise>ms, <Twait>ms, <Tmeas>ms, AutoRange, TmeasReduction, <Ilimit>mA);
```

## Description

Sets the parameters for the LV isolation test.

## Metadata

- Category: Parameters
- Code: 2305
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Voltage`: `tvoltage=PARAM_DontChange` — Test voltage which the test system tries to build up.
- `Threshold`: `tresistance=PARAM_DontChange` — Threshold resistance for the transition between connection and discontinuity.
; If the measured resistance is lower than the threshold, the system detects a connection.; If the measured resistance is higher, the system detects a discontinuity.
- `Trise`: `ttime=PARAM_DontChange` — Time interval within which the test voltage must be reached.
- `Twait`: `ttime=PARAM_DontChange` — Time between reaching the test voltage and first measurement of the resistance.
- `Tmeas`: `ttime=PARAM_DontChange` — Duration of the actual measurement within which the threshold must be exceeded.
- `AutoRange`: `boolean=PARAM_DontChange` — If the Autorange option is activated, additional measurements with changing ranges are executed if an error occurs to determine the exact resistance value.; Allowed values: ON, OFF
- `TmeasReduction`: `boolean=PARAM_DontChange` — If this option is enabled the measurement is considered done and aborted as soon as the threshold resistance is reached.; Allowed values: ON, OFF
- `ILimit`: `tcurrent=PARAM_DontChange` — Maximum current which is allowed during the test and and in case of an error.

## Example

```ats
ParamIsolationLV(30V, 80kOhm, PARAM_DontChange, 10ms, PARAM_DontChange, ON, ON, 5mA);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_LVVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_LVThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_LVTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_LVTwait` | `real` | Parameter: Wait time in seconds |
| `RES_LVTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_LVAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_LVCurrentLimit` | `real` | Parameter: Current limit in Ampere |
| `RES_LVTmeasReduction` | `boolean` | Parameter: Measurement time reduction (dwelltime bypass) |
| `RES_VoltageChanged` | `boolean` | TRUE, if voltage was modified, otherwise FALSE |
| `RES_ThresholdChanged` | `boolean` | TRUE, if threshold was modified, otherwise FALSE |
| `RES_TriseChanged` | `boolean` | TRUE, if maximum rise time was modified, otherwise FALSE |
| `RES_TwaitChanged` | `boolean` | TRUE, if wait time was modified, otherwise FALSE |
| `RES_TmeasChanged` | `boolean` | TRUE, if measurement time was modified, otherwise FALSE |
| `RES_AutoRangeChanged` | `boolean` | TRUE, if automatic ranging was modified, otherwise FALSE |
| `RES_CurrentLimitChanged` | `boolean` | TRUE, if current limit was modified, otherwise FALSE |
| `RES_TmeasReductionChanged` | `boolean` | TRUE, if measurement time reduction was modified, otherwise FALSE |

## See also

`IsolationTestLV`, `NoConnAllLV`, `NoConnectionLV`, `NoConnGroupLV`, `ParamContinuity`, `ParamDielectricBreakdown`, `ParamGetIsolationLV`, `ParamIsolationHV`
