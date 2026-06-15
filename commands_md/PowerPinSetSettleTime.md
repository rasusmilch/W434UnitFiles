# PowerPinSetSettleTime

## Declaration

```ats
function PowerPinSetSettleTime(SettleTime: ttime): void;
```

## Call pattern

```ats
PowerPinSetSettleTime(<SettleTime>s);
```

## Description

Sets the relay settle time for powerpins.

## Metadata

- Category: Powerpin Access
- Code: 264193
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `SettleTime`: `ttime`

## Example

```ats
PowerPinSetSettleTime(200ms);
```

## See also

`PowerIPinSetHigh`, `PowerIPinSetLow`, `PowerIPinSetTPHigh`, `PowerIPinSetTPLow`, `PowerMPinSetHigh`, `PowerMPinSetLow`, `PowerMPinSetTPHigh`, `PowerMPinSetTPLow`, `PowerUPinSetHigh`, `PowerUPinSetLow`, `PowerUPinSetTPHigh`, `PowerUPinSetTPLow`
