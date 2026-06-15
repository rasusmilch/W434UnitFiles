# MiscGetNumberOfExecutedCommands

## Declaration

```ats
function MiscGetNumberOfExecutedCommands(CommandGroup: integer): integer;
```

## Call pattern

```ats
MiscGetNumberOfExecutedCommands(CMDGRP_?);
```

## Description

Returns the number of commands in commandgroup "CommandGroup" the were executed during the test.

## Metadata

- Category: Miscellaneous
- Code: 266503
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `CommandGroup`: `integer` — Allowed values: CMDGRP_Continuity, CMDGRP_IsolationLV, CMDGRP_IsolationHV, CMDGRP_DielectricBreakdown, CMDGRP_ElectricalComponents, CMDGRP_OpticalComponents, CMDGRP_CANBus, CMDGRP_IDD, CMDGRP_VoltageAndCurrent, CMDGRP_LV

## Example

```ats
ContinuityCommands = MiscGetNumberOfExecutedCommands(CMDGRP_Continuity);
```
