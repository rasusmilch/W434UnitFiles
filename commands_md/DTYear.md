# DTYear

## Declaration

```ats
function DTYear(DateTime: real): integer;
```

## Call pattern

```ats
DTYear(DateTime);
```

## Description

Returns the year from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263174
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
Year = DTYear(DTGetTestDateTime());
UIWriteNormal(Year);
```

## See also

`DTDay`, `DTDayOfWeek`, `DTGetTestDateTime`, `DTHour`, `DTMilliSecond`, `DTMinute`, `DTMonth`, `DTNow`, `DTSecond`
