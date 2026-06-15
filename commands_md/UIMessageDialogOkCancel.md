# UIMessageDialogOkCancel

## Declaration

```ats
function UIMessageDialogOkCancel(Text: string): integer;
```

## Call pattern

```ats
UIMessageDialogOkCancel('Text');
```

## Description

Shows an information pop-up window with the buttons OK and Cancel.

## Metadata

- Category: Userinterface Access
- Code: 263937
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Return value

The function returns which button was pressed.

Possible values:

DIALOGRESULT_Ok, DIALOGRESULT_Cancel

## Example

```ats
Button = UIMessageDialogOkCancel('Is this ok with you?');
if (Button == DIALOGRESULT_Ok)
begin
   UIWriteNormal('It is ok');
end
else
begin
   UIWriteNormal('It is not ok');
end;
```

## See also

`UIErrorDialog`, `UIInfoDialog`, `UIMessageDialogCustom`, `UIMessageDialogOkCancelEx`, `UIMessageDialogYesNo`, `UIMessageDialogYesNoCancel`
