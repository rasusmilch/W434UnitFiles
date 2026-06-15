# ProjectSelectionGetLastProject

## Declaration

```ats
function ProjectSelectionGetLastProject(): string;
```

## Call pattern

```ats
ProjectSelectionGetLastProject();
```

## Description

Returns the filename of the last open project.

## Metadata

- Category: Project Selection
- Code: 264965
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program
- Count result: no
- Archive allowed: no

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

`ProjectSelectionEditModuleList`, `ProjectSelectionGetProjectFromDialog`, `ProjectSelectionSetAutostartTest`, `ProjectSelectionSetComplete`, `ProjectSelectionSetModulelistFile`, `ProjectSelectionSetProjectFile`
