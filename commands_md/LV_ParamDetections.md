# LV_ParamDetections

## Declaration

```ats
function LV_ParamDetections(Current: tcurrent=PARAM_DontChange; Threshold: tresistance=PARAM_DontChange; Twait: ttime=PARAM_DontChange; Tmeas: ttime=PARAM_DontChange; ULimit: tvoltage=PARAM_DontChange): void;
```

## Call pattern

```ats
LV_ParamDetections(<Current>mA, <Threshold>Ohm, <Twait>ms, <Tmeas>ms, <Ulimit>V);
```

## Description

Sets the parameters for the detection test at the LV-Matrix.

Default values
: 100 mA, 100 Ohm, 0 ms, 1 ms, 20 V

## Metadata

- Category: Parameters
- Code: 2315
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Current`: `tcurrent=PARAM_DontChange` — Test current which the test system tries to build up.
- `Threshold`: `tresistance=PARAM_DontChange` — Threshold resistance for the transition between connection and discontinuity. 
; If the measured resistance is lower than the threshold, the system detects a connection.; If the measured resistance is higher, the system detects a discontinuity.
- `Twait`: `ttime=PARAM_DontChange` — Time interval within which the test voltage must be reached.
- `Tmeas`: `ttime=PARAM_DontChange` — Time between reaching the test voltage and first measurement of the resistance.
- `ULimit`: `tvoltage=PARAM_DontChange` — Duration of the actual measurement within which the threshold must be exceeded.

## Example

```ats
LV_ParamDetections(10mA, 120Ohm, PARAM_DontChange, 0.01ms, 15V);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_Name` | `string` | Name |
| `RES_Result` | `integer` | Result |
| `RES_ManualTest` | `boolean` | Manual test |
| `RES_TwaitChanged` | `boolean` | TRUE, if wait time was modified, otherwise FALSE |
| `RES_TmeasChanged` | `boolean` | TRUE, if measurement time was modified, otherwise FALSE |
| `RES_CurrentChanged` | `boolean` | TRUE, if current was modified, otherwise FALSE |
| `RES_ThresholdChanged` | `boolean` | TRUE, if threshold was modified, otherwise FALSE |
| `RES_VoltageLimitChanged` | `boolean` | TRUE, if voltage limit was modified, otherwise FALSE |
| `RES_LV_D_Twait` | `real` | Parameter: Wait time |
| `RES_LV_D_Tmeas` | `real` | Parameter: Measurement time |
| `RES_LV_D_Threshold` | `real` | Parameter: Resistance threshold |
| `RES_LV_D_Current` | `real` | Parameter: Current |
| `RES_LV_D_VoltageLimit` | `real` | Parameter: Voltage limit |

## See also

`LV_ParamConnectorDetections`, `LV_DetectionTest`
