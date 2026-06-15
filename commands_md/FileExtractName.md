# FileExtractName

## Declaration

```ats
function FileExtractName(Filename: string): string;
```

## Call pattern

```ats
FileExtractName('Filename');
```

## Description

Returns the characters of "Filename" starting after the colon or the backslash that separates the path information from the filename. If the "Filename" does not contain drive- or pathinformations the return value equals "Filename".

## Metadata

- Category: File Access
- Code: 263696
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

`FileChangeExt`, `FileExtractPath`
