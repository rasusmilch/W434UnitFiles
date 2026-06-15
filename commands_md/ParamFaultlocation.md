# ParamFaultlocation

## Declaration

```ats
function ParamFaultlocation(Commands: integer; OnOff: boolean):void;
```

## Call pattern

```ats
ParamFaultlocation(COMMANDS_?, ON|OFF);
```

## Description

Turns the functionality "Fault location" for the specified commandgroup on or off.

## Metadata

- Category: Parameters
- Code: 266254
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_IsolationLV
- `OnOff`: `boolean`

## Example

```ats
ParamFaultlocation(COMMANDS_Continuity, ON);
WireTest('Wire1', "Pin1", "Pin2");
ParamFaultlocation(COMMANDS_Continuity, OFF);
```
