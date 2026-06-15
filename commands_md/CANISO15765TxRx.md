# CANISO15765TxRx

## Declaration

```ats
function CANISO15765TxRx(Controller: integer; TargetAddress: integer; Priority: integer; TxData: tintegerarray; Timeout: ttime; var RxDataLength: integer; RxData: tcreatearray): boolean;
```

## Call pattern

```ats
CANISO15765TxRx(<Controller 1-8>, <TargetAddress $00-$FE>, <Priority 1-7>, [<TxData>], <Timeout>s, RxDataLength, RxData);
```

## Description

Transmits data on the CAN bus by using the ISO15765 protocol.
Afterwards the reply is received and returned in RxDataLength and RxData.

Autostart for CAN is ignored for this function.

## Metadata

- Category: CAN bus
- Code: 270599
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Controller`: `integer` — Number of the controller
; The extended mode must be set for this controller.; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8
- `TargetAddress`: `integer` — Address of the device to which the message shall be sent. ($00 - $FE)
- `Priority`: `integer` — Priority of the message (0-7)
- `TxData`: `tintegerarray` — Data to be sent
- `Timeout`: `ttime` — Maximum time the test system waits for a reply.
- `var RxDataLength`: `integer` — Variable in which the number of received data bytes is returned.
- `RxData`: `tcreatearray` — Variable in which the received data bytes are returned.

## Return value

The function returns TRUE if it was successfully executed, otherwise FALSE.

## Example

```ats
CANControllerInit(1, CAN_Mode_Extended, CAN_Speed_250k);
CANISO15765SetAddress($F9);
CANControllerStart(1);
RxDataLength = 0;
Success = CANISO16765TxRx(1, $FE, 3, [$21, $01, $01, $01], 10s,
             RxDataLength, RxData);
if (Success)
begin
   UIWriteNormal(StrAdd('Rx data length: ', RxDataLength));
   for Count = 1 to RxDataLength do
   begin
      UIWriteNormal(StrAdd('$', FormatIntToHex(RxData[Count], 2)));
   end;
end
else
begin
   UIWriteError(StrAdd('Error code: ', CANGetError()));
end;
CANControllerStop(1);
```
