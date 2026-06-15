# NWFindComponents

## Declaration

```ats
function NWFindComponents(Components: tcreatearray; Component: integer; ComponentData: integer; Search: string; Module: string = MODULE_All): integer;
```

## Call pattern

```ats
NWFindComponents(FoundComponents, COMPONENT_?, COMPONENT_DATA_?, 'Search', MODULE_?);
```

## Description

The function searches with a keyword for components in the net list and returns them in a variable.
It is possible to search for component names and component information.

The function does not find components which were automatically added.
These are for example connections of a four wire adaption or the elements of a meta component.




## Metadata

- Category: Network Access
- Code: 265995
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program
- Count result: no
- Archive allowed: no

## Parameters

- `Components`: `tcreatearray` — Variable into which the list of found components will be written.
; The content of the list also depends on the kind of components to be searched for.
; Components[Index, 1] = Name
; Components[Index, 2] = Information
; Components[Index, 3] = Pin1 or PinA1 or Pin prefix
; Components[Index, 4] = Pin2 or PinA2
; Components[Index, 5] = PinB1
; Components[Index, 6] = PinB2
- `Component`: `integer` — Kind of components to be searched for.; Allowed values: COMPONENT_Wire, COMPONENT_Switch, COMPONENT_Resistor, COMPONENT_Capacitor, COMPONENT_Diode, COMPONENT_ZDiode, COMPONENT_CTwist, COMPONENT_CustomComponent, COMPONENT_RLCCombination, COMPONENT_Attenuator, COMPONENT_OpticalFiber, COMPONENT_Relay, COMPONENT_TerminalBlock, COMPONENT_VariableResistor
- `ComponentData`: `integer` — Specifies in which field is searched; Allowed values: COMPONENT_DATA_Name, COMPONENT_DATA_Information, COMPONENT_DATA_TestInfo
- `Search`: `string` — The keyword can contain the asterisk (*) as a wildcard.; Examples: abc*, *abc. *abc*, *
; If ComponentData = COMPONENT_DATA_TestInfo, only the following constants can be used:
; TEST_INFO_Tested: Searches components which were tested
; TEST_INFO_NotTested: Searches components which were not tested
; TEST_INFO_Passed: Searches components whose test passed at least once
; TEST_INFO_Failed: Searches components whose test failed at least once
; TEST_INFO_NoAccess_Splice: Searches components which were not tested due to not connected splices
; TEST_INFO_NoAccess_Switch: Searches components which were not tested due to open switches
; TEST_INFO_NoCommand: Searches components for which no test function was executed
; TEST_INFO_Repeated: Searches components whose test was repeated
- `Module`: `string = MODULE_All` — Specifies in which module the components will be searched.; If a module name is passed the components will only be searched in this module.; Allowed values: MODULE_All, MODULE_Current

## Return value

The function returns the found components in the passed variable.
The function value is the number of the found components.

## Example

```ats
//Example 1: Searches wires whose information data starts with an "a"
Count = NWFindComponents(FoundComponents, COMPONENT_Wire, COMPONENT_DATA_Information, 'a*', MODULE_All);
for Index = 1 to Count do
begin
   Name = FormatAlignLeft(FoundComponents[Index, 1], 20, ' ');
   Info = FormatAlignLeft(FoundComponents[Index, 2], 20, ' ');
   Pin1 = FoundComponents[Index, 3];
   Pin1 = PinGetData(Pin1, PIN_AnyName);
   Pin1 = FormatAlignLeft(Pin1, 20, ' ');
   Pin2 = FoundComponents[Index, 4];
   Pin2 = PinGetData(Pin2, PIN_AnyName);
   Pin2 = FormatAlignLeft(Pin2, 20, ' ');
   Text = StrAdd(Name, Info);
   Text = StrAdd(Text, Pin1);
   Text = StrAdd(Text, Pin2);
   UIWriteNormal(Text);
end;

//Example 2: Searches not tested resistors
Count = NWFindComponents(FoundComponents, COMPONENT_Resistor, COMPONENT_DATA_TestInfo, TEST_INFO_NotTested, MODULE_All);
for Index = 1 to Count do
begin
   Name = FormatAlignLeft(FoundComponents[Index, 1], 20, ' ');
   Pin1 = FoundComponents[Index, 3];
   Pin1 = PinGetData(Pin1, PIN_AnyName);
   Pin1 = FormatAlignLeft(Pin1, 20, ' ');
   Pin2 = FoundComponents[Index, 4];
   Pin2 = PinGetData(Pin2, PIN_AnyName);
   Pin2 = FormatAlignLeft(Pin2, 20, ' ');
   Text = StrAdd(Name, Pin1);
   Text = StrAdd(Text, Pin2);
   UIWriteNormal(Text);
end;
```
