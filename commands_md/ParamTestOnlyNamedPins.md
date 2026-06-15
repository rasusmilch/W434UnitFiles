# ParamTestOnlyNamedPins

## Declaration

```ats
function ParamTestOnlyNamedPins(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamTestOnlyNamedPins(COMMANDS_?, ON|OFF);
```

## Description

The function enables and disables the exclusive test of named pins.

By default not only named pins are tested.

## Metadata

- Category: Parameters
- Code: 266257
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
ParamTestOnlyNamedPins(COMMANDS_IsolationLV, ON);
ParamTestOnlyNamedPins(COMMANDS_IsolationHV, ON);
ParamTestOnlyNamedPins(COMMANDS_DielectricBreakdown, ON);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `ParamAutomaticIsolationTestNCA`, `ParamTestComponentNetworks`, `ParamTestNetworksWithPowerPins`, `ParamTestOnlyUsedPins`, `ParamTestSecondaryPinsOnFail`
