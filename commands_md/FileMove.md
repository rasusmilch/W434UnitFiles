# FileMove

## Declaration

```ats
function FileMove(SourceFilename: string; DestinationFilename: string): boolean;
```

## Call pattern

```ats
FileMove('SourceFilename', 'DestinationFilename');
```

## Description

Moves the file "SourceFilename" to the file "DestinationFilename"

## Metadata

- Category: File Access
- Code: 263713
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
   FileMove('c:\Testini.ini', 'c:\Testini2.ini');
end;
```

## See also

`FileCopyToPrinter`, `FileCreateDirectory`, `FileDelete`, `FileDirectoryExists`, `FileExists`, `FileCopy`
