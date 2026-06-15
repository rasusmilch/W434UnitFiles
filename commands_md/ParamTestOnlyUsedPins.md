# ParamTestOnlyUsedPins

## Declaration

```ats
function ParamTestOnlyUsedPins(Commands: integer; OnOff: boolean): void;
```

## Call pattern

```ats
ParamTestOnlyUsedPins(COMMANDS_?, ON|OFF);
```

## Description

The function enables and disables the exclusive test of pins which are used in the net list.

By default not only used pins are tested.

## Metadata

- Category: Parameters
- Code: 266258
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
ParamTestOnlyUsedPins(COMMANDS_IsolationLV, OFF);
ParamTestOnlyUsedPins(COMMANDS_IsolationHV, OFF);
ParamTestOnlyUsedPins(COMMANDS_DielectricBreakdown, OFF);
```

## See also

`DielectricBreakdownTest`, `IsolationTestHV`, `IsolationTestLV`, `ParamAutomaticIsolationTestNCA`, `ParamTestComponentNetworks`, `ParamTestNetworksWithPowerPins`, `ParamTestOnlyNamedPins`, `ParamTestSecondaryPinsOnFail`
