# UISetLabelFontStyle

## Declaration

```ats
function UISetLabelFontStyle(Label: integer; Bold: boolean; Italic: boolean; Underline: boolean): void;
```

## Call pattern

```ats
UISetLabelFontStyle(INFOLABEL_?, Bold, Italic, Underline);
```

## Description

Specifies the font style of the label "Label".

## Metadata

- Category: Userinterface Access
- Code: 263953
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Bold`: `boolean` — Allowed values: TRUE, FALSE
- `Italic`: `boolean` — Allowed values: TRUE, FALSE
- `Underline`: `boolean` — Allowed values: TRUE, FALSE

## Example

```ats
UISetLabelFontStyle(INFOLABEL_1, TRUE, TRUE, TRUE);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
