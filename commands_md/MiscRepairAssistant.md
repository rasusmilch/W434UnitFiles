# MiscRepairAssistant

## Declaration

```ats
function MiscRepairAssistant(var ErrorsToRepair: integer; var ErrorsRepaired: integer; SavingAllowed: boolean): void;
```

## Call pattern

```ats
MiscRepairAssistant(ErrorsToRepair, ErrorsRepaired, TRUE|FALSE);
```

## Description

Executes the repair assistant.

All errors that are supported by the repair assistant will be listed in a window.
They can be re-tested after the repair.
If the re-testing is successful the fail counter will be decremented accordingly.

If no errors occured that are supported by the repair assistant the window will not appear.

Supported functions are:

WireTest, SwitchTest, ResistorTest, ResistorTestCustom, CapacitorTest, DiodeTest, DiodeTestCustom, ZDiodeTest, ZDiodeTestCustom, CTwistTestAC, ConnectionTest, ConnectionTestLV, ConnectionTestHV, ConnectionTestDB, NoConnection, NoConnectionLV, NoConnectionHV, NoConnectionDB, RLCSerialInductanceTest, RLCParallelInductanceTest, RLCSerialCapacitanceTest, RLCParallelCapacitanceTest, RLCSerialResistanceTest, RLCParallelResistanceTest, RLCDissipationTest, RLCQualityTest, RLCPhaseAngleTest, RLCImpedanceImaginaryTest, RLCImpedanceRealTest, RLCImpedanceAbsoluteTest, VoltageTest, VoltageTestCustom, ProbeTest, NoConnLowerLV, NoConnLowerHV, NoConnLowerDB, NoConnAllLV, NoConnAllHV, NoConnAllDB

## Metadata

- Category: Miscellaneous
- Code: 266511
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `var ErrorsToRepair`: `integer` — Returns the number of repairable errors when the repair assistant starts up.
- `var ErrorsRepaired`: `integer` — Returns the number of repaired errors.
- `SavingAllowed`: `boolean` — If TRUE ist passed it is possible to save the errors to a new repair project.; Allowed values: TRUE, FALSE

## Example

```ats
ErrorsToRepair = 0;
ErrorsRepaired = 0;
MiscRepairAssistant(ErrorsToRepair, ErrorsRepaired, TRUE);
UIWriteNormal(StrAdd('Errors to repair: ', ErrorsToRepair));
UIWriteNormal(StrAdd('Errors repaired : ', ErrorsRepaired));
```
