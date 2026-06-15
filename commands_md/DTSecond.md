# DTSecond

## Declaration

```ats
function DTSecond(DateTime: real): integer;
```

## Call pattern

```ats
DTSecond(DateTime);
```

## Description

Returns the second from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263180
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
Second = DTSecond(DTGetTestDateTime());
UIWriteNormal(Second);
```

## See also

`DTDay`, `DTDayOfWeek`, `DTGetTestDateTime`, `DTHour`, `DTMilliSecond`, `DTMinute`, `DTMonth`, `DTNow`, `DTYear`
