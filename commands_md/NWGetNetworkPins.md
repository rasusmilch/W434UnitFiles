# NWGetNetworkPins

## Declaration

```ats
function NWGetNetworkPins(PinList: tcreatearray; Pin: tpin; Components: tintegerarray; SwitchState: integer; WithSplices: boolean = FALSE): integer;
```

## Call pattern

```ats
NWGetNetworkPins(PinList, "Pin", [COMPONENT_?, COMPONENT_?, ...], OPEN|CLOSED|ANY, TRUE|FALSE);
```

## Description

The function searches all pins which are connected to the passed pin and returns them in list.

It is possible to specify which components and switchs states are taken into account as a "connection".

## Metadata

- Category: Network Access
- Code: 266009
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinList`: `tcreatearray` — Variable in which the pin addresses will be returned
- `Pin`: `tpin` — All pins which are connected to this pin will be returned
- `Components`: `tintegerarray` — List of components which are taken into account as a connection; Allowed values: COMPONENT_Wire, COMPONENT_Switch, COMPONENT_Resistor, COMPONENT_Capacitor, COMPONENT_Diode, COMPONENT_ZDiode, COMPONENT_CTwist, COMPONENT_RLCCombination, COMPONENT_Attenuator, COMPONENT_CustomComponent, COMPONENT_VariableResistor
- `SwitchState`: `integer` — State of teh switches which are taken into account as a connection; Allowed values: OPEN, CLOSED, ANY
- `WithSplices`: `boolean = FALSE` — If TRUE is passed splices and real pins will be returned. If FALSE is passed only real pins will be returned.; Allowed values: TRUE, FALSE

## Return value

The function returns the number of found pins.

The addresses of the found pins will be returned in "PinList".
The addresses are ascending sorted.

## Example

```ats
Count = NWGetNetworkPins(NetworkPins, "1", [COMPONENT_Wire, COMPONENT_Resistor, COMPONENT_Switch], ANY);
for Index = 1 to Count do
begin
   UIWriteNormal(PinGetData(NetworkPins[Index], PIN_AnyName));
end;
```

## See also

`MiscAddLists`, `MiscSubtractLists`, `NoConnGroupDB`, `NoConnGroupHV`, `NoConnGroupLV`, `NWCreatePinlist`, `PinCreateList`, `PinGroupSetHighLow`, `PinsInRange`
