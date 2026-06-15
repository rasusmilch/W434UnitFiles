# CANRtr

## Declaration

```ats
function CANRtr(Controller: integer; RequestedIdentifier: integer; RequestedDataLength: integer): boolean;
```

## Call pattern

```ats
CANRtr(<Controller 1-8>, $<RequestedIdentifier>, <RequestedDataLength 0-8>);
```

## Description

The function sends a remote frame (RTR) on the CAN bus.

## Metadata

- Category: CAN bus
- Code: 270600
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Controller`: `integer`
- `RequestedIdentifier`: `integer`
- `RequestedDataLength`: `integer`

## Return value

The function returns TRUE if it was successfully executed, otherwise FALSE.

## Example

```ats
function can_test1(Name: string; Controller: integer; Identifier: integer;
            DataLength: integer; Data: tarray;
            var Pass: boolean; var Fail: boolean): void;
begin
   if ((DataLength >= 2) AND (Data[2] == $10))
   begin
      Pass = TRUE;
   end;
end;

function main(): void;
begin
   UIClearScreen();

   Success = CANControllerInit(1, CAN_Mode_Extendend, CAN_Speed_250k);
   if (Success)
   begin
      CANControllerStart(1);
      CANRtr(1, $100, 2);
      CANRxTest('Test 1', 1, $100, can_test1, 10s);
      CANControllerStop(1);
   end
   else
   begin
      ErrorCode = CANGetError();
      UIWriteError(StrAdd('CAN error: ', ErrorCode));
   end;
end;
```

## See also

`CANControllerGetError`, `CANControllerInit`, `CANControllerStart`, `CANRtrRxTest`, `CANRxTest`, `CANTx`
