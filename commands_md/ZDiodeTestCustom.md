# ZDiodeTestCustom

## Declaration

```ats
function ZDiodeTestCustom(Name: string; Pin1: tpin; Pin2: tpin; Trise: ttime=PARAM_UseDefault; Twait: ttime=PARAM_UseDefault; Tmeas: ttime=PARAM_UseDefault): boolean; tests zdiodes;
```

## Call pattern

```ats
ZDiodeTestCustom('Name', "Pin1", "Pin2", <Trise>s, <Twait>s, <Tmeas>s);
```

## Description

Tests a Z-diode between Pin1 and Pin2 with custom parameters.

The function always refers to a zdiode in the netlist.

## Metadata

- Category: Electrical testing
- Code: 778
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
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_ExtVoltageFound` | `boolean` | External voltage found |
| `RES_ExtVoltagePin1` | `integer` | Pin1 with external voltage |
| `RES_ExtVoltagePin2` | `integer` | Pin2 with external voltage |
| `RES_ExtVoltageValue` | `real` | Value of the external voltage |
| `RES_ExtVoltagePrefix` | `string` | Prefix of the external voltage |
| `RES_Value1` | `real` | First measured voltage in Volt |
| `RES_Prefix1` | `string` | Prefix of the first measured voltage |
| `RES_Value2` | `real` | Second measured voltage in Volt |
| `RES_Prefix2` | `string` | Prefix of the second measured voltage |
| `RES_U1Ok` | `boolean` | TRUE if U1 ok, otherwise FALSE |
| `RES_U2Ok` | `boolean` | TRUE if U2 ok, otherwise FALSE |
| `RES_U3Ok` | `boolean` | TRUE if U3 ok, otherwise FALSE |
| `RES_U4Ok` | `boolean` | TRUE if U4 ok, otherwise FALSE |
| `RES_Voltage1` | `real` | Parameter: U1 in Volt |
| `RES_Voltage2` | `real` | Parameter: U2 in Volt |
| `RES_Voltage3` | `real` | Parameter: U3 in Volt |
| `RES_Voltage4` | `real` | Parameter: U4 in Volt |
| `RES_CurrentForward` | `real` | Parameter: Measurement current in forward direction |
| `RES_CurrentReverse` | `real` | Parameter: Measurement current in reverse direction |
| `RES_Tmeas` | `real` | Parameter: Mesurement time in seconds |
| `RES_Value` | `real` | Measured value in Ohm |
| `RES_Prefix` | `string` | Prefix of the measured value |
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

`ZDiodeTest`
