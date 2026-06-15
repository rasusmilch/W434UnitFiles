# FileCloseBinary

## Declaration

```ats
function FileCloseBinary(Handle: integer): void;
```

## Call pattern

```ats
FileCloseBinary(Handle);
```

## Description

Closes the binary file with the handle "Handle".

## Metadata

- Category: File Access
- Code: 263710
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`

## Example

```ats
Handle = FileOpenBinary('c:\Testdatei.bin');
if (Handle <> 0)
begin
   Date = DTDate();
   DateString = DTDateString(Date);
   FileReplaceBinary(Handle, '#Datum#', DateString);
   FileSaveAsBinary(Handle, 'C:\TestMitDatum.bin');
   FileCloseBinary(Handle);
end;
```

## See also

`FileCopyToPrinter`, `FileOpenBinary`, `FileReplaceBinary`, `FileSaveAsBinary`, `FileSaveBinary`
