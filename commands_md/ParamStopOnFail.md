# ParamStopOnFail

## Declaration

```ats
function ParamStopOnFail(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamStopOnFail(COMMANDS_?, ON|OFF);
```

## Description

Turns the functionality "Stop on Fail" for the specified commandgroup on or off.

## Metadata

- Category: Parameters
- Code: 266240
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_IsolationLV, COMMANDS_IsolationHV, COMMANDS_DielectricBreakdown, COMMANDS_ElectricalComponents, COMMANDS_Voltage, COMMANDS_OpticalComponents, COMMANDS_CANBus, COMMANDS_Detections, COMMANDS_IDD, COMMANDS_TwistedPair
- `OnOff`: `boolean` — Allowed values: ON, OFF

## Example

```ats
ParamStopOnFail(COMMANDS_Continuity, ON);
WireTest('Wire1', "Pin1", "Pin2");
ParamStopOnFail(COMMANDS_Continuity, OFF);
```

## See also

`ConnectionTest`, `ParamAutostart`, `ParamPowerPinsDuringStopOnFail`, `ParamSearchDepth`, `SwitchTest`, `WireTest`
