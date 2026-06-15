# AdapterCablesGetList

## Declaration

```ats
function AdapterCablesGetList(ListVariable: tcreatearray; ListType: integer): integer;
```

## Call pattern

```ats
AdapterCablesGetList(ListVariable, ADAPTERCABLES_?);
```

## Description

Creates a list of adaptercables depending on "ListType" and returns the number of elements in the list.

## Metadata

- Category: Adapter Cables
- Code: 269056
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ListVariable`: `tcreatearray`
- `ListType`: `integer` — Allowed values: ADAPTERCABLES_All, ADAPTERCABLES_Connected, ADAPTERCABLES_Missing, ADAPTERCABLES_RangeTestIsolation

## Example

```ats
Count = AdapterCablesGetList(Cables, ADAPTERCABLES_All);
for Cable = 1 to Count do
begin
   UIWriteNormal(Cables[Cable]);
end;
```
