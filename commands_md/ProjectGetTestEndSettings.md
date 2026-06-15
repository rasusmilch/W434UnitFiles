# ProjectGetTestEndSettings

## Declaration

```ats
function ProjectGetTestEndSettings(Value: integer; Index: integer = 0): string;
```

## Call pattern

```ats
ProjectGetTestEndSettings(TESTEND_?);
```

## Description

Returns the settings for test end programs from the tabsheet "Programs" in the project properties.

## Metadata

- Category: Project Data
- Code: 268305
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `integer` — Allowed values: TESTEND_ConfirmReportPrint, TESTEND_UnplugCheck
- `Index`: `integer = 0`

## Example

```ats
ConfirmReportPrint = ProjectGetTestEndSettings(TESTEND_ConfirmReportPrint);
```

## See also

`ProjectGetFilename`, `ProjectGetName`, `ProjectGetTestInitSettings`, `ProjectGetTestStartSettings`
