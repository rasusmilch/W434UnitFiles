# NoConnectionHVCombi

## Declaration

```ats
function NoConnectionHVCombi(Name: string; Pin1: tpin; Pin2: tpin): boolean;
```

## Call pattern

```ats
NoConnectionHVCombi('Name', "Pin1", "Pin2");
```

## Description

Tests with high direct and alternating voltage whether the insulation between Pin1 and Pin2 corresponds to the specified parameters.

First a high voltage isolation test is executed.
Afterwards follows the dielectric breakdown test.
The last part is a second HV isolation test whose measured value is compared with the value of the first measurement.
The test step passes if all measured values are below the thresholds and the value of the second HV DC measurement is within the specified tolerances of the first measurement.

The function uses the parameters of the HV isolation test and the dielectric breakdown test.

If the second DC measurement shall be compared with the first one it is recommended to disable the parameter "Tmeas reduction".



## Metadata

- Category: Electrical testing
- Code: 3328
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
NoConnectionHVCombi('NoConnectionHVCombi1', "Pin1", "Pin2");
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
| `RES_HVDischargeEnergyMonitoringEnabled` | `boolean` | Discharge energy monitoring enabled |
| `RES_DBVoltage` | `real` | DB Parameter: Voltage in Volt |
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
| `RES_UHV2Tol` | `real` | Parameter: Lower tolerance for the value of the second HV measurment compare to the first. |
| `RES_LHV2Tol` | `real` | Parameter: Upper tolerance for the value of the second HV measurment compare to the first. |
| `RES_DBDone` | `boolean` | TRUE if the DB measurement was executed |
| `RES_HV2Done` | `boolean` | TRUE if the second HV measurement was executed |
| `RES_ErrorInfo` | `integer` | Further information if an error occurred |
| `RES_HV1Arc` | `boolean` | First HV test: Arc occured |
| `RES_HV1dIdt` | `boolean` | First HV test: dIdt occured |
| `RES_HV1ELim` | `boolean` | First HV test: Energy limit exceeded |
| `RES_HV1Value` | `real` | First HV test: Measured value in Ohm |
| `RES_HV1Prefix` | `string` | First HV test: Prefix of the measured value |
| `RES_HV1IValue` | `real` | Measured current value in Ampere |
| `RES_HV1IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV1UValue` | `real` | Measured voltage value in Volt |
| `RES_HV1UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_HV2Arc` | `boolean` | Second HV test: Arc occured |
| `RES_HV2dIdt` | `boolean` | Second HV test: dIdt occured |
| `RES_HV2ELim` | `boolean` | Second HV test: Energy limit exceeded |
| `RES_HV2Value` | `real` | Second HV test: Measured value in Ohm |
| `RES_HV2Prefix` | `string` | Second HV test: Prefix of the measured value |
| `RES_HV2IValue` | `real` | Measured current value in Ampere |
| `RES_HV2IPrefix` | `string` | Prefix of the measured current value |
| `RES_HV2UValue` | `real` | Measured voltage value in Volt |
| `RES_HV2UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_DBArc` | `boolean` | DB test: Arc occured |
| `RES_DBValueValid` | `boolean` | DB test: Flag whether measured values are valid |
| `RES_DBValueIr` | `real` | DB test: Measured real current in Ampere |
| `RES_DBPrefixIr` | `string` | DB test: Prefix of the measured real current |
| `RES_DBValueIi` | `real` | DB test: Measured imaginary current in Ampere |
| `RES_DBPrefixIi` | `string` | DB test: Prefix of the measured imaginary current |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`IsolationTestHVCombi`, `NoConnAllHVCombi`, `NoConnectionDB`, `NoConnectionHV`, `NoConnectionLV`, `NoConnGroupHVCombi`, `ParamDielectricBreakdown`, `ParamIsolationHV`, `ParamIsolationHVCombi`
