# UIEditDialog

## Declaration

```ats
function UIEditDialog(Title: string; Text: string; AllowEmptyInput: boolean; HasCancelButton: boolean; var InputResult: string): integer;
```

## Call pattern

```ats
UIEditDialog('Title', 'Text', AllowEmptyInput, HasCancelButton, InputResult);
```

## Description

Shows an input pop-up window with the specified texts.

A default text can be passed in "InputResult".

## Metadata

- Category: Userinterface Access
- Code: 263936
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Title`: `string`
- `Text`: `string`
- `AllowEmptyInput`: `boolean` — Allowed values: TRUE, FALSE
- `HasCancelButton`: `boolean` — Allowed values: TRUE, FALSE
- `var InputResult`: `string`

## Return value

The function returns which button was pressed.

Possible values: 

DIALOGRESULT_Ok, DIALOGRESULT_Cancel

The entered value is returned in "InputResult".

## Example

```ats
InputResult = 'No number';
Button = UIEditDialog('Order number', 'Enter the number', FALSE, TRUE, InputResult);
if (Button == DIALOGRESULT_Ok)
begin
   UIWriteNormal(StrAdd('Order number: ', InputResult));
end
else
begin
   UIWriteNormal('Canceled');
end;
```

## See also

`UIEditDialogCustom`, `UIEditDialogEx`
