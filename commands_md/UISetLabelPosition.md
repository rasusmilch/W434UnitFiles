# UISetLabelPosition

## Declaration

```ats
function UISetLabelPosition(Label: integer; Left: integer; Top: integer): void;
```

## Call pattern

```ats
UISetLabelPosition(INFOLABEL_?, Left, Top);
```

## Description

Sets the label "Label" to the specified position.

## Metadata

- Category: Userinterface Access
- Code: 263945
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Left`: `integer`
- `Top`: `integer`

## Example

```ats
UISetLabelPosition(INFOLABEL_1, 80, 20);
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
