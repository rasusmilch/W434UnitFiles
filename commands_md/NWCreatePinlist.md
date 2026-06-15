# NWCreatePinlist

## Declaration

```ats
function NWCreatePinlist(PinList: tcreatearray; Component: integer; ComponentData: integer; Search: string; PinData: integer; DoubleAllowed: boolean): integer;
```

## Call pattern

```ats
NWCreatePinlist(PinList, COMPONENT_?, COMPONENTDATA_?, 'Search', COMPONENTPINS_?, TRUE|FALSE);
```

## Description

Creates a list of pins based on the networkdata of the UUT

## Metadata

- Category: Network Access
- Code: 265987
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `PinList`: `tcreatearray`
- `Component`: `integer` — Allowed values: COMPONENT_Wire, COMPONENT_Switch, COMPONENT_Resistor, COMPONENT_Capacitor, COMPONENT_Diode, COMPONENT_ZDiode, COMPONENT_CTwist, COMPONENT_RLCCombination, COMPONENT_VariableResistor
- `ComponentData`: `integer` — Allowed values: COMPONENTDATA_Name, COMPONENTDATA_Information
- `Search`: `string`
- `PinData`: `integer` — Allowed values: COMPONENTPINS_First, COMPONENTPINS_Second, COMPONENTPINS_Both, COMPONENTPINS_Primary
- `DoubleAllowed`: `boolean` — Allowed values: TRUE, FALSE

## Return value

The function returns the numer of found pins.

## Example

```ats
NWCreatePinlist(PinList, COMPONENT_Wire, COMPONENTDATA_Information, '*500*', COMPONENTPINS_Primary, FALSE);
```

## Example notes

The example searches all wires in the information field of all wires whose information field contains the text "500".

Then it searches all primary pins for that wires and returns them in the variable "PinList".

## See also

`MiscAddLists`, `MiscSubtractLists`, `NoConnGroupDB`, `NoConnGroupHV`, `NoConnGroupLV`, `NWGetNetworkPins`, `PinCreateList`, `PinGroupSetHighLow`, `PinsInRange`
