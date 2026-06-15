# NWGetMetaComponentData

## Declaration

```ats
function NWGetMetaComponentData(Component: integer; PinPrefix: string; ComponentData: integer; var Value: string): boolean;
```

## Call pattern

```ats
NWGetMetaComponentData(COMPONENT_?, 'Pin prefix', ?_DATA_?, Value);
```

## Description

The values of meta components can be retrieved with this function during the run time of a test.
The supported meta components are relays and terminal blocks.

## Metadata

- Category: Network Access
- Code: 265997
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Component`: `integer` — Kind of component; Allowed values: COMPONENT_Relay, COMPONENT_TerminalBlock
- `PinPrefix`: `string` — Pin prefix
- `ComponentData`: `integer` — Data field to be retrieved.; The constants that can be used her depend on the selected kind of component.
; RELAY_DATA_Name, RELAY_DATA_Info, RELAY_DATA_Type, RELAY_DATA_StateCount, RELAY_DATA_StateName, RELAY_DATA_StateStable, RELAY_DATA_CoilActivationVoltage
; TERMINAL_BLOCK_DATA_Name, TERMINAL_BLOCK_DATA_Info, TERMINAL_BLOCK_DATA_Type
- `var Value`: `string` — Variable in whicht the value will be returned.
; The index of the contact for RELAY_DATA_StateName and RELAY_DATA_StateStable must be passed in this variable.

## Return value

The function returns TRUE if the value could be retrieved, otherwise FALSE.

## Example

```ats
Value = '';
Success = NWGetMetaComponentData(COMPONENT_Relay, 'SX93', RELAY_DATA_Type, Value);
if (Success)
begin
   Text = StrAdd('Relay type: ', Value);
   UIWriteNormal(Text);
end
else
begin
   UIWriteWarning('Relay not found');
end;
```

## See also

`NWFindComponents`, `NWGetComponentData`
