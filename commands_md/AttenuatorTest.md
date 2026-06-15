# AttenuatorTest

## Declaration

```ats
function AttenuatorTest(Name: string; TransmitterPin1: tpin; TransmitterPin2: tpin; ReceiverPin1: tpin; ReceiverPin2: tpin; PolarityTest: boolean = TRUE): boolean; tests attenuators;
```

## Call pattern

```ats
AttenuatorTest('Name', "TransmitterPin1", "TransmitterPin2", "ReceiverPin1", "ReceiverPin2");
```

## Description

Tests an attenuator between TransmitterPin1/TransmitterPin2 and ReceiverPin1/ReceiverPin2.

The function always refers to an attenuator in the netlist.

## Metadata

- Category: Electrical testing
- Code: 781
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `TransmitterPin1`: `tpin`
- `TransmitterPin2`: `tpin`
- `ReceiverPin1`: `tpin`
- `ReceiverPin2`: `tpin`
- `PolarityTest`: `boolean = TRUE` — Allowed values: TRUE, FALSE

## Return value

The function returns TRUE if the test passed, otherwise FALSE.

## Example

```ats
AttenuatorTest('Attenuator1', "TransmitterPin1", "TransmitterPin2", "ReceiverPin1", "ReceiverPin2");
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
| `RES_PinA1` | `integer` | Transmitterpin 1 |
| `RES_PinA2` | `integer` | Transmitterpin 2 |
| `RES_PinB1` | `integer` | Receiverpin 1 |
| `RES_PinB2` | `integer` | Receiverpin 1 |
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_ExtVoltageFound` | `boolean` | External voltage found |
| `RES_ExtVoltagePin1` | `integer` | Pin1 with external voltage |
| `RES_ExtVoltagePin2` | `integer` | Pin2 with external voltage |
| `RES_ExtVoltageValue` | `real` | Value of the external voltage |
| `RES_ExtVoltagePrefix` | `string` | Prefix of the external voltage |
| `RES_Value` | `real` | Measured value in dB |
| `RES_Prefix` | `string` | Prefix of the measured value |
| `RES_PolarityOk` | `boolean` | Polarity ok |
| `RES_Attenuation` | `real` | Parameter: Reference value in dB |
| `RES_LowerTol` | `real` | Parameter: Lower tolerance in dB |
| `RES_UpperTol` | `real` | Parameter: Upper tolerance in dB |
| `RES_MinAttenuation` | `real` | Parameter: Minimum allowed value in dB (Reference value - lower tolerance) |
| `RES_MaxAttenuation` | `real` | Parameter: Maximum allowed value in dB (Reference value + upper tolerance) |
| `RES_Frequency` | `real` | Frequency which was used for the measurement |
| `RES_Impedance` | `real` | Impedance of the attenuator |
| `RES_PolarityTest` | `boolean` | Polarity test |
| `RES_InPhase` | `boolean` | Polarity is inphase |
| `RES_Tmeas` | `real` | Parameter: Mesurement time in seconds |
| `RES_OriginalPinA1` | `integer` | Address of the first programmed transmitterpin |
| `RES_OriginalPinA2` | `integer` | Address of the second programmed transmitterpin |
| `RES_OriginalPinB1` | `integer` | Address of the first programmed receiverpin |
| `RES_OriginalPinB2` | `integer` | Address of the second programmed receiverpin |

## See also

`Capacitor Test`, `CTwistTestAC`, `DiodeTest`, `MeasureRLC`, `ResistorTest`, `TestAttenuators`, `ZDiodeTest`
