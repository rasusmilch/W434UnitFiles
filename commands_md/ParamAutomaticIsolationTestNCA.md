# ParamAutomaticIsolationTestNCA

## Declaration

```ats
function ParamAutomaticIsolationTestNCA(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamAutomaticIsolationTestNCA(COMMANDS_?, ON|OFF);
```

## Description

This function specifies whether automatic isolation test are executed with NoConnAll??- (test each pin against all other pins) or NoConnLower??- (test each pin against pins with lower address) functions.

The NoConnLower??-functions are used by default.

## Metadata

- Category: Parameters
- Code: 266260
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
ParamAutomaticIsolationTestNCA(COMMANDS_IsolationLV, OFF);
ParamAutomaticIsolationTestNCA(COMMANDS_IsolationHV, OFF);
ParamAutomaticIsolationTestNCA(COMMANDS_DielectricBreakdown, OFF);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `ParamTestComponentNetworks`, `ParamTestNetworksWithPowerPins`, `ParamTestOnlyNamedPins`, `ParamTestOnlyUsedPins`, `ParamTestSecondaryPinsOnFail`
