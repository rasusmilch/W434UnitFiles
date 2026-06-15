# PinCreateList

## Declaration

```ats
function PinCreateList(ListVariable: tcreatearray; DataID: integer; SearchText: string; IncludeSplices: boolean = FALSE): integer;
```

## Call pattern

```ats
PinCreateList(ListVariable, PIN_?, 'SearchText');
```

## Description

Creates a list of pins depending on "DataID" and "Text" and returns the number of elements in the list.

## Metadata

- Category: Pin Access
- Code: 268547
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ListVariable`: `tcreatearray`
- `DataID`: `integer` — Allowed values: PIN_AnyName, PIN_Name, PIN_AdapterName, PIN_SysName, PIN_SysNumName, PIN_AnyNameWithComment, PIN_AdapterNameWIthComment, PIN_Comment, PIN_AdapterComment, PIN_InstallationZone, PIN_ConnectorName, PIN_ConnectorSeparator, PIN_Led, PIN_4Wire, PIN_IsSplice, PIN_IsolationLVAllowed, PIN_IsolationHVAllowed, PIN_DielectricBreakdownAllowed, PIN_MaxVoltageDC, PIN_MaxVoltageAC, PIN_Info
- `SearchText`: `string`
- `IncludeSplices`: `boolean = FALSE` — Allowed values: TRUE, FALSE

## Example

```ats
PinCreateList(List110, PIN_Info, '110V');
PinCreateList(List24, PIN_Info, '24V');
PinCreateList(ListGround, PIN_Info, 'Ground');
NoConnGroupLV('GroupTest1', '110V', List110, 'Ground', ListGround);
NoConnGroupLV('GroupTest2', '24V', List24, 'Ground', ListGround);
MiscAddLists(List, List110, List24);
NoConnGroupLV('GroupTest3', '24V + 110V', List, 'Ground', ListGround);
```

## See also

`MiscAddLists`, `MiscSubtractLists`, `NoConnGroupDB`, `NoConnGroupHV`, `NoConnGroupLV`, `NWCreatePinlist`, `NWGetNetworkPins`, `PinGroupSetHighLow`, `PinsInRange`
