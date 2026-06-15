# NoConnAllHVTwoLevels

## Declaration

```ats
function NoConnAllHVTwoLevels(Name: string; Pin: tpin): boolean;
```

## Call pattern

```ats
NoConnAllHVTwoLevels('Name', "Pin");
```

## Description

The function tests whether the specified pin is not connected to any pin to which it mustn't be connected.

This test is done with high voltage (DC) which is applied in two steps.

The first level can be programmed with the function ParamIsolationHVFirstLevel.
For the second level the values of the project parameters respectively of the function ParamIsolationHV will be used.

If there is no error detected during the first level, the voltage of the second level will be applied without switching the generator off.
If a short is detected during the first level the voltage of the second level won't be applied.
Note: Instead of the option "Search all pins" of the parameter "Search depth on error" the option "Search first pin" will be executed.
[image: ..\..\images\IsolationHVTwoLevels.bmp]
The values for U1, Trise1, Twait1, Tmeas1 and Ramp1 can be set with ParamIsolationFirstLevel function. 

The values for U2, Trise2, Twait2, Tmeas2 and Ramp2 can be set with ParamIsolationHV.
Ramp3 is always the negative counterpart of Ramp2.

## Metadata

- Category: Electrical testing
- Code: 3585
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
NoConnAllHVTwoLevels('NoConnAllHVCombi1', "Pin1");
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
| `RES_Level1Value` | `real` | First HV test: Measured value in Ohm |
| `RES_Level1Prefix` | `string` | First HV test: Prefix of the measured value |
| `RES_Level1IValue` | `real` | Measured current value in Ampere |
| `RES_Level1IPrefix` | `string` | Prefix of the measured current value |
| `RES_Level1UValue` | `real` | Measured voltage value in Volt |
| `RES_Level1UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_Level2Value` | `real` | Zweiter HV test: Measured value in Ohm |
| `RES_Level2Prefix` | `string` | Zweiter HV test: Prefix of the measured value |
| `RES_Level2IValue` | `real` | Measured current value in Ampere |
| `RES_Level2IPrefix` | `string` | Prefix of the measured current value |
| `RES_Level2UValue` | `real` | Measured voltage value in Volt |
| `RES_Level2UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_ErrorPinCount` | `integer` | Number of pins with error |
| `RES_ErrorPins[ ]` | `integer` | Addresses of the pins with error |
| `RES_Level1Errors[ ]` | `real` | TRUE, if the error occurred in level 1, otherwise FALSE |
| `RES_Arcs[ ]` | `boolean` | TRUE, if the error is an arc, otherwise FALSE |
| `RES_dIdts[ ]` | `boolean` | TRUE, if it is a dIdt error, otherwise FALSE |
| `RES_ELims[]` | `boolean` | Flag whether the energy limit was exceeded |
| `RES_Values[ ]` | `real` | Measured values in Ohm |
| `RES_Prefixes[ ]` | `string` | Prefix for the measured values |
| `RES_IValues[ ]` | `real` | Measured current values in Ampere |
| `RES_IPrefixes[ ]` | `string` | Prefix for the measured current values |
| `RES_UValues[ ]` | `real` | Measured voltage values in Volt |
| `RES_UPrefixes[ ]` | `string` | Prefix of the measured voltage values |
| `RES_HighPinCount` | `integer` | Number of pins which are connected to the specified pin |
| `RES_HighPins[ ]` | `integer` | List of the specified pin and all pins which are connected to it |

## See also

`IsolationTestHVTwoLevels`, `NoConnAllHV`, `NoConnectionHVTwoLevels`, `NoConnGroupHVTwoLevels`, `ParamIsolationHV`, `ParamIsolationHVFirstLevel`
