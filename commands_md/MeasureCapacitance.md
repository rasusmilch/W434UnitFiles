# MeasureCapacitance

## Declaration

```ats
function MeasureCapacitance(Pin1: tpin; Pin2: tpin; var Prefix: string; var Value: tcapacitance; Umax: tvoltage = PARAM_UseDefault; Cstart: tcapacitance = PARAM_UseDefault): boolean;
```

## Call pattern

```ats
MeasureCapacitance("Pin1", "Pin2", Prefix, Value, <Umax>V, <Cstart>nF);
```

## Description

Measures a capacitance between the passed pins.
The function does not refer to the netlist.

## Metadata

- Category: Electrical testing
- Code: 268037
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `var Prefix`: `string`
- `var Value`: `tcapacitance`
- `Umax`: `tvoltage = PARAM_UseDefault`
- `Cstart`: `tcapacitance = PARAM_UseDefault`

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
Success = MeasureCapacitance("Pin1", "Pin2", Prefix, Value, 3V, 100nF);
if (Success)
begin
   UIWriteNormal(StrAdd(Prefix, FormatCapacitance(Value)));
end
else
begin
   UIWriteError('Measurement failed!');
end;
```

## See also

`CapacitorTest`, `MeasureResistance`
