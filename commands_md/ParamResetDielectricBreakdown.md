# ParamResetDielectricBreakdown

## Declaration

```ats
function ParamResetDielectricBreakdown(): void;
```

## Call pattern

```ats
ParamResetDielectricBreakdown();
```

## Description

Resets the measurement parameters for the dielectric breakdown test to the values in the parameter file.

The default parameters will be used if there is no parameter file available.

## Metadata

- Category: Parameters
- Code: 2311
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_DBVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_DBThresholdIr` | `real` | Parameter: Threshold for the real current in Ampere |
| `RES_DBThresholdIi` | `real` | Parameter: Threshold for the imaginary current in Ampere |
| `RES_DBTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_DBTwait` | `real` | Parameter: Wait time in seconds |
| `RES_DBTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_DBVoltageRamp` | `real` | Parameter: Voltage ramp in Volt per second |
| `RES_DBTmeasFactor` | `real` | Parameter: Factor for the measurement time during search for shorts |
| `RES_DBFrequency` | `real` | Parameter: Frequency |
| `RES_DBAutoRange` | `boolean` | Automatic ranging |
| `RES_VoltageChanged` | `boolean` | TRUE, if voltage was modified, otherwise FALSE |
| `RES_ThresholdIrChanged` | `boolean` | TRUE, if threshold for the real current was modified, otherwise FALSE |
| `RES_ThresholdIiChanged` | `boolean` | TRUE, if threshold for the imaginary current was modified, otherwise FALSE |
| `RES_TriseChanged` | `boolean` | TRUE, if maximum rise time was modified, otherwise FALSE |
| `RES_TwaitChanged` | `boolean` | TRUE, if wait time was modified, otherwise FALSE |
| `RES_TmeasChanged` | `boolean` | TRUE, if measurement time was modified, otherwise FALSE |
| `RES_TmeasFactorChanged` | `boolean` | TRUE, if factor for the measurement time was modified, otherwise FALSE |
| `RES_VoltageRampChanged` | `boolean` | TRUE, if voltage ramp was modified, otherwise FALSE |
| `RES_FrequencyChanged` | `boolean` | TRUE, if frequency was modified, otherwise FALSE |
| `RES_AutoRangeChanged` | `boolean` | TRUE, if automatic ranging was changed |
