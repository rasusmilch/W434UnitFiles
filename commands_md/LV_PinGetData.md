# LV_PinGetData

## Declaration

```ats
function LV_PinGetData(PinAddress: integer; DataID: integer): string;
```

## Call pattern

```ats
LV_PinGetData(PinAddress, PIN_?);
```

## Description

Returns informations about the pin with address "PinAddress".

## Metadata

- Category: Pin Access
- Code: 268567
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `PinAddress`: `integer`
- `DataID`: `integer` — Allowed values: PIN_AnyName, PIN_Name, PIN_AdapterName, PIN_SysName, PIN_SysNumName, PIN_AnyNameWithComment, PIN_AdapterNameWithComment, PIN_Comment, PIN_AdapterComment, PIN_InstallationZone, PIN_ConnectorName, PIN_ConnectorSeparator, PIN_Info

## Example

```ats
AnyName = LV_PinGetData("1", PIN_AnyName);
```
