# FileSaveIni

## Declaration

```ats
function FileSaveIni(Handle: integer): boolean;
```

## Call pattern

```ats
FileSaveIni(Handle);
```

## Description

Saves the Ini-File specified by the handle "Handle".

## Metadata

- Category: File Access
- Code: 263700
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`

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

`FileCloseIni`, `FileGetIni`, `FileOpenIni`, `FileReadIni`, `FileSetIni`, `FileWriteIni`
