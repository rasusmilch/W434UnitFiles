# FileCopy

## Declaration

```ats
function FileCopy(SourceFilename: string; DestinationFilename: string): boolean;
```

## Call pattern

```ats
FileCopy('SourceFilename', 'DestinationFilename');
```

## Description

Copies the file "SourceFilename" to the file "DestinationFilename".

## Metadata

- Category: File Access
- Code: 263693
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `SourceFilename`: `string` — File picker parameter
- `DestinationFilename`: `string` — File picker parameter

## Return value

Returns TRUE if successful, otherwise FALSE.

## Example

```ats
if (FileExists('c:\Testini.ini'))
begin
   FileCopy('c:\Testini.ini', 'c:\Testini2.ini');
   FileDelete('c:\Testini.ini');
end;
```

## See also

`FileCopyToPrinter`, `FileCreateDirectory`, `FileDelete`, `FileDirectoryExists`, `FileExists`, `FileMove`
