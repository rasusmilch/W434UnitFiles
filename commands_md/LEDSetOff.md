# LEDSetOff

## Declaration

```ats
function LEDSetOff(Led: tled): void;
```

## Call pattern

```ats
LEDSetOff("Led");
```

## Description

Turns the LED "Led" off.

## Metadata

- Category: LED Access
- Code: 264467
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Led`: `tled`

## Example

```ats
LEDSetOn("Led1");
DTWait(3s);
LEDSetOff("Led1");
```

## See also

`LEDResetAll`, `LEDSetOff`, `LEDSetTPOn`
