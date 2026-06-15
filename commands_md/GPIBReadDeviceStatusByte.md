# GPIBReadDeviceStatusByte

## Declaration

```ats
function GPIBReadDeviceStatusByte(DeviceAddress: integer; var StatusByte: integer): boolean;
```

## Call pattern

```ats
GPIBReadDeviceStatusByte(DeviceAddress, StatusByte);
```

## Description

Reads the status byte of the specified device and returns the value in "StatusByte".

## Metadata

- Category: GPIB
- Code: 266758
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DeviceAddress`: `integer`
- `var StatusByte`: `integer`

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
StatusByte = 0;
if (GPIBReadDeviceStatusByte(3, StatusByte))
begin
   UIWriteNormal(StrAdd('Status byte: ', StatusByte));
end
else
begin
   ErrorCode = GPIBGetError();
   UIWriteNormal(StrAdd('Error code: ', ErrorCode));
end;
```

## See also

`GPIBGetError`, `GPIBSendDeviceCommand`, `GPIBSendString`, `GPIBSetEOSValue`, `GPIBSetTimeout`
