# UIMediaDialogCustom

## Declaration

```ats
function UIMediaDialogCustom(Title: string; MessageText: string; Filename: string; Buttons: tstringarray; Repeat: boolean = FALSE): integer;
```

## Call pattern

```ats
UIMediaDialogCustom('Title', 'MessageText', 'Filename', [], TRUE|FALSE);
```

## Description

Shows an media pop-up window with up to five customizeable buttons.

## Metadata

- Category: Userinterface Access
- Code: 263971
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Title`: `string`
- `MessageText`: `string`
- `Filename`: `string` — File picker parameter
- `Buttons`: `tstringarray`
- `Repeat`: `boolean = FALSE` — Allowed values: TRUE, FALSE

## Return value

The function returns which button was pressed.

Possible values:

DIALOGRESULT_Closed, DIALOGRESULT_Button1, DIALOGRESULT_Button2, DIALOGRESULT_Button3, DIALOGRESULT_Button4, DIALOGRESULT_Button5

## Example

```ats
Button = UIMediaDialogCustom('Custom Buttons', 'Click!',
            '.\Images\CEETIS_SplashScreen.jpg',
            ['Message', 'Dialog', 'Custom']);
switch (Button)
begin
   case DIALOGRESULT_Closed: begin
      UIWriteNormal('Closed');
   end;
   case DIALOGRESULT_Button1: begin
      UIWriteNormal('Message');
   end;
   case DIALOGRESULT_Button2: begin
      UIWriteNormal('Dialog');
   end;
   case DIALOGRESULT_Button3: begin
      UIWriteNormal('Custom');
   end;
end;
```

## See also

`UIMediaDialogClose`, `UIMediaDialogOk`, `UIMediaDialogOkCancel`, `UIMediaDialogOpen`, `UIMediaDialogYesNo`, `UIMediaDialogYesNoCancel`
