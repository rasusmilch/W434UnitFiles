# GenVoltageOnEx

## Declaration

```ats
function GenVoltageOnEx(Uon_Parameters: tarray): integer;
```

## Call pattern

```ats
GenVoltageOnEx(Uon_Parameter);
```

## Description

All options voltage on.
Parameter and hardware are dependent.

If you stimulate on the U2- or U3-bus be aware that there is a 6.25 kOhm-resistor in parallel to the UUT.
In addition a fraction of the current will flow through a voltage monitoring unit.

## Metadata

- Category: Generators
- Code: 270093
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Uon_Parameters`: `tarray`

## Return value

TRUE: voltage OK:

FALSE: voltage insufficient:

Uon_RESULT_ARC

## Example

```ats
CreateGeneratorParameterList(STIMULATE_Voltage,  Parameters);
Parameters[Uon_PARAM_Device] = DEVICE_AutoSelect;
Parameters[Uon_PARAM_Trise] = 0.02;
Parameters[Uon_PARAM_GenToJack] = FALSE;
Parameters[Uon_PARAM_GenToMatrix] = TRUE;
Parameters[Uon_PARAM_Floating] = FALSE;
Parameters[Uon_PARAM_GenGuarded] = FALSE;
Parameters[Uon_PARAM_StimBus] = STIMBUS_Force;
Parameters[Uon_PARAM_PeakVoltage] = 100V;
Parameters[Uon_PARAM_Frequency] = 0Hz;
Parameters[Uon_PARAM_Slope] = 1000Vpms;
Parameters[Uon_PARAM_MaxCurrent] = 10mA;

Result = GenVoltageOnEx(Parameters);
if (Result == TRUE)
begin
   UIInfoDialog('HVG on');
end
else
begin
   if (Result == Uon_RESULT_Arc)
   begin
      UIInfoDialog('HVG ARC');
   end
   else
   begin
      UIInfoDialog('HVG Voltage < 100');
   end;
end;
```

## Example notes

Possible values:

DEVICE_AutoSelect, DEVICE_UI51, DEVICE_UI52, DEVICE_UI53 DEVICE_UI53_U2,
DEVICE_UI53_U3; DEVICE_UI54, DEVICE_UI54_U2, DEVICE_UI54_U3, DEVICE_UI55,
DEVICE_HVG2250, DEVICE_HVG5000, DEVICE_HVG7000

STIMBUS_Force, STIMBUS_U2, STIMBUS_U3

## See also

`CreateGeneratorParameterList`, `GenMeasureResistanceEx`, `GenMeasureVoltageEx`
