# ProjectGetName

## Declaration

```ats
function ProjectGetName(): string;
```

## Call pattern

```ats
ProjectGetName();
```

## Description

Returns the name of the current project.

## Metadata

- Category: Project Data
- Code: 268289
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Name = ProjectGetName();
UIWriteNormal(Name);
```

## See also

`ProjectGetChecksum`, `ProjectGetCounterValue`, `ProjectGetDescriptionLine`, `ProjectGetDescriptionLineCount`, `ProjectGetFilename`, `ProjectGetModuleCount`, `ProjectGetModuleFilename`, `ProjectGetModuleName`, `ProjectGetSectionCount`, `ProjectGetSectionName`, `ProjectGetTestEndSettings`, `ProjectGetTestInitSettings`, `ProjectGetTestStartSettings`, `ProjectGetUnitCount`, `ProjectGetUnitFilename`, `ProjectGetUnitName`, `ProjectSectionEnabled`
