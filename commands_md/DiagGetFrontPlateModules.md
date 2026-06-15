# DiagGetFrontPlateModules

## Declaration

```ats
function DiagGetFrontPlateModules(IdentifierListVariable: tcreatearray; NameListVariable: tcreatearray): integer;
```

## Call pattern

```ats
DiagGetFrontPlateModules(IdentifierListVariable, NameListVariable);
```

## Description

Creates lists with the identifiers and names of all frontpanelmodules of the system and returns the number of elements in the lists.

## Metadata

- Category: Diagnostics
- Code: 269312
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `IdentifierListVariable`: `tcreatearray`
- `NameListVariable`: `tcreatearray`

## Example

```ats
Count = DiagGetFrontPlateModules(Identifiers, Names);
for Frontplate = 1 to Count do
begin
   UIWriteNormal(Identifiers[Frontplate]);
   UIWriteNormal(Names[Frontplate]);
end;
```

## See also

`DiagGetAdapterConnectorCode`
