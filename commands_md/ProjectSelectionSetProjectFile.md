# ProjectSelectionSetProjectFile

## Declaration

```ats
function ProjectSelectionSetProjectFile(File: string): void;
```

## Call pattern

```ats
ProjectSelectionSetProjectFile('File');
```

## Description

Selects "File" as the next project to be loaded.

## Metadata

- Category: Project Selection
- Code: 264960
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program
- Count result: no
- Archive allowed: no

## Parameters

- `File`: `string`

## Example

```ats
Complete = TRUE;
Project = ProjectSelectionGetLastProject();
Button = ProjectSelectionGetProjectFromDialog(Project, ['Start automatically']);
switch (Button)
begin
   case DIALOGRESULT_Ok: begin
      ProjectSelectionSetProjectFile(Project);
   end;
   case DIALOGRESULT_Cancel: begin
      Complete = FALSE;
   end;
   case DIALOGRESULT_Button3: begin
      ProjectSelectionSetProjectFile(Project);
      ProjectSelectionSetAutostartTest(TRUE);
   end;
end;
ProjectSelectionSetComplete(Complete);
```

## See also

`ProjectSelectionEditModuleList`, `ProjectSelectionGetLastProject`, `ProjectSelectionGetProjectFromDialog`, `ProjectSelectionSetAutostartTest`, `ProjectSelectionSetComplete`, `ProjectSelectionSetModulelistFile`
