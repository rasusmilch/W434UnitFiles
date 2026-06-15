# NoConnAll3xHV

## Declaration

```ats
function NoConnAll3xHV(Name: string; Pin: tpin): boolean;
```

## Call pattern

```ats
NoConnAll3xHV('Name', "Pin");
```

## Description

Tests three times with high direct voltage whether the insulation between Pin and all other pins corresponds to the specified parameters.

For the first and third measurement the normal HV parameters are used.
The parameters for the second measurement can be set with ParamIsolation3xHV2ndMeasurement.

The test step passes if all measured values are below the thresholds and the value of the second HV DC measurement is within the specified tolerances of the first measurement.
The tolerances can be set with ParamIsolation3xHV.

If the first measurement shall be compared with the third it is recommended to disable the parameter "Tmeas reduction".

Note: Instead of the option "Search all pins" of the parameter "Search depth on error" the option "Search first pin" will be executed.

## Metadata

- Category: Electrical testing
- Code: 8193
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin`: `tpin`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
NoConnAll3xHV('NoConnAll3xHV1', "Pin1");
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
| `RES_Pin` | `integer` | High pin |
| `RES_OriginalPin` | `integer` | Address of the programmed pin |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_AutomaticIsolationTest` | `boolean` | TRUE, if the teststep was executed during an automatic isolation test |
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
| `RES_HV1Value` | `real` | First measurement: Measured value in Ohm (in case of pass or if a HV1/HV3 error occurred) |
| `RES_HV1Prefix` | `string` | First measurement: Prefix of the measured value (in case of pass or if a HV1/HV3 error occurred) |
| `RES_HV1IValue` | `real` | Measured current value in Ampere |
| `RES_HV1IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV1UValue` | `real` | Measured voltage value in Volt |
| `RES_HV1UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_HV2Value` | `real` | Second measurement: Measured value in Ohm (in case of pass or if a HV1/HV3 error occurred) |
| `RES_HV2Prefix` | `string` | Second measurement: Prefix of the measured value (in case of pass or if a HV1/HV3 error occurred) |
| `RES_HV2IValue` | `real` | Measured current value in Ampere |
| `RES_HV2IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV2UValue` | `real` | Measured voltage value in Volt |
| `RES_HV2UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_HV3Value` | `real` | Third measurement: Measured value in Ohm (in case of pass or if a HV1/HV3 error occurred) |
| `RES_HV3Prefix` | `string` | Third measurement: Prefix of the measured value (in case of pass or if a HV1/HV3 error occurred) |
| `RES_HV3IValue` | `real` | Measured current value in Ampere |
| `RES_HV3IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV3UValue` | `real` | Measured voltage value in Volt |
| `RES_HV3UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_ErrorPinCount` | `integer` | Number of pins with error |
| `RES_ErrorPins[ ]` | `integer` | Addresses of the pins with error |
| `RES_HVArcs[ ]` | `boolean` | HV error: Flag whether an arc occured |
| `RES_HVdIdts[ ]` | `boolean` | HV error: Flag for detected errros whether an dIdt occurred |
| `RES_HVELims[]` | `boolean` | Flag whether the energy limit was exceeded |
| `RES_HVValues[ ]` | `real` | HV error: Measured values in Ohm |
| `RES_HVPrefixes[ ]` | `string` | HV error: Prefix for the measured values |
| `RES_HVIValues[ ]` | `real` | Measured current values in Ampere |
| `RES_HVIPrefixes[ ]` | `string` | Prefix for the measured current values |
| `RES_HVUValues[ ]` | `real` | Measured voltage values in Volt |
| `RES_HVUPrefixes[ ]` | `string` | Prefix of the measured voltage values |
| `RES_HighPinCount` | `integer` | Number of pins which are connected to the specified pin |
| `RES_HighPins[ ]` | `integer` | List of the specified pin and all pins which are connected to it |

## See also

`IsolationTest3xHV`, `NoConnAllDB`, `NoConnAllHV`, `NoConnAllLV`, `NoConnAllHVCombi`, `NoConnAllHVTwoLevels`, `NoConnection3xHV`, `NoConnGroup3xHV`, `ParamIsolationHV`, `ParamIsolation3xHV`, `ParamIsolation3xHV2ndMeasurement`
