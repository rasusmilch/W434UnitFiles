# IsolationGroupTestLV

## Declaration

```ats
function IsolationGroupTestLV(): void;
```

## Call pattern

```ats
IsolationGroupTestLV();
```

## Description

The function executes an automatic LV isolaton test with group commands.
It is only adequate for small UUTs because of the groupwise matrix switching.

Notice: Pins and networks which are excluded from the LV isolation test by run parameters are completely ignored during this test.

## Metadata

- Category: Electrical testing
- Code: 1036
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## See also

`DielectricBreakdownGroupTest`, `IsolationGroupTestHV`, `IsolationTestLV`, `NoConnGroupLV`, `ParamIsolationLV`
