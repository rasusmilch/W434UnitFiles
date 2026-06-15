# ProjectSelectionSetComplete

## Declaration

```ats
function ProjectSelectionSetComplete(Complete: boolean): void;
```

## Call pattern

```ats
ProjectSelectionSetComplete(TRUE|FALSE);
```

## Description

Specifies whether the project selection terminated correctly.

## Metadata

- Category: Project Selection
- Code: 264963
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program
- Count result: no
- Archive allowed: no

## Parameters

- `Complete`: `boolean` — Allowed values: TRUE, FALSE

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

`ProjectSelectionEditModuleList`, `ProjectSelectionGetLastProject`, `ProjectSelectionGetProjectFromDialog`, `ProjectSelectionSetAutostartTest`, `ProjectSelectionSetModulelistFile`, `ProjectSelectionSetProjectFile`
