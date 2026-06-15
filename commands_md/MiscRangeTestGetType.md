# MiscRangeTestGetType

## Declaration

```ats
function MiscRangeTestGetType(): integer;
```

## Call pattern

```ats
MiscRangeTestGetType();
```

## Description

Returns the type of the range test which is currently executed.

## Metadata

- Category: Miscellaneous
- Code: 266501
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Return value

Possible values:

RANGETEST_None, RANGETEST_Functions, RANGETEST_Connectors, RANGETEST_AdtIsolationLV, RANGETEST_AdtIsolationHV, RANGETEST_AdtDielectricBreakdown

## See also

`MiscRangeTestConnectors`, `MiscRangeTestFunction`, `MiscRangeTestFunctionCount`, `MiscRangeTestRunning`
