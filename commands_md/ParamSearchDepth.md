# ParamSearchDepth

## Declaration

```ats
function ParamSearchDepth(Commands: integer; Search: integer): void;
```

## Call pattern

```ats
ParamSearchDepth(COMMANDS_?, SEARCH_?);
```

## Description

The function sets the search depth for errors which are detected during a LV isolation test, a HV isolation test or a dielectric breakdown test.

## Metadata

- Category: Parameters
- Code: 266255
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Commands`: `integer` — Allowed values: COMMANDS_IsolationLV, COMMANDS_IsolationHV, COMMANDS_DielectricBreakdown
- `Search`: `integer` — Allowed values: SEARCH_Off, SEARCH_FirstPin, SEARCH_AllPins

## Example

```ats
ParamSearchDepth(COMMANDS_IsolationLV, SEARCH_AllPins);
ParamSearchDepth(COMMANDS_IsolationHV, SEARCH_FirstPin);
ParamSearchDepth(COMMANDS_DielectricBreakdown, SEARCH_Off);
```

## See also

`ParamAutostart`, `ParamStopOnFail`
