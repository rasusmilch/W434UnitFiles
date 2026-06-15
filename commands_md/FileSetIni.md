# FileSetIni

## Declaration

```ats
function FileSetIni(Handle: integer; Section: string; Key: string; Value: string): void;
```

## Call pattern

```ats
FileSetIni(Handle, 'Section', 'Key', 'Value');
```

## Description

Writes the value "Value" at the key "Key" in section "Section" into an Ini-file which is specified by handle "Handle".

## Metadata

- Category: File Access
- Code: 263684
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`
- `Section`: `string`
- `Key`: `string`
- `Value`: `string`

## Example

```ats
Handle = FileOpenIni('c:\Testini.ini');
FileSetIni(Handle, 'Section1', 'Key1', 'MyValue');
FileSaveIni(Handle);
Value = FileGetIni(Handle, 'Section1', 'Key1', 'DefaultValue');
FileCloseIni(Handle);
UIWriteNormal(Value);
```

## See also

`FileCloseIni`, `FileGetIni`, `FileOpenIni`, `FileReadIni`, `FileSaveIni`, `FileWriteIni`
