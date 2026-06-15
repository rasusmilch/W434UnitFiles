# ModListFilename

## Declaration

```ats
function ModListFilename(): string;
```

## Call pattern

```ats
ModListFilename();
```

## Description

Returns the filename of the modulelist.

## Metadata

- Category: Modulelist
- Code: 267520
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Filename = ModListFilename();
UIWriteNormal(Filename);
```

## See also

`ModListModuleCount`, `ModListModuleExists`, `ModListModuleFilename`, `ModListModuleName`, `ModListModuleNameExists`, `ModListUUTName`
