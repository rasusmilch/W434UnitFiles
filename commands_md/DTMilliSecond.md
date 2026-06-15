# DTMilliSecond

## Declaration

```ats
function DTMilliSecond(DateTime: real): integer;
```

## Call pattern

```ats
DTMilliSecond(DateTime);
```

## Description

Returns the millisecond from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263181
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
MilliSecond = DTMilliSecond(DTGetTestDateTime());
UIWriteNormal(MilliSecond);
```

## See also

`DTDay`, `DTDayOfWeek`, `DTGetTestDateTime`, `DTHour`, `DTMinute`, `DTMonth`, `DTNow`, `DTSecond`, `DTYear`
