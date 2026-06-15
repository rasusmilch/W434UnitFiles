# LEDSetTPOn

## Declaration

```ats
function LEDSetTPOn(Pin: tpin): void;
```

## Call pattern

```ats
LEDSetTPOn("Pin");
```

## Description

Turns the LED that is assigned to "Pin" on.

## Metadata

- Category: LED Access
- Code: 264464
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Pin`: `tpin`

## Example

```ats
LEDSetTPOn("Pin1");
DTWait(3s);
LEDSetTPOff("Pin1");
```

## See also

`LEDSetOn`, `LEDSetTPOff`
