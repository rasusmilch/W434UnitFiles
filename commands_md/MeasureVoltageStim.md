# MeasureVoltageStim

## Declaration

```ats
function MeasureVoltageStim(Pin1: tpin; Pin2: tpin; Current: tcurrent; MaxVoltage: tvoltage; var Prefix: string; var Value: tvoltage; Trise: ttime = PARAM_UseDefault; Twait: ttime = PARAM_UseDefault; Tmeas: ttime = PARAM_UseDefault): boolean;
```

## Call pattern

```ats
MeasureVoltageStim("Pin1", "Pin2", <Current>mA, <MaxVoltage>V, Prefix, Value, <Trise>ms, <Twait>ms, <Tmeas>ms);
```

## Description

The voltage between Pin1 and Pin2 will be measured with a constant current of A.

## Metadata

- Category: Electrical testing
- Code: 268033
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Current`: `tcurrent`
- `MaxVoltage`: `tvoltage` — Specifies the maximum voltage to be generated.
- `var Prefix`: `string`
- `var Value`: `tvoltage`
- `Trise`: `ttime = PARAM_UseDefault`
- `Twait`: `ttime = PARAM_UseDefault`
- `Tmeas`: `ttime = PARAM_UseDefault`

## Return value

The command returns TRUE if

- the generator can build up and hold the specified current

- the prefix of the measurement is ' ' (equals '=')

If the result of the command is TRUE the measured voltage will be returned in the variable 'Value'. If not 0 will be returned in 'Value'.

## Example

```ats
MeasureVoltageStim("1", "2", 10mA, 40V, Prefix, Value, 50ms, 0ms, 20ms);
UIWriteNormal(StrAdd(Prefix, FormatVoltage(Value)));
```

## See also

`MeasureCurrentStim`
