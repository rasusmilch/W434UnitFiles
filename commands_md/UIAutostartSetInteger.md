# UIAutostartSetInteger

## Declaration

```ats
function UIAutostartSetInteger(Commands: integer; Property: string; Value: integer): void;
```

## Call pattern

```ats
UIAutostartSetInteger(COMMANDS_?, 'Property', <Value>);
```

## Description

Sets the value of an integer property of an Autostart window.

## Metadata

- Category: Userinterface Access
- Code: 263976
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Not listed
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_IsolationLV, COMMANDS_ElectricalComponents, COMMANDS_Voltage
- `Property`: `string` — Allowed values: 'Left', 'Top', 'BackgroundColor', 'FontColor'
- `Value`: `integer`

## Example

```ats
ParamAutostart(COMMANDS_Continuity, ON);
UIAutostartSelectWindowType(COMMANDS_Continuity, 'Media01');
UIAutostartSetColor(COMMANDS_Continuity, 'TextFont', COLOR_White);
UIAutostartSetColor(COMMANDS_Continuity, 'TextBackground', COLOR_Red);
UIAutostartSetWindowPosition(COMMANDS_Continuity, 20, 50);
UIAutostartSetString(COMMANDS_Continuity, 'Text', 'Press red button!<br>Roten Knopf dr�cken!');
UIAutostartSetString(COMMANDS_Continuity, 'File', 'c:\ButtonRed.jpg');
UIAutostartSetBoolean(COMMANDS_Continuity, 'ShowPins', FALSE);
WireTest('RedButton', "RedButtonPin1", "RedButtonPin2");
UIAutostartSelectWindowType(COMMANDS_Continuity, 'Default');
```

## See also

`ParamAutostart`, `UIAutostartSelectWindowType`, `UIAutostartSetBoolean`, `UIAutostartSetColor`, `UIAutostartSetPosition`, `UIAutostartSetString`
