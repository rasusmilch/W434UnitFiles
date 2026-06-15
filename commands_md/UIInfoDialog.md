# UIInfoDialog

## Declaration

```ats
function UIInfoDialog(Text: string): void;
```

## Call pattern

```ats
UIInfoDialog('Text');
```

## Description

Shows an information pop-up window with an OK button.

## Metadata

- Category: Userinterface Access
- Code: 263940
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
UIInfoDialog('Information!');
```

## See also

`UIErrorDialog`, `UIInfoDialogEx`, `UIMessageDialogCustom`, `UIMessageDialogOkCancel`, `UIMessageDialogYesNo`, `UIMessageDialogYesNoCancel`
