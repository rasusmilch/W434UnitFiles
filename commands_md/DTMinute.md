# DTMinute

## Declaration

```ats
function DTMinute(DateTime: real): integer;
```

## Call pattern

```ats
DTMinute(DateTime);
```

## Description

Returns the minute from Date+Time.

## Metadata

- Category: Date and Time
- Code: 263179
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
Minute = DTMinute(DTGetTestDateTime());
UIWriteNormal(Minute);
```

## See also

`DTDay`, `DTDayOfWeek`, `DTGetTestDateTime`, `DTHour`, `DTMilliSecond`, `DTMonth`, `DTNow`, `DTSecond`, `DTYear`
