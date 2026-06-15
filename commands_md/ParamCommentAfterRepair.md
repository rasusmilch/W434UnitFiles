# ParamCommentAfterRepair

## Declaration

```ats
function ParamCommentAfterRepair(StopOnFail, RepairAssistant: boolean; Reserved: boolean = OFF): void;
```

## Call pattern

```ats
ParamCommentAfterRepair(ON|OFF, ON|OFF);
```

## Description

Enables and disables the possibility to enter comments after a repair

## Metadata

- Category: Parameters
- Code: 266268
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `StopOnFail`: `boolean` — Prompt for a comment after "Stop-on-Error"; Allowed values: ON, OFF
- `RepairAssistant`: `boolean` — Prompt for a comment in the Repair Assistant; Allowed values: ON, OFF
- `Reserved`: `boolean = OFF` — Reserved for later use; Allowed values: ON, OFF

## Example

```ats
ParamStopOnFail(COMMANDS_Continuity, ON);
ParamCommentAfterRepair(ON, ON);
```
