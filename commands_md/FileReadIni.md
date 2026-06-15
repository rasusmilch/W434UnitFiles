# FileReadIni

## Declaration

```ats
function FileReadIni(Filename: string; Section: string; Key: string; Default: string): string;
```

## Call pattern

```ats
FileReadIni('Filename', 'Section', 'Key', 'Default');
```

## Description

Returns the value of "Key" in the section "Section" of the Ini-File with name "Filename".

## Metadata

- Category: File Access
- Code: 263681
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter
- `Section`: `string`
- `Key`: `string`
- `Default`: `string`

## Return value

The value of "Default" is returned if file, section or key do not exists.

## Example

```ats
Value = FileReadIni('c:\Testini.ini', 'Section1', 'Key1', 'DefaultValue');
UIWriteNormal(Value);
```

## See also

`FileCloseIni`, `FileGetIni`, `FileOpenIni`, `FileSaveIni`, `FileSetIni`, `FileWriteIni`
