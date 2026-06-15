# LEDSetAbsOn

## Declaration

```ats
function LEDSetAbsOn(Led: tledabs): void;
```

## Call pattern

```ats
LEDSetAbsOn("X.Y");
```

## Description

Turns the absolutely addressed LED "X.Y" on.

## Metadata

- Category: LED Access
- Code: 264468
- Visible in alphabetical index: yes
- Deprecated: yes
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Led`: `tledabs`

## Example

```ats
LEDSetAbsOn("14.a1");
DTWait(3s);
LEDSetAbsOff("14.a1");
```

## See also

`LEDSetOn`, `LEDSetTPOn`
