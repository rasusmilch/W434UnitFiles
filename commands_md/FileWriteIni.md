# FileWriteIni

## Declaration

```ats
function FileWriteIni(Filename: string; Section: string; Key: string; Value: string): boolean;
```

## Call pattern

```ats
FileWriteIni('Filename', 'Section', 'Key', 'Value');
```

## Description

Writes the value "Value" at the key "Key" in section "Section" into an Ini-file with name "Filename".

## Metadata

- Category: File Access
- Code: 263680
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter
- `Section`: `string`
- `Key`: `string`
- `Value`: `string`

## Return value

Returns TRUE if successful, otherwise FALSE.

## Example

```ats
Success = FileWriteIni('c:\Testini.ini', 'Section1', 'Key1', 'MyValue');
```

## See also

`FileCloseIni`, `FileGetIni`, `FileOpenIni`, `FileReadIni`, `FileSaveIni`, `FileSetIni`
