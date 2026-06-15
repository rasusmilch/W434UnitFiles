# ParamIsCommandGroupActive

## Declaration

```ats
function ParamIsCommandGroupActive(CommandGroup: integer): boolean;
```

## Call pattern

```ats
ParamIsCommandGroupActive(CMDGRP_?);
```

## Description

Returns TRUE if the commandgroup "CommandGroup" is active, otherwise FALSE.

## Metadata

- Category: Parameters
- Code: 266246
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program
- Count result: no
- Archive allowed: no

## Parameters

- `CommandGroup`: `integer` — Allowed values: CMDGRP_Continuity, CMDGRP_IsolationLV, CMDGRP_IsolationHV, CMDGRP_DielectricBreakdown, CMDGRP_ElectricalComponents, CMDGRP_OpticalComponents, CMDGRP_CANBus, CMDGRP_IDD, CMDGRP_VoltageAndCurrent, CMDGRP_LV

## Example

```ats
if (ParamIsCommandGroupActive(CMDGRP_Continuity))
begin
   UIWriteNormal('Continuity test enabled');
end
else
begin
   UIWriteNormal('Continuity test disabled');
end;
```

## See also

`ParamIsCommandGroupAvailable`
