# GenGetTemperature

## Declaration

```ats
function GenGetTemperature(Sensor: integer):real;
```

## Call pattern

```ats
GenGetTemperature(Sensor_?)
```

## Description

Temperature inside the system (only W484)

## Metadata

- Category: Generators
- Code: 270101
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Sensor`: `integer`

## Example

```ats
Temperature = GenGetTemperature(Sensor_1);
Msg = StrAdd('Temperature sensor 1: ', Temperature);
Msg = StrAdd(Msg, '�C');
UIInfoDialog(Msg);
```
