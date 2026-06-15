# MeasureAttenuation

## Declaration

```ats
function MeasureAttenuation(PinA1: tpin; PinA2: tpin; PinB1: tpin; PinB2: tpin; MeasurePolarity: boolean; Frequency: tfrequency; Impedance: tresistance; var Prefix: string; var Value: tattenuation; var InPhase: boolean): boolean;
```

## Call pattern

```ats
MeasureAttenuation("PinA1", "PinA2", "PinB1", "PinB2", TRUE|FALSE, <Frequency>Hz, 50Ohm|77Ohm, Prefix, Value, InPhase);
```

## Description

The function measures the attenuation between PinA1/PinA2 (sender) and PinB1/PinB2 (receiver).
It can also measure whether the receiving side is in phase to the sending side.

## Metadata

- Category: Electrical testing
- Code: 268047
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinA1`: `tpin` — Sender: Pin 1
- `PinA2`: `tpin` — Sender: Pin 2
- `PinB1`: `tpin` — Receiver: Pin 1
- `PinB2`: `tpin` — Receiver: Pin 2
- `MeasurePolarity`: `boolean` — If TRUE is passed the polarity between Sender and Receiver will be measured. If FALSE is passed this measurement will be skipped.; Allowed values: TRUE, FALSE
- `Frequency`: `tfrequency` — Frequency for the measurement (For GEN 1MHz: 1kHz - 1MHz)
- `Impedance`: `tresistance` — Impedance: The GEN 1MHz allows 50Ohm or 77Ohm only.; Allowed values: 50Ohm, 77Ohm
- `var Prefix`: `string` — Variable for the prefix of the measured value ( or empty if equal)
- `var Value`: `tattenuation` — Variable for the measured value in dB
- `var InPhase`: `boolean` — Variable for the result of the polarity measurement (TRUE = in phase)

## Return value

The function returns TRUE if the measurement was successful.

## Example

```ats
Prefix = '';
Value = 0;
InPhase = FALSE;
Success = MeasureAttenuation("PinA1", "PinA2", "PinB1", "PinB2", TRUE, 100kHz, 77Ohm, Prefix, Value, InPhase);
if (Success)
begin
   ValueText = FormatAttenuation(Value);
   ValueText = StrAdd(Prefix, ValueText);
   ValueText = StrAdd('Attenuation: ', ValueText);
   UIWriteNormal(ValueText);
   if (InPhase)
   begin
      UIWriteNormal('The signal at sender and receiver is in phase');
   end
   else
   begin
      UIWriteWarning('The signal at sender and receiver is not in phase');
   end;
end
else
begin
   UIWriteError('Measurement failed');
end;
```

## See also

`AttenuationFrequencySweep`, `AttenuatorTest`
