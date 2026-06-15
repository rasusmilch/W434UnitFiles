# UISetLabelHeight

## Declaration

```ats
function UISetLabelHeight(Label: integer; Height: integer): void;
```

## Call pattern

```ats
UISetLabelHeight(INFOLABEL_?, Height);
```

## Description

Specifies the height of the label "Label" (only if Autosize is disabled).

## Metadata

- Category: Userinterface Access
- Code: 263949
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Height`: `integer`

## Example

```ats
UISetLabelHeight(INFOLABEL_1, 40);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
