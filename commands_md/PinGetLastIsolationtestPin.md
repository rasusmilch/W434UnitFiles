# PinGetLastIsolationtestPin

## Declaration

```ats
function PinGetLastIsolationtestPin(): integer;
```

## Call pattern

```ats
PinGetLastIsolationtestPin();
```

## Description

Returns the last pin that was tested during an automatic isolation test if this test was aborted.

## Metadata

- Category: Pin Access
- Code: 268561
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Pin = PinGetLastIsolationtestPin();
Cable = PinGetData(Pin, PIN_AdapterCableName);
UIWriteNormal(Cable);
```
