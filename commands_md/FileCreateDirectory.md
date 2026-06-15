# FileCreateDirectory

## Declaration

```ats
function FileCreateDirectory(Directory: string): boolean;
```

## Call pattern

```ats
FileCreateDirectory('Directory');
```

## Description

Creates a directory which must be completely specified in "Directory". If superior directories do not exist they will be automatically created.

## Metadata

- Category: File Access
- Code: 263695
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Directory`: `string` — Directory picker parameter

## Return value

Returns TRUE if successful, otherwise FALSE.

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

`FileCopy`, `FileDelete`, `FileDirectoryExists`, `FileExists`, `FileMove`
