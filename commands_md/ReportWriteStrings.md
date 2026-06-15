# ReportWriteStrings

## Declaration

```ats
function ReportWriteStrings(Text: string; Strings: tstringarray): void;
```

## Call pattern

```ats
ReportWriteStrings('Text', ['String1', 'String2', ...]);
```

## Description

Writes the passed texts into the report.

## Metadata

- Category: Data to Report
- Code: 1796
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`
- `Strings`: `tstringarray`

## Example

```ats
ReportWriteStrings('Text', ['String1', 'String2']);
```

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_Text` | `string` | Text |
| `RES_StringCount` | `integer` | Number of texts in the list. |
| `RES_Strings[ ]` | `string` | Texts of the list |
