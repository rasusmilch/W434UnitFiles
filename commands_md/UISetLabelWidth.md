# UISetLabelWidth

## Declaration

```ats
function UISetLabelWidth(Label: integer; Width: integer): void;
```

## Call pattern

```ats
UISetLabelWidth(INFOLABEL_?, Width);
```

## Description

Specifies the width of the label "Label" (only if Autosize is disabled).

## Metadata

- Category: Userinterface Access
- Code: 263948
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Width`: `integer`

## Example

```ats
UISetLabelWidth(INFOLABEL_1, 200);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`
