# ProjectGetUnitName

## Declaration

```ats
function ProjectGetUnitName(Index: integer): string;
```

## Call pattern

```ats
ProjectGetUnitName(Index);
```

## Description

Returns the name of the unit with index "Index" of the current project.

## Metadata

- Category: Project Data
- Code: 268293
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Index`: `integer`

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

`ProjectGetFilename`, `ProjectGetModuleName`, `ProjectGetName`, `ProjectGetUnitCount`, `ProjectGetUnitFilename`
