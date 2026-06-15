# RelayContactTest

## Declaration

```ats
function RelayContactTest(PinPrefix: string; ContactIndex: integer = RELAY_AllContacts): void; tests relay_contacts;
```

## Call pattern

```ats
RelayContactTest('Pin prefix', ContactIndex);
```

## Description

Tests the contacts of the specified relay.

The contacts will be tested with automatically created SwitchTest commands.

## Metadata

- Category: Meta components
- Code: 271617
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string` — Pin prefix of the relay.
- `ContactIndex`: `integer = RELAY_AllContacts` — Index of the contact to be tested. Use RELAY_AllContacts to test all contacts of the relay.

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

`NWSetRelayState`, `RelayCoilTest`, `SwitchTest`
