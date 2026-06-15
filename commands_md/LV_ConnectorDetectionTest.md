# LV_ConnectorDetectionTest

## Declaration

```ats
function LV_ConnectorDetectionTest(Name: string; Pin: tlvconnectordetectionpin; OnOff: boolean): boolean;
```

## Call pattern

```ats
LV_ConnectorDetectionTest('<Name>', "Pin1", ON|OFF);
```

## Description

The function tests connector detections at the LV matrix

The usage "Connector detection" must be set for this pin in the pin table.

## Metadata

- Category: Detections
- Code: 3840
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin`: `tlvconnectordetectionpin`
- `OnOff`: `boolean` — ON:; To pass this tets step the voltage has to be within the limits
; OFF:; To pass this tets step the voltage has to be out of the limits; Allowed values: ON, OFF

## Example

```ats
LV_ConnectorDetectionTest('Connector 1', "LV-Pin1", ON);

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
| `RES_STime` | `real` | Start time |
| `RES_ETime` | `real` | End time |
| `RES_Pin` | `integer` | Address of the pin |
| `RES_On` | `boolean` | TRUE, if the detection must be closed |
| `RES_LV_CD_Twait` | `real` | Parameter: Wait time |
| `RES_LV_CD_Tmeas` | `real` | Parameter: Measurement time |
| `RES_LV_CD_ILowerThreshold` | `real` | Parameter: Lower current threshold |
| `RES_LV_CD_IUpperThreshold` | `real` | Parameter: Upper current threshold |
| `RES_LV_CD_ULowerThreshold` | `real` | Parameter: Lower voltage threshold |
| `RES_LV_CD_UUpperThreshold` | `real` | Parameter: Upper voltage threshold |
| `RES_LV_CD_IThresholdEnabled` | `boolean` | Parameter: Current thresholds enabled |
| `RES_Comment` | `string` | Comment |
| `RES_DelcaredAsPassed` | `boolean` | Declared as passed |
| `RES_DelcaredAsPassedByUser` | `string` | User who delcared as passed |

## See also

`LV_DetectionTest`
