# ProjectGetModuleCount

## Declaration

```ats
function ProjectGetModuleCount(): integer;
```

## Call pattern

```ats
ProjectGetModuleCount();
```

## Description

Returns the number of modules of the current project.

## Metadata

- Category: Project Data
- Code: 268295
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

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

`ProjectGetFilename`, `ProjectGetModuleChecksum`, `ProjectGetModuleFilename`, `ProjectGetModuleName`, `ProjectGetName`, `ProjectGetUnitCount`
