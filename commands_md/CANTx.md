# CANTx

## Declaration

```ats
function CANTx(Controller: integer; Identifier: integer; Data: tintegerarray): boolean;
```

## Call pattern

```ats
CANTx(<Controller>, $<Identifier>, [<Data>]);
```

## Description

Transmits data on the CAN bus.

## Metadata

- Category: CAN bus
- Code: 270597
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Controller`: `integer` — Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `Identifier`: `integer`
- `Data`: `tintegerarray`

## Return value

The function returns TRUE if it was successfully executed, otherwise FALSE.

## Example

```ats
Success = CANControllerInit(1, CAN_Mode_Extendend, CAN_Speed_250k);
if (Success)
begin
   CANControllerStart(1);
   CANTx(1, $100, [$01, $02]);
   CANControllerStop(1);
end
else
begin
   ErrorCode = CANGetError();
   UIWriteError(StrAdd('CAN error: ', ErrorCode));
end;
```

## See also

`CANControllerInit`, `CANControllerStart`, `CANGetError`
