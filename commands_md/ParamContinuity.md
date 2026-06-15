# ParamContinuity

## Declaration

```ats
function ParamContinuity(Current: tcurrent=PARAM_DontChange; Threshold: tresistance=PARAM_DontChange; Trise: ttime=PARAM_DontChange; Twait: ttime=PARAM_DontChange; Tmeas: ttime=PARAM_DontChange; AutoRange: boolean=PARAM_DontChange; ULimit: tvoltage=PARAM_DontChange): void;
```

## Call pattern

```ats
ParamContinuity(<Current>mA, <Threshold>Ohm, <Trise>ms, <Twait>ms, <Tmeas>ms, AutoRange, <Ulimit>V);
```

## Description

Sets the parameters for the continuity test.

## Metadata

- Category: Parameters
- Code: 2304
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Current`: `tcurrent=PARAM_DontChange` — Test current which the test system tries to build up.
- `Threshold`: `tresistance=PARAM_DontChange` — Threshold resistance for the transition between connection and discontinuity. 
; If the measured resistance is lower than the threshold, the system detects a connection.; If the measured resistance is higher, the system detects a discontinuity.
- `Trise`: `ttime=PARAM_DontChange` — Time interval within which the test voltage must be reached.
- `Twait`: `ttime=PARAM_DontChange` — Time between reaching the test voltage and first measurement of the resistance.
- `Tmeas`: `ttime=PARAM_DontChange` — Duration of the actual measurement within which the threshold must be exceeded.
- `AutoRange`: `boolean=PARAM_DontChange` — If the Autorange option is activated, additional measurements with changing ranges are executed if an error occurs to determine the exact resistance value.; Allowed values: ON, OFF
- `ULimit`: `tvoltage=PARAM_DontChange` — Maximum voltage which is allowed during the test and and in case of an error.

## Example

```ats
ParamContinuity(10mA, 12Ohm, PARAM_DontChange, PARAM_DontChange, 20ms, ON, 10V);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_CCurrent` | `real` | Parameter: Current in Ampere |
| `RES_CThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_CTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_CTwait` | `real` | Parameter: Wait time in seconds |
| `RES_CTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_CAutoRange` | `boolean` | Parameter: Automatic ranging active |
| `RES_CVoltageLimit` | `real` | Parameter: Voltage limit in Volt |
| `RES_CurrentChanged` | `boolean` | TRUE, if current was modified, otherwise FALSE |
| `RES_ThresholdChanged` | `boolean` | TRUE, if threshold was modified, otherwise FALSE |
| `RES_TriseChanged` | `boolean` | TRUE, if maximum rise time was modified, otherwise FALSE |
| `RES_TwaitChanged` | `boolean` | TRUE, if wait time was modified, otherwise FALSE |
| `RES_TmeasChanged` | `boolean` | TRUE, if measurement time was modified, otherwise FALSE |
| `RES_AutoRangeChanged` | `boolean` | TRUE, if automatic ranging was modified, otherwise FALSE |
| `RES_VoltageLimitChanged` | `boolean` | TRUE, if voltage limit was modified, otherwise FALSE |

## See also

`ConnectionTest`, `IsConnected`, `ParamDielectricBreakdown`, `ParamGetContinuity`, `ParamIsolationHV`, `ParamIsolationLV`, `WireTest`
