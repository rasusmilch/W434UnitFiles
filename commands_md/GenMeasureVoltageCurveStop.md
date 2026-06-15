# GenMeasureVoltageCurveStop

## Declaration

```ats
function GenMeasureVoltageCurveStop(TimeList: tcreatearray; VoltageList: tcreatearray): integer;
```

## Call pattern

```ats
GenMeasureVoltageCurveStop(TimeList, VoltageList);
```

## Description

This function terminates a measurement wich was started with GenMeasureVoltageCurveStart and returns the measured values.

## Metadata

- Category: Electrical testing
- Code: 270096
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `TimeList`: `tcreatearray` — Contains the time stamps of the single measurements.
- `VoltageList`: `tcreatearray` — Contains the measured voltage values in volts.

## Return value

The return value of the function is the number of measured values.

A return value of 0 means that an error (e.g. range overflow) occurred during the measurement.

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
if (Count > 0)
begin
   File = '.\Temp\Curve.jpg';
   Width = 1024;
   Height = 768;
   UICurveToImage(File, 'Curve', 't [ms]', 'U [V]', TimeList, VoltageList, Width, Height, 1000);
   UIMediaDialogOk('Curve', File, FALSE);
end
else
begin
   UIWriteNormal('Measurement invalid');
end;
```

## See also

`GenMeasureVoltageCurveStart`, `MeasureVoltageCurve`
