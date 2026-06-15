# LEDSetTPOff

## Declaration

```ats
function LEDSetTPOff(Pin: tpin): void;
```

## Call pattern

```ats
LEDSetTPOff("Pin");
```

## Description

Turns the LED that is assigned to "Pin" off.

## Metadata

- Category: LED Access
- Code: 264465
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

`LEDResetAll`, `LEDSetOff`, `LEDSetTPOn`
