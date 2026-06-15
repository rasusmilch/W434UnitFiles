# StrWordWrap

## Declaration

```ats
function StrWordWrap(Text: string; MaxLength: integer; Lines: tcreatearray): integer;
```

## Call pattern

```ats
StrWordWrap('Text', <MaxLength>, Lines);
```

## Description

Inserts a line break when the maxium line length is surpassed.

## Metadata

- Category: String Processing
- Code: 262414
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`
- `MaxLength`: `integer`
- `Lines`: `tcreatearray`

## Return value

Returns the number of lines in the list.

## Example

```ats
LineCount = StrWordWrap('abcdefghijklmnopqrstuvwxyz abcde fghij klmno pqrst u . 0v w x. y z!', 3, Lines);
for Index = 1 to LineCount do
begin
   UIWriteNormal(Lines[Index]);
end;
```

## See also

`StrPosition`, `StrAdd`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrContains`, `StrReplace`, `MiscListFromString`, `MiscListToString`
