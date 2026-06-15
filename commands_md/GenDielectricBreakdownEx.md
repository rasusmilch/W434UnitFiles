# GenDielectricBreakdownEx

## Declaration

```ats
function GenDielectricBreakdownEx(DB_Parameters: tarray; DB_Results: tcreatearray): boolean;
```

## Call pattern

```ats
GenDielectricBreakdownEx(DB_Parameters, DB_Results);
```

## Description

 All options dielectric breakdown  measurement.

Parameter and hardware are dependent.

## Metadata

- Category: Generators
- Code: 270090
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `DB_Parameters`: `tarray`
- `DB_Results`: `tcreatearray`

## Example

```ats
PinGroupSetHighLow(["1","2"], ["3","4"]);
CreateMeasurementParameterList(MEASUREMENT_DB,DB_Parameters);
DB_Parameters[DB_PARAM_Device] = DEVICE_AutoSelect;
DB_Parameters[DB_PARAM_Trise] = 100ms;
DB_Parameters[DB_PARAM_Twait] = 100ms;
DB_Parameters[DB_PARAM_Tmeas] = 100ms;
DB_Parameters[DB_PARAM_NotchFrequency] = 50Hz;
DB_Parameters[DB_PARAM_AutorangeMeas] = TRUE;
DB_Parameters[DB_PARAM_KelvinMode] = FALSE;
DB_Parameters[DB_PARAM_ProbeToJack] = FALSE;
DB_Parameters[DB_PARAM_GenToJack] = FALSE;
DB_Parameters[DB_PARAM_GenToMatrix] = TRUE;
DB_Parameters[DB_PARAM_Floating] = TRUE;
DB_Parameters[DB_PARAM_Voltage_RMS] = 500V;
DB_Parameters[DB_PARAM_Frequency] = 50Hz;
DB_Parameters[DB_PARAM_Slope] = 1e6;
DB_Parameters[DB_PARAM_Max_Current_RMS] = 17mA;
DB_Parameters[DB_PARAM_Expected_Ireal_RMS] = 1mA;
DB_Parameters[DB_PARAM_Expected_Iimag_RMS] = 5mA;
Valid = GenDielectricBreakdownEx(DB_Parameters, DB_ResultValues);
if (Valid)
begin
   IrealPeak = StrAdd('Ireal_peak = ',DB_ResultValues[DB_RESULT_ValuePrefix]);
   IrealPeak = StrAdd(IrealPeak, FormatCurrent(DB_ResultValues[DB_RESULT_Ireal_peak]));
   UIWriteNormal(IrealPeak);
   IimagPeak = StrAdd('Iimag_peak = ',DB_ResultValues[DB_RESULT_ValuePrefix]);
   IimagPeak = StrAdd(IimagPeak, FormatCurrent(DB_ResultValues[DB_RESULT_Iimag_peak]));
   UIWriteNormal(IimagPeak);
   IrealRMS = StrAdd('Ireal_RMS = ',DB_ResultValues[DB_RESULT_ValuePrefix]);
   IrealRMS = StrAdd(IrealRMS, FormatCurrent(DB_ResultValues[DB_RESULT_Ireal_RMS]));
   UIWriteNormal(IrealRMS);
   IimagRMS = StrAdd('Iimag_RMS = ',DB_ResultValues[DB_RESULT_ValuePrefix]);
   IimagRMS = StrAdd(IimagRMS, FormatCurrent(DB_ResultValues[DB_RESULT_Iimag_RMS]));
   UIWriteNormal(IimagRMS);
end
else
begin
   if (DB_ResultValues[DB_RESULT_Arc])
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

`CreateMeasurementParameterList`, `GenMeasureResistanceEx`
