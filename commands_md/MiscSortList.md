# MiscSortList

## Declaration

```ats
function MiscSortList(LIst: tarray; SortMode: integer): boolean;
```

## Call pattern

```ats
MiscSortList(List, SORTMODE_?);
```

## Description

Sorts the specified list alphabetically or numerically

## Metadata

- Category: Miscellaneous
- Code: 266515
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `LIst`: `tarray`
- `SortMode`: `integer` — Allowed values: SORTMODE_alpha, SORTMODE_integer, SORTMODE_real

## Return value

The function returns TRUE if sorting was successful, otherwise FALSE

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

`MiscCreateList`, `MiscGetListSize`
