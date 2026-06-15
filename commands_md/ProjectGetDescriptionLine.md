# ProjectGetDescriptionLine

## Declaration

```ats
function ProjectGetDescriptionLine(Line: integer): string;
```

## Call pattern

```ats
ProjectGetDescriptionLine(Line);
```

## Description

Returns the line with Index "Index" from the description of the current project.

## Metadata

- Category: Project Data
- Code: 268291
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Line`: `integer`

## Example

```ats
Count = ProjectGetDescriptionLineCount();
for Line = 1 to Count do
begin
   UIWriteNormal(ProjectGetDescriptionLine(Line));
end;
```

## See also

`ProjectGetDescriptionLineCount`, `ProjectGetFilename`, `ProjectGetName`
