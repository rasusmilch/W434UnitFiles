# FileExpandName

## Declaration

```ats
function FileExpandName(FileWithRelativePath: string; RelativeTo: string = ''): string;
```

## Call pattern

```ats
FileExpandName('FileWithRelativePath', 'RelativeTo');
```

## Description

Returns the passed relative filename with an absolute path.

The directory passed in "RelativeTo" is used as the base directory.

If an empty string ist passed for "RelativeTo" the function will use the CEETIS data directory:

Windows 2000 and XP: C:\Documents and Settings\All Users\Documents\CEETIS

Windows Vista: C:\Users\Public\Documents\CEETIS


## Metadata

- Category: File Access
- Code: 263705
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `FileWithRelativePath`: `string`
- `RelativeTo`: `string = ''`

## Example

```ats
FileCreateDirectory('c:\abc\xyz');
FileWithRelativePath = '.\xyz\Test.txt';
FileWithAbsolutePath = FileExpandName(FileWithRelativePath, 'c:\abc');
UIWriteNormal(FileWithAbsolutePath);
FileWithRelativePath = FileMakePathRelative(FileWithAbsolutePath, 'c:\abc');
UIWriteNormal(FileWithRelativePath);
```
