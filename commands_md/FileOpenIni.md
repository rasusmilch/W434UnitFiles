# FileOpenIni

## Declaration

```ats
function FileOpenIni(Filename: string): integer;
```

## Call pattern

```ats
FileOpenIni('Filename');
```

## Description

Opens an Ini-file with the name "Filename" and returns a handle for it.

## Metadata

- Category: File Access
- Code: 263682
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter

## Return value

If successful the function will return a so called "handle". This is a positive integer value between 1 and 10000000. The handle is required for further operations (reading, writing, closing) with that file.

In the case of an error the function will return 0.

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

`FileCloseIni`, `FileGetIni`, `FileReadIni`, `FileSaveIni`, `FileSetIni`, `FileWriteIni`
