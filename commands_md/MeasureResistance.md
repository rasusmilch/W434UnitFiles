# MeasureResistance

## Declaration

```ats
function MeasureResistance(Pin1: tpin; Pin2: tpin; var Prefix: string; var Value: tresistance; Pmax: tpower = PARAM_UseDefault): boolean;
```

## Call pattern

```ats
MeasureResistance("Pin1", "Pin2", Prefix, Value, <Pmax>W);
```

## Description

Measures the resistance between the passed pins.

The function does not refer to the net list.

The parameters for the measurement are:

Rstart=10kOhm, Pmax=0,5W, Trise=100ms, Twait=0ms, Tmeas=100ms, Imin=0mA, Imax=90mA, Umin=0V, Umax=UmaxLV

## Metadata

- Category: Electrical testing
- Code: 268035
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
Success = MeasureResistance("Pin1", "Pin2", Prefix, Value, 1W);
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

`MeasureCapacitance`, `MeasureResistanceCustom`, `ResistorTest`
