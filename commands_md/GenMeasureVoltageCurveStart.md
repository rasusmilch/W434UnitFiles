# GenMeasureVoltageCurveStart

## Declaration

```ats
function GenMeasureVoltageCurveStart(MeasurementBus: integer; MaxVoltage: tvoltage; Tmeas: ttime; Ttrigger: ttime): void;
```

## Call pattern

```ats
GenMeasureVoltageCurveStart(MEASBUS_?, <MaxVoltage>V, <Tmeas>s, <Ttrigger>s);
```

## Description

This function starts a time triggered voltage measurement.

W454 and W444: Maximum 32767 measurements

W434: Maximum 8191 measurements

## Metadata

- Category: Electrical testing
- Code: 270095
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `MeasurementBus`: `integer` — Bus at which shall be measured; Allowed values: MEASBUS_Sense, MEASBUS_U2, MEASBUS_U3
- `MaxVoltage`: `tvoltage` — Maximum expected voltage
- `Tmeas`: `ttime` — Total measurement time
- `Ttrigger`: `ttime` — Time interval for the single measurements.

## Example

```ats
PowerUPinSetTPHigh(EXTIO_U2, "1");
PowerUPinSetTPLow(EXTIO_U2, "2");
ParamExternalVoltageCheck(OFF);

PinSetHighLow("1", "2");

GenMeasureVoltageCurveStart(MEASBUS_Sense, 28V, 60ms, 0.1ms);

GenCurrentOn(STIMBUS_U2, 3A, 28V);
GenCurrentOff(STIMBUS_U2);

Count = GenMeasureVoltageCurveStop(TimeList, VoltageList);

UIWriteNormal(Count);
File = '.\Temp\Curve.jpg';
Width = 1024;
Height = 768;
UICurveToImage(File, 'Curve', 't [ms]', 'U [V]', TimeList, VoltageList, Width, Height, 1000);
UIMediaDialogOk('Curve', File, FALSE);
```

## See also

`GenMeasureVoltageCurveStop`, `MeasureVoltageCurve`
