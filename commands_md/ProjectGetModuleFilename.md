# ProjectGetModuleFilename

## Declaration

```ats
function ProjectGetModuleFilename(Index: integer): string;
```

## Call pattern

```ats
ProjectGetModuleFilename(Index);
```

## Description

Returns the filename of the module with index "Index" of the current project.

## Metadata

- Category: Project Data
- Code: 268297
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Index`: `integer`

## Example

```ats
Count = ProjectGetModuleCount();
for Module = 1 to Count do
begin
   Filename = ProjectGetModuleFilename(Module);
   Name = ProjectGetModuleName(Module);
   UIWriteNormal(StrAdd('Module filename: ', Filename));
   UIWriteNormal(StrAdd('Module name: ', Name));
end;
```

## See also

`ProjectGetFilename`, `ProjectGetModuleChecksum`, `ProjectGetModuleCount`, `ProjectGetModuleName`, `ProjectGetName`, `ProjectGetUnitFilename`
