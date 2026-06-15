# MiscRangeTestConnectors

## Declaration

```ats
function MiscRangeTestConnectors(RangeTestConnectors: tcreatearray; UsedConnectors: boolean = TRUE): integer;
```

## Call pattern

```ats
MiscRangeTestConnectors(RangeTestConnectors);
```

## Description

If UsedConnectors is TRUE the function returns the connectors which were selected for a connector range test.

If UsedConnectors is FALSE the function returns the connectors which were disabled for the test.

## Metadata

- Category: Miscellaneous
- Code: 266502
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `RangeTestConnectors`: `tcreatearray`
- `UsedConnectors`: `boolean = TRUE`

## Return value

The function returns the number of connectors.

The names of the connectors are returned in "RangeTestConnectors".

## Example

```ats
ConnectorCount =  MiscRangeTestConnectors(RangeTestConnectors, TRUE);
for Count = 1 to ConnectorCount do
begin
   UIWriteNormal(RangeTestConnectors[Count]);
end;
```

## See also

`MiscRangeTestFunction`, `MiscRangeTestFunctionCount`, `MiscRangeTestGetType`, `MiscRangeTestRunning`
