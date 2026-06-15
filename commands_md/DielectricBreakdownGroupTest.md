# DielectricBreakdownGroupTest

## Declaration

```ats
function DielectricBreakdownGroupTest(): void;
```

## Call pattern

```ats
DielectricBreakdownGroupTest();
```

## Description

The function executes an automatic dielectric breakdown test with group commands.
It is only adequate for small UUTs because of the groupwise matrix switching.

Notice: Pins and networks which are excluded from the dielectric breakdown test by run parameters are completely ignored during this test.

## Metadata

- Category: Electrical testing
- Code: 1547
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
DielectricBreakdownGroupTest();
```

## See also

`DielectricBreakdownTest`, `IsolationGroupTestHV`, `IsolationGroupTestLV`, `NoConnGroupDB`, `ParamDielectricBreakdown`
