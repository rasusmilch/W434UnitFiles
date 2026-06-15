# UIMessageDialogYesNoCancelEx

## Declaration

```ats
function UIMessageDialogYesNoCancelEx(Text: string; FontSize: integer = PARAM_UseDefault; FontBold: boolean = FALSE; FontColor: integer = PARAM_UseDefault; BackgroundColor: integer = PARAM_UseDefault; Left: integer = PARAM_UseDefault; Top: integer = PARAM_UseDefault; Width: integer = PARAM_UseDefault; Height: integer = PARAM_UseDefault): integer;
```

## Call pattern

```ats
UIMessageDialogYesNoCancelEx('Text', <FontSize>, <FontBold>TRUE|FALSE, <FontColor>COLOR_?, <BackgroundColor>COLOR_?, <Left>, <Top>, <Width>, <Height>);
```

## Description

Shows an information pop-up window with the buttons Yes, No and Cancel.

Fontsize, colors, position and size of the window can be customized.

## Metadata

- Category: Userinterface Access
- Code: 263987
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`
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

DIALOGRESULT_Yes, DIALOGRESULT_No, DIALOGRESULT_Cancel

## Example

```ats
Button = UIMessageDialogYesNoCancelEx('Do you like this?',
            72, TRUE, COLOR_DkBlue, COLOR_White, 40, 40, 1000, 400);
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

`UIMessageDialogCustomEx`, `UIMessageDialogOkCancelEx`, `UIMessageDialogYesNoCancel`, `UIMessageDialogYesNoEx`
