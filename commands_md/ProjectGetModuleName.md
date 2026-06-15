# ProjectGetModuleName

## Declaration

```ats
function ProjectGetModuleName(Index: integer): string;
```

## Call pattern

```ats
ProjectGetModuleName(Index);
```

## Description

Returns the name of the module with index "Index" of the current project.

## Metadata

- Category: Project Data
- Code: 268296
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

`ProjectGetFilename`, `ProjectGetModuleChecksum`, `ProjectGetModuleCount`, `ProjectGetModuleFilename`, `ProjectGetName`, `ProjectGetUnitName`
