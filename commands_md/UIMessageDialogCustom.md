# UIMessageDialogCustom

## Declaration

```ats
function UIMessageDialogCustom(Title: string; MessageText: string; Buttons: tstringarray): integer;
```

## Call pattern

```ats
UIMessageDialogCustom('Title', 'MessageText', [<Buttons>]);
```

## Description

Shows an information popup window with up to five customizeable buttons.

## Metadata

- Category: Userinterface Access
- Code: 263970
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Title`: `string`
- `MessageText`: `string`
- `Buttons`: `tstringarray`

## Return value

The function returns which button was pressed.

Possible values:

DIALOGRESULT_Closed, DIALOGRESULT_Button1, DIALOGRESULT_Button2, DIALOGRESULT_Button3, DIALOGRESULT_Button4, DIALOGRESULT_Button5

## Example

```ats
Button = UIMessageDialogCustom('Custom Buttons', 'Click!', ['Message', 'Dialog', 'Custom']);
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
