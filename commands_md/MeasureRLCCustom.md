# MeasureRLCCustom

## Declaration

```ats
function MeasureRLCCustom(Name: string; Pin1: tpin; Pin2: tpin; Values: tcreatearray; Trise: ttime=PARAM_UseDefault; Twait: ttime=PARAM_UseDefault; Tmeas: ttime=PARAM_UseDefault; Bias: boolean=PARAM_UseDefault): boolean; tests rlccombinations;
```

## Call pattern

```ats
MeasureRLCCustom('Name', "Pin1", "Pin2", ResultValues, <Trise>s, <Twait>s, <Tmeas>s, <Bias>);
```

## Description

Measures a RLC combination between Pin1 and Pin2 with custom parameters. Creates a list "Values" and fills it with the measured values.

The function always refers to a RLC combination in the netlist.

## Metadata

- Category: Electrical testing
- Code: 779
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Values`: `tcreatearray`
- `Trise`: `ttime=PARAM_UseDefault`
- `Twait`: `ttime=PARAM_UseDefault`
- `Tmeas`: `ttime=PARAM_UseDefault`
- `Bias`: `boolean=PARAM_UseDefault`

## Return value

The function returns TRUE if the measurement was successful, otherwise FALSE.
The result list contains the following values:

Values[RLC_Zr]: Real value of the impedance in Ohm

Values[RLC_Zi]: Imaginary value of the impedance in Ohm

Values[RLC_ZPrefix]: Prefix of the impedance value

Values[RLC_Yr]: Real value of the conductance in Siemens

Values[RLC_Yi]: Imaginary value of the conductance in Siemens

Values[RLC_YPrefix]: Prefix value of the conductance value

Values[RLC_Zabs]: Impedance absolute value in Ohm

Values[RLC_Yabs]: Conductance absolute value in Siemens

Values[RLC_Phase]: Phase value between U and I in degree

Values[RLC_Quality]: Quality factor

Values[RLC_TanDelta]: Dissipation factor

Values[RLC_Fmeas]: Accurate frequency in Hertz

Values[RLC_Rser]: Serial resistance value in Ohm

Values[RLC_RserPrefix]: Prefix of the serial resistance value

Values[RLC_Lser]: Serial inductance value in Henry

Values[RLC_LserPrefix]: Prefix of the serial inductance value

Values[RLC_Cser]: Serial capacitance value in Farad

Values[RLC_CserPrefix]: Prefix of the serial capacitance value

Values[RLC_Rpar]: Parallel resistance value in Ohm

Values[RLC_RparPrefix]: Prefix of the parallel resistance value

Values[RLC_Lpar]: Parallel inductance value in Henry

Values[RLC_LparPrefix]: Prefix of the parallel inductance value

Values[RLC_Cpar]: Parallel capacitance value in Farad

Values[RLC_CparPrefix]: Prefix of the parallel capacitance value


## Example

```ats
MeasureRLCCustom('Name', "Pin1", "Pin2", ResultValues, PARAM_UseDefault, 10ms);

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

## Example notes

Measures a RLC combination between Pin1 and Pin2 and writes the values on the screen.

The wait time is customized.
For the other parameters the default values will be used.

## See also

`MeasureResistanceEx`, `MeasureRLC`, `MeasureRLCEx`, `MeasureVoltageEx`
