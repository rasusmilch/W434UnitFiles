# ReportWriteMeasurementParameters

## Declaration

```ats
function ReportWriteMeasurementParameters(CommandGroup: integer): void;
```

## Call pattern

```ats
ReportWriteMeasurementParameters(CMDGRP_?);
```

## Description

Writes the measurement parameters of the passed command group into the report

## Metadata

- Category: Data to Report
- Code: 1795
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `CommandGroup`: `integer` — Allowed values: CMDGRP_Continuity, CMDGRP_IsolationLV, CMDGRP_IsolationHV, CMDGRP_DielectricBreakdown

## Example

```ats
ReportWriteMeasurementParameters(CMDGRP_Continuity);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_CommandGroup` | `integer` | Commandgroup whose parameters shall be written |
| `RES_CCurrent` | `real` | Parameter: Current in Ampere |
| `RES_CThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_CTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_CTwait` | `real` | Parameter: Wait time in seconds |
| `RES_CTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_CAutoRange` | `boolean` | Parameter: Automatic ranging active |
| `RES_CVoltageLimit` | `real` | Parameter: Voltage limit in Volt |
| `RES_LVVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_LVThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_LVTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_LVTwait` | `real` | Parameter: Wait time in seconds |
| `RES_LVTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_LVAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_LVCurrentLimit` | `real` | Parameter: Current limit in Ampere |
| `RES_LVTmeasReduction` | `boolean` | Parameter: Measurement time reduction (dwelltime bypass) |
| `RES_HVVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_HVThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_HVTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_HVTwait` | `real` | Parameter: Wait time in seconds |
| `RES_HVTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_HVVoltageRamp` | `real` | Parameter: Voltage ramp in Volts per second |
| `RES_HVTmeasFactor` | `real` | Parameter: Factor for the measurement time during search for shorts |
| `RES_HVAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_HVTmeasReduction` | `boolean` | Parameter: Measurement time reduction (dwelltime bypass) |
| `RES_HVCurrentLimit` | `real` | Parameter: Current limit in Ampere |
| `RES_DBVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_DBThresholdIr` | `real` | Parameter: Threshold for the real current in Ampere |
| `RES_DBThresholdIi` | `real` | Parameter: Threshold for the imaginary current in Ampere |
| `RES_DBTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_DBTwait` | `real` | Parameter: Wait time in seconds |
| `RES_DBTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_DBVoltageRamp` | `real` | Parameter: Voltage ramp in Volt per second |
| `RES_DBTmeasFactor` | `real` | Parameter: Factor for the measurement time during search for shorts |
| `RES_DBFrequency` | `real` | Parameter: Frequency |
| `RES_PowerFrequency` | `real` | Parameter: Power frequency in Hertz |

## See also

`ParamContinuity`, `ParamDielectricBreakdown`, `ParamIsolationHV`, `ParamIsolationLV`, `ReportWrite`, `ReportWriteTag`
