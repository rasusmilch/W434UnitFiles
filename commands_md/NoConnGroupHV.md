# NoConnGroupHV

## Declaration

```ats
function NoConnGroupHV(Name: string; HighGroupName: string; HighGroup: tpinarray; LowGroupName: string; LowGroup: tpinarray): boolean;
```

## Call pattern

```ats
NoConnGroupHV('Name', 'HighGroupName', HighGroup, 'LowGroupName', LowGroup);
```

## Description

Tests with high voltage whether the pins in HighGroup are not connected to the pins in LowGroup.

Splices and virtual pins, which are passed within the groups are ignored.

## Metadata

- Category: Electrical testing
- Code: 1287
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
NoConnGroupHV('GroupTest1', 'HighGroupName', ["Pin1", "Pin3"], 'LowGroupName', ["Pin2", "Pin4"]);
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
| `RES_HighGroup` | `string` | Name of the high group |
| `RES_LowGroup` | `string` | Name of the low group |
| `RES_HighGroupPinCount` | `integer` | Number of pins in the high group |
| `RES_LowGroupPinCount` | `integer` | Number of pins in the low group |
| `RES_HighGroupPins[ ]` | `integer` | Addresses of the pins in the high group |
| `RES_LowGroupPins[ ]` | `integer` | Addresses of the pins in the low group |
| `RES_ErrorCount` | `integer` | Number of detected errors |
| `RES_ErrorHighPins[ ]` | `integer` | Addresses of the high pins with errors |
| `RES_ErrorLowPins[ ]` | `integer` | Addresses of the low pins with errors |
| `RES_Arcs[ ]` | `boolean` | Flags whether an arc occured |
| `RES_dIdts[ ]` | `boolean` | Flag whether a dIdt occurred |
| `RES_ELims[]` | `boolean` | Flag whether the energy limit was exceeded |
| `RES_Values[ ]` | `real` | Measured values in Ohm |
| `RES_Prefixes[ ]` | `string` | Prefix of the measured values |
| `RES_IValues[ ]` | `real` | Measured current values in Ampere |
| `RES_IPrefixes[ ]` | `string` | Prefix for the measured current values |
| `RES_UValues[ ]` | `real` | Measured voltage values in Volt |
| `RES_UPrefixes[ ]` | `string` | Prefix of the measured voltage values |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`IsolationGroupTestHV`, `NoConnAllHV`, `NoConnectionHV`, `NoConnGroupDB`, `NoConnGroupLV`, `ParamIsolationHV`, `PinCreateList`
