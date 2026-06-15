# ReportWriteNormal

## Declaration

```ats
function ReportWriteNormal(Text: string; Forced: boolean=FALSE): void;
```

## Call pattern

```ats
ReportWriteNormal('Text', TRUE|FALSE);
```

## Description

Writes a text into the report.

## Metadata

- Category: Data to Report
- Code: 1792
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`
- `Forced`: `boolean=FALSE` — Specifies, whether the output must be forced independent of parameter settings.; Allowed values: TRUE, FALSE

## Example

```ats
ReportWriteNormal('Text');
ReportWriteNormal('Text', TRUE);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_Text` | `string` | Text which shall be written into the report |

## See also

`ReportWriteError`, `ReportWriteTag`
