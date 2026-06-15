# MiscRangeTestRunning

## Declaration

```ats
function MiscRangeTestRunning(): boolean;
```

## Call pattern

```ats
MiscRangeTestRunning();
```

## Description

Returns TRUE if a range test is running, otherwise FALSE.

## Metadata

- Category: Miscellaneous
- Code: 266504
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
if (MiscRangeTestRunning())
begin
   FunctionName = MiscRangeTestFunction();
   UIWriteNormal(StrAdd('Range test running. Function: ', FunctionName));
end
else
begin
   UIWriteNormal('Normal test running');
end;
```

## See also

`MiscRangeTestConnectors`, `MiscRangeTestFunction`, `MiscRangeTestFunctionCount`, `MiscRangeTestGetType`
