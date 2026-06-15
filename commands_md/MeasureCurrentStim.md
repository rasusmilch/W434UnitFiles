# MeasureCurrentStim

## Declaration

```ats
function MeasureCurrentStim(Pin1: tpin; Pin2: tpin; Voltage: tvoltage; MaxCurrent: tcurrent; var Prefix: string; var Value: tcurrent; Trise: ttime = PARAM_UseDefault; Twait: ttime = PARAM_UseDefault; Tmeas: ttime = PARAM_UseDefault): boolean;
```

## Call pattern

```ats
MeasureCurrentStim("Pin1", "Pin2", <Voltage>V,<MaxCurrent>mA,  Prefix, Value, <Trise>ms, <Twait>ms, <Tmeas>ms);
```

## Description

The current between Pin1 and Pin2 will be measured with a constant voltage of V.

## Metadata

- Category: Electrical testing
- Code: 268034
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Voltage`: `tvoltage`
- `MaxCurrent`: `tcurrent` — Specifies the maximum current to be generated.
- `var Prefix`: `string`
- `var Value`: `tcurrent`
- `Trise`: `ttime = PARAM_UseDefault`
- `Twait`: `ttime = PARAM_UseDefault`
- `Tmeas`: `ttime = PARAM_UseDefault`

## Return value

The command returns TRUE if

- the generator can build up and hold the specified voltage

- the prefix of the measurement is ' ' (equals '=')

If the result of the command is TRUE the measured current will be returned in the variable 'Value'. If not 0 will be returned in 'Value'.

## Example

```ats
Prefix = '';
Value = 0;
MeasureCurrentStim("1", "2", 100V, 20mA,  Prefix, Value, 50ms, 0ms, 20ms);
UIWriteNormal(StrAdd(Prefix, FormatCurrent(Value)));
```

## See also

`MeasureVoltageStim`
