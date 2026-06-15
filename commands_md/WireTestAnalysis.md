# WireTestAnalysis

## Declaration

```ats
function WireTestAnalysis(Name: string; Pin1: tpin; Pin2: tpin): integer; tests wires;
```

## Call pattern

```ats
WireTestAnalysis('Name', "Pin1", "Pin2");
```

## Description

Tests a wire between Pin1 and Pin2.

The function always refers to a wire in the netlist.

## Metadata

- Category: Electrical testing
- Code: 519
- Visible in alphabetical index: yes
- Deprecated: yes
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`

## Return value

The function returns:

TESTSTEP_Passed, if the test passed

TESTSTEP_Failed, if an error was detected

TESTSTEP_Invalid, if the result of the test is invalid

TESTSTEP_NotExecuted, if the test was not executed

## Example

```ats
WireTestAnalysis('Wire 1', "Pin1", "Pin2");
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
| `RES_ColorCount` | `integer` | Number of colors |
| `RES_Colors[ ]` | `integer` | Colors of the wire |
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
| `RES_CCurrent` | `real` | Parameter: Current in Ampere |
| `RES_CThreshold` | `real` | Parameter: Threshold in Ohm |
| `RES_CTrise` | `real` | Parameter: Maximum rise time in seconds |
| `RES_CTwait` | `real` | Parameter: Wait time in seconds |
| `RES_CTmeas` | `real` | Parameter: Measurement time in seconds |
| `RES_CAutoRange` | `boolean` | Parameter: Automatic ranging |
| `RES_CVoltageLimit` | `real` | Parameter: Voltage limit in volt |
| `RES_CompPathCount` | `integer` | Number of components in the component path |
| `RES_CompPathPin1[ ]` | `integer` | First pins of the components in the component path |
| `RES_CompPathPin2[ ]` | `integer` | Second pins of the components in the component path |
| `RES_CompPathNames[ ]` | `string` | Names of the components in the component path |
| `RES_CompPathKinds[ ]` | `integer` | Types of the components in the component path |
| `RES_CompPathPinCount` | `integer` | Number of different pins in the component path |
| `RES_CompPathPins[]` | `integer` | List of the different pins in the component path |
| `RES_CompPathInfos[]` | `string` | List of component information from the net list |
| `RES_CompPathStates[]` | `string` | List of switching states of the components (Possible values: 7, - or empty |
| `RES_CompInformation` | `string` | Text from the column "Information" in the netlist. |
| `RES_Interchange` | `boolean` | TRUE, if an interchange was detected during a two pole teststep |
| `RES_NetworkCount` | `integer` | Number of detected networks |
| `RES_NetworkPinCount[]` | `integer` | Number of pins for each network |
| `RES_ValuesToNextNW[]` | `real` | Resistance to network with next higher index |
| `RES_ValuesToNextNWPrefix[]` | `string` | Prefix of the resistance to network with next higher index |
| `RES_ValuesToNextNWArc[]` | `boolean` | TRUE, if an arc was detected to the network with next higher index |
| `RES_ShortCount[]` | `integer` | Number of Shorts that were detected for each network |
| `RES_NCAExecuted[]` | `boolean` | Number of Shorts that were detected for each network |
| `RES_NCAValues[]` | `real` | Resistance if the NCA found no shorts |
| `RES_NCAValuesPrefix[]` | `string` | Prefix of the resistance if the NCA found no shorts |
| `RES_NetworkPins[x, y]` | `integer` | Pins of each network [NetworkIndex, PinIndex] |
| `RES_Shorts[x, y]` | `integer` | Addresses of the pins to which shorts were detected for each network [NetworkIndex, PinIndex] |
| `RES_ShortValues[x, y]` | `real` | Resistances of the shorts [NetworkIndex, PinIndex] |
| `RES_ShortPrefixes[x, y]` | `string` | Prefixes of the resistances of the shorts [NetworkIndex, PinIndex] |
| `RES_ShortArcs[x, y]` | `boolean` | TRUE, if an arc was detected [NetworkIndex, PinIndex] |
| `RES_OriginalPin1` | `integer` | Address of the first programmed pin |
| `RES_OriginalPin2` | `integer` | Address of the second programmed pin |
| `RES_CompLVExcluded` | `boolean` | TRUE, if the component is excluded from the automatic LV isolation test in the netlist |
| `RES_CompHVExcluded` | `boolean` | TRUE, if the component is excluded from the automatic HV isolation test in the netlist |
| `RES_CompDBExcluded` | `boolean` | TRUE, if the component is excluded from the automatic dielectric breakdown test in the netlist |

## See also

`ConnectionTest`, `ParamContinuity`, `WireTest`
