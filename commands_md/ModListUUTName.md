# ModListUUTName

## Declaration

```ats
function ModListUUTName(): string;
```

## Call pattern

```ats
ModListUUTName();
```

## Description

Returns the UUT name from the modulelist.

## Metadata

- Category: Modulelist
- Code: 267521
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
UUTName = ModListUUTName();
UIWriteNormal(UUTName);
```

## See also

`ModListFilename`, `ModListModuleCount`, `ModListModuleExists`, `ModListModuleFilename`, `ModListModuleName`, `ModListModuleNameExists`
