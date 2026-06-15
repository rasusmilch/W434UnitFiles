# OpticalPinGetData

## Declaration

```ats
function OpticalPinGetData(PinAddress: integer; DataID: integer): string;
```

## Call pattern

```ats
OpticalPinGetData(PinAddress, OPTICALPIN_?);
```

## Description

Returns informations about the optical pin with address "PinAddress".

## Metadata

- Category: Pin Access
- Code: 268562
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `PinAddress`: `integer`
- `DataID`: `integer` — Allowed values: OPTICALPIN_AnyName, OPTICALPIN_Name, OPTICALPIN_AnyNameWithComment, OPTICALPIN_NameWithComment, OPTICALPIN_Comment, OPTICALPIN_InstallationZone, OPTICALPIN_Info

## Example

```ats
AnyName = PinGetData(1, PIN_AnyName);
UIWriteNormal(AnyName);
```

## See also

`OFAttenuationTest`
