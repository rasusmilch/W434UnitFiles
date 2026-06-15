# NoConnAllDB

## Declaration

```ats
function NoConnAllDB(Name: string; Pin: tpin): boolean;
```

## Call pattern

```ats
NoConnAllDB('Name', "Pin");
```

## Description

Tests with alternating voltage whether Pin is not connected to any other Pin.
The function is not executed if the passed pin belongs to a grounded network.

## Metadata

- Category: Electrical testing
- Code: 1537
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
NoConnAllDB('NoConnAllDB1', "Pin1");
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
| `RES_ErrorPinCount` | `integer` | Number of pins with error |
| `RES_ErrorPins[ ]` | `integer` | Addresses of the pins with error |
| `RES_Arcs[ ]` | `boolean` | Flag whether an arc occured |
| `RES_ValuesValid[ ]` | `boolean` | Flags whether measured values are valid |
| `RES_ValuesIr[ ]` | `real` | Measured real currents in Ampere |
| `RES_PrefixesIr[ ]` | `string` | Prefixes for the real currents |
| `RES_ValuesIi[ ]` | `real` | Measured imaginary currents in Ampere |
| `RES_PrefixesIi[ ]` | `string` | Prefixes for the imaginary currents |
| `RES_OriginalPin` | `integer` | Address of the programmed pin |
| `RES_AutomaticIsolationTest` | `boolean` | TRUE, if the teststep was executed during an automatic isolation test |
| `RES_HighPinCount` | `integer` | Number of pins which are connected to the specified pin |
| `RES_HighPins[ ]` | `integer` | List of the specified pin and all pins which are connected to it |

## See also

`DielectricBreakdownTest`, `NoConnAllHV`, `NoConnAllLV`, `ParamDielectricBreakdown`
