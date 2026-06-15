# MiscGetLastTest

## Declaration

```ats
function MiscGetLastTest(var LastProject: string; var UserBreak: boolean; var Pass: boolean): boolean;
```

## Call pattern

```ats
MiscGetLastTest(Project, UserBreak, Pass);
```

## Description

Returns informations about the last test run. The informations are always updated after the termination of the test end program.

## Metadata

- Category: Miscellaneous
- Code: 266507
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `var LastProject`: `string` — Filename of the last project
- `var UserBreak`: `boolean` — TRUE if the last test was aborted, otherwise FALSE
- `var Pass`: `boolean` — TRUE if the last test passed, otherwise FALSE

## Return value

Returns TRUE, if informations are available, otherwise FALSE.

## Example

```ats
LastProject = '';
UserBreak = FALSE;
Pass = FALSE;
if (MiscGetLastTest(LastProject, UserBreak, Pass))
begin
   UIWriteNormal(StrAdd('Last project: ', LastProject));
   if (UserBreak)
   begin
      UIWriteNormal('Aborted by user');
   end
   else
   begin
      if (Pass)
      begin
         UIWriteNormal('Passed');
      end
      else
      begin
         UIWriteNormal('Failed');
      end;
   end;
end
else
begin
   UIWriteNormal('No data available');
end;
```
