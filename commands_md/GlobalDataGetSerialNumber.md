# GlobalDataGetSerialNumber

## Declaration

```ats
function GlobalDataGetSerialNumber(): string;
```

## Call pattern

```ats
GlobalDataGetSerialNumber();
```

## Description

Retrieves the serial number from the global data list.

## Metadata

- Category: Global data
- Code: 269831
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
GlobalDataSetSerialNumber('1234567890');
SerialNumber = GlobalDataGetSerialNumber();
UIWriteNormal(SerialNumber);
```

## See also

`GlobalDataClear`, `GlobalDataGetOrderNumber`, `GlobalDataRead`, `GlobalDataSetSerialNumber`
