# MiscGetVersion

## Declaration

```ats
function MiscGetVersion(Version: integer): string;
```

## Call pattern

```ats
MiscGetVersion(VERSION_?);
```

## Description

Returns version numbers of software and firmware.

## Metadata

- Category: Miscellaneous
- Code: 266518
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Version`: `integer` — Version number of CEETIS
; Version number of the firmware of the control unit (STE) of the test system
; Version number of the LV PLUS service
; Version number of the firmware of the LV PLUS controller; Allowed values: VERSION_CEETIS, VERSION_Firmware, VERSION_LV_PLUS_Service, VERSION_LV_PLUS_Firmware

## Example

```ats
CEETISVersion = MiscGetVersion(VERSION_CEETIS);
UIWriteNormal(StrAdd('CEETIS Version: ', CEETISVersion));

FirmwareVersion = MiscGetVersion(VERSION_Firmware);
UIWriteNormal(StrAdd('Firmware Version: ', FirmwareVersion));

LVPLUSServiceVersion = MiscGetVersion(VERSION_LV_PLUS_Service);
UIWriteNormal(StrAdd('LV PLUS Service Version: ', LVPLUSServiceVersion));

LVPLUSFirmwareVersion = MiscGetVersion(VERSION_LV_PLUS_Firmware);
UIWriteNormal(StrAdd('LV PLUS Firmware Version: ', LVPLUSFirmwareVersion));
```

## See also

`ProjectGetVersion`, `MiscGetTestStationIdentifier`, `MiscGetCompanyInfo`
