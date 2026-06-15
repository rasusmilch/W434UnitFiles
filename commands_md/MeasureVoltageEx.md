# MeasureVoltageEx

## Declaration

```ats
function MeasureVoltageEx(Pin1: tpin; Pin2: tpin; Parameters: tarray; Results: tcreatearray): boolean;
```

## Call pattern

```ats
MeasureVoltageEx("Pin1","Pin2", Parameters, Results);
```

## Description

Measures the voltage between the passed pins. Valid are DC voltages and voltages with a sine waveform.

## Metadata

- Category: Electrical testing
- Code: 268041
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Parameters`: `tarray`
- `Results`: `tcreatearray`

## Example

```ats
CreateMeasurementParameterList(MEASUREMENT_Voltage,Parameters);

Parameters[U_PARAM_Device] = DEVICE_AutoSelect;
Parameters[U_PARAM_Twait] = 10ms;
Parameters[U_PARAM_Tmeas] = 20ms;
Parameters[U_PARAM_NotchFrequency] = 50Hz;
Parameters[U_PARAM_AutorangeMeas] = TRUE;
Parameters[U_PARAM_GenGuarded] = FALSE;
Parameters[U_PARAM_ProbeToJack] = FALSE;
Parameters[U_PARAM_GenToJack] = FALSE;
Parameters[U_PARAM_GenToMatrix] = TRUE;
Parameters[U_PARAM_Floating] = TRUE;
Parameters[U_PARAM_Autosense] = FALSE;
Parameters[U_PARAM_LowOutputResistance] = FALSE;
Parameters[U_PARAM_HighSenseFloating] = TRUE;
Parameters[U_PARAM_LowSenseFloating] = TRUE;
Parameters[U_PARAM_WatchdogEnabled] = TRUE;
Parameters[U_PARAM_MeasBus] = MEASBUS_Sense;
Parameters[U_PARAM_ExpectedVoltage] = 1000V;
Parameters[U_PARAM_ExpectedFrequency] = 0Hz;
Parameters[U_PARAM_UmaxAutorange] = 1000V;
Parameters[U_PARAM_UminAutorange] = 0;
Parameters[U_PARAM_FrequencyAccurancy] = 1000Hz;

Value = MeasureVoltageEx("1","3", Parameters, ResultValues);
if (Value)
begin
   ValueACVoltage = StrAdd('AC voltage peak = ',ResultValues[U_RESULT_ACVoltagePeakPrefix]);
   ValueACVoltage = StrAdd(ValueACVoltage, FormatVoltage(ResultValues[U_RESULT_ACVoltagePeak]));
   UIWriteNormal(ValueACVoltage);
   ValueACVoltage = StrAdd('AC voltage RMS  = ',ResultValues[U_RESULT_ACVoltageRMSPrefix]);
   ValueACVoltage = StrAdd(ValueACVoltage, FormatVoltage(ResultValues[U_RESULT_ACVoltageRMS]));
   UIWriteNormal(ValueACVoltage);
   ValueACFrequency = StrAdd('AC frequency   = ',ResultValues[U_RESULT_ACFrequencyPrefix]);
   ValueACFrequency = StrAdd(ValueACFrequency, ResultValues[U_RESULT_ACFrequency]);
   UIWriteNormal(ValueACFrequency);
   ValueDCVoltage = StrAdd('DC voltage    = ',ResultValues[U_RESULT_DCVoltagePrefix]);
   ValueDCVoltage = StrAdd(ValueDCVoltage, FormatVoltage(ResultValues[U_RESULT_DCVoltage]));
   UIWriteNormal(ValueDCVoltage);
   ValueVoltagePeak = StrAdd('VoltagePeak   = ',ResultValues[U_RESULT_VoltagePeakPrefix]);
   ValueVoltagePeak = StrAdd(ValueVoltagePeak, FormatVoltage(ResultValues[U_RESULT_VoltagePeak]));
   UIWriteNormal(ValueVoltagePeak);
   ValueVoltageRMS = StrAdd('VoltageRMS    = ',ResultValues[U_RESULT_VoltageRMSPrefix]);
   ValueVoltageRMS = StrAdd(ValueVoltageRMS, FormatVoltage(ResultValues[U_RESULT_VoltageRMS]));
   UIWriteNormal(ValueVoltageRMS);
end;
```

## See also

`CreateMeasurementParameterList`, `MeasureResistanceEx`, `MeasureRLCEx`
