# AttenuationFrequencySweep

## Declaration

```ats
function AttenuationFrequencySweep(TransmitterPin1: tpin; TransmitterPin2: tpin; ReceiverPin1: tpin; ReceiverPin2: tpin; MinFrequency: tfrequency; MaxFrequency: tfrequency; StepWidth: tfrequency; Impedance: tresistance; FrequencyValues: tcreatearray; AttenuationValues: tcreatearray): integer;
```

## Call pattern

```ats
AttenuationFrequencySweep("TransmitterPin1", "TransmitterPin2", "ReceiverPin1", "ReceiverPin2", <Min>Hz, <Max>Hz, <Step>Hz, 50|77Ohm, FrequencyValues, AttenuationValues);
```

## Description

Measures the attenuation of an UUT with different frequencies within a specified frequency range.

## Metadata

- Category: Electrical testing
- Code: 268042
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `TransmitterPin1`: `tpin`
- `TransmitterPin2`: `tpin`
- `ReceiverPin1`: `tpin`
- `ReceiverPin2`: `tpin`
- `MinFrequency`: `tfrequency`
- `MaxFrequency`: `tfrequency`
- `StepWidth`: `tfrequency`
- `Impedance`: `tresistance` — Allowed values: 50Ohm, 77Ohm
- `FrequencyValues`: `tcreatearray`
- `AttenuationValues`: `tcreatearray`

## Return value

The function returns the number of value pairs.

## Example

```ats
AttenuationFrequencySweep("1", "2", "3", "4", 100kHz, 400kHz, 10kHz, 50Ohm, FrequencyValues, AttenuationValues);
File = 'C:\Images\AttenuationSweep.jpg';
UICurveToImage(File, 'Attenuation Sweep', 'f [kHz]', 'A [dB]', FrequencyValues, AttenuationValues, 1024, 768, 0.001);
UIMediaDialogOk('Attenuation Sweep', File);
```

## See also

`UICurvesToImage`, `UICurveToImage`, `UIDefineCurve`
