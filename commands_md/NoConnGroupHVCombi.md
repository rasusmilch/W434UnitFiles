# NoConnGroupHVCombi

## Declaration

```ats
function NoConnGroupHVCombi(Name: string; HighGroupName: string; HighGroup: tpinarray; LowGroupName: string; LowGroup: tpinarray): boolean;
```

## Call pattern

```ats
NoConnGroupHVCombi('Name', 'HighGroupName', HighGroup, 'LowGroupName', LowGroup);
```

## Description

Tests with high direct and alternating voltage whether the insulation between HighGroup and LowGroup corresponds to the specified parameters.

First a high voltage isolation test is executed.
Afterwards follows the dielectric breakdown test.
The last part is a second HV isolation test whose measured value is compared with the value of the first measurement.
The test step passes if all measured values are below the thresholds and value of the second HV DC measurement is within the specified tolerances of the first measurement.

Splices and virtual pins, which are passed within the groups are ignored.

The function uses the parameters of the HV isolation test and the dielectric breakdown test.

If the second DC measurement shall be compared with the first one it is recommended to disable the parameter "Tmeas reduction".
Note: Instead of the option "Search all pins" of the parameter "Search depth on error" the option "Search first pin" will be executed.

## Metadata

- Category: Electrical testing
- Code: 3335
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
NoConnGroupHVCombi('GroupTest1', 'HighGroupName', ["Pin1", "Pin3"], 'LowGroupName', ["Pin2", "Pin4"]);
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
| `RES_HVDischargeEnergyMonitoringEnabled` | `boolean` | Discharge energy monitoring enabledRES_DBVoltage;real;202160#DB Parameter: Voltage in Volt |
| `RES_DBThresholdIr` | `real` | DB Parameter: Threshold for the real current in Ampere |
| `RES_DBThresholdIi` | `real` | DB Parameter: Threshold for the imaginary current in Ampere |
| `RES_DBTrise` | `real` | DB Parameter: Maximum rise time in seconds |
| `RES_DBTwait` | `real` | DB Parameter: Wait time in seconds |
| `RES_DBTmeas` | `real` | DB Parameter: Measurement time in seconds |
| `RES_DBVoltageRamp` | `real` | DB Parameter: Voltage ramp in Volts per second |
| `RES_DBTmeasFactor` | `real` | DB Parameter: Factor for the measurement time while searching for shorts |
| `RES_Delay1` | `real` | Parameter: Time between first HV measurement and DB measurement |
| `RES_Delay2` | `real` | Parameter: Time between DB measurement and second HV measurement |
| `RES_ExecuteHV2` | `boolean` | Parameter: The second HV measurement will be done if this value is TRUE |
| `RES_UHVDiffTol` | `real` | Parameter: Lower tolerance for difference between first and second HV measurement |
| `RES_LHVDiffTol` | `real` | Parameter: Upper tolerance for difference between first and second HV measurement |
| `RES_DBDone` | `boolean` | TRUE if the DB measurement was executed |
| `RES_HV2Done` | `boolean` | TRUE if the second HV measurement was executed |
| `RES_ErrorInfo` | `integer` | Further information if an error occurred |
| `RES_HV1Value` | `real` | First HV test: Measured value in Ohm (in case of pass or if a HV1/HV2 error occured) |
| `RES_HV1Prefix` | `string` | First HV test: Prefix of the measured value (in case of pass or if a HV1/HV2 error occured) |
| `RES_HV1IValue` | `real` | Measured current value in Ampere |
| `RES_HV1IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV1UValue` | `real` | Measured voltage value in Volt |
| `RES_HV1UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_HV2Value` | `real` | Second HV test: Measured value in Ohm (in case of pass or if a HV1/HV2 error occured) |
| `RES_HV2Prefix` | `string` | Second HV test: Prefix of the measured value (in case of pass or if a HV1/HV2 error occured) |
| `RES_HV2IValue` | `real` | Measured current value in Ampere |
| `RES_HV2IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV2UValue` | `real` | Measured voltage value in Volt |
| `RES_HV2UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_DBValueValid` | `boolean` | DB test: Flag whether measured values are valid (in case of pass or if a HV1/HV2 error occured) |
| `RES_DBValueIr` | `real` | DB test: Measured real current in Ampere (in case of pass or if a HV1/HV2 error occured) |
| `RES_DBPrefixIr` | `string` | DB test: Prefix of the measured real current (in case of pass or if a HV1/HV2 error occured) |
| `RES_DBValueIi` | `real` | DB test: Measured imaginary current in Ampere (in case of pass or if a HV1/HV2 error occured) |
| `RES_DBPrefixIi` | `string` | DB test: Prefix of the measured imaginary current (in case of pass or if a HV1/HV2 error occured) |
| `RES_HVArcs[ ]` | `boolean` | HV error: Flag for detected errros whether an arc occured |
| `RES_HVdIdts[ ]` | `boolean` | HV error: Flag for detected errros whether an dIdt occurred |
| `RES_HVELims[]` | `boolean` | Flag whether the energy limit was exceeded |
| `RES_HVValues[ ]` | `real` | HV error: Measured values in Ohm |
| `RES_HVPrefixes[ ]` | `string` | HV error: Prefix for the measured values |
| `RES_HVIValues[ ]` | `real` | Measured current values in Ampere |
| `RES_HVIPrefixes[ ]` | `string` | Prefix for the measured current values |
| `RES_HVUValues[ ]` | `real` | Measured voltage values in Volt |
| `RES_HVUPrefixes[ ]` | `string` | Prefix of the measured voltage values |
| `RES_DBArcs[ ]` | `boolean` | DB error: Flag for detected errros whether an arc occured |
| `RES_DBValuesValid[ ]` | `boolean` | DB error. Flags for detected errors whether measured values are valid |
| `RES_DBValuesIr[ ]` | `real` | DB error: Measured real currents in Ampere |
| `RES_DBPrefixesIr[ ]` | `string` | DB error: Prefixes of the real currents for detected errors |
| `RES_DBValuesIi[ ]` | `real` | DB error: Measured imaginary currents in Ampere |
| `RES_DBPrefixesIi[ ]` | `string` | DB error: Prefixes of the imaginary currents for detected errors |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`IsolationTestHVCombi`, `NoConnAllHVCombi`, `NoConnectionHVCombi`, `NoConnGroupDB`, `NoConnGroupHV`, `ParamDielectricBreakdown`, `ParamIsolationHV`, `ParamIsolationHVCombi`, `PinCreateList`
