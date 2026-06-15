# PinGuard

## Declaration

```ats
function PinGuard(GuardPins: tpinarray): void;
```

## Call pattern

```ats
PinGuard(["GuardPin1", "GuardPin2", ...]);
```

## Description

Sets the passed pins to guard when executing the next two pole command.

## Metadata

- Category: Pin Access
- Code: 268564
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `GuardPins`: `tpinarray`

## Example

```ats
PinGuard(["75", "78"]);
ResistorTest('R1', "1", "2");
```

## See also

`CapacitorTest`, `MeasureRLC`, `ResistorTest`, `ResistorTestCustom`
