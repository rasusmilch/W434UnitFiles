# ParamDischargeEnergyMonitoring

## Declaration

```ats
function ParamDischargeEnergyMonitoring(EnableDisable: boolean): void;
```

## Call pattern

```ats
ParamDischargeEnergyMonitoring(ON|OFF);
```

## Description

You can disable and enable the discharge energy monitoring of the HVG 4300 with this function.

The discharge energy monitoring checks continously that the enmergy in the UUT does not exceed 350 uJ.,

Only the HVG 4300 of the W484 has the capabiity to monior the energy.

## Metadata

- Category: Parameters
- Code: 266263
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `EnableDisable`: `boolean` — Allowed values: ON, OFF

## Example

```ats
ParamDischargeEnergyMonitoring(OFF);
```
