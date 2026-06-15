# MiscListToString

## Declaration

```ats
function MiscListToString(ListVariable: tarray; Separator: string = ';'): string;
```

## Call pattern

```ats
MiscListToString(ListVariable, Separator);
```

## Description

Returns the content of a list as a string.
In tzhe string the items are separated bei the specified separator.

## Metadata

- Category: Miscellaneous
- Code: 266516
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ListVariable`: `tarray`
- `Separator`: `string = '`

## Example

```ats
MiscCreateList(ListA, 4);
ListA[1] = 'This';
ListA[2] = 'is';
ListA[3] = 'a';
ListA[4] = 'list';
Text = MiscListToString(ListA, ';');
UIWriteNormal(Text);
Count = MiscListFromString(Text, ListB);
for Index = 1 to Count do
begin
   UIWriteNormal(ListB[Index]);
end;
```

## See also

`MiscGetListSize`, `MiscListFromString`, `MiscSortList`, `StrWordWrap`
