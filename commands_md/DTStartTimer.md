# DTStartTimer

## Declaration

```ats
function DTStartTimer(TimerName: string): void;
```

## Call pattern

```ats
DTStartTimer('TimerName');
```

## Description

Starts a timer with a free selectable name.
The resolution of the timer is 1ms.

## Metadata

- Category: Date and Time
- Code: 263186
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

`DTGetTimer`, `DTWait`
