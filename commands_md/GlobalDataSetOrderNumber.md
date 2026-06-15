# GlobalDataSetOrderNumber

## Declaration

```ats
function GlobalDataSetOrderNumber(OrderNumber: string): void;
```

## Call pattern

```ats
GlobalDataSetOrderNumber('OrderNumber');
```

## Description

Stores the passed value as a order number in the global data list.

## Metadata

- Category: Global data
- Code: 269832
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `OrderNumber`: `string`

## Example

```ats
GlobalDataSetOrderNumber('1234567890');
OrderNumber = GlobalDataGetOrderNumber();
UIWriteNormal(OrderNumber);
```

## See also

`GlobalDataClear`, `GlobalDataGetOrderNumber`, `GlobalDataSetSerialNumber`, `GlobalDataWrite`
