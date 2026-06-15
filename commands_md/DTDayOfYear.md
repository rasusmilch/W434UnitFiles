# DTDayOfYear

## Declaration

```ats
function DTDayOfYear(DateTime: real): integer;
```

## Call pattern

```ats
DTDayOfYear(DateTime);
```

## Description

Returns the day of the year from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263184
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
DayOfYear = DTDayOfYear(DTGetTestDateTime());
UIWriteNormal(DayOfYear);
```

## See also

`DTDay`, `DTDayOfWeek`, `DTGetTestDateTime`, `DTNow`, `DTWeekOfYear`
