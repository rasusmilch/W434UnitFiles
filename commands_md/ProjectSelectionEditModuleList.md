# ProjectSelectionEditModuleList

## Declaration

```ats
function ProjectSelectionEditModuleList(Project: string; var ModuleListFile: string): integer;
```

## Call pattern

```ats
ProjectSelectionEditModuleList(Project, ModuleListFile);
```

## Description

Opens a pop-up window with a check list with all  possible project module names.
Reads the current project module list and check the listed modules.
The modules can be checked or unchecked.
The new module list can be saved with a new file name on window closing.
An already saved list can be loaded.

## Metadata

- Category: Project Selection
- Code: 264967
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Project selection program
- Count result: no
- Archive allowed: no

## Parameters

- `Project`: `string` — Project file name; File picker parameter
- `var ModuleListFile`: `string` — Module list file name; File picker parameter

## Return value

The file name of the saved module list will be returned in variable ModuleListFile.

If no file is saved or opened the current project module list file name will be given back in ModuleListFile.

The function returns which button was pressed..

Possible values:

DIALOGRESULT_Ok, DIALOGRESULT_Cancel

## Example

```ats
Complete = TRUE;
Project = ProjectSelectionGetLastProject();
Button = ProjectSelectionGetProjectFromDialog(Project, []);
switch (Button)
begin
   case DIALOGRESULT_Ok: begin
      ProjectSelectionSetProjectFile(Project);
   end;
   case DIALOGRESULT_Cancel: begin
      Complete = FALSE;
   end;
end;
ProjectSelectionSetComplete(Complete);
if (Complete)
begin
   NewModuleListFile = '';
   Button = ProjectSelectionEditModuleList(Project, NewModuleListFile);
   switch (Button)
   begin
      case DIALOGRESULT_Ok:
      begin
         ProjectSelectionSetModulelistFile(NewModuleListFile);
      end;
      case DIALOGRESULT_Cancel:
      begin
         Complete = FALSE;
      end;
   end;
 end;
```

## See also

`ProjectSelectionGetLastProject`, `ProjectSelectionGetProjectFromDialog`, `ProjectSelectionSetAutostartTest`, `ProjectSelectionSetComplete`, `ProjectSelectionSetModulelistFile`, `ProjectSelectionSetProjectFile`
