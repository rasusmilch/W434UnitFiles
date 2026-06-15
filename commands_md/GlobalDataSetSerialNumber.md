# GlobalDataSetSerialNumber

## Declaration

```ats
function GlobalDataSetSerialNumber(SerialNumber: string): void;
```

## Call pattern

```ats
GlobalDataSetSerialNumber('SerialNumber');
```

## Description

Stores the passed value as a serial number in the global data list.

## Metadata

- Category: Global data
- Code: 269830
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `SerialNumber`: `string`

## Example

```ats
GlobalDataSetSerialNumber('1234567890');
SerialNumber = GlobalDataGetSerialNumber();
UIWriteNormal(SerialNumber);
```

## See also

`GlobalDataClear`, `GlobalDataGetSerialNumber`, `GlobalDataSetOrderNumber`, `GlobalDataWrite`
