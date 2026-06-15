# NWGetComponentData

## Declaration

```ats
function NWGetComponentData(Component: integer; Pin1: tpin; Pin2: tpin; ComponentData: integer; var Value: string): boolean;
```

## Call pattern

```ats
NWGetComponentData(COMPONENT_?, "Pin1", "Pin2", ?_DATA_?, Value);
```

## Description

The values of components can be retrieved with this function during the run time of a test.
The supported components are wires, switches, resistors, capacitors, diodes, Z-diodes, C-Twists, RLC combinations and custom components.

## Metadata

- Category: Network Access
- Code: 265996
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Component`: `integer` — Allowed values: COMPONENT_Wire, COMPONENT_Switch, COMPONENT_Resistor, COMPONENT_Capacitor, COMPONENT_Diode, COMPONENT_ZDiode, COMPONENT_CTwist, COMPONENT_CustomComponent, COMPONENT_RLCCombination, COMPONENT_VariableResistor
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `ComponentData`: `integer` — Data field to be retrieved.; The constants that can be used her depend on the selected kind of component.
; WIRE_DATA_Name, WIRE_DATA_Info, WIRE_DATA_LV_allowed, WIRE_DATA_HV_allowed, WIRE_DATA_DB_allowed
; SWITCH_DATA_Name, SWITCH_DATA_Info, SWITCH_DATA_State
; RESISTOR_DATA_Name, RESISTOR_DATA_Info, RESISTOR_DATA_R, RESISTOR_DATA_LowTol, RESISTOR_DATA_UpTol, RESISTOR_DATA_Pmax
; CAPACITOR_DATA_Name, CAPACITOR_DATA_Info, CAPACITOR_DATA_C, CAPACITOR_DATA_LowTol, CAPACITOR_DATA_UpTol, CAPACITOR_DATA_Umax
; DIODE_DATA_Name, DIODE_DATA_Info, DIODE_DATA_U1, DIODE_DATA_U2, DIODE_DATA_U3, DIODE_DATA_I
; ZDIODE_DATA_Name, ZDIODE_DATA_Info, ZDIODE_DATA_U1, ZDIODE_DATA_U2, ZDIODE_DATA_U3, ZDIODE_DATA_U4, ZDIODE_DATA_I_fwd, ZDIODE_DATA_I_rev
; CTWIST_DATA_Name, CTWIST_DATA_Info, CTWIST_DATA_C, CTWIST_DATA_LowTol, CTWIST_DATA_UpTol
; RLC_DATA_Name, RLC_DATA_Info, RLC_DATA_f, RLC_DATA_Umax, RLC_DATA_Imax
; CUSTOM_COMPONENT_DATA_Name, CUSTOM_COMPONENT_DATA_Info
; For constants with VARIABLE_RESISTOR_DATA_State? the index of the desired state must be passed in "Value".; VARIABLE_RESISTOR_DATA_Name, VARIABLE_RESISTOR_DATA_Info, VARIABLE_RESISTOR_DATA_StateCount, VARIABLE_RESISTOR_DATA_StateName, VARIABLE_RESISTOR_DATA_StateValue, VARIABLE_RESISTOR_DATA_StateLowTol, VARIABLE_RESISTOR_DATA_StateUpTol, VARIABLE_RESISTOR_DATA_StatePmax, VARIABLE_RESISTOR_DATA_StateInfo

- `var Value`: `string` — Variable in whicht the value will be returnd.

## Return value

The function returns TRUE if the value could be retrieved, otherwise FALSE.

## Example

```ats
Value = '';
Success = NWGetComponentData(COMPONENT_Capacitor, "Pin1", "Pin2", CAPACITOR_DATA_C, Value);
if (Success)
begin
   Value = FormatCapacitance(Value);
   Text = StrAdd('Capacitance: ', Value);
   UIWriteNormal(Text);
end
else
begin
   UIWriteWarning('Capacitor not found');
end;
```
