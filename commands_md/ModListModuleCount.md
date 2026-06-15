# ModListModuleCount

## Declaration

```ats
function ModListModuleCount(): integer;
```

## Call pattern

```ats
ModListModuleCount();
```

## Description

Returns the number of modules in the modulelist.

## Metadata

- Category: Modulelist
- Code: 267522
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

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

`ModListFilename`, `ModListModuleExists`, `ModListModuleFilename`, `ModListModuleName`, `ModListModuleNameExists`, `ModListUUTName`
