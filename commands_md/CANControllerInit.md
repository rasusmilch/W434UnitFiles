# CANControllerInit

## Declaration

```ats
function CANControllerInit(Controller: integer; Mode: integer; Speed: integer): boolean;
```

## Call pattern

```ats
CANControllerInit(<Controller>, <Mode>, <Speed>);
```

## Description

Sets Mode and Speed for a CAN controller

## Metadata

- Category: CAN bus
- Code: 270592
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Controller`: `integer` — Number of the controller; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `Mode`: `integer` — Mode (Standard = 11 bit identifier, Extended = 29 bit identifier); Allowed values: CAN_Mode_Standard, CAN_Mode_Extended
- `Speed`: `integer` — Transmission rate; Allowed values: CAN_Speed_10k, CAN_Speed_20k, CAN_Speed_50k, CAN_Speed_100k, CAN_Speed_125k, CAN_Speed_250k, CAN_Speed_500k, CAN_Speed_800k, CAN_Speed_1000k

## Return value

The function returns TRUE if it was successfully executed, otherwise FALSE.

## Example

```ats
Success = CANControllerInit(1, CAN_Mode_Extended, CAN_Speed_250k);
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
