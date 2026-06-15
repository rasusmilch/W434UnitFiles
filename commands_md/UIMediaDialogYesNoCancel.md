# UIMediaDialogYesNoCancel

## Declaration

```ats
function UIMediaDialogYesNoCancel(Text: string; Filename: string; Repeat: boolean=FALSE): integer;
```

## Call pattern

```ats
UIMediaDialogYesNoCancel('Text', 'Filename', Repeat);
```

## Description

Shows an information pop-up window with the buttons Yes, No and Cancel.

## Metadata

- Category: Userinterface Access
- Code: 263966
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`
- `Filename`: `string` — File picker parameter
- `Repeat`: `boolean=FALSE` — Allowed values: TRUE, FALSE

## Return value

The function returns which button was pressed.

Possible values:

DIALOGRESULT_Yes, DIALOGRESULT_No, DIALOGRESULT_Cancel

## Example

```ats
Button = UIMediaDialogYesNoCancel('Do you like this?', '.\Images\CEETIS_SplashScreen.jpg');
if (Button == DIALOGRESULT_Yes)
begin
   UIWriteNormal('I like it');
end
else
begin
   if (Button == DIALOGRESULT_No)
   begin
      UIWriteNormal('I do not like it');
   end
   else
   begin
      UIWriteNormal('I am not sure');
   end;
end;
```

## See also

`UIMediaDialogClose`, `UIMediaDialogCustom`, `UIMediaDialogOk`, `UIMediaDialogOkCancel`, `UIMediaDialogOpen`, `UIMediaDialogYesNo`
