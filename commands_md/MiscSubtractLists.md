# MiscSubtractLists

## Declaration

```ats
function MiscSubtractLists(ResultList: tcreatearray; List1: tarray; List2: tarray): integer;
```

## Call pattern

```ats
MiscSubtractLists(ResultList, List1, List2);
```

## Description

Returns a list which contains all items from List1 which are not in List2 as well.

## Metadata

- Category: Miscellaneous
- Code: 266513
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ResultList`: `tcreatearray`
- `List1`: `tarray`
- `List2`: `tarray`

## Return value

The function returns the number of items in the result list.

## Example

```ats
PinsInRange(RangePins, "Pin1", "Pin32");
NWGetNetworkPins(NetworkPins, "1", [COMPONENT_Wire, COMPONENT_Switch], CLOSED, TRUE);
PinCount = MiscSubtractLists(Pins, RangePins, NetworkPins);
for Index = 1 to PinCount do
begin
   UIWriteNormal(PinGetData(Pins[Index], PIN_AnyName));
end;
```

## See also

`MiscAddLists`, `NoConnGroupDB`, `NoConnGroupHV`, `NoConnGroupLV`, `NWCreatePinlist`, `NWGetNetworkPins`, `PinCreateList`, `PinGroupSetHighLow`, `PinsInRange`
