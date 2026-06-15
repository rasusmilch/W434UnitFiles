# UICurvesToImage

## Declaration

```ats
function UICurvesToImage(Filename: string; Title: string; XAxis: string; YAxis: string; Curves: tstringarray; Width: integer = PARAM_UseDefault; Height: integer = PARAM_UseDefault): boolean;
```

## Call pattern

```ats
UICurvesToImage('Filename.jpg', 'Title', 'XAxis', 'YAxis', ['Curve1', 'Curve2', ...], Width, Height);
```

## Description

The function creates an image file with a diagram.
The curves that shall be displayed in teh diagram must be defined with UIDefineCurve before.

## Metadata

- Category: Userinterface Access
- Code: 263982
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — Name of the output file. Bitmap (*.bmp) and JPEG (*.jpg) files are possible.
- `Title`: `string` — Title of the diagram
- `XAxis`: `string` — Label of the X axis
- `YAxis`: `string` — Label of the Y axis
- `Curves`: `tstringarray` — List of the curves to be displayed.
- `Width`: `integer = PARAM_UseDefault` — Width of the image in pixels
- `Height`: `integer = PARAM_UseDefault` — Height of the image in pixels

## Return value

The function returns TRUE if the image could be created, otherwise FALSE.

## Example

```ats
MeasureVoltageCurve("1", "2", ListTime, ListVoltage, 11V, 0.02s, 0.025ms);
UIDefineCurve('Curve 1-2', ListTime, ListVoltage, COLOR_Red, 1000);

MeasureVoltageCurve("3", "4", ListTime, ListVoltage, 11V, 0.02s, 0.025ms);
UIDefineCurve('Curve 3-4', ListTime, ListVoltage, COLOR_Blue, 1000);

File = 'C:\Images\TwoVoltageCurves.jpg';
UICurvesToImage(File, 'Two Voltage Curves', 't [ms]', 'U [V]', ['Curve 1-2', 'Curve 3-4'], 1024, 768);

UIMediaDialogOk('Two Voltage Curves', File);

File = 'C:\Images\Sweep.jpg';
UICurvesToImage(File, 'Sweeps', 'f [Hz]', 'A [dB]', ['Curve 1-4', 'Curve5-8'], 1024, 768);

UIMediaDialogOk('Sweeps', File);
```

## See also

`AttenuationFrequencySweep`, `MeasureVoltageCurve`, `UICurveToImage`, `UIDefineCurve`
