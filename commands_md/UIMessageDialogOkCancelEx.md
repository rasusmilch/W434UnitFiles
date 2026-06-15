# UIMessageDialogOkCancelEx

## Declaration

```ats
function UIMessageDialogOkCancelEx(Text: string; FontSize: integer = PARAM_UseDefault; FontBold: boolean = FALSE; FontColor: integer = PARAM_UseDefault; BackgroundColor: integer = PARAM_UseDefault; Left: integer = PARAM_UseDefault; Top: integer = PARAM_UseDefault; Width: integer = PARAM_UseDefault; Height: integer = PARAM_UseDefault): integer;
```

## Call pattern

```ats
UIMessageDialogOkCancelEx('Text', <FontSize>, <FontBold>TRUE|FALSE, <FontColor>COLOR_?, <BackgroundColor>COLOR_?, <Left>, <Top>, <Width>, <Height>);
```

## Description

Shows an information pop-up window with the buttons OK and Cancel.

Fontsize, colors, position and size of the window can be customized.

## Metadata

- Category: Userinterface Access
- Code: 263985
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

DIALOGRESULT_Ok, DIALOGRESULT_Cancel

## Example

```ats
Button = UIMessageDialogOkCancelEx('Is this ok with you?',
            48, FALSE, COLOR_DkBlue, COLOR_White, 40, 40, 1000, 400);
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

`UIMessageDialogCustomEx`, `UIMessageDialogOkCancel`, `UIMessageDialogYesNoCancelEx`, `UIMessageDialogYesNoEx`
