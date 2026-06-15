# ParamFourWireAdaptionMonitoring

## Declaration

```ats
function ParamFourWireAdaptionMonitoring(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamFourWireAdaptionMonitoring(COMMANDS_?, ON|OFF);
```

## Description

The function enables and disables the four wire adaption monitoring

## Metadata

- Category: Parameters
- Code: 266264
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_ElectricalComponents
- `OnOff`: `boolean` — Allowed values: ON, OFF

## Example

```ats
ParamFourWireAdaptionMonitoring(COMMANDS_Continuity, ON);
WireTest('Wire1', "Pin1", "Pin2");
ParamFourWireAdaptionMonitoring(COMMANDS_Continuity, OFF);
```

## See also

`ConnectionTest`, `IsConnected`, `ResistorTest`, `SwitchTest`, `WireTest`
