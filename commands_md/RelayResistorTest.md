# RelayResistorTest

## Declaration

```ats
function RelayResistorTest(PinPrefix: string; ResistorIndex: integer = RELAY_AllResistors): void; tests relay_resistors;
```

## Call pattern

```ats
RelayResistorTest('Pin prefix', ResistorIndex);
```

## Description

Tests the resistors (except the coil) of the specified relay.

The resistors will be tested with automatically created ResistorTest commands.

## Metadata

- Category: Meta components
- Code: 271620
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string`
- `ResistorIndex`: `integer = RELAY_AllResistors`

## Example

```ats
RelayResistorTest('REL QC248');
```

## See also

`RelayCoilTest`, `RelayConnectionTest`, `RelayContactTest`, `RelayDiodeTest`, `ResistorTest`, `TerminalBlockResistorTest`
