# FileSaveBinary

## Declaration

```ats
function FileSaveBinary(Handle: integer): boolean;
```

## Call pattern

```ats
FileSaveBinary(Handle);
```

## Description

Saves the binary file specified by the handle "Handle".

## Metadata

- Category: File Access
- Code: 263708
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
   FileSaveBinary(Handle);
   FileCloseBinary(Handle);
end;
```

## See also

`FileCloseBinary`, `FileCopyToPrinter`, `FileOpenBinary`, `FileReplaceBinary`, `FileSaveAsBinary`
