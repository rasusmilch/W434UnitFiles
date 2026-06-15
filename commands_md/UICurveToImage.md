# UICurveToImage

## Declaration

```ats
function UICurveToImage(Filename: string; Title: string; XAxis: string; YAxis: string; XData: tarray; YData: tarray; Width: integer = PARAM_UseDefault; Height: integer = PARAM_UseDefault; XFactor: real = PARAM_UseDefault; YFactor: real = PARAM_UseDefault; Start: integer = PARAM_UseDefault; End: integer = PARAM_UseDefault): boolean;
```

## Call pattern

```ats
UICurveToImage('Filename', 'Title', 'X axis', 'Y axis', XData, YData);
```

## Description

Creates a file with the image of a graph.

## Metadata

- Category: Userinterface Access
- Code: 263979
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
- `XData`: `tarray` — X values
- `YData`: `tarray` — Y values
- `Width`: `integer = PARAM_UseDefault` — Width of the image in pixels
- `Height`: `integer = PARAM_UseDefault` — Height of the image in pixels
- `XFactor`: `real = PARAM_UseDefault` — Factor with which the X values are multilpied before entered into the diagram (e.g. to convert seconds to milliseconds)
- `YFactor`: `real = PARAM_UseDefault` — Factor with which the Y values are multilpied before entered into the diagram (e.g. to convert volts to millivolts)
- `Start`: `integer = PARAM_UseDefault` — Index from which the values are taken from the list and entered into the diagram.
- `End`: `integer = PARAM_UseDefault` — Index up to which the values are taken from the list and entered into the diagram.

## Return value

The function returns TRUE if the image could be created, otherwise FALSE.

## Example

```ats
File = 'C:\Images\CurveImage1.jpg';
Count = MeasureVoltageCurve("1", "2", ListTime, ListVoltage, 11V, 40ms, 0.05ms);
if (Count > 0)
begin
   UICurveToImage(File, 'My diagram', 't [ms]', 'U [V]',
      ListTime, ListVoltage, 1024, 768, 1000);
   UIMediaDialogOk('It worked!', File, FALSE);
end
else
begin
   UIWriteWarning('No data');
end;
```

## See also

`AttenuationFrequencySweep`, `MeasureVoltageCurve`, `UICurvesToImage`, `UIDefineCurve`
