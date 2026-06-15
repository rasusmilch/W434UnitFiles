# DTGetTimer

## Declaration

```ats
function DTGetTimer(TimerName: string): real;
```

## Call pattern

```ats
DTGetTimer('TimerName');
```

## Description

Returns the current value of the passed timer.
The timer must have been startet with DTStartTimer before.
If it was not started the function will return TIMER_NotFound.

## Metadata

- Category: Date and Time
- Code: 263187
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `TimerName`: `string`

## Example

```ats
DTStartTimer('Duration Wires');
TestWires();
Duration = DTGetTimer('Duration Wires');
UIWriteNormal(FormatTime(Duration));
```

## See also

`DTStartTimer`, `DTWait`
