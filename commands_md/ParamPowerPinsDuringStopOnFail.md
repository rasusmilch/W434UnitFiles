# ParamPowerPinsDuringStopOnFail

## Declaration

```ats
function ParamPowerPinsDuringStopOnFail(KeepOn: boolean): void;
```

## Call pattern

```ats
ParamPowerPinsDuringStopOnFail(ON|OFF);
```

## Description

You can specify with this function whether the power pins shall stay activated or shall be deactivated during "Stop-on-fail"

ON is the default state
If OFF the power pins will be activated when leaving the "Stop-on-fail" window.

## Metadata

- Category: Parameters
- Code: 266262
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `KeepOn`: `boolean` — ON means that the Powerpins stay activated during "Stop-on-fail".; This is the default state
; OFF means that the Powerpins are deactivated during "Stop-on-fail".; Allowed values: ON, OFF

## Example

```ats
ParamStopOnFail(COMMANDS_Continuity, ON);
ConnectionTest('ConnectionTest', "1", "2");
ParamPowerPinsDuringStopOnFail(OFF);
ConnectionTest('ConnectionTest', "1", "2");
```

## See also

`ParamStopOnFail`
