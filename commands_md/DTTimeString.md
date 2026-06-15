# DTTimeString

## Declaration

```ats
function DTTimeString(DateTime: real): string;
```

## Call pattern

```ats
DTTimeString(DateTime);
```

## Description

Converts Date+Time into a string with the time according to the Windows settings.

## Metadata

- Category: Date and Time
- Code: 263173
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
Time = DTTime();
TimeString = DTTimeString(Time);
UIWriteNormal(TimeString);
```

## See also

`DTDateTimeString`, `DTNow`, `DTTime`
