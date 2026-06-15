# UISetLabelFontSize

## Declaration

```ats
function UISetLabelFontSize(Label: integer; Size: integer): void;
```

## Call pattern

```ats
UISetLabelFontSize(INFOLABEL_?, Size);
```

## Description

Specifies the font size of the label "Label".

## Metadata

- Category: Userinterface Access
- Code: 263952
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Size`: `integer`

## Example

```ats
UISetLabelFontSize(INFOLABEL_1, 14);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
