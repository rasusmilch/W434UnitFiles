# DTDateString

## Declaration

```ats
function DTDateString(DateTime: real): string;
```

## Call pattern

```ats
DTDateString(DateTime);
```

## Description

Converts Date+Time into a string with the date according to the Windows settings.

## Metadata

- Category: Date and Time
- Code: 263172
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
Date = DTDate();
DateString = DTDateString(Date);
UIWriteNormal(Date);
```

## See also

`DTDateTimeString`, `DTNow`, `DTTime`
