# FileDirectoryExists

## Declaration

```ats
function FileDirectoryExists(Directory: string): boolean;
```

## Call pattern

```ats
FileDirectoryExists('Directory');
```

## Description

Returns TRUE if the directory with the name "Directory" exists, otherwise FALSE.

## Metadata

- Category: File Access
- Code: 263694
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Directory`: `string` — Directory picker parameter

## Example

```ats
if (FileDirectoryExists('c:\testdirectory'))
begin
   UIWriteNormal('Testdirectory exists');
end
else
begin
   if (FileCreateDirectory('c:\testdirectory'))
   begin
      UIWriteNormal('Testdirectory created');
   end
   else
   begin
      UIWriteNormal('No directory');
   end;
end;
```

## See also

`FileCopy`, `FileCreateDirectory`, `FileDelete`, `FileExists`, `FileGetList`, `FileMove`
