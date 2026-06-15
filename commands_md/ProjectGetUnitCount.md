# ProjectGetUnitCount

## Declaration

```ats
function ProjectGetUnitCount(): integer;
```

## Call pattern

```ats
ProjectGetUnitCount();
```

## Description

Returns the number of units of the current project.

## Metadata

- Category: Project Data
- Code: 268292
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Count = ProjectGetUnitCount();
for Unit = 1 to Count do
begin
   Filename = ProjectGetUnitFilename(Unit);
   Name = ProjectGetUnitName(Unit);
   UIWriteNormal(StrAdd('Unit filename: ', Filename));
   UIWriteNormal(StrAdd('Unit name: ', Name));
end;
```

## See also

`ProjectGetFilename`, `ProjectGetModuleCount`, `ProjectGetName`, `ProjectGetUnitFilename`, `ProjectGetUnitName`
