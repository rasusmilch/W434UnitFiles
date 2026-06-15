# GenMeasureVoltage

## Declaration

```ats
function GenMeasureVoltage(MeasBus: integer; var Prefix: string; var Value: tvoltage):boolean;
```

## Call pattern

```ats
GenMeasureVoltage(MEASBUS_?, Prefix, Value);
```

## Description

Measures the voltage on the measurement bus (Sense, U2 or U3)

If you measure on the U2- or U3-bus be aware that there is a 6.25 kOhm-resistor in parallel to the object to be measured.
In addition a fraction of the measurment current will flow through a voltage monitoring unit.

Measurments with this function on the U2- and U3-bus are not very accurate.



## Metadata

- Category: Generators
- Code: 270086
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `MeasBus`: `integer` — Allowed values: MEASBUS_Sense, MEASBUS_U2, MEASBUS_U3
- `var Prefix`: `string`
- `var Value`: `tvoltage`

## Return value

The function returns TRUE if the measurement of the value is equal, otherwise FALSE.

## Example

```ats
GenCurrentOn(STIMBUS_U3, 100mA, 10V);
Prefix = '';
Value  = '';
GenMeasureVoltage(MEASBUS_U3, Prefix, Value);
UIWriteNormal(StrAdd(Prefix, FormatVoltage(Value)));
GenCurrentOff(STIMBUS_U3);
```

## See also

`GenMeasureCurrent`, `GenMeasureResistance`, `GenMeasureVoltageEx`, `GenMeasureResistanceEx`
