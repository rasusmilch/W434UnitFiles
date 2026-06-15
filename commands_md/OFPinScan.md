# OFPinScan

## Declaration

```ats
function OFPinScan(Name: string; Pin: topticalpin; Threshold: tattenuation = 30dB; TransmitterPower: tpowerlevel = 12dBm): void;
```

## Call pattern

```ats
OFPinScan('Name', "Pin");
```

## Description

The function searches all optical pins which are connected to the passed pin.

## Metadata

- Category: Optical fibers
- Code: 2561
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Name`: `string`
- `Pin`: `topticalpin`
- `Threshold`: `tattenuation = 30dB`
- `TransmitterPower`: `tpowerlevel = 12dBm`

## Example

```ats
OFPinScan('Name', "OpticalPin1", 25dB, 12dBm);
```
