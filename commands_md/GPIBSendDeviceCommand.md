# GPIBSendDeviceCommand

## Declaration

```ats
function GPIBSendDeviceCommand(DeviceAddress: integer; Command: integer): boolean;
```

## Call pattern

```ats
GPIBSendDeviceCommand(DeviceAddress, GPIB_Cmd_?);
```

## Description

Sends a command to the device with address "DeviceAddress" on the GPIB.

## Metadata

- Category: GPIB
- Code: 266754
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DeviceAddress`: `integer`
- `Command`: `integer` — Allowed values: GPIB_Cmd_ClearDevice, GPIB_Cmd_Remote, GPIB_Cmd_Local

## Return value

The function returns TRUE if the operation was successful, otherwise FALSE.

## Example

```ats
if (GPIBSendDeviceCommand(3, GPIB_Cmd_ClearDevice))
begin
   UIWriteNormal('Command sent');
end
else
begin
   ErrorCode = GPIBGetError();
   UIWriteNormal(StrAdd('Error code: ', ErrorCode));
end;
```

## See also

`GPIBGetError`, `GPIBReceiveString`, `GPIBSendString`, `GPIBSetTimeout`
