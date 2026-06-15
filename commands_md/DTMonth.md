# DTMonth

## Declaration

```ats
function DTMonth(DateTime: real): integer;
```

## Call pattern

```ats
DTMonth(DateTime);
```

## Description

Returns the month from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263175
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
Month = DTMonth(DTGetTestDateTime());
UIWriteNormal(Month);
```

## See also

`DTDay`, `DTDayOfWeek`, `DTGetTestDateTime`, `DTHour`, `DTMilliSecond`, `DTMinute`, `DTNow`, `DTSecond`, `DTYear`
