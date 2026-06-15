# PrintReport

## Declaration

```ats
function PrintReport(ReportName: string): void;
```

## Call pattern

```ats
PrintReport('ReportName');
```

## Description

Prints the report or label with the name "ReportName".

## Metadata

- Category: Printing and Archiving
- Code: 265729
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ReportName`: `string`

## Example

```ats
PrintReport('My report');
```

## See also

`PrintAllLabels`, `PrintAllReports`
