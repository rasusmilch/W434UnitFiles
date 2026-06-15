# NoConnLowerHV

## Declaration

```ats
function NoConnLowerHV(Name: string; Pin: tpin): boolean;
```

## Call pattern

```ats
NoConnLowerHV('Name', "Pin");
```

## Description

Tests with high voltage whether Pin is not connected to any other pin with a lower address

## Metadata

- Category: Electrical testing
- Code: 1282
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin`: `tpin`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

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
| `RES_Value` | `real` | Measured value in Ohm |
| `RES_Prefix` | `string` | Prefix of the measured value |
| `RES_IValue` | `real` | Measured current value in Ampere |
| `RES_IPrefix` | `string` | Prefix of the measured current value |
| `RES_UValue` | `real` | Measured voltage value in Volt |
| `RES_UPrefix` | `string` | Prefix of the measured voltage value |
| `RES_HVVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_HVThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_HVIThreshold` | `real` | Parameter: Threshold in Ampere |
| `RES_HVUseIThreshold` | `boolean` | Parameter: Use current threshold |
| `RES_HVTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_HVTwait` | `real` | Parameter: Wait time in seconds |
| `RES_HVTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_HVAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_HVCurrentLimit` | `real` | Parameter: Maximum current in Ampere |
| `RES_HVTmeasReduction` | `boolean` | Parameter: Measurement time reduction (Dwelltime bypass) |
| `RES_HVVoltageRamp` | `real` | Parameter: Voltage ramp in Volts per second |
| `RES_HVTmeasFactor` | `real` | Parameter: Factor for the measurement time while searching for shorts |
| `RES_HVdIdtEnabled` | `boolean` | TRUE, if the dIdt detector was enabled, otherwise FALSE |
| `RES_HVdIdtCurrentThreshold` | `real` | Current threshold for the dIdt detector which must not be exceeded longer than the time threshold. |
| `RES_HVdIdtTimeThreshold` | `real` | Time threshold for the dIdt detector which must not be exceeded with a current wihich ist greater than the current threshold. |
| `RES_HVDischargeEnergyMonitoringEnabled` | `boolean` | Discharge energy monitoring enabled |
| `RES_ErrorPinCount` | `integer` | Number of pins with error |
| `RES_ErrorPins[ ]` | `integer` | Addresses of the pins with error |
| `RES_Arcs[ ]` | `boolean` | Flag whether an arc occured |
| `RES_dIdts[ ]` | `boolean` | Flag whether a dIdt occurred |
| `RES_ELims[]` | `boolean` | Flag whether the energy limit was exceeded |
| `RES_Values[ ]` | `real` | Measured values in Ohm |
| `RES_Prefixes[ ]` | `string` | Prefix for the measured values |
| `RES_IValues[ ]` | `real` | Measured current values in Ampere |
| `RES_IPrefixes[ ]` | `string` | Prefix for the measured current values |
| `RES_UValues[ ]` | `real` | Measured voltage values in Volt |
| `RES_UPrefixes[ ]` | `string` | Prefix of the measured voltage values |
| `RES_OriginalPin` | `integer` | Address of the programmed pin |
| `RES_AutomaticIsolationTest` | `boolean` | TRUE, if the teststep was executed during an automatic isolation test |
| `RES_HighPinCount` | `integer` | Number of pins which are connected to the specified pin |
| `RES_HighPins[ ]` | `integer` | List of the specified pin and all pins which are connected to it |

## See also

`IsolationTestHV`, `NoConnAllHV`, `NoConnLowerDB`, `NoConnLowerLV`
