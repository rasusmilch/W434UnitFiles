# SimpleNoConnPinVsGroupHV

## Declaration

```ats
function SimpleNoConnPinVsGroupHV(Name: string; HighPin: tpin; LowGroupName: string; LowPins: tpinarray): boolean;
```

## Call pattern

```ats
SimpleNoConnPinVsGroupHV('Name', "HighPin", 'LowGroupName', ["Low1", "Low2", ...]);
```

## Description

The function tests the isolation between a single pin and a group of pins.

In case of a fault it will try to identifiy the specific pin of the group.

An adaption rule mus be obeyed if the test system is equipped with DualPoint cards.
Only the pins 1, 4, 5, 7, 10, 11, 14, 15, ... of the DualPoint cards can be used.

Notice: Inapprobriate selection of pins or ignoring the adption rule can lead to faults or even partial destruction of the UUT.

## Metadata

- Category: Electrical testing
- Code: 1294
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `HighPin`: `tpin`
- `LowGroupName`: `string`
- `LowPins`: `tpinarray`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
SimpleNoConnPinVsGroupHV('Name', "HighPin", 'Low Group Name', ["LowPin1", "LowPin2", "LowPin3"]);
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
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_Value` | `real` | Measured value in Ohm |
| `RES_Prefix` | `string` | Prefix of the measured value |
| `RES_IValue` | `real` | Measured current value in Ampere |
| `RES_IPrefix` | `string` | Prefix of the measured current value |
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
| `RES_LowGroup` | `string` | Name of the low group |
| `RES_LowGroupPinCount` | `integer` | Number of pins in the low group |
| `RES_LowGroupPins[ ]` | `integer` | Addresses of the pins in the low group |
| `RES_ErrorPinCount` | `integer` | Number of pins with error |
| `RES_ErrorPins[ ]` | `integer` | Addresses of the pins with error |
| `RES_Arcs[ ]` | `boolean` | Flag whether an arc occured |
| `RES_dIdts[ ]` | `boolean` | Flag whether a dIdt occurred |
| `RES_ELims[]` | `boolean` | Flag whether the energy limit was exceeded |
| `RES_Values[ ]` | `real` | Measured values in Ohm |
| `RES_Prefixes[ ]` | `string` | Prefix for the measured values |
| `RES_IValues[ ]` | `real` | Measured current values in Ampere |
| `RES_IPrefixes[ ]` | `string` | Prefix for the measured current values |
| `RES_OriginalPin` | `integer` | Address of the programmed pin |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`SimpleNoConnPinVsGroupDB`, `NoConnAllHV`, `NoConnGroupHV`, `NoConnectionHV`
