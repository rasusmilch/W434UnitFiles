# ParamTwistedPair

## Declaration

```ats
function ParamTwistedPair(Specifications: integer; DCResistanceCompensation: tresistance = 0Ohm; NVP_Percent: real = 70; IsDCLoopResistanceTestEnabled: boolean = ON; IsAttenuationTestEnabled: boolean = ON; IsPropagationTestEnabled: boolean = ON): void;
```

## Call pattern

```ats
ParamTwistedPair(TWISTED_PAIR_Spec_ISO11801, <x>Ohm, <NVP>, ON|OFF, ON|OFF, ON|OFF);
```

## Description

This funciton sets various parameters for the test of twisted pair cables

## Metadata

- Category: Parameters
- Code: 2323
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Specifications`: `integer` — Specification, which is used for testing the cables; Allowed values: TWISTED_PAIR_Spec_ISO11801
- `DCResistanceCompensation`: `tresistance = 0Ohm` — A resistance value which will be subtracted from the measured DC Loop resistance to remove effects of connectors.
- `NVP_Percent`: `real = 70` — Nominal value of propagation (NVP) of the cables in percent (1-100)
- `IsDCLoopResistanceTestEnabled`: `boolean = ON` — If ON is passed the DC loop resistance will be tested; Allowed values: ON, OFF
- `IsAttenuationTestEnabled`: `boolean = ON` — If ON is passed the attenuation values will be testen
; Attenuation values: Insertion Loss (IL), Return Loss (RL), Near End Crosstalk (NEXT), Far End Crosstalk (FEXT); Allowed values: ON, OFF
- `IsPropagationTestEnabled`: `boolean = ON` — If ON is passed, Propagation Delay and Delay Skew will be tested; Allowed values: ON, OFF

## Example

```ats
ParamTwistedPair(TWISTED_PAIR_Spec_ISO11801, 2Ohm, 65);
TwistedPairTest('Twisted Pair', TWISTED_PAIR_CAT5, ON, 'Default', 10m, 0.5m, 1m);
```

## See also

`TwistedPairTestFrequencies`, `TwistedPairRunCompensation`, `TwistedPairTest2PE`, `TwistedPairTest`, `ParamStopOnFail`
