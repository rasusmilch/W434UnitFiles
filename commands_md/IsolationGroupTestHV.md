# IsolationGroupTestHV

## Declaration

```ats
function IsolationGroupTestHV(): void;
```

## Call pattern

```ats
IsolationGroupTestHV();
```

## Description

The function executes an automatic HV isolaton test with group commands.
It is only adequate for small UUTs because of the groupwise matrix switching.

Notice: Pins and networks which are excluded from the HV isolation test by run parameters are completely ignored during this test.

## Metadata

- Category: Electrical testing
- Code: 1291
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
IsolationGroupTestHV()
```

## See also

`DielectricBreakdownGroupTest`, `IsolationGroupTestLV`, `IsolationTestHV`, `NoConnGroupHV`, `ParamIsolationHV`
