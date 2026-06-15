# CANISO15765SetTesterAddress

## Declaration

```ats
function CANISO15765SetTesterAddress(Address: integer): boolean;
```

## Call pattern

```ats
CANISO15765SetTesterAddress(<Address $00-$FE>);
```

## Description

Set the address of the tester for CAN transmissions over the ISO15765 protocol.
Default value is $F9.

## Metadata

- Category: CAN bus
- Code: 270598
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Address`: `integer`

## Return value

The function returns TRUE if it was successfully executed, otherwise FALSE.

## Example

```ats
CANISO15765SetTesterAddress($F9);
```

## See also

`CANGetError`, `CANISO15765TxRxTest`
