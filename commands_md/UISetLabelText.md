# UISetLabelText

## Declaration

```ats
function UISetLabelText(Label: integer; Text: string): void;
```

## Call pattern

```ats
UISetLabelText(INFOLABEL_?, 'Text');
```

## Description

Sets the text of the label "Label".

## Metadata

- Category: Userinterface Access
- Code: 263942
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Label`: `integer` — Allowed values: INFOLABEL_1, INFOLABEL_2, INFOLABEL_3, INFOLABEL_4
- `Text`: `string`

## Example

```ats
UISetLabelText(INFOLABEL_1, 'My text');
```

## See also

`UIResetLabel`, `UIResetLabels`, `UISetLabelAlignment`, `UISetLabelAutosize`, `UISetLabelColor`, `UISetLabelFontColor`, `UISetLabelFontName`, `UISetLabelFontSize`, `UISetLabelFontStyle`, `UISetLabelHeight`, `UISetLabelPosition`, `UISetLabelVisible`, `UISetLabelWidth`
