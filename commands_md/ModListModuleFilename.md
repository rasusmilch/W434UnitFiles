# ModListModuleFilename

## Declaration

```ats
function ModListModuleFilename(Index: integer): string;
```

## Call pattern

```ats
ModListModuleFilename(Index);
```

## Description

Returns the filename of the module with index "Index" relative to the modulelist.

## Metadata

- Category: Modulelist
- Code: 267523
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

`ModListFilename`, `ModListModuleCount`, `ModListModuleExists`, `ModListModuleName`, `ModListModuleNameExists`, `ModListUUTName`
