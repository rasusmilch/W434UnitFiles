# ProjectSelectionGetProjectFromDialog

## Declaration

```ats
function ProjectSelectionGetProjectFromDialog(var Project: string; CustomButtons: tstringarray): integer;
```

## Call pattern

```ats
ProjectSelectionGetProjectFromDialog(<SelectedProject>, []);
```

## Description

Opens a pop-up window for project selection.

The filename of a project which will be preselected can be passed in "Project".

## Metadata

- Category: Project Selection
- Code: 264964
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program
- Count result: no
- Archive allowed: no

## Parameters

- `var Project`: `string`
- `CustomButtons`: `tstringarray` — Captions for up to 10 more buttons

## Return value

The function returns which button was pressed.

Possible values:

DIALOGRESULT_Ok, DIALOGRESULT_Cancel, DIALOGRESULT_Button3, DIALOGRESULT_Button4, DIALOGRESULT_Button5, DIALOGRESULT_Button6, DIALOGRESULT_Button7, DIALOGRESULT_Button8, DIALOGRESULT_Button9, DIALOGRESULT_Button10, DIALOGRESULT_Button11, DIALOGRESULT_Button12

The filename of the selected project is returned in "Project".

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

`ProjectSelectionEditModuleList`, `ProjectSelectionGetLastProject`, `ProjectSelectionSetAutostartTest`, `ProjectSelectionSetComplete`, `ProjectSelectionSetModulelistFile`, `ProjectSelectionSetProjectFile`
