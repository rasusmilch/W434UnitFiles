# GenMeasureCurrent

## Declaration

```ats
function GenMeasureCurrent(MeasBus: integer; var Prefix: string; var Value: tcurrent):boolean;
```

## Call pattern

```ats
GenMeasureCurrent(MEASBUS_?, Prefix, Value);
```

## Description

Measures the current which is stimulated by the internal generator

If you measure on the U2- or U3-bus be aware that there is a 6.25 kOhm-resistor in parallel to the object to be measured.
In addition a fraction of the measurment current will flow through a voltage monitoring unit.

Measurments with this function on the U2- and U3-bus are not very accurate.


## Metadata

- Category: Generators
- Code: 270087
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `MeasBus`: `integer` — Allowed values: MEASBUS_Sense, MEASBUS_U2, MEASBUS_U3
- `var Prefix`: `string`
- `var Value`: `tcurrent`

## Example

```ats
GenVoltageOn(STIMBUS_U3, 10V, 10mA);
Prefix = '';
Value  = '';
GenMeasureCurrent(MEASBUS_U3, Prefix, Value);
UIWriteNormal(StrAdd(Prefix, FormatCurrent(Value)));
GenVoltageOff(STIMBUS_U3);
```

## See also

`GenMeasureCurrentEx`, `GenMeasureResistance`, `GenMeasureVoltage`, `MeasuerCurrentStim`, `GenMeasureResistanceEx`
