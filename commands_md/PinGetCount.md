# PinGetCount

## Declaration

```ats
function PinGetCount(): integer;
```

## Call pattern

```ats
PinGetCount();
```

## Description

Returns the number of pins inclusively SystemGround.

## Metadata

- Category: Pin Access
- Code: 268545
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
Count = PinGetCount();
for Pin = 0 to Count - 1 do
begin
   AnyName = PinGetData(Pin, PIN_AnyName);
   UIWriteNormal(AnyName);
end;
```

## See also

`PinGetAddress`, `PinGetData`
