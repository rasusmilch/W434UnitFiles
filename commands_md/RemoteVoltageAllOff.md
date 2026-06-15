# RemoteVoltageAllOff

## Declaration

```ats
function RemoteVoltageAllOff(): void;
```

## Call pattern

```ats
RemoteVoltageAllOff();
```

## Description

Deactivates the analog channels of all remote cards.
The current voltage values remain stored, and are turned on again, if the channels are reactivated.

## Metadata

- Category: Remote Interface Access
- Code: 268805
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Example

```ats
RemoteSetVoltageRange(1, REMOTE_Voltage_Range_10V);
RemoteSetVoltageRange(2, REMOTE_Voltage_Range_10V);
RemoteSetVoltage(1, 1, 3.5V);
RemoteSetVoltage(2, 1, 7V);
RemoteVoltageOnOff(1, 1, ON);
RemoteVoltageOnOff(2, 1, ON);
RemoteVoltageAllOff();
```

## See also

`RemoteSetVoltage`, `RemoteSetVoltageRange`, `RemoteVoltageOnOff`
