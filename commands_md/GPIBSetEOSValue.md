# GPIBSetEOSValue

## Declaration

```ats
function GPIBSetEOSValue(DeviceAddress: integer; EOSValue: integer): boolean;
```

## Call pattern

```ats
GPIBSetEOSValue(DeviceAddress, EOSValue);
```

## Description

With this function the character for the end-of-transmission-signalling can be set for a device on the GPIB bus.

The default value can be set by using GPIB_EOS_Default.

## Metadata

- Category: GPIB
- Code: 266757
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `DeviceAddress`: `integer`
- `EOSValue`: `integer` — Allowed values: GPIB_EOS_Default

## Example

```ats
GPIBSetEOSValue(5, 10);
Success = GBIBReceiveString(5, ReceiveString);
GPIBSetEOSValue(5, GPIB_EOS_Default);
```

## See also

`GBIBReceiveString`
