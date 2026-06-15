# NoConnGroupDB

## Declaration

```ats
function NoConnGroupDB(Name: string; HighGroupName: string; HighGroup: tpinarray; LowGroupName: string; LowGroup: tpinarray): boolean;
```

## Call pattern

```ats
NoConnGroupDB('Name', 'HighGroupName', HighGroup, 'LowGroupName', LowGroup);
```

## Description

Tests with alternating voltage whether the pins in HighGroup are not connected to the pins in LowGroup.

Splices and virtual pins, which are passed within the groups are ignored.

## Metadata

- Category: Electrical testing
- Code: 1543
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
NoConnGroupDB('GroupTest1', 'HighGroupName', ["Pin1", "Pin3"], 'LowGroupName', ["Pin2", "Pin4"]);
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
| `RES_ValueValid` | `boolean` | Flag whether measured values are valid |
| `RES_ValueIr` | `real` | Measured real current in Ampere |
| `RES_PrefixIr` | `string` | Prefix of the measured real current |
| `RES_ValueIi` | `real` | Measured imaginary current in Ampere |
| `RES_PrefixIi` | `string` | Prefix of the measured imaginary current |
| `RES_DBVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_DBThresholdIr` | `real` | Parameter: Threshold for the real current in Ampere |
| `RES_DBThresholdIi` | `real` | Parameter: Threshold for the imaginary current in Ampere |
| `RES_DBTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_DBTwait` | `real` | Parameter: Wait time in seconds |
| `RES_DBTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_DBVoltageRamp` | `real` | Parameter: Voltage ramp in Volts per second |
| `RES_DBTmeasFactor` | `real` | Parameter: Factor for the measurement time while searching for shorts |
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
| `RES_ValuesValid[ ]` | `boolean` | Flags whether the measured values are valid |
| `RES_ValuesIr[ ]` | `real` | Measured real currents in Ampere for detected errors |
| `RES_PrefixesIr[ ]` | `string` | Prefixes for the real currents |
| `RES_ValuesIi[ ]` | `real` | Measured imaginary currents in Ampere |
| `RES_PrefixesIi[ ]` | `string` | Prefixes for the imaginary currents |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`DielectricBreakdownGroupTest`, `NoConnAllDB`, `NoConnectionDB`, `NoConnGroupHV`, `NoConnGroupLV`, `ParamDielectricBreakdown`, `PinCreateList`
