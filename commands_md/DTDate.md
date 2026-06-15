# DTDate

## Declaration

```ats
function DTDate(): real;
```

## Call pattern

```ats
DTDate();
```

## Description

Returns the actual date as a floatingpoint value.

## Metadata

- Category: Date and Time
- Code: 263169
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Date = DTDate();
DateString = DTDateString(Date);
UIWriteNormal(DateString);
```

## See also

`DTDateString`, `DTGetTestDateTime`, `DTNow`, `DTTime`
