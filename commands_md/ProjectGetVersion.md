# ProjectGetVersion

## Declaration

```ats
function ProjectGetVersion(Version: integer; Format: string = ''): string;
```

## Call pattern

```ats
ProjectGetVersion(VERSION_?, '<Format>');
```

## Description

Returns the version number of the project or parts of it.

## Metadata

- Category: Project Data
- Code: 268308
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Version`: `integer` — Allowed values: VERSION_Full_Version, VERSION_Major_Version, VERSION_Minor_Version, VERSION_Revision
- `Format`: `string = ''` — The number of #-characters defines the minimum number of decimal places.
; If VERSION_Full_Version is used the numbers will be inserted in the sequence Major Version - Minor Version - Revision.
; If an empty string is passed for the format, the pattern '#.##.##' will be used for VERSION_Full_Version.; '#' will be used for all other constants.

## Example

```ats
FullVersion = ProjectGetVersion(VERSION_Full_Version, '#.##-##');
UIWriteNormal(StrAdd('Full Version: ', FullVersion));

MajorVersion = ProjectGetVersion(VERSION_Major_Version, '##');
UIWriteNormal(StrAdd('Major Version: ', MajorVersion));

MinorVersion = ProjectGetVersion(VERSION_Minor_Version, '###');
UIWriteNormal(StrAdd('Minor Version: ', MinorVersion));

Revision = ProjectGetVersion(VERSION_Revision, '####');
UIWriteNormal(StrAdd('Revision: ', Revision));
```

## See also

`MiscGetVersion`
