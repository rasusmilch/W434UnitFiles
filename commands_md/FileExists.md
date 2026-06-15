# FileExists

## Declaration

```ats
function FileExists(Filename: string): boolean;
```

## Call pattern

```ats
FileExists('Filename');
```

## Description

Returns TRUE if the file with the name "Filename" exists, otherwise FALSE.

## Metadata

- Category: File Access
- Code: 263691
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter

## Example

```ats
if (FileExists('c:\Testini.ini'))
begin
   FileCopy('c:\Testini.ini', 'c:\Testini2.ini');
   FileDelete('c:\Testini.ini');
end;
```

## See also

`FileCopy`, `FileCreateDirectory`, `FileDelete`, `FileDirectoryExists`, `FileGetList`, `FileMove`
