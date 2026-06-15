# UIMessageDialogCustomEx

## Declaration

```ats
function UIMessageDialogCustomEx(Title: string; MessageText: string; Buttons: tstringarray; FontSize: integer = PARAM_UseDefault; FontBold: boolean = FALSE; FontColor: integer = PARAM_UseDefault; BackgroundColor: integer = PARAM_UseDefault; Left: integer = PARAM_UseDefault; Top: integer = PARAM_UseDefault; Width: integer = PARAM_UseDefault; Height: integer = PARAM_UseDefault): integer;
```

## Call pattern

```ats
UIMessageDialogCustomEx('Title', 'MessageText', [<Buttons>], <FontSize>, <FontBold>TRUE|FALSE, <FontColor>COLOR_?, <BackgroundColor>COLOR_?, <Left>, <Top>, <Width>, <Height>);
```

## Description

Shows an information popup window with up to five customizeable buttons.

Fontsize, colors, position and size of the window can be customized.

## Metadata

- Category: Userinterface Access
- Code: 263988
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Title`: `string`
- `MessageText`: `string`
- `Buttons`: `tstringarray`
- `FontSize`: `integer = PARAM_UseDefault`
- `FontBold`: `boolean = FALSE` — Allowed values: TRUE, FALSE
- `FontColor`: `integer = PARAM_UseDefault` — Allowed values: COLOR_Black, COLOR_White, COLOR_Red, COLOR_Blue, COLOR_DkGray, COLOR_Gray, COLOR_DkRed, COLOR_Green, COLOR_DkGreen, COLOR_DkBlue, COLOR_Brown, COLOR_DkBrown, COLOR_Yellow, COLOR_Olive, COLOR_Orange, COLOR_Purple, COLOR_Teal, COLOR_Magenta, COLOR_Cyan, COLOR_Automatic
- `BackgroundColor`: `integer = PARAM_UseDefault` — Allowed values: COLOR_Black, COLOR_White, COLOR_Red, COLOR_Blue, COLOR_DkGray, COLOR_Gray, COLOR_DkRed, COLOR_Green, COLOR_DkGreen, COLOR_DkBlue, COLOR_Brown, COLOR_DkBrown, COLOR_Yellow, COLOR_Olive, COLOR_Orange, COLOR_Purple, COLOR_Teal, COLOR_Magenta, COLOR_Cyan, COLOR_Automatic
- `Left`: `integer = PARAM_UseDefault`
- `Top`: `integer = PARAM_UseDefault`
- `Width`: `integer = PARAM_UseDefault`
- `Height`: `integer = PARAM_UseDefault`

## Return value

The function returns which button was pressed.

Possible values:

DIALOGRESULT_Closed, DIALOGRESULT_Button1, DIALOGRESULT_Button2, DIALOGRESULT_Button3, DIALOGRESULT_Button4, DIALOGRESULT_Button5

## Example

```ats
Button = UIMessageDialogCustomEx('Custom Buttons', 'Click a button!',
            ['Message', 'Dialog', 'Custom'],
            104, TRUE, COLOR_DkBlue, COLOR_White, 40, 40, 1000, 400);
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

`UIMessageDialogCustom`, `UIMessageDialogOkCancelEx`, `UIMessageDialogYesNoCancelEx`, `UIMessageDialogYesNoEx`
