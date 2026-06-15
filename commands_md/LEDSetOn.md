# LEDSetOn

## Declaration

```ats
function LEDSetOn(Led: tled): void;
```

## Call pattern

```ats
LEDSetOn("Pin");
```

## Description

Turns the LED "Led" on.

## Metadata

- Category: LED Access
- Code: 264466
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

`LEDSetOn`, `LEDSetTPOff`
