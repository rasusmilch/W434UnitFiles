# UIResetLabel

## Declaration

```ats
function UIResetLabel(Label: integer): void;
```

## Call pattern

```ats
UIResetLabel(INFOLABEL_?);
```

## Description

Resets appearance of the label "Label" to its start values.

## Metadata

- Category: Userinterface Access
- Code: 263954
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4

## Example

```ats
UIResetLabel(INFOLABEL_1);
```

## See also

`UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
