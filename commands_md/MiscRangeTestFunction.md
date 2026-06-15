# MiscRangeTestFunction

## Declaration

```ats
function MiscRangeTestFunction(Index: integer = 1): string;
```

## Call pattern

```ats
MiscRangeTestFunction(<Index>);
```

## Description

Returns the name of the funtions that were executed if a range test was running.

## Metadata

- Category: Miscellaneous
- Code: 266505
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Index`: `integer = 1`

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

`MiscRangeTestConnectors`, `MiscRangeTestFunctionCount`, `MiscRangeTestGetType`, `MiscRangeTestRunning`
