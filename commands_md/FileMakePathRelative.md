# FileMakePathRelative

## Declaration

```ats
function FileMakePathRelative(FileWithAbsolutePath: string; RelativeTo: string = ''): string;
```

## Call pattern

```ats
FileMakePathRelative('FileWithAbsolutePath', 'RelativeTo');
```

## Description

Returns the passed absolute filename with a path relative to the directory passed in "RelativeTo".

If an empty string ist passed for "RelativeTo" the function will use the CEETIS data directory:

Windows 2000 and XP: C:\Documents and Settings\All Users\Documents\CEETIS

Windows Vista: C:\Users\Public\Documents\CEETIS

## Metadata

- Category: File Access
- Code: 263704
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `FileWithAbsolutePath`: `string`
- `RelativeTo`: `string = ''`

## Example

```ats
FileCreateDirectory('c:\abc\xyz');
FileWithAbsolutePath = 'c:\abc\xyz\Test.txt';
FileWithRelativePath = FileMakePathRelative(FileWithAbsolutePath, 'c:\abc');
UIWriteNormal(FileWithRelativePath);
FileWithAbsolutePath = FileExpandName(FileWithRelativePath, 'c:\abc');
UIWriteNormal(FileWithAbsolutePath);

```

## See also

`FileCreateDirectory`, `FileExpandName`
