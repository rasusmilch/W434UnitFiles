# ParamAutostartTimeout

## Declaration

```ats
function ParamAutostartTimeout(Commands: integer; Action: integer; Timeout: ttime = 5s): void;
```

## Call pattern

```ats
ParamAutostartTimeout(COMMANDS_?, AUTOSTART_TIMEOUT_ACTION_?, <Timeout>s);
```

## Description

This function specifies what happens after the test waited for a specified time in the Autostart

It has only an effect if the Autostart is activated.

The default behaviour (wait in Autostart indefinitely) can be set by passing the value AUTOSTART_TIMEOUT_ACTION_None to the parameter Action.

## Metadata

- Category: Parameters
- Code: 266261
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_ElectricalComponents, COMMANDS_IsolationLV, COMMANDS_Voltage, COMMANDS_Detections
- `Action`: `integer` — AUTOSTART_TIMEOUT_ACTION_None
; Wait in Autostart indefinitely; AUTOSTART_TIMEOUT_ACTION_CountAsFail; Count the test step as failed after the timeout; AUTOSTART_TIMEOUT_ACTION_StopOnFail; Switch to stop on fail after the timeout; Allowed values: AUTOSTART_TIMEOUT_ACTION_None, AUTOSTART_TIMEOUT_ACTION_CountAsFail, AUTOSTART_TIMEOUT_ACTION_StopOnFail
- `Timeout`: `ttime = 5s`

## Example

```ats
ParamAutostart(COMMANDS_Continuity, ON);
ParamAutostartTimeout(COMMANDS_Continuity, AUTOSTART_TIMEOUT_ACTION_StopOnFail, 20s);
ConnectionTest('Connection 1', "1", "2");
ParamAutostartTimeout(COMMANDS_Continuity, AUTOSTART_TIMEOUT_ACTION_None);
```

## See also

`ConnectionTesLV,`, `ConnectionTest`, `NoConnAll`, `NoConnAllLV`, `NoConnection`, `NoConnectionLV`, `NoConnGroupLV`, `ParamAutostart`, `ResistorTest`, `SwitchTest`, `VariableResistorTest`, `WireTest`
