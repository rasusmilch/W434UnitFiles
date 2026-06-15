# GenMeasureResistanceEx

## Declaration

```ats
function GenMeasureResistanceEx(Parameters: tarray; Results: tcreatearray): boolean;
```

## Call pattern

```ats
GenMeasureResistanceEx(Parameters, Results);
```

## Description

Resistor measurement with freely selectable parameters.

Parameters depend on the test system.
If you measure on the U2- or U3-bus be aware that there is a 6.2 kOhm-resistor in parallel to the object to be measured.
In addition a fraction of the measurment current will flow through a voltage monitoring unit.

Measurments with this function on the U"- and U3-bus are not very accurate.

## Metadata

- Category: Generators
- Code: 270089
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Parameters`: `tarray`
- `Results`: `tcreatearray`

## Example

```ats
PinGroupSetHighLow(["1","2"], ["3","4"]);
CreateMeasurementParameterList(MEASUREMENT_Resistance,Parameters);
Parameters[R_PARAM_Device] = DEVICE_AutoSelect;
Parameters[R_PARAM_Trise] = 10ms;
Parameters[R_PARAM_Twait] = 0ms;
Parameters[R_PARAM_Tmeas] = 20ms;
Parameters[R_PARAM_NotchFrequency] = 50Hz;
Parameters[R_PARAM_AutorangeMeas] = TRUE;
Parameters[R_PARAM_KelvinMode] = FALSE;
Parameters[R_PARAM_GenGuarded] = FALSE;
Parameters[R_PARAM_ProbeToJack] = FALSE;
Parameters[R_PARAM_GenToJack] = FALSE;
Parameters[R_PARAM_GenToMatrix] = TRUE;
Parameters[R_PARAM_Floating] = TRUE;
Parameters[R_PARAM_Autosense] = TRUE;
Parameters[R_PARAM_LowOutputResistance] = FALSE;
Parameters[R_PARAM_HighSenseFloating] = TRUE;
Parameters[R_PARAM_LowSenseFloating] = TRUE;
Parameters[R_PARAM_WatchdogEnabled] = TRUE;
Parameters[R_PARAM_MeasBus] = MEASBUS_Sense;
Parameters[R_PARAM_ExpectedValue] = 1kOhm;
Parameters[R_PARAM_MinVoltage] = 0V;
Parameters[R_PARAM_MaxVoltage] = 40V;
Parameters[R_PARAM_Slope] = 2e6;
Parameters[R_PARAM_MinCurrent] = 0;
Parameters[R_PARAM_MaxCurrent] = 10mA;
Parameters[R_PARAM_MaxPower] = 1W;
Parameters[R_PARAM_AutorangeStim] = FALSE;
Parameters[R_PARAM_DwellTimeBypass] = FALSE;
Valid = GenMeasureResistanceEx(Parameters, ResultValues);
if (Valid)
begin
   ValueOhm = StrAdd('Value    = ',ResultValues[R_RESULT_ValuePrefix]);
   ValueOhm = StrAdd(ValueOhm, FormatResistance(ResultValues[R_RESULT_Value]));
   UIWriteNormal(ValueOhm);
   ValueCurrent = StrAdd('Current  = ',ResultValues[R_RESULT_CurrentPrefix]);
   ValueCurrent = StrAdd(ValueCurrent, FormatCurrent(ResultValues[R_RESULT_Current]));
   UIWriteNormal(ValueCurrent);
   ValueVoltage = StrAdd('Voltage  = ',ResultValues[R_RESULT_VoltagePrefix]);
   ValueVoltage = StrAdd(ValueVoltage, FormatVoltage(ResultValues[R_RESULT_Voltage]));
   UIWriteNormal(ValueVoltage);
end
else
begin
   if (ResultValues[R_RESULT_Arc])
   begin
      UIWriteNormal('ARC');
   end
   else
   begin
      UIWriteNormal('Measurement invalid');
   end;
end;
```

## See also

`CreateMeasurementParameterList`, `GenDielectricBreakdownEx`, `MeasureResistanceEx`
