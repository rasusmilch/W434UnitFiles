# UISetLabelFontColor

## Declaration

```ats
function UISetLabelFontColor(Label: integer; Color: integer): void;
```

## Call pattern

```ats
UISetLabelFontColor(INFOLABEL_?, COLOR_?);
```

## Description

Specifies the font color of the label "Label".

## Metadata

- Category: Userinterface Access
- Code: 263951
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Color`: `integer` — Allowed values: COLOR_Black, COLOR_White, COLOR_Red, COLOR_DkRed, COLOR_Blue, COLOR_DkBlue, COLOR_Green, COLOR_DkGreen, COLOR_Gray, COLOR_DkGray, COLOR_Brown, COLOR_DkBrown, COLOR_Yellow, COLOR_Olive, COLOR_Orange, COLOR_Purple, COLOR_Teal, COLOR_Magenta, COLOR_Cyan, COLOR_Automatic

## Example

```ats
UISetLabelFontColor(INFOLABEL_1, COLOR_Orange);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
