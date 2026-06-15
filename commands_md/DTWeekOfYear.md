# DTWeekOfYear

## Declaration

```ats
function DTWeekOfYear(DateTime: real; var Year: integer): integer;
```

## Call pattern

```ats
DTWeekOfYear(DateTime, Year);
```

## Description

Returns the week of the year for the passed date.

The function works accordingly to ISO 8601. This means that the week starts on monday and ends on sunday.

"Year" returns the year with the week.
The reason is that the first week of a year is defined as the firs week with at least four days within the new year.
If the first day of a year is friday, saturday or sunday, DTWeekOfYear will return the last week of the last year for the first three days of the new year.
This applies accordingly to the end of a year. If the last day of a year is monday, tuesday or wednesday, DTWeekOfYear will return the value 1 during the last three days of the last year.

## Metadata

- Category: Date and Time
- Code: 263185
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`
- `var Year`: `integer`

## Example

```ats
Year = 0;
WeekOfYear = DTWeekOfYear(DTGetTestDateTime(), Year);
UIWriteNormal(StrAdd(StrAdd(StrAdd('Week ', WeekOfYear), ' of year '), Year));
```

## See also

`DTDay`, `DTDayOfWeek`, `DTDayOfYear`, `DTGetTestDateTime`, `DTNow`
