# LV_ParamConnectorDetections

## Declaration

```ats
function LV_ParamConnectorDetections(LowerVoltageThreshold: tvoltage=PARAM_DontChange; UpperVoltageThreshold: tvoltage=PARAM_DontChange; Twait: ttime=PARAM_DontChange; Tmeas: ttime=PARAM_DontChange; UseCurrentThreshold: boolean=PARAM_DontChange; LowerCurrentThreshold: tcurrent=PARAM_DontChange; UpperCurrentThreshold: tcurrent=PARAM_DontChange): void;
```

## Call pattern

```ats
LV_ParamConnectorDetections(<LowerVoltageThreshold>V, <UpperVoltageThreshold>V, <Twait>ms, <Tmeas>ms, ON|OFF, <LowerCurrentThreshold>mA, <UpperCurrentThreshold>mA);
```

## Description

Sets the parameters for the connector detection test at the LV-Matrix.

Default values
: -500 mV, 5V, 0 ms 1ms, OFF, -5 mA, 5mA

## Metadata

- Category: Parameters
- Code: 2316
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `LowerVoltageThreshold`: `tvoltage=PARAM_DontChange` — Test current which the test system tries to build up.
- `UpperVoltageThreshold`: `tvoltage=PARAM_DontChange` — Threshold resistance for the transition between connection and discontinuity. 
; If the measured resistance is lower than the threshold, the system detects a connection.; If the measured resistance is higher, the system detects a discontinuity.
- `Twait`: `ttime=PARAM_DontChange` — Time interval within which the test voltage must be reached.
- `Tmeas`: `ttime=PARAM_DontChange` — Time between reaching the test voltage and first measurement of the resistance.
- `UseCurrentThreshold`: `boolean=PARAM_DontChange` — Duration of the actual measurement within which the threshold must be exceeded.
- `LowerCurrentThreshold`: `tcurrent=PARAM_DontChange` — If the Autorange option is activated, additional measurements with changing ranges are executed if an error occurs to determine the exact resistance value.; Allowed values: ON, OFF
- `UpperCurrentThreshold`: `tcurrent=PARAM_DontChange` — Maximum voltage which is allowed during the test and and in case of an error.

## Example

```ats
LV_ParamConnectorDetections(-0.5V, 5V, PARAM_DontChange, 0.01ms, OFF);
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
| `RES_U_LowerThresholdChanged` | `boolean` | TRUE, if lower voltage threshold was modified, otherwise FALSE |
| `RES_U_UpperThresholdChanged` | `boolean` | TRUE, if upper voltage threshold was modified, otherwise FALSE |
| `RES_I_ThresholdEnabledChanged` | `boolean` | TRUE, if "Current thresholds enabled" was modified, otherwise FALSE |
| `RES_I_LowerThresholdChanged` | `boolean` | TRUE, if lower current threshold was modified, otherwise FALSE |
| `RES_I_UpperThresholdChanged` | `boolean` | TRUE, if upper current threshold was modified, otherwise FALSE |
| `RES_LV_CD_Twait` | `real` | Parameter: Wait time |
| `RES_LV_CD_Tmeas` | `real` | Parameter: Measurement time |
| `RES_LV_CD_ILowerThreshold` | `real` | Parameter: Lower current threshold |
| `RES_LV_CD_IUpperThreshold` | `real` | Parameter: Upper current threshold |
| `RES_LV_CD_ULowerThreshold` | `real` | Parameter: Lower voltage threshold |
| `RES_LV_CD_UUpperThreshold` | `real` | Parameter: Upper voltage threshold |
| `RES_LV_CD_IThresholdEnabled` | `boolean` | Parameter: Current thresholds enabled |

## See also

`LV_ParamDetections`, `LV_ConnectorDetectionTest`
