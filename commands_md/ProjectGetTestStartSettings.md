# ProjectGetTestStartSettings

## Declaration

```ats
function ProjectGetTestStartSettings(Value: integer; Index: integer = 0): string;
```

## Call pattern

```ats
ProjectGetTestStartSettings(TESTSTART_?, Index);
```

## Description

Returns the settings f�r test start programs from the tabsheet "Programs" in the project properties.

## Metadata

- Category: Project Data
- Code: 268304
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `integer` — Allowed values: TESTSTART_SerialNumber, TESTSTART_InputData
- `Index`: `integer = 0`

## Example

```ats
SerialNumber = ProjectGetTestStartSettings(TESTSTART_SerialNumber);
InputData1 = ProjectGetTestStartSettings(TESTSTART_InputData, 1);
InputData2 = ProjectGetTestStartSettings(TESTSTART_InputData, 2);
```

## See also

`ProjectGetFilename`, `ProjectGetName`, `ProjectGetTestEndSettings`, `ProjectGetTestInitSettings`
