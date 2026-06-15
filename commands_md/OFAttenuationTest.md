# OFAttenuationTest

## Declaration

```ats
function OFAttenuationTest(Name: string; Transmitter: topticalpin; Receiver: topticalpin): boolean; tests opticalfibers;
```

## Call pattern

```ats
OFAttenuationTest('Name', "Transmitter", "Receiver");
```

## Description

Test the attenuation of an optical fiber from "Transmitter" to "Receiver".

## Metadata

- Category: Optical fibers
- Code: 2560
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Transmitter`: `topticalpin`
- `Receiver`: `topticalpin`

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
OFAttenuationTest('Optical Fiber 1', "OpticalPin1", "OpticalPin2");
OFAttenuationTest('Optical Fiber 1', "OpticalPin2", "OpticalPin1");
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
| `RES_Pin1` | `integer` | Transmitter |
| `RES_Pin2` | `integer` | Receiver |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_Autostart` | `boolean` | Autostart |
| `RES_Value` | `real` | Measured value in dB |
| `RES_Prefix` | `string` | Prefix of the measured value |
| `RES_Attenuation` | `real` | Parameter: Reference value in dB |
| `RES_LowerTol` | `real` | Parameter: Lower tolerance in dB |
| `RES_UpperTol` | `real` | Parameter: Upper tolerance in dB |
| `RES_MinAttenuation` | `real` | Parameter: Minimum allowed value in dB (Reference value - lower tolerance) |
| `RES_MaxAttenuation` | `real` | Parameter: Maximum allowed value in dB (Reference value + upper tolerance) |
| `RES_TransmitterPower` | `real` | Parameter: Transmitter power in dBm |
| `RES_Compensation` | `real` | Compensation of the adaption in dB |
| `RES_CompPathCount` | `integer` | Number of components in the component path |
| `RES_CompPathPin1[ ]` | `integer` | First pins of the components in the component path |
| `RES_CompPathPin2[ ]` | `integer` | Second pins of the components in the component path |
| `RES_CompPathNames[ ]` | `string` | Names of the components in the component path |
| `RES_CompPathKinds[ ]` | `integer` | Types of the components in the component path |
| `RES_CompPathPinCount` | `integer` | Number of different pins in the component path |
| `RES_CompPathPins[]` | `integer` | List of the different pins in the component path |
| `RES_CompInformation` | `string` | Text from the column "Information" in the netlist. |

## See also

`NWSetOpticalFiberValues`, `TestOpticalFibers`
