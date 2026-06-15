# FileOpenBinary

## Declaration

```ats
function FileOpenBinary(Filename: string): integer;
```

## Call pattern

```ats
FileOpenBinary('Filename');
```

## Description

Opens an binary file with the name "Filename" and returns a handle for it.

## Metadata

- Category: File Access
- Code: 263707
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter

## Return value

If successful the function will return a so called "handle". This is a positive integer value between 10000001 and 20000000. The handle is required for further operations (reading, writing, closing) with that file.

In the case of an error the function will return 0.

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

`FileCloseBinary`, `FileCopyToPrinter`, `FileReplaceBinary`, `FileSaveAsBinary`, `FileSaveBinary`
