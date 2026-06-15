# UISetLabelVisible

## Declaration

```ats
function UISetLabelVisible(Label: integer; Visible: boolean): void;
```

## Call pattern

```ats
UISetLabelVisible(INFOLABEL_?, Visible);
```

## Description

Determines whether the label "Label" is visible or not.

## Metadata

- Category: Userinterface Access
- Code: 263944
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Visible`: `boolean` — Allowed values: TRUE, FALSE

## Example

```ats
UISetLabelVisible(INFOLABEL_1, FALSE);
DTWait(3s);
UISetLabelVisible(INFOLABEL_1, TRUE);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelWidth`
