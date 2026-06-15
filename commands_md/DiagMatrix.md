# DiagMatrix

## Declaration

```ats
function DiagMatrix(Diagnostics: integer; AbortAllowed: boolean; ShowResultOnPass: boolean; ShowResultOnFail: boolean): integer;
```

## Call pattern

```ats
DiagMatrix(MTX_DIAG_?, FALSE, TRUE, FALSE);
```

## Description

Executes a matrix diagnostics.

The test- and hybrid-pins will be tested.

Hint:
Before a diagnostics is executed make sure that the UUT is disconnected from the tester and that all external power supplies are switched off.

## Metadata

- Category: Diagnostics
- Code: 269314
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: yes
- Archive allowed: no

## Parameters

- `Diagnostics`: `integer` — Allowed values: MTX_DIAG_Continuity, MTX_DIAG_DCLeakage
- `AbortAllowed`: `boolean` — Allow to abort the diagnostics
; If the diagnostics is aborted the test will be aborted as well; Allowed values: TRUE, FALSE
- `ShowResultOnPass`: `boolean` — Show the result if the diagnostics passed; Allowed values: TRUE, FALSE
- `ShowResultOnFail`: `boolean` — Show the result if the diagnostics failed; Allowed values: TRUE, FALSE

## Return value

Possible values:

TESTSTEP_Passed, TESTSTEP_Failed, TESTSTEP_Invalid, TESTSTEP_NotExecuted.

## Example

```ats
MtxOk = DiagMatrix(MTX_DIAG_Continuity, TRUE, FALSE, TRUE);
if (MtxOk == TESTSTEP_Passed)
begin
   UIWriteNormal('Matrix ok');
end
else
begin
   UIWriteError('Error in matrix found');
end;


```
