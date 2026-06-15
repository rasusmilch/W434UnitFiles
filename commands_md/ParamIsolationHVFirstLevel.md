# ParamIsolationHVFirstLevel

## Declaration

```ats
function ParamIsolationHVFirstLevel(Voltage: tvoltage=PARAM_DontChange; Threshold: tresistance=PARAM_DontChange; Trise: ttime=PARAM_DontChange; Twait: ttime=PARAM_DontChange; Tmeas: ttime=PARAM_DontChange; AutoRange: boolean=PARAM_DontChange; TmeasReduction: boolean=PARAM_DontChange; ILimit: tcurrent=PARAM_DontChange; TmeasFactor: real=PARAM_DontChange; VoltageRamp: tvoltageramp=PARAM_DontChange; DIdtEnabled: boolean=PARAM_DontChange; DIdtCurrentThreshold: tcurrent=PARAM_DontChange;DIdtTimeThreshold: ttime=PARAM_DontChange; ExpectedValue: tresistance=PARAM_DontChange): void;
```

## Call pattern

```ats
ParamIsolationHVFirstLevel(<Voltage>V, <Threshold>Ohm, <Trise>ms, <Twait>ms, <Tmeas>ms, <AutoRange>ON|OFF, <TmeasReduction>ON|OFF, <Ilimit>mA, TmeasFactor, <VoltageRamp>Vps, <DIdtEnabled>ON|OFF, <DIdtCurrentThreshold>uA, <DIdtTimeThreshold>us, <ExpectedValue>Ohm|OFF);
```

## Description

Sets the parameters for the first level of the two level HV isolation test.

For the second level the parameters of the "normal" HV isolationtest are used.

[image: ..\..\images\IsolationHVTwoLevels.bmp]
The values for U1, Trise1, Twait1, Tmeas1 and Ramp1 can be set with this function.

The values for U2, Trise2, Twait2, Tmeas2 and Ramp2 can be set with ParamIsolationHV.
Ramp3 is always the neagtive counterpart to Ramp2.


## Metadata

- Category: Parameters
- Code: 2314
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Voltage`: `tvoltage=PARAM_DontChange` — Test voltage which the test system tries to build up.; Presetting; : 50V
- `Threshold`: `tresistance=PARAM_DontChange` — Threshold resistance for the transition between connection and discontinuity. 
; If the measured resistance is lower than the threshold, the system detects a connection.; If the measured resistance is higher, the system detects a discontinuity.; Presetting; : 100 kOhm
- `Trise`: `ttime=PARAM_DontChange` — Time interval within which the test voltage must be reached.; Presetting; : 500ms
- `Twait`: `ttime=PARAM_DontChange` — Time between reaching the test voltage and first measurement of the resistance.; Presetting; : 100ms
- `Tmeas`: `ttime=PARAM_DontChange` — Duration of the actual measurement within which the threshold must be exceeded.; Presetting; : 100ms
- `AutoRange`: `boolean=PARAM_DontChange` — If the Autorange option is activated, additional measurements with changing ranges are executed if an error occurs to determine the exact resistance value.; Presetting; :; On; Allowed values: ON, OFF
- `TmeasReduction`: `boolean=PARAM_DontChange` — If this option is enabled the measurement is considered done and aborted as soon as the threshold resistance is reached.; Presetting; :; On; Allowed values: ON, OFF
- `ILimit`: `tcurrent=PARAM_DontChange` — Maximum current which is allowed during the test and and in case of an error.; Presetting; : 1mA
- `TmeasFactor`: `real=PARAM_DontChange` — Speeds the search for errors up if high measurement times are used.; Presetting; : 1
- `VoltageRamp`: `tvoltageramp=PARAM_DontChange` — Slope of the test voltage.; Presetting; : 1000V/ms
- `DIdtEnabled`: `boolean=PARAM_DontChange` — Enables respectively disables the dIdt detector.
; The detector detects whether the current which flows during a measurement exceeds a specified value for a specified time.; Note: The dIdt detector is not supported by all test systems.; Presetting; :; Off; Allowed values: ON, OFF
- `DIdtCurrentThreshold`: `tcurrent=PARAM_DontChange` — Current threshold for the dIdt detector which must not be exceeded longer than the time threshold.; Presetting; : 500uA
- `DIdtTimeThreshold`: `ttime=PARAM_DontChange` — Time threshold for the dIdt detector which must not be exceeded with a current which ist greater than the current threshold.; Presetting; : 10us
- `ExpectedValue`: `tresistance=PARAM_DontChange` — Expected measured value
; Can be used if the expected measured value differs strongly from the specified threshold
; The usage of expected value can be disabled by passing OFF
; If this parameter is enabled the test system always executes an required automatic range switching of the measuring devices.

## Example

```ats
ParamIsolationHVFirstLevel(50V, 110kOhm, 2s, PARAM_DontChange, 2s, ON, OFF, 10mA, 1, 1000Vpms);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_HVFLVoltage` | `real` | Parameter: Voltage in Volt |
| `RES_HVFLThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_HVFLIThreshold` | `real` | Parameter: Threshold in Ampere |
| `RES_HVFLUseIThreshold` | `boolean` | Parameter: Use current threshold |
| `RES_HVFLTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_HVFLTwait` | `real` | Parameter: Wait time in seconds |
| `RES_HVFLTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_HVFLVoltageRamp` | `real` | Parameter: Voltage ramp in Volts per second |
| `RES_HVFLTmeasFactor` | `real` | Parameter: Factor for the measurement time during search for shorts |
| `RES_HVFLAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_HVFLTmeasReduction` | `boolean` | Parameter: Measurement time reduction (dwelltime bypass) |
| `RES_HVFLCurrentLimit` | `real` | Parameter: Current limit in Ampere |
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
| `RES_HVFLdIdtEnabled` | `boolean` | TRUE, if the dIdt detector was enabled, otherwise FALSE |
| `RES_HVFLdIdtCurrentThreshold` | `real` | Current threshold for the dIdt detector which must not be exceeded longer than the time threshold. |
| `RES_HVFLdIdtTimeThreshold` | `real` | Time threshold for the dIdt detector which must not be exceeded with a current wihich ist greater than the current threshold. |
| `RES_dIdtEnabledChanged` | `boolean` | TRUE, if DIdtEnabled was changed, otherwise FALSE |
| `RES_dIdtCurrentThresholdChanged` | `boolean` | TRUE, if DIdtCurrentThreshold was changed, otherwise FALSE |
| `RES_dIdtTimeThresholdChanged` | `boolean` | TRUE, if DIdtTimeThreshold was changed, otherwise FALSE |

## See also

`IsolationTestHVTwoLevels`, `NoConnAllHVTwoLevels`, `NoConnectionHVTwoLevels`, `NoConnGroupHVTwoLevels`, `ParamIsolationHV`
