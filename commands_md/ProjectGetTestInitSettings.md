# ProjectGetTestInitSettings

## Declaration

```ats
function ProjectGetTestInitSettings(Value: integer; Index: integer = 0): string;
```

## Call pattern

```ats
ProjectGetTestInitSettings(TESTINIT_?);
```

## Description

Returns the settings f�r test initilzation programs from the tabsheet "Programs" in the project properties.

## Metadata

- Category: Project Data
- Code: 268303
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `integer` — Allowed values: TESTINIT_OrderNumber
- `Index`: `integer = 0`

## Example

```ats
OrderNumberEnabled = ProjectGetTestInitSettings(TESTINIT_OrderNumber);
```

## See also

`ProjectGetFilename`, `ProjectGetName`, `ProjectGetTestEndSettings`, `ProjectGetTestStartSettings`
