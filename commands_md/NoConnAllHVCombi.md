# NoConnAllHVCombi

## Declaration

```ats
function NoConnAllHVCombi(Name: string; Pin: tpin): boolean;
```

## Call pattern

```ats
NoConnAllHVCombi('Name', "Pin");
```

## Description

Tests with high direct and alternating voltage whether the insulation between Pin and all other pins corresponds to the specified parameters.

The function is not executed if the passed pin belongs to a grounded network.

First a high voltage isolation test is executed.
Afterwards follows the dielectric breakdown test.
The last part is a second HV isolation test whose measured value is compared with the value of the first measurement.
The test step passes if all measured values are below the thresholds and value of the second HV DC measurement is within the specified tolerances of the first measurement.

The function uses the parameters of the HV isolation test and the dielectric breakdown test.

If the second DC measurement shall be compared with the first one it is recommended to disable the parameter "Tmeas reduction".
Note: Instead of the option "Search all pins" of the parameter "Search depth on error" the option "Search first pin" will be executed.

## Metadata

- Category: Electrical testing
- Code: 3329
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
NoConnAllHVCombi('NoConnAllHVCombi1', "Pin1");
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
| `RES_UHV2Tol` | `real` | Parameter: Lower tolerance for the value of the second HV measurement compared to the first. |
| `RES_LHV2Tol` | `real` | Parameter: Upper tolerance for the value of the second HV measurement compare to the first. |
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
| `RES_DBArcs[ ]` | `boolean` | DB error: Flag whether an arc occured |
| `RES_DBValuesValid[ ]` | `boolean` | DB error. Flags whether measured values are valid |
| `RES_DBValuesIr[ ]` | `real` | DB error: Measured real currents in Ampere |
| `RES_DBPrefixesIr[ ]` | `string` | DB error: Prefixes for the real currents |
| `RES_DBValuesIi[ ]` | `real` | DB error: Measured imaginary currents in Ampere |
| `RES_DBPrefixesIi[ ]` | `string` | DB error: Prefixes for the imaginary currents |
| `RES_HighPinCount` | `integer` | Number of pins which are connected to the specified pin |
| `RES_HighPins[ ]` | `integer` | List of the specified pin and all pins which are connected to it |

## See also

`IsolationTestHVCombi`, `NoConnAllDB`, `NoConnAllHV`, `NoConnAllLV`, `NoConnectionHVCombi`, `NoConnGroupHVCombi`, `ParamDielectricBreakdown`, `ParamIsolationHV`, `ParamIsolationHVCombi`
