# PrintingAllowed

## Declaration

```ats
function PrintingAllowed(): boolean;
```

## Call pattern

```ats
PrintingAllowed();
```

## Description

The function determines, depending on the result of the last test and the settings in the "Output" menu, whether printing is allowed or not.

## Metadata

- Category: Printing and Archiving
- Code: 265732
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test end program
- Count result: no
- Archive allowed: no

## Return value

The function returns TRUE if printing is allowed, otherwise FALSE.

## Example

```ats
ConfirmPrint = PrintingAllowed();
if (ConfirmPrint)
begin
   ConfirmPrint = ProjectGetTestEndSettings(TESTEND_ConfirmReportPrint);
end;
if (ConfirmPrint)
begin
   //show Yes/No dialog
   Button = UIMessageDialogYesNo(LocalText('92#Print report?'));
   //if "Yes" was clicked
   if (Button == DIALOGRESULT_Yes)
   begin
      PrintConfirmed = TRUE;
   end
   else
   begin
      PrintConfirmed = FALSE;
   end;
end
else
begin
   PrintConfirmed = FALSE;
end;
```

## See also

`PrintAllReports`, `PrintReport`, `ProjectGetTestEndSettings`
