# NWGetRelayCoilPins

## Declaration

```ats
function NWGetRelayCoilPins(PinPrefix: string; var CoilPin1: integer; var CoilPin2: integer): boolean;
```

## Call pattern

```ats
NWGetRelayCoilPins('Pin prefix', CoilPin1, CoilPin2);
```

## Description

Returns the two pins of the coil of a relay.

## Metadata

- Category: Network Access
- Code: 265994
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string` — Pin prefix of the relay
- `var CoilPin1`: `integer`
- `var CoilPin2`: `integer`

## Return value

The funciton returns TRUE if the pins could be identified, otherwise FALSE.

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

`NWSetRelayState`, `RelayCoilTest`, `RelayContactTest`
