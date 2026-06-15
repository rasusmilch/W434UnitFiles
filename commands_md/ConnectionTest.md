# ConnectionTest

## Declaration

```ats
function ConnectionTest(Name: string; Pin1: tpin; Pin2: tpin): boolean;
```

## Call pattern

```ats
ConnectionTest('Name', "Pin1", "Pin2");
```

## Description

Tests a connection between Pin1 and Pin2.

The function does not refer to the netlist. Pin1 and Pin2 can be any pins.

## Metadata

- Category: Electrical testing
- Code: 514
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
ConnectionTest('Connection1', "Pin1", "Pin2");
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
| `RES_4Wire` | `boolean` | 4-Wire measurement |
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
| `RES_CCurrent` | `real` | Parameter: Current in Ampere |
| `RES_CThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_CTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_CTwait` | `real` | Parameter: Wait time in seconds |
| `RES_CTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_CAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_CVoltageLimit` | `real` | Parameter: Voltage limit in volt |
| `RES_InterchangedWiresPin1` | `integer` | Address of the first pin to which an interchange was detected. |
| `RES_InterchangedWiresPin2` | `integer` | Address of the second pin to which an interchange was detected. |
| `RES_OriginalPin1` | `integer` | Address of the first programmed pin |
| `RES_OriginalPin2` | `integer` | Address of the second programmed pin |

## See also

`IsConnected`, `NetworkTest`, `ParamAutostart`, `ParamCheckForInterchangedWires`, `ParamContinuity`, `ParamStopOnFail`, `WireTest`
