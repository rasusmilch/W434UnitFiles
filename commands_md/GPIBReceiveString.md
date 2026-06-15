# GPIBReceiveString

## Declaration

```ats
function GPIBReceiveString(DeviceAddress: integer; var Data: string): boolean;
```

## Call pattern

```ats
GPIBReceiveString(DeviceAddress, Data);
```

## Description

Receives a string from the device with address "DeviceAddress" on the GPIB and returns it in "Data".

## Metadata

- Category: GPIB
- Code: 266753
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DeviceAddress`: `integer`
- `var Data`: `string`

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
Data = '';
if (GPIBReceiveString(3, Data))
begin
   UIWriteNormal(StrAdd('Data: ', Data));
end
else
begin
   ErrorCode = GPIBGetError();
   UIWriteNormal(StrAdd('Error code: ', ErrorCode));
end;
```

## See also

`GPIBGetError`, `GPIBSendDeviceCommand`, `GPIBSendString`, `GPIBSetEOSValue`, `GPIBSetTimeout`
