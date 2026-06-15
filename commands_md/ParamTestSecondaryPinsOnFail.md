# ParamTestSecondaryPinsOnFail

## Declaration

```ats
function ParamTestSecondaryPinsOnFail(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamTestSecondaryPinsOnFail(COMMANDS_?, ON|OFF);
```

## Description

The function enables and disables the test of secondary pins of networks, in which continuity errors were detected, during the automatic isolation tests.

By default those secondary pins are tested.

## Metadata

- Category: Parameters
- Code: 266259
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
ParamTestSecondaryPinsOnFail(COMMANDS_IsolationLV, OFF);
ParamTestSecondaryPinsOnFail(COMMANDS_IsolationHV, OFF);
ParamTestSecondaryPinsOnFail(COMMANDS_DielectricBreakdown, OFF);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `ParamAutomaticIsolationTestNCA`, `ParamTestComponentNetworks`, `ParamTestNetworksWithPowerPins`, `ParamTestOnlyNamedPins`, `ParamTestOnlyUsedPins`
