# ParamGetAutostart

## Declaration

```ats
function ParamGetAutostart(Commands: integer): boolean;
```

## Call pattern

```ats
ParamGetAutostart(COMMANDS_?);
```

## Description

Returns TRUE, if AutoStart for the specified commands is enabled, otherwise FALSE

## Metadata

- Category: Parameters
- Code: 266267
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_IsolationLV, COMMANDS_IsolationHV, COMMANDS_DielectricBreakdown, COMMANDS_ElectricalComponents, COMMANDS_Voltage, COMMANDS_CANBus, COMMANDS_Detections

## Example

```ats
IsOn = ParamGetAutostart(COMMANDS_Continuity);
if (IsOn)
begin
   UIWriteNormal('AutoStart is on');
end
else
begin
   UIWriteNormal('AutoStart is off');
end;
```
