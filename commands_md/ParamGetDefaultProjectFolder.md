# ParamGetDefaultProjectFolder

## Declaration

```ats
function ParamGetDefaultProjectFolder(): string;
```

## Call pattern

```ats
ParamGetDefaultProjectFolder();
```

## Description

Returns the default folder for projects without the trailing backslash.

## Metadata

- Category: Parameters
- Code: 266249
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
File = 'Test.project';
Folder = ParamGetDefaultProjectFolder();
Project = StrAdd(Folder, '\');
Project = StrAdd(Project, File);
UIWriteNormal(Project);
```
