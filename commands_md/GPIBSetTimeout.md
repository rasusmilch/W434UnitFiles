# GPIBSetTimeout

## Declaration

```ats
function GPIBSetTimeout(Timeout: ttime): boolean;
```

## Call pattern

```ats
GPIBSetTimeout(<Timeout>ms);
```

## Description

Sets the timeout for the receiving of data from the GPIB.

## Metadata

- Category: GPIB
- Code: 266755
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Timeout`: `ttime`

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
if (GPIBSetTimeout(500ms))
begin
   UIWriteNormal('Timeout set');
end
else
begin
   ErrorCode = GPIBGetError();
   UIWriteNormal(StrAdd('Error code: ', ErrorCode));
end;
```

## See also

`GPIBGetError`, `GPIBReceiveString`, `GPIBSendDeviceCommand`, `GPIBSendString`
