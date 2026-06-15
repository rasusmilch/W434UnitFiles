# GlobalDataGetOrderNumber

## Declaration

```ats
function GlobalDataGetOrderNumber(): string;
```

## Call pattern

```ats
GlobalDataGetOrderNumber();
```

## Description

Retrieves the order number from the global data list.

## Metadata

- Category: Global data
- Code: 269833
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
GlobalDataSetOrderNumber('XY-123');
OrderNumber = GlobalDataGetOrderNumber();
UIInfoDialog(OrderNumber);
```

## See also

`GlobalDataClear`, `GlobalDataGetSerialNumber`, `GlobalDataRead`, `GlobalDataSetOrderNumber`
