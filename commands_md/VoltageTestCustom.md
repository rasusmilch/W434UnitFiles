# VoltageTestCustom

## Declaration

```ats
function VoltageTestCustom(Name: string; Pin1: tpin; Pin2: tpin; Value: tvoltage; LowerTol: tvoltage; UpperTol: tvoltage; Twait: ttime=PARAM_UseDefault; Tmeas: ttime=PARAM_UseDefault; Frequency: tfrequency=PARAM_UseDefault): boolean;
```

## Call pattern

```ats
VoltageTestCustom('Name', "Pin1", "Pin2", <Value>V, <LowerTol>V, <UpperTol>V, <Twait>s, <Tmeas>s, <Frequency>Hz);
```

## Description

Tests a voltage between Pin1 and Pin2 with custom parameters.

## Metadata

- Category: Electrical testing
- Code: 2049
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Value`: `tvoltage`
- `LowerTol`: `tvoltage`
- `UpperTol`: `tvoltage`
- `Twait`: `ttime=PARAM_UseDefault`
- `Tmeas`: `ttime=PARAM_UseDefault`
- `Frequency`: `tfrequency=PARAM_UseDefault`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
VoltageTestCustom('Voltage1', "Pin1", "Pin2", 10V, 2V, 2V, 100ms, 200ms);
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
| `RES_Voltage` | `real` | Parameter: Reference value in Volt |
| `RES_LowerTol` | `real` | Parameter: Lower tolerance in Volt |
| `RES_UpperTol` | `real` | Parameter: Upper tolerance in Volt |
| `RES_MinVoltage` | `real` | Parameter: Minimum allowed value in Volt (Reference value - lower tolerance) |
| `RES_MaxVoltage` | `real` | Parameter: Maximum allowed value in Volt (Reference value + upper tolerance) |
| `RES_Twait` | `real` | Parameter: Wait time in seconds |
| `RES_Tmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_Autostart` | `boolean` | Autostart |
| `RES_Value` | `real` | Measured value in Volt |
| `RES_Prefix` | `string` | Prefix of the measured value |
| `RES_OriginalPin1` | `integer` | Address of the first programmed pin |
| `RES_OriginalPin2` | `integer` | Address of the second programmed pin |

## See also

`VoltageFrequencyTest`, `VoltageTest`
