# ParamAutostart

## Declaration

```ats
function ParamAutostart(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamAutostart(COMMANDS_?, ON|OFF);
```

## Description

Turns the functionality "AutoStart" for the specified commandgroup on or off.

## Metadata

- Category: Parameters
- Code: 266241
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_IsolationLV, COMMANDS_IsolationHV, COMMANDS_DielectricBreakdown, COMMANDS_ElectricalComponents, COMMANDS_Voltage, COMMANDS_CANBus, COMMANDS_Detections
- `OnOff`: `boolean` — Allowed values: ON, OFF

## Example

```ats
ParamAutostart(COMMANDS_Continuity, ON);
WireTest('Wire1', "Pin1", "Pin2");
ParamAutostart(COMMANDS_Continuity, OFF);
```

## See also

`NoConnectionLV`, `ParamSearchDepth`, `ParamStopOnFail`, `SwitchTest`, `UIAutostartSelectWindowType`, `VoltageTest`, `WireTest`
