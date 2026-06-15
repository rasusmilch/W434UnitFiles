# GPIBGetError

## Declaration

```ats
function GPIBGetError(): integer;
```

## Call pattern

```ats
GPIBGetError();
```

## Description

Returns the error code of the last GPIB operation.

## Metadata

- Category: GPIB
- Code: 266756
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Return value

Possible values:

GPIB_Error_None, GPIB_Error_CIC, GPIB_Error_NoListeners, GPIB_Error_InvalidAddress, GPIB_Error_InvalidArgument, GPIB_Error_SAC,
GPIB_Error_OperationAborted, GPIB_Error_InvalidBoard, GPIB_Error_DMA, GPIB_Error_OperationNotComplete, GPIB_Error_NoCapability,
GPIB_Error_FileSystem, GPIB_Error_CommandError, GPIB_Error_StatusByteLost, GPIB_Error_SRQ, GPIB_Error_BufferFull,  GPIB_Error_Locked,
GPIB_Error_System, GPIB_Error_NoInit, GPIB_Error_InvalidDevice, GPIB_Error_InvalidCommand

## Example

```ats
if (GPIBSendString(1, '*IDN?'))
begin
   UIWriteNormal('Data sent');
end
else
begin
   ErrorCode = GPIBGetError();
   UIWriteNormal(StrAdd('Error code: ', ErrorCode));
end;
```

## See also

`GPIBReceiveString`, `GPIBSendDeviceCommand`, `GPIBSendString`, `GPIBSetTimeout`
