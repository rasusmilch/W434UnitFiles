# ParamTestNetworksWithPowerPins

## Declaration

```ats
function ParamTestNetworksWithPowerPins(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamTestNetworksWithPowerPins(COMMANDS_?, ON|OFF);
```

## Description

This functions disables and enables the automatic isolation test for networks that are connected to power pins.
By default networks which are connected to power pins are tested during automatic isolation tests.

## Metadata

- Category: Parameters
- Code: 266253
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_IsolationLV, COMMANDS_IsolationHV, COMMANDS_DielectricBreakdown
- `OnOff`: `boolean` — Allowed values: ON, OFF

## Example

```ats
ParamTestNetworksWithPowerPins(COMMANDS_IsolationLV, OFF);
ParamTestNetworksWithPowerPins(COMMANDS_IsolationHV, OFF);
ParamTestNetworksWithPowerPins(COMMANDS_DielectricBreakdown, OFF);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`
