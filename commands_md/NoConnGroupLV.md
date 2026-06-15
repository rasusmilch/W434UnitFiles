# NoConnGroupLV

## Declaration

```ats
function NoConnGroupLV(Name: string; HighGroupName: string; HighGroup: tpinarray; LowGroupName: string; LowGroup: tpinarray): boolean;
```

## Call pattern

```ats
NoConnGroupLV('Name', 'HighGroupName', HighGroup, 'LowGroupName', LowGroup);
```

## Description

Tests with low voltage whether the pins in HighGroup are not connected to the pins in LowGroup.

Splices and virtual pins, which are passed within the groups are ignored.

## Metadata

- Category: Electrical testing
- Code: 1032
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
NoConnGroupLV('GroupTest1', 'HighGroupName', ["Pin1", "Pin3"], 'LowGroupName', ["Pin2", "Pin4"]);
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
| `RES_LVVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_LVThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_LVTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_LVTwait` | `real` | Parameter: Wait time in seconds |
| `RES_LVTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_LVAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_LVCurrentLimit` | `real` | Parameter: Maximum current in Ampere |
| `RES_LVTmeasReduction` | `boolean` | Parameter: Measurement time reduction (Dwelltime bypass) |
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
| `RES_Values[ ]` | `real` | Measured values in Ohm |
| `RES_Prefixes[ ]` | `string` | Prefix of the measured values |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`NoConnAllLV`, `NoConnectionLV`, `NoConnGroupDB`, `NoConnGroupHV`, `ParamIsolationLV`, `PinCreateList`
