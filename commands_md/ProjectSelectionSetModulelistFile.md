# ProjectSelectionSetModulelistFile

## Declaration

```ats
function ProjectSelectionSetModulelistFile(File: string): void;
```

## Call pattern

```ats
ProjectSelectionSetModulelistFile('File');
```

## Description

Selects "File" as the next modulelist to be loaded.

## Metadata

- Category: Project Selection
- Code: 264961
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Project selection program
- Count result: no
- Archive allowed: no

## Parameters

- `File`: `string`

## Example

```ats
ProjectSelectionSetModulelistFile('.\Projects\ModuleList1.txt');
```

## See also

`ProjectSelectionEditModuleList`, `ProjectSelectionGetLastProject`, `ProjectSelectionGetProjectFromDialog`, `ProjectSelectionSetAutostartTest`, `ProjectSelectionSetComplete`, `ProjectSelectionSetProjectFile`
