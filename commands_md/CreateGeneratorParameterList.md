# CreateGeneratorParameterList

## Declaration

```ats
function CreateGeneratorParameterList(MeasurementType: integer; Parameters: tcreatearray):boolean;
```

## Call pattern

```ats
CreateGeneratorParameterList(STIMULATE_?, StimulateParameters);
```

## Description

Creates an array variable for parameters to create an accurate parametrised generator settings.



Due to the wide variety of wave forms generated with this command, the standard diagnostic/calibration can not cover all resulting variants. Please verify the signal used for your application with a certified measurement device.

## Metadata

- Category: Parameters
- Code: 268046
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `MeasurementType`: `integer`
- `Parameters`: `tcreatearray`

## Example

```ats
CreateGeneratorParameterList(STIMULATE_Voltage, StimulateParameters);
StimulateParameters[Uon_PARAM_Device] = DEVICE_UI55;
StimulateParameters[Uon_PARAM_Trise] = 0.02;
StimulateParameters[Uon_PARAM_GenToJack] = FALSE;
StimulateParameters[Uon_PARAM_GenToMatrix] = TRUE;
StimulateParameters[Uon_PARAM_Floating] = TRUE;
StimulateParameters[Uon_PARAM_GenGuarded] = FALSE;
StimulateParameters[Uon_PARAM_StimBus] = STIMBUS_U2;
StimulateParameters[Uon_PARAM_PeakVoltage] = 5V;
StimulateParameters[Uon_PARAM_Frequency] = 100Hz;
StimulateParameters[Uon_PARAM_Slope] = 1000Vps;
StimulateParameters[Uon_PARAM_MaxCurrent] = 10mA;
StimulateParameters[Uon_PARAM_Waveform] = WAVEFORM_Triangle;
StimulateParameters[Uon_PARAM_DC_Offset] = 5V;

GenVoltageOnEx(StimulateParameters);
```

## See also

`CreateMeasurementParameterList`, `GenDielectricBreakdownEx`, `GenMeasureResistanceEx`, `GenMeasureVoltageEx`, `GenVoltageOnEx`, `MeasureResistanceEx`, `MeasureRLCEx`, `MeasureVoltageEx`
