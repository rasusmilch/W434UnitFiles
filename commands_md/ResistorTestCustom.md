# ResistorTestCustom

## Declaration

```ats
function ResistorTestCustom(Name: string; Pin1: tpin; Pin2: tpin; Trise: ttime=PARAM_UseDefault; Twait: ttime=PARAM_UseDefault; Tmeas: ttime=PARAM_UseDefault; Imin: tcurrent=PARAM_UseDefault; Imax: tcurrent=PARAM_UseDefault; Umin: tvoltage=PARAM_UseDefault; Umax: tvoltage=PARAM_UseDefault): boolean; tests resistors;
```

## Call pattern

```ats
ResistorTestCustom('Name', "Pin1", "Pin2", <Trise>s, <Twait>s, <Tmeas>s, <Imin>A, <Imax>A, <Umin>V, <Umax>V);
```

## Description

Tests a resistor between Pin1 and Pin2 with custom parameters.

The function always refers to a resistor in the netlist.

## Metadata

- Category: Electrical testing
- Code: 776
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Trise`: `ttime=PARAM_UseDefault`
- `Twait`: `ttime=PARAM_UseDefault`
- `Tmeas`: `ttime=PARAM_UseDefault`
- `Imin`: `tcurrent=PARAM_UseDefault`
- `Imax`: `tcurrent=PARAM_UseDefault`
- `Umin`: `tvoltage=PARAM_UseDefault`
- `Umax`: `tvoltage=PARAM_UseDefault`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
ResistorTestCustom('Resistor1', "Pin1", "Pin2", PARAM_UseDefault, PARAM_UseDefault, 10ms, 1mA);
```

## Example notes

Tests the resistor Resistor1 between Pin1 and Pin2. 

The measurement time and the minimum current are customized.
For the other parameters the default values will be used.

## Result fields

| Field | Type | Description |
|---|---|---|
| `RES_FileIndex` | `integer` | Index of the file that contains the command |
| `RES_StartLine` | `integer` | Number of the first ATS line that contains the command |
| `RES_EndLine` | `integer` | Number of the last ATS line that contains the command |
| `RES_ModuleFileIndex` | `integer` | Index of the module from whicht the command was called. |
| `RES_ModuleLine` | `integer` | Line of the module from which the command was called. |
| `RES_Name` | `string` | Name |
| `RES_Result` | `integer` | Result |
| `RES_ManualTest` | `boolean` | Manual test |
| `RES_LowForce` | `integer` | Low-Force-Pin |
| `RES_LowSense` | `integer` | Low-Sense-Pin |
| `RES_HighForce` | `integer` | High-Force-Pin |
| `RES_HighSense` | `integer` | High-Sense-Pin |
| `RES_4Wire` | `boolean` | 4-Wire measurement |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_ExtVoltageFound` | `boolean` | External voltage found |
| `RES_ExtVoltagePin1` | `integer` | Pin1 with external voltage |
| `RES_ExtVoltagePin2` | `integer` | Pin2 with external voltage |
| `RES_ExtVoltageValue` | `real` | Value of the external voltage |
| `RES_ExtVoltagePrefix` | `string` | Prefix of the external voltage |
| `RES_Autostart` | `boolean` | Autostart |
| `RES_Arc` | `boolean` | Arc occured |
| `RES_Value` | `real` | Measured value in Ohm |
| `RES_Prefix` | `string` | Prefix of the measured value |
| `RES_Resistance` | `real` | Parameter: Reference value in Ohm |
| `RES_LowerTol` | `real` | Parameter: Lower tolerance in Ohm |
| `RES_UpperTol` | `real` | Parameter: Upper tolerance in Ohm |
| `RES_MinResistance` | `real` | Parameter: Minimum allowed value in Ohm (Reference value - lower tolerance) |
| `RES_MaxResistance` | `real` | Parameter: Maximum allowe value in Ohm (Reference value + upper tolerance) |
| `RES_Trise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_Twait` | `real` | Parameter: Wait time in seconds |
| `RES_Tmeas` | `real` | Parameter: Mesurement time in seconds |
| `RES_MaxPower` | `real` | Parameter: Maximum allowed power in Watt |
| `RES_MinCurrent` | `real` | Parameter: Minimum allowed current in Ampere |
| `RES_MaxCurrent` | `real` | Parameter: Maximum allowed current in Ampere |
| `RES_MinVoltage` | `real` | Parameter: Minimum allowed voltage in Volt |
| `RES_MaxVoltage` | `real` | Parameter: Maximum allowed voltage in Volt |
| `RES_CompPathCount` | `integer` | Number of components in the component path |
| `RES_CompPathPin1[ ]` | `integer` | First pins of the components in the component path |
| `RES_CompPathPin2[ ]` | `integer` | Second pins of the components in the component path |
| `RES_CompPathNames[ ]` | `string` | Names of the components in the component path |
| `RES_CompPathKinds[ ]` | `integer` | Types of the components in the component path |
| `RES_CompPathPinCount` | `integer` | Number of different pins in the component path |
| `RES_CompPathPins[]` | `integer` | List of the different pins in the component path |
| `RES_CompPathInfos[]` | `string` | List of component information from the net list |
| `RES_CompPathStates[]` | `string` | List of switching states of the components (Possible values: 7, - or empty |
| `RES_OriginalPin1` | `integer` | Address of the first programmed pin |
| `RES_OriginalPin2` | `integer` | Address of the second programmed pin |

## See also

`NWSetResistorValues`, `ResistorTest`
