# NoConnection3xHV

## Declaration

```ats
function NoConnection3xHV(Name: string; Pin1: tpin; Pin2: tpin): boolean;
```

## Call pattern

```ats
NoConnection3xHV('Name', "Pin1", "Pin2");
```

## Description

Tests three times with high direct voltage whether the insulation between Pin1 and Pin2 corresponds to the specified parameters.

For the first and third measurement the normal HV parameters are used.
The parameters for the second measurement can be set with ParamIsolation3xHV2ndMeasurement.

The test step passes if all measured values are below the thresholds and the value of the second HV DC measurement is within the specified tolerances of the first measurement.
The tolerances can be set with ParamIsolation3xHV.

If the first measurement shall be compared with the third it is recommended to disable the parameter "Tmeas reduction".

## Metadata

- Category: Electrical testing
- Code: 8192
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
NoConnection3xHV('NoConnection3xHV1', "Pin1", "Pin2");
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
| `RES_LowForce` | `integer` | Low-Force-Pin |
| `RES_LowSense` | `integer` | Low-Sense-Pin |
| `RES_HighForce` | `integer` | High-Force-Pin |
| `RES_HighSense` | `integer` | High-Sense-Pin |
| `RES_OriginalPin1` | `integer` | Address of the first programmed pin |
| `RES_OriginalPin2` | `integer` | Address of the second programmed pin |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_ExtVoltageFound` | `boolean` | External voltage found |
| `RES_ExtVoltagePin1` | `integer` | Pin1 with external voltage |
| `RES_ExtVoltagePin2` | `integer` | Pin2 with external voltage |
| `RES_ExtVoltageValue` | `real` | Value of the external voltage |
| `RES_ExtVoltagePrefix` | `string` | Prefix of the external voltage |
| `RES_HVVoltage` | `real` | HV Parameter: Voltage in Volt |
| `RES_HVThreshold` | `real` | HV Parameter: Threshold in Ohm |
| `RES_HVIThreshold` | `real` | HV Parameter: Threshold in Ampere |
| `RES_HVUseIThreshold` | `boolean` | HV Parameter: Use current threshold |
| `RES_HVTrise` | `real` | HV Parameter: Maximum rise time in seconds |
| `RES_HVTwait` | `real` | HV Parameter: Wait time in seconds |
| `RES_HVTmeas` | `real` | HV Parameter: Measurement time in seconds |
| `RES_HVAutoRange` | `boolean` | HV Parameter: Automatic ranging |
| `RES_HVCurrentLimit` | `real` | HV Parameter: Maximum current in Ampere |
| `RES_HVTmeasReduction` | `boolean` | HV Parameter: Measurement time reduction (Dwelltime bypass) |
| `RES_HVVoltageRamp` | `real` | HV Parameter: Voltage ramp in Volts per second |
| `RES_HVTmeasFactor` | `real` | HV Parameter: Factor for the measurement time while searching for shorts |
| `RES_HVdIdtEnabled` | `boolean` | Parameter: TRUE, if the dIdt detector was enabled, otherwise FALSE |
| `RES_HVdIdtCurrentThreshold` | `real` | Parameter: Current threshold for the dIdt detector which must not be exceeded longer than the time threshold. |
| `RES_HVdIdtTimeThreshold` | `real` | Parameter: Time threshold for the dIdt detector which must not be exceeded with a current which ist greater than the current threshold. |
| `RES_HVDischargeEnergyMonitoringEnabled` | `boolean` | Parameter: Discharge energy monitoring enabled |
| `RES_3xHV2ndM_Voltage` | `real` | HV Parameter: Voltage in Volt |
| `RES_3xHV2ndM_Threshold` | `real` | HV Parameter: Threshold in Ohm |
| `RES_3xHV2ndM_IThreshold` | `real` | HV Parameter: Threshold in Ampere |
| `RES_3xHV2ndM_UseIThreshold` | `boolean` | HV Parameter: Use current threshold |
| `RES_3xHV2ndM_Trise` | `real` | HV Parameter: Maximum rise time in seconds |
| `RES_3xHV2ndM_Twait` | `real` | HV Parameter: Wait time in seconds |
| `RES_3xHV2ndM_Tmeas` | `real` | HV Parameter: Measurement time in seconds |
| `RES_3xHV2ndM_AutoRange` | `boolean` | HV Parameter: Automatic ranging |
| `RES_3xHV2ndM_CurrentLimit` | `real` | HV Parameter: Maximum current in Ampere |
| `RES_3xHV2ndM_TmeasReduction` | `boolean` | HV Parameter: Measurement time reduction (Dwelltime bypass) |
| `RES_3xHV2ndM_VoltageRamp` | `real` | HV Parameter: Voltage ramp in Volts per second |
| `RES_3xHV2ndM_TmeasFactor` | `real` | HV Parameter: Factor for the measurement time while searching for shorts |
| `RES_3xHV2ndM_dIdtEnabled` | `boolean` | Parameter: TRUE, if the dIdt detector was enabled, otherwise FALSE |
| `RES_3xHV2ndM_dIdtCurrentThreshold` | `real` | Parameter: Current threshold for the dIdt detector which must not be exceeded longer than the time threshold. |
| `RES_3xHV2ndM_dIdtTimeThreshold` | `real` | Parameter: Time threshold for the dIdt detector which must not be exceeded with a current which ist greater than the current threshold. |
| `RES_3xHV2ndM_DischargeEnergyMonitoringEnabled` | `boolean` | Parameter: Discharge energy monitoring enabled |
| `RES_3xHV_Delay1` | `real` | Parameter: Delay between the first and the second measurement |
| `RES_3xHV_Delay2` | `real` | Parameter: Delay between the second and the third measurement |
| `RES_3xHV_ExecuteHV3` | `boolean` | Parameter: Flag whether the third measurement shall be executed |
| `RES_3xHV_Lower_1_3_Tol` | `real` | Parameter: Lower tolerance for the value of the third measurement compared to the first. |
| `RES_3xHV_Upper_1_3_Tol` | `real` | Parameter: Upper tolerance for the value of the third measurement compared to the first. |
| `RES_HV2Done` | `boolean` | TRUE if the second measurement was executed |
| `RES_HV3Done` | `boolean` | TRUE if the third measurement was executed |
| `RES_ErrorInfo` | `integer` | Further information if an error occurred |
| `RES_HV1Arc` | `boolean` | First measurement: Arc occurred |
| `RES_HV1dIdt` | `boolean` | First measurement: dIdt occured |
| `RES_HV1ELim` | `boolean` | First measurement: Energy limit exceeded |
| `RES_HV1Value` | `real` | First measurement: Measured value in Ohm |
| `RES_HV1Prefix` | `string` | First measurement: Prefix of the measured value |
| `RES_HV1IValue` | `real` | Measured current value in Ampere |
| `RES_HV1IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV1UValue` | `real` | Measured voltage value in Volt |
| `RES_HV1UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_HV2Arc` | `boolean` | Second measurement: Arc occurred |
| `RES_HV2dIdt` | `boolean` | Second measurement: dIdt occured |
| `RES_HV2ELim` | `boolean` | Second measurement: Energy limit exceeded |
| `RES_HV2Value` | `real` | Second measurement: Measured value in Ohm |
| `RES_HV2Prefix` | `string` | Second measurement: Prefix of the measured value |
| `RES_HV2IValue` | `real` | Measured current value in Ampere |
| `RES_HV2IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV2UValue` | `real` | Measured voltage value in Volt |
| `RES_HV2UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_HV3Arc` | `boolean` | Third measurement: Arc occurred |
| `RES_HV3dIdt` | `boolean` | Third measurement: dIdt occured |
| `RES_HV3ELim` | `boolean` | Third measurement: Energy limit exceeded |
| `RES_HV3Value` | `real` | Third measurement: Measured value in Ohm |
| `RES_HV3Prefix` | `string` | Third measurement: Prefix of the measured value |
| `RES_HV3IValue` | `real` | Measured current value in Ampere |
| `RES_HV3IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV3UValue` | `real` | Measured voltage value in Volt |
| `RES_HV3UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`IsolationTest3xHV`, `NoConnAll3xHV`, `NoConnectionDB`, `NoConnectionHV`, `NoConnectionHVCombi`, `NoConnectionHVTwoLevels`, `NoConnectionLV`, `NoConnGroup3xHV`, `ParamIsolationHV`, `ParamIsolation3xHV`, `ParamIsolation3xHV2ndMeasurement`
