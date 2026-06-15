# MiscListFromString

## Declaration

```ats
function MiscListFromString(Data:string; ListVariable: tcreatearray; Separator: string = ';'): integer;
```

## Call pattern

```ats
MiscListFromString(Data, ListVariable, Separator);
```

## Description

Splits the string at the separators and returns the items as a list.
The number of elements is reurned as function value.

## Metadata

- Category: Miscellaneous
- Code: 266517
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data`: `string`
- `ListVariable`: `tcreatearray`
- `Separator`: `string = '`

## Return value

Number of elements in the list.

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

`MiscGetListSize`, `MiscListToString`, `MiscSortList`, `StrWordWrap`
