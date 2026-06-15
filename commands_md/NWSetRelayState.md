# NWSetRelayState

## Declaration

```ats
function NWSetRelayState(PinPrefix: string; State: string): boolean;
```

## Call pattern

```ats
NWSetRelayState('Pin prefix', <State>);
```

## Description

Switches a relay/multi switch in CEETIS to the specified state.
This means that alle contacts of the relay/multi switch will be swichted accordingly in CEETIS.

## Metadata

- Category: Network Access
- Code: 265993
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string` — Pin prefix of the relay/multi switch.
- `State`: `string` — Number of the state to which the relay/multi switch shall be switched.; Allowed values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

## Return value

The funciton returns TRUE if the action could be executes, otherwise FALSE.

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

`RelayContactTest`
