# ModListModuleName

## Declaration

```ats
function ModListModuleName(Index: integer): string;
```

## Call pattern

```ats
ModListModuleName(Index);
```

## Description

Returns the name of the module with index "Index" relative to the modulelist.

## Metadata

- Category: Modulelist
- Code: 267524
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Index`: `integer`

## Example

```ats
Count = ModListModuleCount();
for Module = 1 to Count do
begin
   Filename = ModListModuleFilename(Module);
   Name = ModListModuleName(Module);
   UIWriteNormal(StrAdd('Filename: ', Filename));
   UIWriteNormal(StrAdd('Name: ', Name));
end;
```

## See also

`ModListFilename`, `ModListModuleCount`, `ModListModuleExists`, `ModListModuleFilename`, `ModListModuleNameExists`, `ModListUUTName`
