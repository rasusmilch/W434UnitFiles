# ParamTestComponentNetworks

## Declaration

```ats
function ParamTestComponentNetworks(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamTestComponentNetworks(COMMANDS_?, ON|OFF);
```

## Description

This functions disables and enables the automatic isolation test for networks that are connected to electrical components pins.

By default networks which are connected to electrical components are not tested during automatic isolation tests.

## Metadata

- Category: Parameters
- Code: 266256
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
ParamTestNetworksWithComponents(COMMANDS_IsolationLV, ON);
ParamTestNetworksWithComponents(COMMANDS_IsolationHV, ON);
ParamTestNetworksWithComponents(COMMANDS_DielectricBreakdown, ON);
```

## See also

`ParamAutomaticIsolationTestNCA`, `ParamTestNetworksWithPowerPins`, `ParamTestOnlyNamedPins`, `ParamTestOnlyUsedPins`, `ParamTestSecondaryPinsOnFail`
