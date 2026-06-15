# ParamIsCommandGroupAvailable

## Declaration

```ats
function ParamIsCommandGroupAvailable(CommandGroup: integer): boolean;
```

## Call pattern

```ats
ParamIsCommandGroupAvailable(CMDGRP_?);
```

## Description

Returns TRUE if the commandgroup "CommandGroup" is available, otherwise FALSE.

## Metadata

- Category: Parameters
- Code: 266265
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program
- Count result: no
- Archive allowed: no

## Parameters

- `CommandGroup`: `integer` — Allowed values: CMDGRP_Continuity, CMDGRP_IsolationLV, CMDGRP_IsolationHV, CMDGRP_DielectricBreakdown, CMDGRP_ElectricalComponents, CMDGRP_OpticalComponents, CMDGRP_CANBus, CMDGRP_IDD, CMDGRP_VoltageAndCurrent, CMDGRP_LV, CMDGRP_TwistedPair

## Example

```ats
if (ParamIsCommandGroupAvailable(CMDGRP_CANBus))
begin
   UIWriteNormal('CAN Bus available');
end
else
begin
   UIWriteNormal('CAN Bus available');
end;
```

## See also

`ParamIsCommandGroupActive`
