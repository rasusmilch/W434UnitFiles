# UIMediaDialogOkCancel

## Declaration

```ats
function UIMediaDialogOkCancel(Text: string; Filename: string; Repeat: boolean=FALSE): integer;
```

## Call pattern

```ats
UIMediaDialogOkCancel('Text', 'Filename', Repeat);
```

## Description

Shows an media pop-up window with the buttons OK and Cancel.

## Metadata

- Category: Userinterface Access
- Code: 263964
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

DIALOGRESULT_Ok, DIALOGRESULT_Cancel

## Example

```ats
Button = UIMediaDialogOkCancel('Is this ok with you?', '.\Images\CEETIS_SplashScreen.jpg');
if (Button == DIALOGRESULT_Ok)
begin
   UIWriteNormal('It is ok');
end
else
begin
   UIWriteNormal('It is not ok');
end;
```

## See also

`UIMediaDialogClose`, `UIMediaDialogCustom`, `UIMediaDialogOk`, `UIMediaDialogOpen`, `UIMediaDialogYesNo`, `UIMediaDialogYesNoCancel`
