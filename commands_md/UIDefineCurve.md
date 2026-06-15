# UIDefineCurve

## Declaration

```ats
function UIDefineCurve(Name: string; XData: tarray; YData: tarray; Color: integer = COLOR_Black; XFactor: real = PARAM_UseDefault; YFactor: real = PARAM_UseDefault; Start: integer = PARAM_UseDefault; End: integer = PARAM_UseDefault): void;
```

## Call pattern

```ats
UIDefineCurve('Name', XData, YData, COLOR_?, XFactor, YFactor, Start, End);
```

## Description

The function defines a curve which can be displayed in an image bey using the function UICurvesToImage.

## Metadata

- Category: Userinterface Access
- Code: 263981
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string` — Name of the curve
- `XData`: `tarray` — Values in X direction
- `YData`: `tarray` — Values in Y direction
- `Color`: `integer = COLOR_Black` — Color of the curve in the diagram; Allowed values: COLOR_Black, COLOR_White, COLOR_Red, COLOR_Blue, COLOR_DkGray, COLOR_Gray, COLOR_DkRed, COLOR_Green, COLOR_DkGreen, COLOR_DkBlue, COLOR_Brown, COLOR_DkBrown, COLOR_Yellow, COLOR_Olive, COLOR_Orange, COLOR_Purple, COLOR_Teal, COLOR_Magenta, COLOR_Cyan
- `XFactor`: `real = PARAM_UseDefault` — Factor with which the X values are multilpied before entered into the diagram (e.g. to convert seconds to milliseconds)
- `YFactor`: `real = PARAM_UseDefault` — Factor with which the Y values are multilpied before entered into the diagram (e.g. to convert volts to millivolts)
- `Start`: `integer = PARAM_UseDefault` — Index from which the values are taken from the list and entered into the diagram.
- `End`: `integer = PARAM_UseDefault` — Index up to which the values are taken from the list and entered into the diagram.

## Example

```ats
MeasureVoltageCurve("1", "2", ListTime, ListVoltage, 11V, 0.02s, 0.025ms);
UIDefineCurve('Curve 1-2', ListTime, ListVoltage, COLOR_Red, 1000);

MeasureVoltageCurve("3", "4", ListTime, ListVoltage, 11V, 0.02s, 0.025ms);
UIDefineCurve('Curve 3-4', ListTime, ListVoltage, COLOR_Blue, 1000);

File = 'C:\Images\TwoVoltageCurves.jpg';
UICurvesToImage(File, 'Two Voltage Curves', 't [ms]', 'U [V]', ['Curve 1-2', 'Curve 3-4'], 1024, 768);

UIMediaDialogOk('Two Voltage Curves', File);
```

## See also

`AttenuationFrequencySweep`, `MeasureVoltageCurve`, `UICurvesToImage`, `UICurveToImage`
