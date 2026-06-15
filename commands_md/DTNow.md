# DTNow

## Declaration

```ats
function DTNow(): real;
```

## Call pattern

```ats
DTNow();
```

## Description

Returns the actual date and the actual time as a floatingpoint value.

## Metadata

- Category: Date and Time
- Code: 263168
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Now = DTNow();
NowString = DTDateTimeString(Now);
UIWriteNormal(NowString);
```

## See also

`DTDate`, `DTDateTimeString`, `DTGetTestDateTime`, `DTTime`
