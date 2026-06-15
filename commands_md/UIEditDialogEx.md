# UIEditDialogEx

## Declaration

```ats
function UIEditDialogEx(Title: string; MessageText: string; Buttons: tstringarray; var InputResult: string; FontSizeEdit: integer = PARAM_UseDefault;  FontSizeMessage: integer = PARAM_UseDefault; FontColor: integer = PARAM_UseDefault; BackgroundColor: integer = PARAM_UseDefault; Left: integer = PARAM_UseDefault; Top: integer = PARAM_UseDefault; Width: integer = PARAM_UseDefault; Height: integer = PARAM_UseDefault): integer;
```

## Call pattern

```ats
UIEditDialogEx('Title','MessageText',[],InputResult, <FontSizeEdit>, <FontSizeMessage>, <FontColor>COLOR_?, <BackgroundColor>COLOR_?, <Left>, <Top>, <Width>, <Height>);
```

## Description

Shows an input pop-up window with up to five customizeable buttons.

A default text can be passed in "InputResult".

## Metadata

- Category: Userinterface Access
- Code: 263990
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
- `FontSizeEdit`: `integer = PARAM_UseDefault`
- `FontSizeMessage`: `integer = PARAM_UseDefault`
- `FontColor`: `integer = PARAM_UseDefault` — Allowed values: COLOR_Black, COLOR_White, COLOR_Blue, COLOR_DkGray, COLOR_Gray, COLOR_DkRed, COLOR_Green, COLOR_DkGreen, COLOR_DkBlue, COLOR_Brown, COLOR_DkBrown, COLOR_Yellow, COLOR_Olive, COLOR_Orange, COLOR_Purple, COLOR_Teal, COLOR_Magenta, COLOR_Cyan, COLOR_Automatic
- `BackgroundColor`: `integer = PARAM_UseDefault` — Allowed values: COLOR_Black, COLOR_White, COLOR_Red, COLOR_Blue, COLOR_DkGray, COLOR_Gray, COLOR_DkRed, COLOR_Green, COLOR_DkGreen, COLOR_DkBlue, COLOR_Brown, COLOR_DkBrown, COLOR_Yellow, COLOR_Olive, COLOR_Orange, COLOR_Purple, COLOR_Teal, COLOR_Magenta, COLOR_Cyan, COLOR_Automatic
- `Left`: `integer = PARAM_UseDefault`
- `Top`: `integer = PARAM_UseDefault`
- `Width`: `integer = PARAM_UseDefault`
- `Height`: `integer = PARAM_UseDefault`

## Return value

The function returns which button was pressed.

Possible values:

DIALOGRESULT_Button1, DIALOGRESULT_Button2, DIALOGRESULT_Button3, DIALOGRESULT_Button4, DIALOGRESULT_Button5

The entered value is returned in "InputResult".

## Example

```ats
InputResult = 'DefaultText';
Button = UIEditDialogEx('Title','MessageText',['Message', 'Dialog', 'Custom'], InputResult, 20, 30, COLOR_Automatic, COLOR_Automatic, 20, 50, 800, 300);
switch (Button)
begin
   case DIALOGRESULT_Button1: begin
      UIWriteNormal('Message');
   end;
   case DIALOGRESULT_Button2: begin
      UIWriteNormal('Dialog');
   end;
   case DIALOGRESULT_Button3: begin
      UIWriteNormal('Ok');
   end;
end;
```

## See also

`UIEditDialog`, `UIEditDialogCustom`
