# ModListModuleExists

## Declaration

```ats
function ModListModuleExists(Filename: string): boolean;
```

## Call pattern

```ats
ModListModuleExists('Filename');
```

## Description

Returns TRUE if a module with the filename "Filename" exists in the modulelist, otherwise FALSE.

## Metadata

- Category: Modulelist
- Code: 267525
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Filename`: `string` — File picker parameter

## Example

```ats
if (ModListModuleExists('Module1Filename'))
begin
   //call functions in module 1
end;
```

## See also

`ModListFilename`, `ModListModuleCount`, `ModListModuleFilename`, `ModListModuleName`, `ModListModuleNameExists`, `ModListUUTName`
