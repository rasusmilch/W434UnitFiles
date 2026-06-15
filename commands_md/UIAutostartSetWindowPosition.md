# UIAutostartSetWindowPosition

## Declaration

```ats
function UIAutostartSetWindowPosition(Commands: integer; Left: integer = PARAM_UseDefault; Top: integer = PARAM_UseDefault): void;
```

## Call pattern

```ats
UIAutostartSetWindowPosition(COMMANDS_?, <Left>, <Top>);
```

## Description

Set the position of an autostart window.

## Metadata

- Category: Userinterface Access
- Code: 263978
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_IsolationLV, COMMANDS_ElectricalComponents, COMMANDS_Voltage
- `Left`: `integer = PARAM_UseDefault` — Distance of the window to the left border in pixels
- `Top`: `integer = PARAM_UseDefault` — Distance of the window to the top border in pixels

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

`ParamAutostart`, `UIAutostartSelectWindowType`, `UIAutostartSetBoolean`, `UIAutostartSetColor`, `UIAutostartSetString`
