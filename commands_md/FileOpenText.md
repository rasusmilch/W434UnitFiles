# FileOpenText

## Declaration

```ats
function FileOpenText(Filename: string): integer;
```

## Call pattern

```ats
FileOpenText('Filename');
```

## Description

Opens a textfile with the name "Filename" and returns a handle for it.

## Metadata

- Category: File Access
- Code: 263686
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter

## Return value

If successful the function will return a so called "handle". This is a negative integer value between -1 and -10000000. The handle is required for further operations (reading, writing, closing) with that file.

In the case of an error the function will return 0.

## Example

```ats
Handle = FileOpenText('c:\Testtext.txt');
for Count = 1 to 10 do
begin
   Line = StrAdd('Line: ', Count);
   FileAddText(Handle, Line);
end;
FileSaveText(Handle);
FileCloseText(Handle);

Handle = FileOpenText('c:\Testtext.txt');
LineCount = FileGetTextLineCount(Handle);
for Count = 1 to LineCount do
begin
   Line = FileGetText(Handle, Count);
   UIWriteNormal(Line);
end;
FileCloseText(Handle);
```

## See also

`FileAddText`, `FileCloseText`, `FileGetText`, `FileGetTextLineCount`, `FileSaveText`
