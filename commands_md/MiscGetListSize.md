# MiscGetListSize

## Declaration

```ats
function MiscGetListSize(ListName: tarray): integer;
```

## Call pattern

```ats
MiscGetListSize(ListName);
```

## Description

Returns the number of elements in a list.

## Metadata

- Category: Miscellaneous
- Code: 266510
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ListName`: `tarray`

## Example

```ats
PinDefineList(ListName, ["Pin1", "Pin2", "Pin3"]);
ListSize = MiscGetListSize(ListName);
UIWriteNormal(ListSize);
```

## Example notes

Returns the number of elements in al list.

## See also

`MiscCreateList`, `MiscGetListSize`, `MiscSortList`, `PinDefineList`
