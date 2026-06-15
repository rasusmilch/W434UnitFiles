# UIMessageDialogYesNo

## Declaration

```ats
function UIMessageDialogYesNo(Text: string): integer;
```

## Call pattern

```ats
UIMessageDialogYesNo('Text');
```

## Description

Shows an information pop-up window with the buttons Yes and No.

## Metadata

- Category: Userinterface Access
- Code: 263938
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

DIALOGRESULT_Yes, DIALOGRESULT_No

## Example

```ats
Button = UIMessageDialogYesNo('Do you like this?');
if (Button == DIALOGRESULT_Yes)
begin
   UIWriteNormal('I like it');
end
else
begin
   UIWriteNormal('I do not like it');
end;
```

## See also

`UIErrorDialog`, `UIInfoDialog`, `UIMessageDialogCustom`, `UIMessageDialogOkCancel`, `UIMessageDialogYesNoCancel`, `UIMessageDialogYesNoEx`
