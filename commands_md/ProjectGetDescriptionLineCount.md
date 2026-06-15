# ProjectGetDescriptionLineCount

## Declaration

```ats
function ProjectGetDescriptionLineCount(): integer;
```

## Call pattern

```ats
ProjectGetDescriptionLineCount();
```

## Description

Returns the number of lines of the description of the current project.

## Metadata

- Category: Project Data
- Code: 268290
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Count = ProjectGetDescriptionLineCount();
for Line = 1 to Count do
begin
   UIWriteNormal(ProjectGetDescriptionLine(Line));
end;
```

## See also

`ProjectGetDescriptionLine`, `ProjectGetFilename`, `ProjectGetName`
