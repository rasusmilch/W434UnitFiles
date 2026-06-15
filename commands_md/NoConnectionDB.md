# NoConnectionDB

## Declaration

```ats
function NoConnectionDB(Name: string; Pin1: tpin; Pin2: tpin): boolean;
```

## Call pattern

```ats
NoConnectionDB('Name', "Pin1", "Pin2");
```

## Description

Tests with alternating voltage whether Pin1 and Pin2 are not connected with each other.

## Metadata

- Category: Electrical testing
- Code: 1536
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
NoConnectionDB('NoConnectionDB1', "Pin1", "Pin2");
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
| `RES_Arc` | `boolean` | Arc occured |
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
| `RES_OriginalPin1` | `integer` | Address of the first programmed pin |
| `RES_OriginalPin2` | `integer` | Address of the second programmed pin |
| `RES_ShortToLowerVoltageLevel` | `boolean` | TRUE, if there is possibly a short to a lower voltage level |

## See also

`IsolationTestDB`, `NoConnAllDB`, `NoConnectionHV`, `NoConnectionLV`, `NoConnGroupDB`, `ParamDielectricBreakdown`
