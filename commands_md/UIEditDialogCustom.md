# UIEditDialogCustom

## Declaration

```ats
function UIEditDialogCustom(Title: string; MessageText: string; Buttons: tstringarray; var InputResult: string): integer;
```

## Call pattern

```ats
UIEditDialogCustom('Title', 'MessageText', [], InputResult);
```

## Description

Shows an input pop-up window with up to five customizeable buttons.

A default text can be passed in "InputResult".

## Metadata

- Category: Userinterface Access
- Code: 263972
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Title`: `string`
- `MessageText`: `string`
- `Buttons`: `tstringarray`
- `var InputResult`: `string`

## Return value

The function returns which button was pressed.

Possible values:

DIALOGRESULT_Button1, DIALOGRESULT_Button2, DIALOGRESULT_Button3, DIALOGRESULT_Button4, DIALOGRESULT_Button5

The entered value is returned in "InputResult".

## Example

```ats
InputResult = 'DefaultText';
Button = UIEditDialogCustom('Custom Buttons', 'Click!',
            ['Message', 'Dialog', 'Custom'], InputResult);
UIWriteNormal(StrAdd('Input: ', InputResult));
switch (Button)
begin
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

`UIEditDialog`
