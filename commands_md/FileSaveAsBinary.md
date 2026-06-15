# FileSaveAsBinary

## Declaration

```ats
function FileSaveAsBinary(Handle: integer; NewFilename: string): boolean;
```

## Call pattern

```ats
FileSaveAsBinary(Handle, 'NewFilename');
```

## Description

Saves the binary file specified by the handle "Handle" as a new file with the name 'NewFilename'.

## Metadata

- Category: File Access
- Code: 263709
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`
- `NewFilename`: `string` — File picker parameter

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

`FileCloseBinary`, `FileCopyToPrinter`, `FileOpenBinary`, `FileReplaceBinary`, `FileSaveBinary`
