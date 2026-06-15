# FileAddText

## Declaration

```ats
function FileAddText(Handle: integer; TextLine: string): void;
```

## Call pattern

```ats
FileAddText(Handle, 'TextLine');
```

## Description

Writes the text in "Line" at the specified position into the textfile specified by the handle "Handle".

## Metadata

- Category: File Access
- Code: 263688
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Handle`: `integer`
- `TextLine`: `string`

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

`FileCloseText`, `FileGetText`, `FileGetTextLineCount`, `FileOpenText`, `FileSaveText`
