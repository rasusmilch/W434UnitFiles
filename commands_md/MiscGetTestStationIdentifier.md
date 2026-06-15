# MiscGetTestStationIdentifier

## Declaration

```ats
function MiscGetTestStationIdentifier(): string;
```

## Call pattern

```ats
MiscGetTestStationIdentifier();
```

## Description

Returns the test station identifier which is set at Configuration -> Test station -> Miscellaneous

## Metadata

- Category: Miscellaneous
- Code: 266512
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
TestStationID = MiscGetTestStationIdentifier();
```

## See also

`MiscGetVersion`, `MiscGetCompanyInfo`
