# ModListModuleNameExists

## Declaration

```ats
function ModListModuleNameExists(Name: string): boolean;
```

## Call pattern

```ats
ModListModuleNameExists('Name');
```

## Description

Returns TRUE if a module with the name "Name" exists in the modulelist, otherwise FALSE.

## Metadata

- Category: Modulelist
- Code: 267526
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`

## Example

```ats
if (ModListModuleNameExists('Module1Name'))
begin
   //call functions in module 1
end;
```

## See also

`ModListFilename`, `ModListModuleCount`, `ModListModuleExists`, `ModListModuleFilename`, `ModListModuleName`, `ModListUUTName`
