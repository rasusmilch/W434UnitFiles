# FileDelete

## Declaration

```ats
function FileDelete(Filename: string): boolean;
```

## Call pattern

```ats
FileDelete('Filename');
```

## Description

Deletes the file specified by the filename "Filename".

## Metadata

- Category: File Access
- Code: 263692
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter

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

`FileCopy`, `FileCreateDirectory`, `FileDirectoryExists`, `FileExists`, `FileMove`
