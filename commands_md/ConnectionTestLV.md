# ConnectionTestLV

## Declaration

```ats
function ConnectionTestLV(Name: string; Pin1: tpin; Pin2: tpin): boolean;
```

## Call pattern

```ats
ConnectionTestLV('Name', "Pin1", "Pin2");
```

## Description

Tests with the parameters of the LV isolation test whether there is a connection between Pin1 and Pin2.

## Metadata

- Category: Electrical testing
- Code: 1033
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
ConnectionTestLV('ConnectionTestLV1', "Pin1", "Pin2");
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
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_ExtVoltageFound` | `boolean` | External voltage found |
| `RES_ExtVoltagePin1` | `integer` | Pin1 with external voltage |
| `RES_ExtVoltagePin2` | `integer` | Pin2 with external voltage |
| `RES_ExtVoltageValue` | `real` | Value of the external voltage |
| `RES_ExtVoltagePrefix` | `string` | Prefix of the external voltage |
| `RES_Autostart` | `boolean` | Autostart |
| `RES_Arc` | `boolean` | Arc occured |
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
| `RES_OriginalPin1` | `integer` | Address of the first programmed pin |
| `RES_OriginalPin2` | `integer` | Address of the second programmed pin |

## See also

`ConnectionTest`, `ConnectionTestDB`, `ConnectionTestHV`, `ParamIsolationLV`
