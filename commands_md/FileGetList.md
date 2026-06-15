# FileGetList

## Declaration

```ats
function FileGetList(Directory: string; Filter: string; Files: tcreatearray; IncudeSubdirectories: boolean = FALSE): integer;
```

## Call pattern

```ats
FileGetList('Directory', '*.*', Files, FALSE);
```

## Description

Reads the files from the directory "Directory".

The function does NOT work for any directory in the windows system directory, the program files dirctory or the root directory of a drive.

## Metadata

- Category: File Access
- Code: 263702
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Directory`: `string` — The directory from which the filenames shall be read.; Directory picker parameter
- `Filter`: `string` — A filter that specifies the filenames.
; For example '*.*' or '*.project'.
- `Files`: `tcreatearray` — A list variable in which the filenames are returned.
- `IncudeSubdirectories`: `boolean = FALSE` — If FALSE is passed only the files from the directory will be read.
; If TRUE is passed the files from the directory and all subdirectories will be read.; Allowed values: TRUE, FALSE

## Return value

The files are returned in the list "Files".

The return value of the function is the number of the files that were read.


## Example

```ats
FileCount = FileGetList('.\Projects', '*.project', Files, TRUE);
for File = 1 to FileCount do
begin
   UIWriteNormal(Files[File]);
end;
```

## See also

`FileDirectoryExists`, `FileExists`
