# ReportWriteTag

## Declaration

```ats
function ReportWriteTag(Tag: string; Text: string): void;
```

## Call pattern

```ats
ReportWriteTag('Tag', 'Text');
```

## Description

Writes a text, depending on Tag into the report.

## Metadata

- Category: Data to Report
- Code: 1794
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Tag`: `string`
- `Text`: `string`

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_Text` | `string` | Text which shall be written into the report |
| `RES_Tag` | `string` | Custom defined tag for the text |

## See also

`ReportWriteError`, `ReportWriteNormal`
