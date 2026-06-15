# FileExtractPath

## Declaration

```ats
function FileExtractPath(Filename: string): string;
```

## Call pattern

```ats
FileExtractPath('Filename');
```

## Description

Returns the characters of "Filename" up to exclusively the colon or backslash that separates the path information from the filename. If the "Filename" does not contain drive- or pathinformations an empty string will be returned.

## Metadata

- Category: File Access
- Code: 263697
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter

## Example

```ats
Path = FileExtractPath('c:\Testini.ini');
Name = FileExtractName('c:\Testini.ini');
UIWriteNormal(StrAdd('Path: ', Path));
UIWriteNormal(StrAdd('Name: ', Name));
```

## See also

`FileChangeExt`, `FileExtractName`
