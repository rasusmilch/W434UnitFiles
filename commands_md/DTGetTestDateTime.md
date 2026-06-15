# DTGetTestDateTime

## Declaration

```ats
function DTGetTestDateTime(): real;
```

## Call pattern

```ats
DTGetTestDateTime();
```

## Description

Returns the date and the time of the test as a floatingpoint value.

## Metadata

- Category: Date and Time
- Code: 263182
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
DateTime = DTGetTestDateTime();
DateTimeString = DTDateTimeString(DateTime);
UIWriteNormal(DateTimeString);
```

## See also

`DTDateString`, `DTDateTimeString`, `DTNow`, `DTTimeString`
