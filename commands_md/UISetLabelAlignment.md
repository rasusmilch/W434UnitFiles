# UISetLabelAlignment

## Declaration

```ats
function UISetLabelAlignment(Label: integer; Alignment: integer): void;
```

## Call pattern

```ats
UISetLabelAlignment(INFOLABEL_?, Alignment);
```

## Description

Specifies the alignment of the label "Label".

## Metadata

- Category: Userinterface Access
- Code: 263947
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Alignment`: `integer` — Allowed values: ALIGN_LeftJustify, ALIGN_RightJustify, ALIGN_Center

## Example

```ats
UISetLabelAlignment(INFOLABEL_1, ALIGN_Center);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
