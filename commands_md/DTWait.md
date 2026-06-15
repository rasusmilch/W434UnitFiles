# DTWait

## Declaration

```ats
function DTWait(Time: ttime): void;
```

## Call pattern

```ats
DTWait(WaitTime);
```

## Description

Pauses the test for the specified time.

## Metadata

- Category: Date and Time
- Code: 263183
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Time`: `ttime`

## Example

```ats
UIWriteNormal('Waiting for 5s');
DTWait(5s);
UIWriteNormal('Running');
```
