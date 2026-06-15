# FileCopyToPrinter

## Declaration

```ats
function FileCopyToPrinter(SourceFilename: string; Printer: string): boolean;
```

## Call pattern

```ats
FileCopyToPrinter('SourceFilename', 'Printer');
```

## Description

Files can be copied to a LPT- or COM-interface with this function.

It makes it also possible to copy files to a Windows printer.
For this purpose the printer driver is bypassed and the data is sent in raw format.

## Metadata

- Category: File Access
- Code: 263712
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `SourceFilename`: `string`
- `Printer`: `string`

## Example

```ats
//Example 1
if (FileExists('c:\PrintFile.prn'))
begin
   FileCopyToPrinter('c:\PrintFile.prn', 'LPT1');
end;

//Example 2
if (FileExists('c:\PrintFile.prn'))
begin
   FileCopyToPrinter('c:\PrintFile.prn', 'COM1');
end;

//Example 2
if (FileExists('c:\PrintFile.prn'))
begin
   FileCopyToPrinter('c:\PrintFile.prn', 'MyPrinter');
end;
```

## Example notes

Example 1: Copies the specified file to the LPT1-Interface

Example 2: Copies the specified file to the COM1-Interface

Example 3: Copies the specified file to the Windows-printer with the name "MyPrinter"

## See also

`FileCloseBinary`, `FileCopy`, `FileOpenBinary`, `FileReplaceBinary`, `FileSaveAsBinary`, `FileSaveBinary`, `FileMove`
