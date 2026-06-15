# RelayCoilTest

## Declaration

```ats
function RelayCoilTest(PinPrefix: string): void; tests relay_coils;
```

## Call pattern

```ats
RelayCoilTest('Pin prefix');
```

## Description

Tests the coil of the specified relay.

The coil will either be tested with a ResistorTest command or a WireTest command.

## Metadata

- Category: Meta components
- Code: 271618
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string` — Pin prefix of the relay.

## Example

```ats
//Relay off
NWSetRelayState('RelayXP1174', '1');
//test the coil of the relay
RelayCoilTest('RelayXP1174');
//test the contacts of the relay in OFF state
RelayContactTest('RelayXP1174');
//energize the relay
CoilPin1 = 0;
CoilPin2 = 0;
Success = NWGetRelayCoilPins('RelayXP1174', CoilPin1, CoilPin2);
if (Success)
begin
   PowerUPinSetTPHigh(EXTIO_U2, CoilPin1);
   PowerUPinSetTPLow(EXTIO_U2, CoilPin2);
end;
//tell CEETIS the new relay state (Name of the state is X)
NWSetRelayState('RelayXP1174', 'X');
//test the contacts of the relay in ON state
RelayContactTest('RelayXP1174');
//de-energize the relay
PowerPinResetAll();
//tell CEETIS the new relay state
NWSetRelayState('RelayXP1174', '1');
```

## See also

`RelayContactTest`, `ResistorTest`, `WireTest`
