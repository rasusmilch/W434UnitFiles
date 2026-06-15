# FileExtractExtension

## Declaration

```ats
function FileExtractExtension(Filename: string):string;
```

## Call pattern

```ats
FileExtractExtension('Filename');
```

## Description

Returns the characters of the Extension.

## Metadata

- Category: File Access
- Code: 263703
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string`

## Example

```ats
Extension = FileExtractExtension('c:\Testfile.txt');
UIWriteNormal(StrAdd('Extension: ',Extension));
```

## See also

`FileChangeExt`, `FileEctractName`, `FileExtractPath`
