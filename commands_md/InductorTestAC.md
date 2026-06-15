# InductorTestAC

## Declaration

```ats
function InductorTestAC(Name: string; Pin1: tpin; Pin2: tpin): boolean; tests inductors;
```

## Call pattern

```ats
InductorTestAC('Name', "Pin1", "Pin2");
```

## Description

Tests an inductor between Pin1 and Pin2 with AC.

The function always refers to a inductor in the netlist.

## Metadata

- Category: Electrical testing
- Code: 780
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Not listed
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
InductorTestAC('Inductor1', "Pin1", "Pin2");
```

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
| `RES_Value` | `real` | Measured value in Henry |
| `RES_Prefix` | `string` | Prefix of the measured value |
| `RES_Inductance` | `real` | Parameter: Reference value in Henry |
| `RES_LowerTol` | `real` | Parameter: Lower tolerance in Henry |
| `RES_UpperTol` | `real` | Parameter: Upper tolerance in Henry |
| `RES_MinInductance` | `real` | Parameter: Minimum allowed value in Henry (Reference value - lower tolerance) |
| `RES_MaxInductance` | `real` | Parameter: Maximum allowed value in Henry (Reference value + upper tolerance) |
| `RES_MaxCurrent` | `real` | Parameter: Maximum allowed current in Ampere |
| `RES_CompPathCount` | `integer` | Number of components in the component path |
| `RES_CompPathPin1[ ]` | `integer` | First pins of the components in the component path |
| `RES_CompPathPin2[ ]` | `integer` | Second pins of the components in the component path |
| `RES_CompPathNames[ ]` | `string` | Names of the components in the component path |
| `RES_CompPathKinds[ ]` | `integer` | Types of the components in the component path |
| `RES_CompPathPinCount` | `integer` | Number of different pins in the component path |
| `RES_CompPathPins[]` | `integer` | List of the different pins in the component path |
| `RES_CompPathInfos[]` | `string` | List of component information from the net list |
| `RES_CompPathStates[]` | `string` | List of switching states of the components (Possible values: 7, - or empty |

## See also

`AttenuatorTest`, `CapacitorTest`, `CTwistTest`, `DiodeTest`, `MeasureRLC`, `ResistorTest`, `ZDiodeTest`
