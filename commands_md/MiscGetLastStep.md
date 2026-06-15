# MiscGetLastStep

## Declaration

```ats
function MiscGetLastStep(): integer;
```

## Call pattern

```ats
MiscGetLastStep();
```

## Description

Returns a value that tells which step was executed last.

## Metadata

- Category: Miscellaneous
- Code: 266508
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Return value

Possible values:

STEP_None, STEP_ProjectSelection, STEP_TestInitialization, STEP_WaitForTeststart, STEP_Test, STEP_ReportGeneration, STEP_TestEnd

## Example

```ats
LastStep = MiscGetLastStep();
switch (LastStep)
begin
   case STEP_None: begin
      UIWriteNormal('Nothing');
   end;
   case STEP_ProjectSelection: begin
      UIWriteNormal('Project selection');
   end;
   case STEP_TestInitialization: begin
      UIWriteNormal('Test initialization');
   end;
   case STEP_WaitForTeststart: begin
      UIWriteNormal('Waited for teststart');
   end;
   case STEP_Test: begin
      UIWriteNormal('Test');
   end;
   case STEP_ReportGeneration: begin
      UIWriteNormal('Report generation');
   end;
   case STEP_TestEnd: begin
      UIWriteNormal('Test end');
   end;
end;
```

## See also

`ProjectSelectionSetAutostartTest`, `TestEndSetNextStep`, `TestInitSetNextStep`
