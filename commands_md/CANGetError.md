# CANGetError

## Declaration

```ats
function CANGetError(): integer;
```

## Call pattern

```ats
CANGetError();
```

## Description

Returns the error code of the last CAN operation

## Metadata

- Category: CAN bus
- Code: 270596
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Return value

Possible values:

CAN_Error_None, CAN_Error_NoHardwareDriver, CAN_Error_InvalidState, CAN_Error_InvalidSpeed, CAN_Error_HardwareDriver,
CAN_Error_InvalidController, CAN_Error_InvalidMode, CAN_Error_ISO15765_InvalidAddress, CAN_Error_NoDataReceived

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

`CANControllerInit`, `CANControllerSetAcceptanceFilter`, `CANControllerStart`, `CANControllerStop`, `CANISO15765TxRxTest`, `CANRxTest`, `CANTx`, `CANTxRxTest`
