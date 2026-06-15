# MiscRangeTestFunctionCount

## Declaration

```ats
function MiscRangeTestFunctionCount(): integer;
```

## Call pattern

```ats
MiscRangeTestFunctionCount();
```

## Description

Returns the number of functions that were selected for the range test.

## Metadata

- Category: Miscellaneous
- Code: 266509
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
if (MiscRangeTestRunning())
begin
   Count = MiscRangeTestFunctionCount();
   for Index = 1 to Count do
   begin
      FunctionName = MiscRangeTestFunction(Index);
      UIWriteNormal(StrAdd('Range test running. Function: ', FunctionName));
   end;
end
else
begin
   UIWriteNormal('Normal test running');
end;
```

## See also

`MiscRangeTestConnectors`, `MiscRangeTestFunction`, `MiscRangeTestGetType`, `MiscRangeTestRunning`
