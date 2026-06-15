# RLCParallelCapacitanceTest

## Declaration

```ats
function RLCParallelCapacitanceTest(Name: string; Pin1: tpin; Pin2: tpin; Minimum: tcapacitance; Maximum: tcapacitance): boolean; tests rlccombinations;
```

## Call pattern

```ats
RLCParallelCapacitanceTest('Name', "Pin1", "Pin2", <Minimum>uF, <Maximum>uF);
```

## Description

The function tests the capacitance of a RLC combination.

It is assumed that the RLC combination is a parallel circuit.

The function always refers to a RLC combination in the netlist.

## Metadata

- Category: Electrical testing
- Code: 792
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `Minimum`: `tcapacitance`
- `Maximum`: `tcapacitance`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
RLCParallelCapacitanceTest('RLC 1 Cpar', "Pin1", "Pin2", 8nF, 12nF);
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
| `RES_4Wire` | `boolean` | 4-Wire measurement |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_ExtVoltageFound` | `boolean` | External voltage found |
| `RES_ExtVoltagePin1` | `integer` | Pin1 with external voltage |
| `RES_ExtVoltagePin2` | `integer` | Pin2 with external voltage |
| `RES_ExtVoltageValue` | `real` | Value of the external voltage |
| `RES_ExtVoltagePrefix` | `string` | Prefix of the external voltage |
| `RES_MaxVoltage` | `real` | Parameter: Maximum allowed voltage in Volt |
| `RES_MaxCurrent` | `real` | Parameter: Maximum allowed current in Ampere |
| `RES_Trise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_Twait` | `real` | Parameter: Wait time in seconds |
| `RES_Tmeas` | `real` | Parameter: Mesurement time in seconds |
| `RES_Cmin` | `real` | Parameter: Minimum capacitance in Farad |
| `RES_Cmax` | `real` | Parameter: Maximum capacitance in Farad |
| `RES_Value` | `real` | Measured value in Farad |
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

`MeasureRLC`, `RLCDissipationTest`, `RLCImpedanceAbsoluteTest`, `RLCImpedanceImaginaryTest`, `RLCImpedanceRealTest`, `RLCParallelCapacitanceTest`, `RLCParallelResistanceTest`, `RLCParallelResistanceTestRLCPhaseAngleTest`, `RLCQualityTest`, `RLCSerialResistanceTest`
