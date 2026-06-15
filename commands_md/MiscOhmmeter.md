# MiscOhmmeter

## Declaration

```ats
function MiscOhmmeter(Name: string; Pin1: tpin; Pin2: tpin; var IsMinMaxValid: boolean; var MinValue: real; var MaxValue: real; var IsLastValueValid: boolean; var LastValue: real; Text: string = ''; IsPinChangeAllowed: boolean = FALSE; IsStartStopAllowed: boolean = FALSE): integer;
```

## Call pattern

```ats
MiscOhmmeter('Name', "Pin1", "Pin2", IsMinMaxValid, MinValue, MaxValue, IsLastValueValid, LastValue, 'Text', TRUE|FALSE, TRUE|FALSE);
```

## Description

Shows a window with an ohmmeter which measures the resistance between the two specified pins.

The measurement parameters are: Voltage: 0-40V; Current; 0 -200mA; Maximum power: 0,5W; Trise=100ms; Twait=0ms; Tmeas=100ms
The measurement is repeted approximately every 50 ms

## Metadata

- Category: Miscellaneous
- Code: 266529
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `var IsMinMaxValid`: `boolean` — Returns TRUE if minimum and maximum values are valid, otherwise FALSE
- `var MinValue`: `real` — Returns the lowest measured valuue in Ohms
- `var MaxValue`: `real` — Returns the highest measured valuue in Ohms
- `var IsLastValueValid`: `boolean` — Returns TRUE if the last value is valid, otherwise FALSE
- `var LastValue`: `real` — Returns the last measured valuue in Ohms
- `Text`: `string = ''` — Custom text, which will be displayed in the window
- `IsPinChangeAllowed`: `boolean = FALSE` — Pins can be changed during the test if TRUE is passed
- `IsStartStopAllowed`: `boolean = FALSE` — Measurement can be stopped during the test if TRUE is passed.

## Return value

DIALOGRESULT_Ok
DIALOGRESULT_Cancel

## Example

```ats
IsMinMaxValid = FALSE;
MinValue = 0;
MaxValue = 0;
IsLastValueValid = FALSE;
LastValue = 0;
Text = 'Turn the potentiometer first to the very left, then to the very right and set it to the average value at the end.';
DlgResult = MiscOhmmeter('R1', "Pin61", "Pin62", IsMinMaxValid, MinValue, MaxValue, IsLastValueValid, LastValue, Text, TRUE, FALSE);
if (DlgResult == DIALOGRESULT_Cancel)
begin
   MiscAbortTest();
end
else
begin
   if (IsMinMaxValid)
   begin
      UIWriteNormal(StrAdd('Minimum: ', FormatResistance(MinValue)));
      UIWriteNormal(StrAdd('Maximum: ', FormatResistance(MaxValue)));
   end;
   if (IsLastValueValid)
   begin
      Tol = LastValue * 0.1;
      UIWriteNormal(StrAdd('Last value: ', FormatResistance(LastValue)));
      NWSetResistorValues('R1', "Pin61", "Pin62", LastValue, Tol, Tol);
      ResistorTest('R1', "Pin61", "Pin62");
   end
   else
   begin
      UIWriteError(StrAdd('R1', ': Invalid value'));
      ReportWriteError(StrAdd('R1', ': Invalid value'));
      FailCounterCount(FAILCOUNTER_ElectricalComponents);
   end;
end;
```

## See also

`MeasureResistance`, `MeasureResistanceCustom`, `ResistorTest`, `ResistorTestCustom`
