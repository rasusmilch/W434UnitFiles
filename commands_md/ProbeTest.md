# ProbeTest

## Declaration

```ats
function ProbeTest(Name: string; Pin: tpin): integer;
```

## Call pattern

```ats
ProbeTest('Name', "Pin");
```

## Description

Tests whether a pin is connected with the probe.

For this tests the measurement parameters for the continuity test are used.

## Metadata

- Category: Electrical testing
- Code: 522
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin`: `tpin`

## Return value

The function returns:

TESTSTEP_Passed, if the test passed

TESTSTEP_Failed, if an error was detected

TESTSTEP_NotExecuted, if the test was not executed

## Example

```ats
ProbeTest('ProbeTest1', "Pin1");
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
| `RES_Pin` | `integer` | Address of the tested pin |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_ExtVoltageFound` | `boolean` | External voltage found |
| `RES_ExtVoltagePin1` | `integer` | Pin1 with external voltage |
| `RES_ExtVoltagePin2` | `integer` | Pin2 with external voltage |
| `RES_ExtVoltageValue` | `real` | Value of the external voltage |
| `RES_ExtVoltagePrefix` | `string` | Prefix of the external voltage |
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
| `RES_OriginalPin` | `integer` | Address of the programmed pin |

## See also

`ConnectionTest`, `MiscProbe`, `ProbeTestSearch`, `WireTest`
