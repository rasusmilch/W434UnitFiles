# UIBeep

## Declaration

```ats
function UIBeep(Frequency: tfrequency; Time: ttime; UseSoundCard: boolean = FALSE): void;
```

## Call pattern

```ats
UIBeep(<Frequency>Hz, <Time>ms);
```

## Description

Produces a beep with the passed frequency and the passed duration on the system speaker or the sound card

## Metadata

- Category: Userinterface Access
- Code: 263980
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Frequency`: `tfrequency`
- `Time`: `ttime`
- `UseSoundCard`: `boolean = FALSE` — Plays the beep on the soundcard if TRUE is passed.; Allowed values: TRUE, FALSE

## Example

```ats
UIBeep(1000Hz, 1000ms);
UIBeep(440Hz, 500ms, TRUE);

```

## See also

`UIWriteError`, `UIWriteNormal`, `UIWriteWarning`
