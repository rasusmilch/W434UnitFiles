# ProjectGetFilename

## Declaration

```ats
function ProjectGetFilename(): string;
```

## Call pattern

```ats
ProjectGetFilename();
```

## Description

Returns the filename of the current project.

## Metadata

- Category: Project Data
- Code: 268288
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Filename = ProjectGetFilename();
UIWriteNormal(Filename);
```

## See also

`ProjectGetChecksum`, `ProjectGetCounterValue`, `ProjectGetDescriptionLine`, `ProjectGetDescriptionLineCount`, `ProjectGetModuleCount`, `ProjectGetModuleFilename`, `ProjectGetModuleName`, `ProjectGetName`, `ProjectGetSectionCount`, `ProjectGetSectionName`, `ProjectGetTestEndSettings`, `ProjectGetTestInitSettings`, `ProjectGetTestStartSettings`, `ProjectGetUnitCount`, `ProjectGetUnitFilename`, `ProjectGetUnitName`, `ProjectSectionEnabled`
