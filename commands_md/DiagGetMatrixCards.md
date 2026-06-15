# DiagGetMatrixCards

## Declaration

```ats
function DiagGetMatrixCards(IdentifierListVariable: tcreatearray; NameListVariable: tcreatearray): integer;
```

## Call pattern

```ats
DiagGetMatrixCards(IdentifierListVariable, NameListVariable);
```

## Description

Creates lists with the identifiers and names of all matrix cards of the system and returns the number of elements in the lists.

## Metadata

- Category: Diagnostics
- Code: 269315
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
Count = DiagGetMatrixCards(Identifiers, Names);
for Index = 1 to Count do
begin
   UIWriteNormal(Identifiers[Index]);
   UIWriteNormal(Names[Index]);
end;
```

## See also

`DiagGetAdapterConnectorCode`
