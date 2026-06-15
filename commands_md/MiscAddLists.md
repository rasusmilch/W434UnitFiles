# MiscAddLists

## Declaration

```ats
function MiscAddLists(ResultList: tcreatearray; List1: tarray; List2: tarray): integer;
```

## Call pattern

```ats
MiscAddLists(ResultList, List1, List2);
```

## Description

Creates the list "ResultList" by merging the contents of "List1" and "List2".

## Metadata

- Category: Miscellaneous
- Code: 266500
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ResultList`: `tcreatearray`
- `List1`: `tarray`
- `List2`: `tarray`

## Return value

Returns the number of elements of the new list.

## Example

```ats
PinCreateList(List110, PIN_Info, '110V');
PinCreateList(List24, PIN_Info, '24V');
PinCreateList(ListGround, PIN_Info, 'Ground');
NoConnGroupLV('110V', List110, 'Ground', ListGround);
NoConnGroupLV('24V', List24, 'Ground', ListGround);
MiscAddLists(List, List110, List24);
NoConnGroupLV('24V + 110V', List, 'Ground', ListGround);
```

## See also

`NoConnGroupDB`, `NoConnGroupHV`, `NoConnGroupLV`, `PinCreateList`
