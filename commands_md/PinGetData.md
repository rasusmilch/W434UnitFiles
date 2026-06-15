# PinGetData

## Declaration

```ats
function PinGetData(PinAddress: integer; DataID: integer): string;
```

## Call pattern

```ats
PinGetData(PinAddress, PIN_?);
```

## Description

Returns informations about the pin with address "PinAddress".

## Metadata

- Category: Pin Access
- Code: 268544
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `PinAddress`: `integer`
- `DataID`: `integer` — Allowed values: PIN_AnyName, PIN_Name, PIN_AdapterName, PIN_SysName, PIN_SysNumName, PIN_AnyNameWithComment, PIN_AdapterNameWithComment, PIN_Comment, PIN_AdapterComment, PIN_InstallationZone, PIN_ConnectorName, PIN_ConnectorSeparator, PIN_Led, PIN_4Wire, PIN_IsSplice, PIN_IsolationLVAllowed, PIN_IsolationHVAllowed, PIN_DielectricBreakdownAllowed, PIN_MaxVoltageDC, PIN_MaxVoltageAC, PIN_Info, PIN_AdapterCableName, PIN_UUTSideAdapterConnector, PIN_SystemSideAdapterConnector, PIN_IsPrimary, PIN_ConnectedWires, PIN_IsConnectedWithElectricalComponent, PIN_IsConnectedWithRealPin, PIN_RCompensationValue

## Example

```ats
Count = PinGetCount();
for Pin = 1 to Count do
begin
   AnyName = PinGetData(Pin, PIN_AnyName);
   UIWriteNormal(AnyName);
end;
```

## See also

`PinGetAddress`, `PinGetCount`
