# PinsInRange

## Declaration

```ats
function PinsInRange(PinList: tcreatearray; FromPin: tpin; ToPin: tpin; IncludeFromPin: boolean = TRUE; IncludeToPin: boolean = TRUE): integer;
```

## Call pattern

```ats
PinsInRange(PinList, "FromPin", "ToPin", TRUE|FALSE, TRUE|FALSE);
```

## Description

The function returns a list of pins which are within the specified pin range.

NOTICE: The function can not be used if the test project works with adapter cables from the adapter cable library.

## Metadata

- Category: Pin Access
- Code: 268566
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinList`: `tcreatearray` — Variable in which the pin addresses will be returned
- `FromPin`: `tpin` — Begin of the range
- `ToPin`: `tpin` — End of the range
- `IncludeFromPin`: `boolean = TRUE` — If TRUE is passed the specified from-pin will be added to the list.; Allowed values: TRUE, FALSE
- `IncludeToPin`: `boolean = TRUE` — If TRUE is passed the specified to-pin will be added to the list.; Allowed values: TRUE, FALSE

## Return value

The function returns the number of pins in the pin list.

The addresses of the found pins will be returned in "PinList".

## Example

```ats
Count = PinsInRange(RangePins, "Pin1", "Pin33");
for Index = 1 to Count do
begin
   UIWriteNormal(PinGetData(RangePins[Index], PIN_AnyName, TRUE, FALSE));
end;
```

## See also

`MiscAddLists`, `MiscSubtractLists`, `NoConnGroupDB`, `NoConnGroupHV`, `NoConnGroupLV`, `NWCreatePinlist`, `NWGetNetworkPins`, `PinCreateList`, `PinGroupSetHighLow`
