# RemoteSetVoltage

## Declaration

```ats
function RemoteSetVoltage(Card: integer; Channel: integer; Voltage: tvoltage): void;
```

## Call pattern

```ats
RemoteSetVoltage(Card, Channel, <Voltage>V);
```

## Description

Sets the voltage of an analog channel of a remote card.
If the channel is acitve, the voltage is instantly turned on.
Otherwise it is turned on when the channel is activated.

## Metadata

- Category: Remote Interface Access
- Code: 268803
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Card`: `integer` — Number of the remote card.
- `Channel`: `integer` — Analog channel of the card.
; Allowed values: 1, 2
- `Voltage`: `tvoltage` — Voltage value in the preset range.

## Example

```ats
RemoteSetVoltageRange(1, REMOTE_Voltage_Range_10V);
RemoteSetVoltage(1, 1, 3.5V);
RemoteVoltageOnOff(1, 1, ON);
```

## See also

`RemoteSetVoltageRange`, `RemoteVoltageAllOff`, `RemoteVoltageOnOff`
