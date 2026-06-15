# UISetLabelFontName

## Declaration

```ats
function UISetLabelFontName(Label: integer; FontName: string): void;
```

## Call pattern

```ats
UISetLabelFontName(INFOLABEL_?, 'FontName');
```

## Description

Specifies the font of the label "Label".

## Metadata

- Category: Userinterface Access
- Code: 263950
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `FontName`: `string`

## Example

```ats
UISetLabelFontName(INFOLABEL_1, 'Courier New');
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelText`, `UISetLabelVisible`, `UISetLabelWidth`
