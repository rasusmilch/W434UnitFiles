# GenStimMeasInfo

## Declaration

```ats
function GenStimMeasInfo(Device:integer;Value:integer):string;
```

## Call pattern

```ats
GenStimMeasInfo(DEVICE_?,INFO_?);
```

## Description

Device hardware information

## Metadata

- Category: Generators
- Code: 270098
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Device`: `integer` — Allowed values: DEVICE_UI51, DEVICE_UI52, DEVICE_UI53, DEVICE_UI53_U2, DEVICE_UI53_U3, DEVICE_UI54, DEVICE_UI54_U2, DEVICE_UI54_U3, DEVICE_HVG2250, DEVICE_HVG5000, DEVICE_HVG7000, DEVICE_UI55, DEVICE_WA02, DEVICE_WA07, DEVICE_VE43, DEVICE_VE46, DEVICE_UI5502, DEVICE_WA12, DEVICE_UI58, DEVICE_HVG4300, DEVICE_HVG5100, DEVICE_HVG4312
- `Value`: `integer` — Allowed values: INFO_Revision, INFO_RevisionNumber, INFO_SerialNumber, INFO_BillOffMaterialsNumber
