# VoltageFrequencyTest

## Declaration

```ats
function VoltageFrequencyTest(Name: string; Pin1: tpin; Pin2: tpin; Voltage: tvoltage; VoltageLowerTol: tvoltage; VoltageUpperTol: tvoltage; Frequency: tfrequency; FrequencyLowerTol: tfrequency; FrequencyUpperTol: tfrequency;Twait: ttime = PARAM_UseDefault; Tmeas: ttime = PARAM_UseDefault): boolean;
```

## Call pattern

```ats
VoltageFrequencyTest('Name', "Pin1", "Pin2", <VoltageValue>V, <LowerTol>V, <UpperTol>V, <Frequency>Hz, <FrequencyLowerTol>Hz <FrequencyUpperTol>Hz, <Twait>s, <Tmeas>s);
```

## Description

The function test a voltage and its frequency between the pins Pin1 and Pin2

## Metadata

- Category: Electrical testing
- Code: 2050
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Voltage`: `tvoltage`
- `VoltageLowerTol`: `tvoltage`
- `VoltageUpperTol`: `tvoltage`
- `Frequency`: `tfrequency`
- `FrequencyLowerTol`: `tfrequency`
- `FrequencyUpperTol`: `tfrequency`
- `Twait`: `ttime = PARAM_UseDefault`
- `Tmeas`: `ttime = PARAM_UseDefault`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
VoltageFrequencyTest('Voltage1', "Pin1", "Pin2", 10V, 2V, 2V, 60Hz, 10Hz, 10Hz, 10ms, 180ms);
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
| `RES_Value` | `real` | Measures voltage value in Volts |
| `RES_Prefix` | `string` | Prefix of the measured voltage value |
| `RES_OriginalPin1` | `integer` | Address of the first programmed pin |
| `RES_OriginalPin2` | `integer` | Address of the second programmed pin |
| `RES_Freq` | `real` | Frequency value to be tested |
| `RES_FreqLowerTol` | `real` | Lower tolerance for the frequency test |
| `RES_FreqUpperTol` | `real` | Upper tolerance for the frequency test |
| `RES_VoltagePassed` | `boolean` | TRUE, if voltage value correct |
| `RES_FrequencyPassed` | `boolean` | TRUE, if frequency value correct |
| `RES_MinFreq` | `real` | Minimum value for the frequency test |
| `RES_MaxFreq` | `real` | Maximum value for the frequency test |
| `RES_fValue` | `real` | Measures voltage value in Hertz |
| `RES_fPrefix` | `string` | Prefix of the measured frequency value |

## See also

`VoltageTest`, `VoltageTestCustom`
