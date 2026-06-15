# PinSetLowAll

## Declaration

```ats
function PinSetLowAll(CheckPins: boolean = FALSE): void;
```

## Call pattern

```ats
PinSetLowAll();
```

## Description

Sets all pins of the matrix to Low.

## Metadata

- Category: Pin Access
- Code: 268554
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `CheckPins`: `boolean = FALSE` — If TRUE is passed a test will be done whether the pins are really set to "Low".
; This can last some minutes.; Allowed values: TRUE, FALSE

## Example

```ats
PinSetLowAll();
```

## See also

`PinSetHighLow`, `PinSetOffAll`
