# GPIBSendString

## Declaration

```ats
function GPIBSendString(DeviceAddress: integer; Data: string): boolean;
```

## Call pattern

```ats
GPIBSendString(DeviceAddress, 'Data');
```

## Description

Sends the string "Data" to the device with address "DeviceAddress" on the GPIB.

## Metadata

- Category: GPIB
- Code: 266752
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DeviceAddress`: `integer`
- `Data`: `string`

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
if (GPIBSendString(3, '*IDN?'))
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

`GPIBGetError`, `GPIBReceiveString`, `GPIBSendDeviceCommand`, `GPIBSetTimeout`
