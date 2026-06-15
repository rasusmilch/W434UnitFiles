# PinGetAddress

## Declaration

```ats
function PinGetAddress(PinName: string): integer;
```

## Call pattern

```ats
PinGetAddress('Pin name');
```

## Description

Returns the address of the pin with name "PinName".

## Metadata

- Category: Pin Access
- Code: 268546
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `PinName`: `string`

## Return value

The function returns the address of the passed pin.
If no valid pin name is passed, the function will return PINADDRESS_Invalid (= -2147483647)

## Example

```ats
Address1 = PinGetAddress('Pin1');
Address2 = PinGetAddress('Pin2');
ConnectionTest('', Address1, Address2);
```

## See also

`PinGetCount`, `PinGetData`
