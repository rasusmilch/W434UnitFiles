# ProjectGetChecksum

## Declaration

```ats
function ProjectGetChecksum(Index: integer): integer;
```

## Call pattern

```ats
ProjectGetChecksum(CHECKSUM_?);
```

## Description

Reading checksum from .cats, .param or .cnetlist file.

## Metadata

- Category: Project Data
- Code: 268302
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Index`: `integer` — Allowed values: CHECKSUM_Ats, CHECKSUM_Parameter, CHECKSUM_Netlist

## Example

```ats
Checksum = ProjectGetChecksum(CHECKSUM_Parameter);
ParameterChecksum = StrAdd('Parameter Checksum = ', Checksum);
UIWriteNormal(ParameterChecksum);
```

## See also

`ProjectGetFilename`, `ProjectGetModuleChecksum`, `ProjectGetName`
