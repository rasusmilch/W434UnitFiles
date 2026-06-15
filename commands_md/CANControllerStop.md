# CANControllerStop

## Declaration

```ats
function CANControllerStop(Controller: integer): boolean;
```

## Call pattern

```ats
CANControllerStop(<Controller>);
```

## Description

Stops a CAN controller

## Metadata

- Category: CAN bus
- Code: 270594
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Controller`: `integer` — Number of the controller; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8

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

`CANControllerStart`, `CANGetError`
