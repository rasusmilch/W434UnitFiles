# GenMeasureVoltageEx

## Declaration

```ats
function GenMeasureVoltageEx(U_Parameters: tarray; U_Results: tcreatearray): boolean;
```

## Call pattern

```ats
GenMeasureVoltageEx(U_Parameters,U_Results)
```

## Description

All options voltage  measurement.

The parameters depend on the test system.

If you measure on the U2- or U3-bus be aware that there is a 6.25 kOhm-resistor in parallel to the object to be measured.
In addition a fraction of the measurment current will flow through a voltage monitoring unit.

Measurments with this function on the U2- and U3-bus are not very accurate.

## Metadata

- Category: Generators
- Code: 270091
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `U_Parameters`: `tarray`
- `U_Results`: `tcreatearray`

## Example

```ats
CreateMeasurementParameterList(MEASUREMENT_Voltage,U_Parameters);

U_Parameters[U_PARAM_Device] = DEVICE_AutoSelect;
U_Parameters[U_PARAM_Twait] = 10ms;
U_Parameters[U_PARAM_Tmeas] = 20ms;
U_Parameters[U_PARAM_NotchFrequency] = 50Hz;
U_Parameters[U_PARAM_AutorangeMeas] = TRUE;
U_Parameters[U_PARAM_GenGuarded] = FALSE;
U_Parameters[U_PARAM_ProbeToJack] = FALSE;
U_Parameters[U_PARAM_GenToJack] = FALSE;
U_Parameters[U_PARAM_GenToMatrix] = TRUE;
U_Parameters[U_PARAM_Floating] = TRUE;
U_Parameters[U_PARAM_Autosense] = FALSE;
U_Parameters[U_PARAM_LowOutputResistance] = FALSE;
U_Parameters[U_PARAM_HighSenseFloating] = TRUE;
U_Parameters[U_PARAM_LowSenseFloating] = TRUE;
U_Parameters[U_PARAM_WatchdogEnabled] = TRUE;
U_Parameters[U_PARAM_MeasBus] = MEASBUS_Sense;
U_Parameters[U_PARAM_ExpectedVoltage] = 1000V;
U_Parameters[U_PARAM_ExpectedFrequency] = 0Hz;
U_Parameters[U_PARAM_UmaxAutorange] = 1000V;
U_Parameters[U_PARAM_UminAutorange] = 0;
U_Parameters[U_PARAM_FrequencyAccurancy] = 1000Hz;

Value = GenMeasureVoltageEx(U_Parameters, U_ResultValues);
if (Value)
begin
   ValueACVoltage = StrAdd('AC voltage peak = ',U_ResultValues[U_RESULT_ACVoltagePeakPrefix]);
   ValueACVoltage = StrAdd(ValueACVoltage, FormatVoltage(U_ResultValues[U_RESULT_ACVoltagePeak]));
   UIWriteNormal(ValueACVoltage);
   ValueACVoltage = StrAdd('AC voltage RMS  = ',U_ResultValues[U_RESULT_ACVoltageRMSPrefix]);
   ValueACVoltage = StrAdd(ValueACVoltage, FormatVoltage(U_ResultValues[U_RESULT_ACVoltageRMS]));
   UIWriteNormal(ValueACVoltage);
   ValueACFrequency = StrAdd('AC frequency  = ',U_ResultValues[U_RESULT_ACFrequencyPrefix]);
   ValueACFrequency = StrAdd(ValueACFrequency, U_ResultValues[U_RESULT_ACFrequency]);
   UIWriteNormal(ValueACFrequency);
   ValueDCVoltage = StrAdd('DC voltage    = ',U_ResultValues[U_RESULT_DCVoltagePrefix]);
   ValueDCVoltage = StrAdd(ValueDCVoltage, FormatVoltage(U_ResultValues[U_RESULT_DCVoltage]));
   UIWriteNormal(ValueDCVoltage);
   ValueVoltagePeak = StrAdd('VoltagePeak   = ',U_ResultValues[U_RESULT_VoltagePeakPrefix]);
   ValueVoltagePeak = StrAdd(ValueVoltagePeak, FormatVoltage(U_ResultValues[U_RESULT_VoltagePeak]));
   UIWriteNormal(ValueVoltagePeak);
   ValueVoltageRMS = StrAdd('VoltageRMS    = ',U_ResultValues[U_RESULT_VoltageRMSPrefix]);
   ValueVoltageRMS = StrAdd(ValueVoltageRMS, FormatVoltage(U_ResultValues[U_RESULT_VoltageRMS]));
   UIWriteNormal(ValueVoltageRMS);
end;
```

## See also

`CreateMeasurementParameterList`, `GenMeasureCurrentEx`, `GenMeasureResistancEx`, `MeasureVoltageEx`
