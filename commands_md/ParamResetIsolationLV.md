# ParamResetIsolationLV

## Declaration

```ats
function ParamResetIsolationLV(): void;
```

## Call pattern

```ats
ParamResetIsolationLV();
```

## Description

Resets the measurement parameters for the LV isolation test to the values in the parameter file.

The default parameters will be used if there is no parameter file available.

## Metadata

- Category: Parameters
- Code: 2309
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
| `RES_LVVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_LVThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_LVTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_LVTwait` | `real` | Parameter: Wait time in seconds |
| `RES_LVTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_LVAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_LVCurrentLimit` | `real` | Parameter: Current limit in Ampere |
| `RES_LVTmeasReduction` | `boolean` | Parameter: Measurement time reduction (dwelltime bypass) |
| `RES_VoltageChanged` | `boolean` | TRUE, if voltage was modified, otherwise FALSE |
| `RES_ThresholdChanged` | `boolean` | TRUE, if threshold was modified, otherwise FALSE |
| `RES_TriseChanged` | `boolean` | TRUE, if maximum rise time was modified, otherwise FALSE |
| `RES_TwaitChanged` | `boolean` | TRUE, if wait time was modified, otherwise FALSE |
| `RES_TmeasChanged` | `boolean` | TRUE, if measurement time was modified, otherwise FALSE |
| `RES_AutoRangeChanged` | `boolean` | TRUE, if automatic ranging was modified, otherwise FALSE |
| `RES_CurrentLimitChanged` | `boolean` | TRUE, if current limit was modified, otherwise FALSE |
| `RES_TmeasReductionChanged` | `boolean` | TRUE, if measurement time reduction was modified, otherwise FALSE |
