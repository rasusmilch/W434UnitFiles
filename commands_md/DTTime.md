# DTTime

## Declaration

```ats
function DTTime(): real;
```

## Call pattern

```ats
DTTime();
```

## Description

Returns the actual time as a floatingpoint value.

## Metadata

- Category: Date and Time
- Code: 263170
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Time = DTTime();
TimeString = DTTimeString(Time);
UIWriteNormal(TimeString);
```

## See also

`DTDate`, `DTNow`, `DTTimeString`
