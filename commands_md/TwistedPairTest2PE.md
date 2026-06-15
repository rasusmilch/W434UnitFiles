# TwistedPairTest2PE

## Declaration

```ats
function TwistedPairTest2PE(Name: string; Category: integer; IsShieldTestEnabled: boolean; AdapterName: string = 'Default'; CableLength: tlength = 0m; LowerTol: tlength = 0m; UpperTol: tlength = 0m): boolean;
```

## Call pattern

```ats
TwistedPairTest2PE('Name', TWISTED_PAIR_CAT?, ON);
```

## Description

Notice: This test requires a W 850 HF

The function tests, whether a two pair ethernet cable meets the requirements of the specification which was specified with ParamTwistedPair
The frequency band from 1MHz up to the maximum of the specified category is tested.

## Metadata

- Category: Twisted Pair Test
- Code: 4355
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: yes

## Parameters

- `Name`: `string`
- `Category`: `integer` — Cable category which will be tested.; Allowed values: TWISTED_PAIR_CAT4, TWISTED_PAIR_CAT5, TWISTED_PAIR_CAT6, TWISTED_PAIR_CAT6A, TWISTED_PAIR_CAT7, TWISTED_PAIR_CAT7A, TWISTED_PAIR_CAT8_1, TWISTED_PAIR_CAT8_2
- `IsShieldTestEnabled`: `boolean` — The continuity of the shield of the cable will be checked if ON is passed.; Allowed values: ON, OFF
- `AdapterName`: `string = 'Default'` — Name of the adapter which will be used.; The names of the adapters may only consist of the characters 'a'..'z', 'A'..'Z', '0'..'9', '_' and '-'.
- `CableLength`: `tlength = 0m` — The expected cable length.; If a length of 0m is passed, the length will not be tested.
; The length of the cable is calculated by using the Propagation Delay, the speed of light and the NVP.; The cable length is the arithmetic mean of the calculated lenghts of the single wires
- `LowerTol`: `tlength = 0m` — Lower tolerance for the cable length.
- `UpperTol`: `tlength = 0m` — Upper tolerance for the cable length.

## Example

```ats
ParamTwistedPair(TWISTED_PAIR_Spec_ISO11801, 2Ohm, 65);
TwistedPairTest2PE('Twisted Pair', TWISTED_PAIR_CAT5, ON, 'Default', 10m, 0.5m, 1m);
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
| `RES_STime` | `real` | Starttime |
| `RES_ETime` | `real` | Endtime |
| `RES_Comment` | `string` | Comment |
| `RES_Specification` | `integer` | Specification which is used for the test of the cable |
| `RES_DCResistanceCompensation` | `real` | DC resistance compensation value/Ohm |
| `RES_NVP` | `real` | Nominal Velocity of Propagation |
| `RES_IsDCLoopResistanceTestEnabled` | `boolean` | If ON is passed the DC loop resistance will be tested according to the specification |
| `RES_IsAttenuationTestEnabled` | `boolean` | If ON is passed Insertion Loss, Return Loss, NEXT and FEXT will be tested according to the specification |
| `RES_IsPropagationDelayTestEnabled` | `boolean` | If ON is passed propagation delay and delay skew will be tested according to the specification |
| `RES_Category` | `integer` | Category (TWISTED_PAIR_CAT? - constants) |
| `RES_AdapterName` | `string` | Adapter name |
| `RES_IsShieldTestEnabled` | `boolean` | TRUE, if the shield was tested |
| `RES_IsCableLengthTestEnabled` | `boolean` | TRUE, if the cable length was tested |
| `RES_ExpectedCableLength` | `real` | Expected cable length in m |
| `RES_CableLengthLowerTol` | `real` | Lower tolerance for the cable length in m |
| `RES_CableLengthUpperTol` | `real` | Upper tolerance for the cable length in m |
| `RES_IsDCLoopResistanceValid` | `boolean` | TRUE, if the DC loop resistance was tested |
| `RES_WireMapImageFileName` | `string` | Filename of the wire map image |
| `RES_InsertionLossImageFileName` | `string` | Filename of the insertion loss graph |
| `RES_ReturnLossImageFileName` | `string` | Filename of the return loss graph |
| `RES_NEXTImageFileName` | `string` | Filename of the near end crosstalk graph |
| `RES_FEXTImageFileName` | `string` | Filename of the far end crosstalk graph |
| `RES_IsWireMapOk` | `boolean` | TRUE, if continuity and isolation are ok |
| `RES_IsContinuityOk` | `boolean` | TRUE, if continuity is ok |
| `RES_IsIsolationOk` | `boolean` | TRUE, if isolation is ok |
| `RES_IsAttenuationOk` | `boolean` | TRUE, if Insertion Loss, Return Loss, Near End Crosstalk and Far End Crosstalk meet the requirements of the specification, otherwise FALSE |
| `RES_IsInsertionLossOk` | `boolean` | TRUE, if the Insertion Loss meets the requirements of the specification, otherwise FALSE |
| `RES_IsReturnLossOk` | `boolean` | TRUE, if the Return Loss meets the requirements of the specification, otherwise FALSE |
| `RES_IsNEXTOk` | `boolean` | TRUE, if the Near End Crosstalk meets the requirements of the specification, otherwise FALSE |
| `RES_IsFEXTOk` | `boolean` | TRUE, if the Far End Crosstalk meets the requirements of the specification, otherwise FALSE |
| `RES_InsertionLossErrorCount` | `integer` | Number of Insertion Loss errors |
| `RES_ReturnLossErrorCount` | `integer` | Number of Return Loss errors |
| `RES_NEXTErrorCount` | `integer` | Number of NEXT errors |
| `RES_FEXTErrorCount` | `integer` | Number of FEXT errors |
| `RES_DCLoopResistanceErrorCount` | `integer` | Number of DC Loop Resistance errors |
| `RES_DCLoopResistance[]` | `real` | DC loop resistance/Ohm |
| `RES_IsPropagationOk` | `boolean` | TRUE, if Propagation Delay and Delay Skew meet the requirements of the specification, otherwise FALSE |
| `RES_IsPropagationDelayOk` | `boolean` | TRUE, if the Propagation Delay meets the requirements of the specification, otherwise FALSE |
| `RES_IsDelaySkewOk` | `boolean` | TRUE, if the Delay Skew meets the requirements of the specification, otherwise FALSE |
| `RES_PropagationDelayErrorCount` | `integer` | Number of Propagation Delay errors |
| `RES_DelaySkewErrorCount` | `integer` | Number of Delay Skew errors |
| `RES_PropagationDelay[]` | `real` | Propagation Delay |
| `RES_DelaySkew[]` | `real` | Delay Skew |
| `RES_IsCableLengthOk` | `boolean` | TRUE, if the cable length meets the requirements, otherwise FALSE |
| `RES_CableLength` | `real` | Measured cable length |

## See also

`TwistedPairTest`, `TwistedPairTestFrequencies`, `TwistedPairRunCompensation`, `ParamTwistedPair`, `ParamStopOnFail`
