# UIMediaDialogYesNo

## Declaration

```ats
function UIMediaDialogYesNo(Text: string; Filename: string; Repeat: boolean=FALSE): integer;
```

## Call pattern

```ats
UIMediaDialogYesNo('Text', 'Filename', Repeat);
```

## Description

Shows an media pop-up window with the buttons Yes and No.

## Metadata

- Category: Userinterface Access
- Code: 263965
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

DIALOGRESULT_Yes, DIALOGRESULT_No

## Example

```ats
Button = UIMediaDialogYesNo('Do you like this?', '.\Images\CEETIS_SplashScreen.jpg');
if (Button == DIALOGRESULT_Yes)
begin
   UIWriteNormal('I like it');
end
else
begin
   UIWriteNormal('I do not like it');
end;
```

## See also

`UIMediaDialogClose`, `UIMediaDialogCustom`, `UIMediaDialogOk`, `UIMediaDialogOkCancel`, `UIMediaDialogOpen`, `UIMediaDialogYesNoCancel`
