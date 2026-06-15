# NoConnGroup3xHV

## Declaration

```ats
function NoConnGroup3xHV(Name: string; HighGroupName: string; HighGroup: tpinarray; LowGroupName: string; LowGroup: tpinarray): boolean;
```

## Call pattern

```ats
NoConnGroup3xHV('Name', 'HighGroupName', HighGroup, 'LowGroupName', LowGroup);
```

## Description

Tests three times with high direct voltage whether the insulation between HighGroup and LowGroup corresponds to the specified parameters.

For the first and third measurement the normal HV parameters are used.
The parameters for the second measurement can be set with ParamIsolation3xHV2ndMeasurement.

The test step passes if all measured values are below the thresholds and the value of the second HV DC measurement is within the specified tolerances of the first measurement.
The tolerances can be set with ParamIsolation3xHV.

If the first measurement shall be compared with the third it is recommended to disable the parameter "Tmeas reduction".

Note: Instead of the option "Search all pins" of the parameter "Search depth on error" the option "Search first pin" will be executed.

## Metadata

- Category: Electrical testing
- Code: 8198
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `HighGroupName`: `string`
- `HighGroup`: `tpinarray`
- `LowGroupName`: `string`
- `LowGroup`: `tpinarray`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
NoConnGroup3xHV('GroupTest1', 'HighGroupName', ["Pin1", "Pin3"], 'LowGroupName', ["Pin2", "Pin4"]);
```

## Example notes

Tests whether Pin1 and Pin3 are not connected to Pin2 and Pin4.

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
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_HighGroup` | `string` | Name of the high group |
| `RES_LowGroup` | `string` | Name of the low group |
| `RES_HighGroupPinCount` | `integer` | Number of pins in the high group |
| `RES_LowGroupPinCount` | `integer` | Number of pins in the low group |
| `RES_HighGroupPins[ ]` | `integer` | Addresses of the pins in the high group |
| `RES_LowGroupPins[ ]` | `integer` | Addresses of the pins in the low group |
| `RES_ErrorCount` | `integer` | Number of detected errors |
| `RES_ErrorHighPins[ ]` | `integer` | Addresses of the high pins with errors |
| `RES_ErrorLowPins[ ]` | `integer` | Addresses of the low pins with errors |
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
| `RES_HVArcs[ ]` | `boolean` | HV error: Flag for detected errros whether an arc occured |
| `RES_HVdIdts[ ]` | `boolean` | HV error: Flag for detected errros whether an dIdt occurred |
| `RES_HVELims[]` | `boolean` | Flag whether the energy limit was exceeded |
| `RES_HVValues[ ]` | `real` | HV error: Measured values in Ohm |
| `RES_HVPrefixes[ ]` | `string` | HV error: Prefix for the measured values |
| `RES_HVIValues[ ]` | `real` | Measured current values in Ampere |
| `RES_HVIPrefixes[ ]` | `string` | Prefix for the measured current values |
| `RES_HVUValues[ ]` | `real` | Measured voltage values in Volt |
| `RES_HVUPrefixes[ ]` | `string` | Prefix of the measured voltage values |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`IsolationTest3xHV`, `NoConnAll3xHV`, `NoConnection3xHV`, `NoConnGroupDB`, `NoConnGroupHV`, `NoConnGrooupLV`, `ParamIsolationHV`, `ParamIsolation3xHV`, `ParamIsolation3xHV2ndMeasurement`, `PinCreateList`
