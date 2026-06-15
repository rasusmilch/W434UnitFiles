# FileGetIni

## Declaration

```ats
function FileGetIni(Handle: integer; Section: string; Key: string; Default: string): string;
```

## Call pattern

```ats
FileGetIni(Handle, 'Section', 'Key', 'Default');
```

## Description

Returns the value of "Key" in the section "Section" of the Ini-File specified by the handle "Handle".

## Metadata

- Category: File Access
- Code: 263685
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`
- `Section`: `string`
- `Key`: `string`
- `Default`: `string`

## Return value

The value of "Default" is returned if file, section or key do not exists.

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

`FileCloseIni`, `FileOpenIni`, `FileReadIni`, `FileSaveIni`, `FileSetIni`, `FileWriteIni`
