# DTDayOfWeek

## Declaration

```ats
function DTDayOfWeek(DateTime: real): integer;
```

## Call pattern

```ats
DTDayOfWeek(DateTime);
```

## Description

Returns the day of the week from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263177
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
DayOfWeek = DTDayOfWeek(DTGetTestDateTime());
UIWriteNormal(DayOfWeek);
```

## See also

`DTDay`, `DTGetTestDateTime`, `DTHour`, `DTMilliSecond`, `DTMinute`, `DTMonth`, `DTNow`, `DTSecond`, `DTYear`
