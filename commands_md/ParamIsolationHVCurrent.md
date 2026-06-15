# ParamIsolationHVCurrent

## Declaration

```ats
function ParamIsolationHVCurrent(Voltage: tvoltage=PARAM_DontChange; Threshold: tcurrent=PARAM_DontChange; Trise: ttime=PARAM_DontChange; Twait: ttime=PARAM_DontChange; Tmeas: ttime=PARAM_DontChange; TmeasReduction: boolean=PARAM_DontChange; ILimit: tcurrent=PARAM_DontChange; TmeasFactor: real=PARAM_DontChange; VoltageRamp: tvoltageramp=PARAM_DontChange; DIdtEnabled: boolean=PARAM_DontChange; DIdtCurrentThreshold: tcurrent=PARAM_DontChange; DIdtTimeThreshold: ttime=PARAM_DontChange; ExpectedValue: tcurrent=PARAM_DontChange): void;
```

## Call pattern

```ats
ParamIsolationHVCurrent(<Voltage>V, <Threshold>uA, <Trise>ms, <Twait>ms, <Tmeas>ms, TmeasReduction, <Ilimit>mA, TmeasFactor, <VoltageRamp>Vps, <DIdtEnabled>ON|OFF, <DIdtCurrentThreshold>uA, <DIdtTimeThreshold>us, <ExpectedValue>uA|OFF);
```

## Description

Sets the parameters for the HV isolation test.
Allows to use current as a threshold.

If current is used as threshold it is not possible to execute automatic voltage ranging in case of an error during the HV test.

## Metadata

- Category: Parameters
- Code: 2313
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Voltage`: `tvoltage=PARAM_DontChange` — Test voltage which the test system tries to build up.
- `Threshold`: `tcurrent=PARAM_DontChange` — Threshold current for the transition between connection and discontinuity.
; If the measured current is higher than the entered value, the system detects a connection.; If the measured current is lower, the system detects a discontinuity.
- `Trise`: `ttime=PARAM_DontChange` — Time interval within which the test voltage must be reached.
- `Twait`: `ttime=PARAM_DontChange` — Time between reaching the test voltage and first measurement of the resistance.
- `Tmeas`: `ttime=PARAM_DontChange` — Duration of the actual measurement within which the threshold must be exceeded.
- `TmeasReduction`: `boolean=PARAM_DontChange` — If this option is enabled the measurement is considered done and aborted as soon as the threshold current is reached.
- `ILimit`: `tcurrent=PARAM_DontChange` — Maximum current which is allowed during the test and and in case of an error.
- `TmeasFactor`: `real=PARAM_DontChange` — Speeds the search for errors up if high measurement times are used.
- `VoltageRamp`: `tvoltageramp=PARAM_DontChange` — Slope of the test voltage.
- `DIdtEnabled`: `boolean=PARAM_DontChange` — Enables respectively disables the dIdt detector.
; The detector detects whether the current which flows during a measurement exceeds a specified value for a specified time.; Note: The dIdt detector is not supported by all test systems.; Allowed values: ON, OFF
- `DIdtCurrentThreshold`: `tcurrent=PARAM_DontChange` — Current threshold for the dIdt detector which must not be exceeded longer than the time threshold.
- `DIdtTimeThreshold`: `ttime=PARAM_DontChange` — Time threshold for the dIdt detector which must not be exceeded with a current wihich ist greater than the current threshold.
- `ExpectedValue`: `tcurrent=PARAM_DontChange` — Expected measured value
; Can be used if the expected measured value differs strongly from the specified threshold
; The usage of expected value can be disabled by passing OFF.
; If this parameter is enabled the test system always executes an required automatic range switching of the measuring devices.; Allowed values: <Current value>, OFF

## Example

```ats
ParamIsolationHVCurrent(600V, 750nA, 2s, PARAM_DontChange, 2s, OFF, 1mA, 1, 1000Vpms);
```

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

## See also

`IsolationTestHV`, `NoConnAllHV`, `NoConnectionHV`, `NoConnGroupHV`, `ParamIsolationHV`
