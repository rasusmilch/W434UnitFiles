# UIAutostartSetColor

## Declaration

```ats
function UIAutostartSetColor(Commands: integer; Property: string; Value: integer): void;
```

## Call pattern

```ats
UIAutostartSetColor(COMMANDS_?, 'Color', COLOR_?);
```

## Description

Changes a color in an autostart window.

## Metadata

- Category: Userinterface Access
- Code: 263977
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_Continuity, COMMANDS_IsolationLV, COMMANDS_ElectricalComponents, COMMANDS_Voltage
- `Property`: `string` — Allowed values: 'TextFont', 'TextBackground'
- `Value`: `integer` — Allowed values: COLOR_Black, COLOR_White, COLOR_Red, COLOR_Blue, COLOR_DkGray, COLOR_Gray, COLOR_DkRed, COLOR_Green, COLOR_DkGreen, COLOR_DkBlue, COLOR_Brown, COLOR_DkBrown, COLOR_Yellow, COLOR_Olive, COLOR_Orange, COLOR_Purple, COLOR_Teal, COLOR_Magenta, COLOR_Cyan, COLOR_Automatic

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

`ParamAutostart`, `UIAutostartSelectWindowType`, `UIAutostartSetBoolean`, `UIAutostartSetString`, `UIAutostartSetWindowPosition`
