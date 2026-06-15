# UIErrorDialog

## Declaration

```ats
function UIErrorDialog(Text: string): void;
```

## Call pattern

```ats
UIErrorDialog('Text');
```

## Description

Shows an error pop-up window with an OK button.

## Metadata

- Category: Userinterface Access
- Code: 263941
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
UIErrorDialog('Error!');
```

## See also

`UIInfoDialog`, `UIMessageDialogCustom`, `UIMessageDialogOkCancel`, `UIMessageDialogYesNo`, `UIMessageDialogYesNoCancel`
