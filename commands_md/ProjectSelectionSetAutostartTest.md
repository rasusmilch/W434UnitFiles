# ProjectSelectionSetAutostartTest

## Declaration

```ats
function ProjectSelectionSetAutostartTest(AutoStart: boolean): void;
```

## Call pattern

```ats
ProjectSelectionSetAutostartTest(ON|OFF);
```

## Description

Specifies whether the test shall be started automatically after loading of the project.

## Metadata

- Category: Project Selection
- Code: 264962
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program
- Count result: no
- Archive allowed: no

## Parameters

- `AutoStart`: `boolean` — Allowed values: TRUE, FALSE

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

`ProjectSelectionEditModuleList`, `ProjectSelectionGetLastProject`, `ProjectSelectionGetProjectFromDialog`, `ProjectSelectionSetComplete`, `ProjectSelectionSetModulelistFile`, `ProjectSelectionSetProjectFile`, `TestEndSetNextStep`, `TestInitSetNextStep`
