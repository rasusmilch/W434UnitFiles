# NoConnAllLV

## Declaration

```ats
function NoConnAllLV(Name: string; Pin: tpin): boolean;
```

## Call pattern

```ats
NoConnAllLV('Name', "Pin");
```

## Description

Tests with low voltage whether Pin is not connected to any other Pin.

The function is not executed if the passed pin belongs to a grounded network.

## Metadata

- Category: Electrical testing
- Code: 1025
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
NoConnAllLV('NoConnAllLV1', "Pin1");
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
| `RES_Autostart` | `boolean` | Autostart |
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
| `RES_ErrorPinCount` | `integer` | Number of pins with error |
| `RES_ErrorPins[ ]` | `integer` | Addresses of the pins with error |
| `RES_Arcs[ ]` | `boolean` | Flag whether an arc occured |
| `RES_Values[ ]` | `real` | Measured values in Ohm |
| `RES_Prefixes[ ]` | `string` | Prefix for the measured values |
| `RES_OriginalPin` | `integer` | Address of the programmed pin |
| `RES_AutomaticIsolationTest` | `boolean` | TRUE, if the teststep was executed during an automatic isolation test |
| `RES_HighPinCount` | `integer` | Number of pins which are connected to the specified pin |
| `RES_HighPins[ ]` | `integer` | List of the specified pin and all pins which are connected to it |

## See also

`IsolationTestLV`, `NoConnAllDB`, `NoConnAllHV`, `ParamIsolationLV`
