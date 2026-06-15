# DTDay

## Declaration

```ats
function DTDay(DateTime: real): integer;
```

## Call pattern

```ats
DTDay(DateTime);
```

## Description

Returns the day from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263176
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
Day = DTDay(DTGetTestDateTime());
UIWriteNormal(Day);
```

## See also

`DTDayOfWeek`, `DTHour`, `DTMilliSecond`, `DTMinute`, `DTMonth`, `DTNow`, `DTSecond`, `DTYear`
