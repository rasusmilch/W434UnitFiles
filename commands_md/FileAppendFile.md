# FileAppendFile

## Declaration

```ats
function FileAppendFile(SourceFilename: string; DestinationFilename: string): boolean;
```

## Call pattern

```ats
FileAppendFile('SourceFilename', 'DestinationFilename');
```

## Description

Appends the content of the file "SourceFilename" to the file "DestinationFilename".

## Metadata

- Category: File Access
- Code: 263699
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
FileAppendFile('c:\Testtext.txt', 'c:\TesttextLong.txt');
```
