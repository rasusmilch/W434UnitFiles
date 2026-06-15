# GenMeasureCurrentEx

## Declaration

```ats
function GenMeasureCurrentEx(I_Parameters: tarray; I_Results: tcreatearray): boolean;
```

## Call pattern

```ats
GenMeasureCurrentEx(I_Parameters, I_Results)
```

## Description

Current measurement with freely selectable parameters.

Parameter and hardware are dependent.

The AC measurement only works with the HVG 5000 and the models HVG 2-x

## Metadata

- Category: Generators
- Code: 270100
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `I_Parameters`: `tarray`
- `I_Results`: `tcreatearray`

## Example

```ats
CreateMeasurementParameterList(MEASUREMENT_Current, I_Parameters);

I_Parameters[I_PARAM_Device] = DEVICE_AutoSelect;
I_Parameters[I_PARAM_Twait] = 10ms;
I_Parameters[I_PARAM_Tmeas] = 20ms;
I_Parameters[I_PARAM_NotchFrequency] = 50Hz;
I_Parameters[I_PARAM_AutorangeMeas] = TRUE;
I_Parameters[I_PARAM_GenGuarded] = FALSE;
I_Parameters[I_PARAM_ProbeToJack] = FALSE;
I_Parameters[I_PARAM_GenToJack] = FALSE;
I_Parameters[I_PARAM_GenToMatrix] = TRUE;
I_Parameters[I_PARAM_Floating] = TRUE;
I_Parameters[I_PARAM_Autosense] = FALSE;
I_Parameters[I_PARAM_LowOutputResistance] = FALSE;
I_Parameters[I_PARAM_HighSenseFloating] = TRUE;
I_Parameters[I_PARAM_LowSenseFloating] = TRUE;
I_Parameters[I_PARAM_WatchdogEnabled] = TRUE;
I_Parameters[I_PARAM_MeasBus] = MEASBUS_Sense;
I_Parameters[I_PARAM_ExpectedCurrent] = 8mA;

Value = GenMeasureCurrentEx(I_Parameters, I_ResultValues);
if (Value)
begin
   Value = FormatCurrent(I_ResultValues[I_RESULT_Value]);
   Value = StrAdd(I_ResultValues[I_RESULT_ValuePrefix], Value);
   Value = StrAdd('Value: ', Value);
   UIWriteNormal(Value);

   PeakValueReal = FormatCurrent(I_ResultValues[I_RESULT_PeakValue_real]);
   PeakValueReal = StrAdd('Peak value real      = ', PeakValueReal);
   UIWriteNormal(PeakValueReal);

   PeakValueImag = FormatCurrent(I_ResultValues[I_RESULT_PeakValue_imag]);
   PeakValueImag = StrAdd('Peak value imaginary = ', PeakValueImag);
   UIWriteNormal(PeakValueImag);

   RMSValueReal = FormatCurrent(I_ResultValues[I_RESULT_RMSValue_real]);
   RMSValueReal = StrAdd('RMS value real       = ', RMSValueReal);
   UIWriteNormal(RMSValueReal);

   RMSValueImag = FormatCurrent(I_ResultValues[I_RESULT_RMSValue_imag]);
   RMSValueImag = StrAdd('RMS value imaginary  = ', RMSValueImag);
   UIWriteNormal(RMSValueImag);

   Frequency = FormatFrequency(I_ResultValues[I_RESULT_Frequency]);
   Frequency = StrAdd(   'Frequency            = ', Frequency);
   UIWriteNormal(Frequency);

end;
```

## See also

`GenMeasureCurrent`, `GenMeasureVoltageEx`, `MeasureCurrentStim`
