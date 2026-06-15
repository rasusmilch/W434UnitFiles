# MeasureResistanceCustom

## Declaration

```ats
function MeasureResistanceCustom(Pin1: tpin; Pin2: tpin; var Prefix: string; var Value: tresistance; Pmax: tpower = PARAM_UseDefault; Rstart: tresistance = PARAM_UseDefault; Trise: ttime = PARAM_UseDefault;  Twait: ttime = PARAM_UseDefault; Tmeas: ttime = PARAM_UseDefault;  Imin: tcurrent = PARAM_UseDefault; Imax: tcurrent = PARAM_UseDefault; Umin: tvoltage = PARAM_UseDefault; Umax: tvoltage = PARAM_UseDefault): boolean;
```

## Call pattern

```ats
MeasureResistanceCustom("Pin1", "Pin2", Prefix, Value, <Pmax>W, <Rstart>Ohm, <Trise>s, <Twait>s, <Tmeas>s, <Imin>A, <Imax>A, <Umin>V, <Umax>V);
```

## Description

Measures the resistance between the passed pins.

The function does not refer to the net list.


## Metadata

- Category: Electrical testing
- Code: 268036
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `var Prefix`: `string`
- `var Value`: `tresistance`
- `Pmax`: `tpower = PARAM_UseDefault`
- `Rstart`: `tresistance = PARAM_UseDefault`
- `Trise`: `ttime = PARAM_UseDefault`
- `Twait`: `ttime = PARAM_UseDefault`
- `Tmeas`: `ttime = PARAM_UseDefault`
- `Imin`: `tcurrent = PARAM_UseDefault`
- `Imax`: `tcurrent = PARAM_UseDefault`
- `Umin`: `tvoltage = PARAM_UseDefault`
- `Umax`: `tvoltage = PARAM_UseDefault`

## Return value

The function returns TRUE if the measurement was successful, otherwise FALSE.

The measured value is returned in "Prefix" and "Value".

Values for "Prefix":

'%' = "Value" is invalid

'<' = Real value is less than "Value"

'>' = Real value is higher than "Value"

'' = Real value equals "Value"

## Example

```ats
Prefix = '';
Value = 0;
Success = MeasureResistanceCustom("Pin1", "Pin2", Prefix, Value, 120W, 10kOhm, 10ms, 0s, 100ms, 0mA, 10mA, 0V, 40V);
if (Success)
begin
   UIWriteNormal(StrAdd(Prefix, FormatResistance(Value)));
end
else
begin
   UIWriteError('Measurement failed!');
end;
```

## See also

`MeasureResistance`, `ResistorTest`, `ResistorTestCustom`
