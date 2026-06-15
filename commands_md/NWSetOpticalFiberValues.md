# NWSetOpticalFiberValues

## Declaration

```ats
function NWSetOpticalFiberValues(Name: string; Pin1: tpin; Pin2: tpin; AttenuationFwd: tattenuation = PARAM_DontChange; LowerTolFwd: tattenuation = PARAM_DontChange; UpperTolFwd: tattenuation = PARAM_DontChange; TransmitPowerFwd: tpowerlevel = PARAM_DontChange; AttenuationRev: tattenuation = PARAM_DontChange; LowerTolRev: tattenuation = PARAM_DontChange; UpperTolRev: tattenuation = PARAM_DontChange; TransmitPowerRev: tpowerlevel = PARAM_DontChange): void;
```

## Call pattern

```ats
NWSetOpticalFiberValues('Name', "Pin1", "Pin2", <AttenuationFwd>dB, <LowerTolFwd>dB, <UpperTolFwd>dB, <TransmitPowerFwd>dB, <AttenuationRev>dB, <LowerTolRev>dB, <UpperTolRev>dB, <TransmitPowerRev>dB);
```

## Description

Sets the values of the optical fiber between Pin1 and Pin2.

If the optical fiber does not have values for a reverse test in the netlist, the reverse values can not be set with this function.

## Metadata

- Category: Network Access
- Code: 265990
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin1`: `tpin`
- `Pin2`: `tpin`
- `AttenuationFwd`: `tattenuation = PARAM_DontChange`
- `LowerTolFwd`: `tattenuation = PARAM_DontChange`
- `UpperTolFwd`: `tattenuation = PARAM_DontChange`
- `TransmitPowerFwd`: `tpowerlevel = PARAM_DontChange`
- `AttenuationRev`: `tattenuation = PARAM_DontChange`
- `LowerTolRev`: `tattenuation = PARAM_DontChange`
- `UpperTolRev`: `tattenuation = PARAM_DontChange`
- `TransmitPowerRev`: `tpowerlevel = PARAM_DontChange`

## Example

```ats
NWSetOpticalFiberValues(20dB, 4dB, 4dB, PARAM_DontChange, 30dB, 6dB, 6dB, -15dBm);
```

## See also

`OFAttenuationTest`
