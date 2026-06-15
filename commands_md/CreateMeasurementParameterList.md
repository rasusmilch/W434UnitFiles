# CreateMeasurementParameterList

## Declaration

```ats
function CreateMeasurementParameterList(MeasurementType: integer; Parameters: tcreatearray):boolean;
```

## Call pattern

```ats
CreateMeasurementParameterList(MEASUREMENT_?,  Parameters);
```

## Description

Ceate a array veriable

## Metadata

- Category: Parameters
- Code: 268038
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `MeasurementType`: `integer` — Allowed values: MEASUREMENT_Resistance, MEASUREMENT_Voltage, MEASUREMENT_RLC, MEASUREMENT_DB
- `Parameters`: `tcreatearray`

## Example

```ats
CreateMeasurementParameterList(MEASUREMENT_Resistance, Parameters);
```

## See also

`CreateGeneratorParameterList`, `GenDielectricBreakdownEx`, `GenMeasureResistanceEx`, `GenMeasureVoltageEx`, `MeasureResistanceEx`, `MeasureRLCEx`, `MeasureVoltageEx`
