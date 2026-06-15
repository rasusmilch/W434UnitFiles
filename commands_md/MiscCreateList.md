# MiscCreateList

## Declaration

```ats
function MiscCreateList(ListVariable: tcreatearray; Size: integer): void;
```

## Call pattern

```ats
MiscCreateList(ListVariable, Size);
```

## Description

Creates a one-dimensional array with "Size" elements. If the array already exists it will not be created again.

## Metadata

- Category: Miscellaneous
- Code: 266498
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ListVariable`: `tcreatearray`
- `Size`: `integer`

## Example

```ats
MiscCreateList(List, 4);
List[1] = 5;
List[2] = 3;
List[3] = 4;
List[4] = 1;
MiscSortList(List, SORTMODE_integer);
```

## See also

`MiscGetListSize`, `MiscSortList`
