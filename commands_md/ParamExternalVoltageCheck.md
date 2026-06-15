# ParamExternalVoltageCheck

## Declaration

```ats
function ParamExternalVoltageCheck(OnOff: boolean; AllowedVoltage: tvoltage=5V): void;
```

## Call pattern

```ats
ParamExternalVoltageCheck(ON|OFF, <AllowedVoltage>V);
```

## Description

Activates or deactivates the external voltage test and sets the value for the maximum accepted voltage.

Checking for external voltages is normally activated by a power pin command or a command for measuring voltage (e.g. VoltageTest).
The default value for maximum allowed external voltage is 5V.

## Metadata

- Category: Parameters
- Code: 266247
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `OnOff`: `boolean` — Allowed values: ON, OFF
- `AllowedVoltage`: `tvoltage=5V`

## Example

```ats
ParamExternalVoltageCheck(ON, 3V);
```
