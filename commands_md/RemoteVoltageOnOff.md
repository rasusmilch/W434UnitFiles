# RemoteVoltageOnOff

## Declaration

```ats
function RemoteVoltageOnOff(Card: integer; Channel: integer; OnOff: boolean): void;
```

## Call pattern

```ats
RemoteVoltageOnOff(Card, Channel, ON|OFF);
```

## Description

Activates or deactivates one analog channel of a remote card.
When it is deactivated, the current voltage value remains stored, and is turned on again, if the channel is reactivated.

## Metadata

- Category: Remote Interface Access
- Code: 268804
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Card`: `integer` — Number of the remote card.
- `Channel`: `integer` — Analog channel of the card.
; Allowed values: 1, 2
- `OnOff`: `boolean` — Allowed values: ON, OFF

## Example

```ats
RemoteSetVoltageRange(1, REMOTE_Voltage_Range_10V);
RemoteSetVoltage(1, 1, 3.5V);
RemoteVoltageOnOff(1, 1, ON);
```

## See also

`RemoteSetVoltage`, `RemoteSetVoltageRange`, `RemoteVoltageAllOff`
