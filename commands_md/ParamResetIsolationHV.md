# ParamResetIsolationHV

## Declaration

```ats
function ParamResetIsolationHV(): void;
```

## Call pattern

```ats
ParamResetIsolationHV();
```

## Description

Resets the measurement parameters for the HV isolation test to the values in the parameter file.

The default parameters will be used if there is no parameter file available.

## Metadata

- Category: Parameters
- Code: 2310
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
| `RES_HVVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_HVThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_HVIThreshold` | `real` | Parameter: Threshold in Ampere |
| `RES_HVUseIThreshold` | `boolean` | Parameter: Use current threshold |
| `RES_HVTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_HVTwait` | `real` | Parameter: Wait time in seconds |
| `RES_HVTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_HVVoltageRamp` | `real` | Parameter: Voltage ramp in Volts per second |
| `RES_HVTmeasFactor` | `real` | Parameter: Factor for the measurement time during search for shorts |
| `RES_HVAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_HVTmeasReduction` | `boolean` | Parameter: Measurement time reduction (dwelltime bypass) |
| `RES_HVCurrentLimit` | `real` | Parameter: Current limit in Ampere |
| `RES_VoltageChanged` | `boolean` | TRUE, if voltage was modified, otherwise FALSE |
| `RES_ThresholdChanged` | `boolean` | TRUE, if threshold was modified, otherwise FALSE |
| `RES_TriseChanged` | `boolean` | TRUE, if maximum rise time was modified, otherwise FALSE |
| `RES_TwaitChanged` | `boolean` | TRUE, if wait time was modified, otherwise FALSE |
| `RES_TmeasChanged` | `boolean` | TRUE, if measurement time was modified, otherwise FALSE |
| `RES_AutoRangeChanged` | `boolean` | TRUE, if automatic ranging was modified, otherwise FALSE |
| `RES_CurrentLimitChanged` | `boolean` | TRUE, if current limit was modified, otherwise FALSE |
| `RES_TmeasReductionChanged` | `boolean` | TRUE, if measurement time reduction was modified, otherwise FALSE |
| `RES_TmeasFactorChanged` | `boolean` | TRUE, if factor for the measurement time was modified, otherwise FALSE |
| `RES_VoltageRampChanged` | `boolean` | TRUE, if voltage ramp was modified, otherwise FALSE |
| `RES_HVdIdtEnabled` | `boolean` | TRUE, if the dIdt detector was enabled, otherwise FALSE |
| `RES_HVdIdtCurrentThreshold` | `real` | Current threshold for the dIdt detector which must not be exceeded longer than the time threshold. |
| `RES_HVdIdtTimeThreshold` | `real` | Time threshold for the dIdt detector which must not be exceeded with a current wihich ist greater than the current threshold. |
| `RES_dIdtEnabledChanged` | `boolean` | TRUE, if DIdtEnabled was changed, otherwise FALSE |
| `RES_dIdtCurrentThresholdChanged` | `boolean` | TRUE, if DIdtCurrentThreshold was changed, otherwise FALSE |
| `RES_dIdtTimeThresholdChanged` | `boolean` | TRUE, if DIdtTimeThreshold was changed, otherwise FALSE |
