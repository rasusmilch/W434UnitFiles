# ProjectGetModuleChecksum

## Declaration

```ats
function ProjectGetModuleChecksum(ModulFileName: string): string;
```

## Call pattern

```ats
ProjectGetModuleChecksum('Module1.module');
```

## Description

Gives back the check sum of the module with the given module file name. 

The module must be defined in the project properties. 

All module checksums from all project modules will be calculate on loading the project.


## Metadata

- Category: Project Data
- Code: 268307
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ModulFileName`: `string` — File name of the module; File picker parameter

## Return value

Check sum of the module

## Example

```ats
Checksum = ProjectGetModuleChecksum('Module1.module');
Checksum = StrAdd('Modul 1:', Checksum);
UIInfoDialog(Checksum);
```

## See also

`ProjectGetChecksum`, `ProjectGetModuleCount`, `ProjectGetModuleFileName`, `ProjectGetModuleName`
