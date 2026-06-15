# UISetLabelAutosize

## Declaration

```ats
function UISetLabelAutosize(Label: integer; Autosize: boolean): void;
```

## Call pattern

```ats
UISetLabelAutosize(INFOLABEL_?, AutoSize);
```

## Description

Specifies whether the size of label "Label" is set automatically.

## Metadata

- Category: Userinterface Access
- Code: 263946
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Autosize`: `boolean` — Allowed values: TRUE, FALSE

## Example

```ats
UISetLabelAutosize(INFOLABEL_1, TRUE);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
