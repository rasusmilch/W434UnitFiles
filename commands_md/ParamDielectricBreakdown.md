# ParamDielectricBreakdown

## Declaration

```ats
function ParamDielectricBreakdown(Voltage: tvoltage=PARAM_DontChange; Trise: ttime=PARAM_DontChange; Twait: ttime=PARAM_DontChange; Tmeas: ttime=PARAM_DontChange; TmeasFactor: real=PARAM_DontChange; VoltageRamp: tvoltageramp=PARAM_DontChange; Frequency: tfrequency=PARAM_DontChange; ThresholdIr: tcurrent=PARAM_DontChange; ThresholdIi: tcurrent=PARAM_DontChange; AutoRange: boolean=PARAM_DontChange): void;
```

## Call pattern

```ats
ParamDielectricBreakdown(<Voltage>V, <Trise>ms, <Twait>ms, <Tmeas>ms, TmeasFactor, <VoltageRamp>Vps, <Frequency>Hz, <ThresholdIr>mA, <ThresholdIi>mA, ON|OFF);
```

## Description

Sets the parameters for the dielectric breakdown test.

## Metadata

- Category: Parameters
- Code: 2307
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Voltage`: `tvoltage=PARAM_DontChange` — Test voltage which the test system tries to build up.
- `Trise`: `ttime=PARAM_DontChange` — Time interval within which the test voltage must be reached.
- `Twait`: `ttime=PARAM_DontChange` — Time between reaching the test voltage and first measurement of the resistance.
- `Tmeas`: `ttime=PARAM_DontChange` — Duration of the actual measurement within which the threshold must be exceeded.
- `TmeasFactor`: `real=PARAM_DontChange` — Speeds the search for errors up if high measurement times are used.
- `VoltageRamp`: `tvoltageramp=PARAM_DontChange` — Slope of the test voltage.
- `Frequency`: `tfrequency=PARAM_DontChange` — Frequency of the test voltage
- `ThresholdIr`: `tcurrent=PARAM_DontChange` — Threshold current (real fraction) for the transition between connection and discontinuity.
; If the measured current is higher than the entered value, the system detects a connection.; If the measured current is lower, the system detects a discontinuity.
- `ThresholdIi`: `tcurrent=PARAM_DontChange` — Threshold current (imaginary fraction) for the transition between connection and discontinuity.
; If the measured current is higher than the entered value, the system detects a connection.; If the measured current is lower, the system detects a discontinuity.
- `AutoRange`: `boolean=PARAM_DontChange` — If the Autorange option is activated, additional measurements with changing ranges are executed if an error occurs to determine the exact current value.; Allowed values: ON, OFF

## Example

```ats
ParamDielectricBreakdown(500V, 3s, PARAM_DontChange, 2s, 1, 1000Vpms, 50Hz, 4mA, 5mA);
```

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

## See also

`DielectricBreakdownTest`, `NoConnAllDB`, `NoConnectionDB`, `NoConnGroupDB`, `ParamContinuity`, `ParamGetDielectricBreakdown`, `ParamIsolationHV`, `ParamIsolationLV`
