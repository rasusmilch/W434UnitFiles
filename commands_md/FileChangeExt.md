# FileChangeExt

## Declaration

```ats
function FileChangeExt(Filename: string; NewExtension: string): string;
```

## Call pattern

```ats
FileChangeExt('Filename', 'NewExtension');
```

## Description

Changes the fileextension of "Filename" to the value passed in "NewExtension".

The function does not rename the file. It only changes the string.

## Metadata

- Category: File Access
- Code: 263698
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter
- `NewExtension`: `string`

## Example

```ats
Changed = FileChangeExt('c:\Testini.ini', '.txt');
UIWriteNormal(Changed);
```

## See also

`FileExtractName`, `FileExtractPath`
