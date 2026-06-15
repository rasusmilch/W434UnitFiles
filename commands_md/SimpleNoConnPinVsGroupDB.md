# SimpleNoConnPinVsGroupDB

## Declaration

```ats
function SimpleNoConnPinVsGroupDB(Name: string; HighPin: tpin; LowGroupName: string; LowPins: tpinarray): boolean;
```

## Call pattern

```ats
SimpleNoConnPinVsGroupDB('Name', "HighPin", 'LowGroupName', ["Low1", "Low2", ...]);
```

## Description

The function tests the dielectric strength between a single pin and a group of pins.

In case of a fault it will try to identifiy the specific pin of the group.

An adaption rule mus be obeyed if the test system is equipped with DualPoint cards.
Only the pins 1, 4, 5, 7, 10, 11, 14, 15, ... of the DualPoint cards can be used.

Notice: Inapprobriate selection of pins or ignoring the adption rule can lead to faults or even partial destruction of the UUT.

## Metadata

- Category: Electrical testing
- Code: 1550
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
SimpleNoConnPinVsGroupDB('Name', "HighPin", 'Low Group Name', ["LowPin1", "LowPin2", "LowPin3"]);
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
| `RES_LowGroup` | `string` | Name of the low group |
| `RES_LowGroupPinCount` | `integer` | Number of pins in the low group |
| `RES_LowGroupPins[ ]` | `integer` | Addresses of the pins in the low group |
| `RES_ErrorPinCount` | `integer` | Number of pins with error |
| `RES_ErrorPins[ ]` | `integer` | Addresses of the pins with error |
| `RES_Arcs[ ]` | `boolean` | Flag whether an arc occured |
| `RES_OriginalPin` | `integer` | Address of the programmed pin |
| `RES_ValuesValid[ ]` | `boolean` | Flags whether the measured values are valid |
| `RES_ValuesIr[ ]` | `real` | Measured real currents in Ampere for detected errors |
| `RES_PrefixesIr[ ]` | `string` | Prefixes for the real currents |
| `RES_ValuesIi[ ]` | `real` | Measured imaginary currents in Ampere |
| `RES_PrefixesIi[ ]` | `string` | Prefixes for the imaginary currents |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`SimpleNoConnPinVsGroupHV`, `NoConnAllDB`, `NoConnGroupDB`, `NoConnectionDB`
