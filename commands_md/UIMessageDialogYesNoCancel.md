# UIMessageDialogYesNoCancel

## Declaration

```ats
function UIMessageDialogYesNoCancel(Text: string): integer;
```

## Call pattern

```ats
UIMessageDialogYesNoCancel('Text');
```

## Description

Shows an information pop-up window with the buttons Yes, No and Cancel.

## Metadata

- Category: Userinterface Access
- Code: 263939
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

DIALOGRESULT_Yes, DIALOGRESULT_No, DIALOGRESULT_Cancel

## Example

```ats
Button = UIMessageDialogYesNoCancel('Do you like this?');
if (Button == DIALOGRESULT_Yes)
begin
   UIWriteNormal('I like it');
end
else
begin
   if (Button == DIALOGRESULT_No)
   begin
      UIWriteNormal('I do not like it');
   end
   else
   begin
      UIWriteNormal('I am not sure');
   end;
end;
```

## See also

`UIErrorDialog`, `UIInfoDialog`, `UIMessageDialogCustom`, `UIMessageDialogOkCancel`, `UIMessageDialogYesNo`, `UIMessageDialogYesNoCancelEx`
