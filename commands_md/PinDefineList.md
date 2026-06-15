# PinDefineList

## Declaration

```ats
function PinDefineList(ListName: tcreatearray; Pins: tpinarray): void;
```

## Call pattern

```ats
PinDefineList(ListName, ["Pin1", "Pin2", ...]);
```

## Description

Defines al list which contains the passed pins.

## Metadata

- Category: Pin Access
- Code: 268560
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ListName`: `tcreatearray`
- `Pins`: `tpinarray`

## Example

```ats
MaximumVoltageDC = PinGroupGetMaximumVoltage(["Pin1", "Pin2", "Pin3"], TRUE);
PinDefineList(List, ["Pin1", "Pin2", "Pin3"]);
MaximumVoltageAC = PinGroupGetMaximumVoltage(List, FALSE);
```

## See also

`MiscGetListSize`, `NoConnGroupDB`, `NoConnGroupHV`, `NoConnGroupLV`, `PinCreateList`, `PinGroupSetHighLow`
