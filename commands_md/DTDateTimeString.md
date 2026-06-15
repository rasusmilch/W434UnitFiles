# DTDateTimeString

## Declaration

```ats
function DTDateTimeString(DateTime: real): string;
```

## Call pattern

```ats
DTDateTimeString(DateTime);
```

## Description

Converts Date+Time into a string with the date and the time according to the Windows settings.

## Metadata

- Category: Date and Time
- Code: 263171
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DateTime`: `real`

## Example

```ats
TestDateTime = DTGetTestDateTime();
TestDateTimeString = DTDateTimeString(TestDateTime);
UIWriteNormal(TestDateTimeString);
```

## See also

`DTDateString`, `DTGetTestDateTime`, `DTNow`, `DTTimeString`
