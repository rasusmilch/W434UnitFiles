# RemoteSetVoltageRange

## Declaration

```ats
function RemoteSetVoltageRange(Card: integer; Range: integer): void;
```

## Call pattern

```ats
RemoteSetVoltageRange(Card, REMOTE_Voltage_Range_?);
```

## Description

Configures the voltage range of the analog channels of a remote card.
Both channels of the card are deactivated and set to 0V.

## Metadata

- Category: Remote Interface Access
- Code: 268802
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Card`: `integer` — Number of the remote card.
- `Range`: `integer` — Sets the voltage range of the card: 0-5V or 0-10V.
; Allowed values: REMOTE_Voltage_Range_5V, REMOTE_Voltage_Range_10V

## Example

```ats
RemoteSetVoltageRange(1, REMOTE_Voltage_Range_10V);
RemoteSetVoltage(1, 1, 3.5V);
RemoteVoltageOnOff(1, 1, ON);
```

## See also

`RemoteSetVoltage`, `RemoteVoltageAllOff`, `RemoteVoltageOnOff`
