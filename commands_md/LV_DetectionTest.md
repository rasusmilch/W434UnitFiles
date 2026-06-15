# LV_DetectionTest

## Declaration

```ats
function LV_DetectionTest(Name: string; Pin1: tlvpin; Pin2: tlvpin; OnOff: boolean): boolean;
```

## Call pattern

```ats
LV_DetectionTest('<Name>', "Pin1", "Pin2", ON|OFF);
```

## Description

The function tests detections at the LV matrix

## Metadata

- Category: Detections
- Code: 3841
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Pin1`: `tlvpin`
- `Pin2`: `tlvpin`
- `OnOff`: `boolean` — Allowed values: ON, OFF

## Example

```ats
LV_DetectionTest('Connector 1', "LV-Pin1", "LV-Pin2", ON);
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
| `RES_Pin1` | `integer` | Pin 1 |
| `RES_Pin2` | `integer` | Pin 2 |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_On` | `boolean` | TRUE, if the detection must be closed |
| `RES_LV_D_Twait` | `real` | Parameter: Wait time |
| `RES_LV_D_Tmeas` | `real` | Parameter: Measurement time |
| `RES_LV_D_Threshold` | `real` | Parameter: Resistance threshold |
| `RES_LV_D_Current` | `real` | Parameter: Current |
| `RES_LV_D_VoltageLimit` | `real` | Parameter: Voltage limit |
| `RES_Comment` | `string` | Comment |
| `RES_DelcaredAsPassed` | `boolean` | Declared as passed |
| `RES_DelcaredAsPassedByUser` | `string` | User who delcared as passed |
