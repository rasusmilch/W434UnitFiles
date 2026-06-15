# MeasureRLCEx

## Declaration

```ats
function MeasureRLCEx(Pin1: tpin; Pin2: tpin; Parameters: tarray; Results: tcreatearray): boolean;
```

## Call pattern

```ats
MeasureRLCEx("Pin1","Pin2", Parameters, Results);
```

## Description

Measures the RLC combination between the passed pins.

The function does not refer to the net list.

## Metadata

- Category: Electrical testing
- Code: 268040
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
CreateMeasurementParameterList(MEASUREMENT_RLC, Parameters);
Parameters[RLC_PARAM_Device] = DEVICE_AutoSelect;
Parameters[RLC_PARAM_Twait] = 10ms;
Parameters[RLC_PARAM_Tmeas] = 20ms;
Parameters[RLC_PARAM_NotchFrequency] = 50Hz;
Parameters[RLC_PARAM_WatchdogEnabled] = TRUE;
Parameters[RLC_PARAM_Frequency] = 1kHz;
Parameters[RLC_PARAM_MaxVoltage] = 2V;
Parameters[RLC_PARAM_MaxCurrent] = 10mA;
Parameters[RLC_PARAM_Bias] = FALSE;
Parameters[RLC_PARAM_CCompensation] = 0F;

MeasureRLCEx("1", "2", Parameters, ResultValues);

UIWriteNormal('--- Impedance ---');
UIWriteNormal(StrAdd('Zabs = ',
                StrAdd(ResultValues[RLC_ZPrefix],
                   FormatResistance(ResultValues[RLC_Zabs]))));
UIWriteNormal(StrAdd('Zr   = ',
                 StrAdd(ResultValues[RLC_ZPrefix],
                    FormatResistance(ResultValues[RLC_Zr]))));
UIWriteNormal(StrAdd('Zi   = ',
                 StrAdd(ResultValues[RLC_ZPrefix],
                    FormatResistance(ResultValues[RLC_Zi]))));

UIWriteNormal('--- Admittance ---');
UIWriteNormal(StrAdd('Yabs = ',
                 StrAdd(ResultValues[RLC_YPrefix],
                    FormatConductance(ResultValues[RLC_Yabs]))));
UIWriteNormal(StrAdd('Yr   = ',
                 StrAdd(ResultValues[RLC_YPrefix],
                    FormatConductance(ResultValues[RLC_Yr]))));
UIWriteNormal(StrAdd('Yi   = ',
                 StrAdd(ResultValues[RLC_YPrefix],
                    FormatConductance(ResultValues[RLC_Yi]))));

UIWriteNormal('--- Serial RLC ---');
UIWriteNormal(StrAdd('Rser = ',
                 StrAdd(ResultValues[RLC_RserPrefix],
                    FormatResistance(ResultValues[RLC_Rser]))));
UIWriteNormal(StrAdd('Lser = ',
                 StrAdd(ResultValues[RLC_LserPrefix],
                    FormatInductance(ResultValues[RLC_Lser]))));
UIWriteNormal(StrAdd('Cser = ',
                 StrAdd(ResultValues[RLC_CserPrefix],
                    FormatCapacitance(ResultValues[RLC_Cser]))));

UIWriteNormal('--- Parallel RLC ---');
UIWriteNormal(StrAdd('Rpar = ',
                 StrAdd(ResultValues[RLC_RparPrefix],
                    FormatResistance(ResultValues[RLC_Rpar]))));
UIWriteNormal(StrAdd('Lpar = ',
                 StrAdd(ResultValues[RLC_LparPrefix],
                    FormatInductance(ResultValues[RLC_Lpar]))));
UIWriteNormal(StrAdd('Cpar = ',
                 StrAdd(ResultValues[RLC_CparPrefix],
                    FormatCapacitance(ResultValues[RLC_Cpar]))));

UIWriteNormal('--- Miscellaneous ---');
UIWriteNormal(StrAdd('Phase       = ',
                 StrAdd(ArithRound(ResultValues[RLC_Phase], 2), '�')));
UIWriteNormal(StrAdd('Quality     = ',
                 ArithRound(ResultValues[RLC_Quality], 2)));
UIWriteNormal(StrAdd('Dissipation = ',
                 ArithRound(ResultValues[RLC_TanDelta], 2)));
UIWriteNormal(StrAdd('fmeas       = ',
                 FormatFrequency(ResultValues[RLC_Fmeas])));
```

## See also

`CreateMeasurementParameterList`, `MeasureResistanceEx`, `MeasureRLC`, `MeasureRLCCustom`, `MeasureVoltageEx`
