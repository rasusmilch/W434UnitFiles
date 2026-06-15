# NoConnectionHVTwoLevels

## Declaration

```ats
function NoConnectionHVTwoLevels(Name: string; Pin1: tpin; Pin2: tpin): boolean;
```

## Call pattern

```ats
NoConnectionHVTwoLevels('Name', "Pin1", "Pin2");
```

## Description

The function tests whether there is no connection between the two specified pins.

This test is done with high voltage (DC) which is applied in to steps.

The first level can be programmed with the function ParamIsolationHVFirstLevel.
For the second level the values of the project parameters respectively of the function ParamIsolationHV will be used.

If there is no error detected during the first level, the voltage of the second level will be applied without switching the generator off.
If a short is detected during the first level the voltage of the second level won't be applied.
[image: ..\..\images\IsolationHVTwoLevels.bmp]
The values for U1, Trise1, Twait1, Tmeas1 and Ramp1 can be set with ParamIsolationFirstLevel function. 

The values for U2, Trise2, Twait2, Tmeas2 and Ramp2 can be set with ParamIsolationHV.
Ramp3 is always the negative counterpart of Ramp2.

## Metadata

- Category: Electrical testing
- Code: 3584
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
NoConnectionHVTwoLevels('NoConnectionHVTwoLevels1', "Pin1", "Pin2");
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
| `RES_HVFLVoltage` | `real` | First level HV parameter: Voltage in Volt |
| `RES_HVFLThreshold` | `real` | First level HV parameter: Threshold in Ohm |
| `RES_HVFLIThreshold` | `real` | First level HV parameter: Threshold in Ampere |
| `RES_HVFLUseIThreshold` | `boolean` | First level HV parameter: Use current threshold |
| `RES_HVFLTrise` | `real` | First level HV parameter: Maximum rise time in seconds |
| `RES_HVFLTwait` | `real` | First level HV parameter: Wait time in seconds |
| `RES_HVFLTmeas` | `real` | First level HV parameter: Measurement time in seconds |
| `RES_HVFLAutoRange` | `boolean` | First level HV parameter: Automatic ranging |
| `RES_HVFLCurrentLimit` | `real` | First level HV parameter: Maximum current in Ampere |
| `RES_HVFLTmeasReduction` | `boolean` | First level HV parameter: Measurement time reduction (Dwelltime bypass) |
| `RES_HVFLVoltageRamp` | `real` | First level HV parameter: Voltage ramp in Volts per second |
| `RES_HVFLTmeasFactor` | `real` | First level HV parameter: Factor for the measurement time while searching for shorts |
| `RES_HVFLdIdtEnabled` | `boolean` | First level HV parameter: TRUE, if the dIdt detector was enabled, otherwise FALSE |
| `RES_HVFLdIdtCurrentThreshold` | `real` | First level HV parameter: Current threshold for the dIdt detector which must not be exceeded longer than the time threshold. |
| `RES_HVFLdIdtTimeThreshold` | `real` | First level HV parameter: Time threshold for the dIdt detector which must not be exceeded with a current wihich ist greater than the current threshold. |
| `RES_HVVoltage` | `real` | HV Parameter: Voltage in Volt |
| `RES_HVThreshold` | `real` | HV Parameter: Threshold in Ohm |
| `RES_HVIThreshold` | `real` | Parameter: Threshold in Ampere |
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
| `RES_Level2Done` | `boolean` | TRUE, if the second measurement was executed, otherwise FALSE |
| `RES_Level1Error` | `integer` | TRUE, if an error was detected during the first measurement, othewrise FALSE |
| `RES_Level1Arc` | `boolean` | First HV test: Arc occured |
| `RES_Level1dIdt` | `boolean` | First HV test: dIdt occured |
| `RES_Level1ELim` | `boolean` | First HV test: Energy limit exceeded |
| `RES_Level1Value` | `real` | First HV test: Measured value in Ohm |
| `RES_Level1Prefix` | `string` | First HV test: Prefix of the measured value |
| `RES_Level1IValue` | `real` | Measured current value in Ampere |
| `RES_Level1IPrefix` | `string` | Prefix of the measured current value |
| `RES_Level1UValue` | `real` | Measured voltage value in Volt |
| `RES_Level1UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_Level2Arc` | `boolean` | Second HV test: Arc occured |
| `RES_Level2dIdt` | `boolean` | Second HV test: dIdt occured |
| `RES_Level2ELim` | `boolean` | Second HV test: Energy limit exceeded |
| `RES_Level2Value` | `real` | Second HV test: Measured value in Ohm |
| `RES_Level2Prefix` | `string` | Second HV test: Prefix of the measured value |
| `RES_Level2IValue` | `real` | Measured current value in Ampere |
| `RES_Level2IPrefix` | `string` | Prefix of the measured current value |
| `RES_Level2UValue` | `real` | Measured voltage value in Volt |
| `RES_Level2UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`IsolationTestHVTwoLevels`, `NoConnAllHVTwoLevels`, `NoConnectionHV`, `NoConnGroupHVTwoLevels`, `ParamIsolationHV`, `ParamIsolationHVFirstLevel`
