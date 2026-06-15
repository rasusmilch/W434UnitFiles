# DTHour

## Declaration

```ats
function DTHour(DateTime: real): integer;
```

## Call pattern

```ats
DTHour(DateTime);
```

## Description

Returns the hour from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263178
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
Hour = DTHour(DTGetTestDateTime());
UIWriteNormal(Hour);
```

## See also

`DTDay`, `DTDayOfWeek`, `DTGetTestDateTime`, `DTMilliSecond`, `DTMinute`, `DTMonth`, `DTNow`, `DTSecond`, `DTYear`
