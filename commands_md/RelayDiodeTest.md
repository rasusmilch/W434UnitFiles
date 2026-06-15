# RelayDiodeTest

## Declaration

```ats
function RelayDiodeTest(PinPrefix: string; DiodeIndex: integer = RELAY_AllDiodes): void; tests relay_diodes;
```

## Call pattern

```ats
RelayDiodeTest('Pin prefix', DiodeIndex);
```

## Description

Tests the diodes of the specified relay.

The diodes will be tested with automatically created DiodeTest commands.

## Metadata

- Category: Meta components
- Code: 271621
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string`
- `DiodeIndex`: `integer = RELAY_AllDiodes`

## Example

```ats
RelayDiodeTest('REL QC248');
```

## See also

`DiodeTest`, `RelayCoilTest`, `RelayConnectionTest`, `RelayContactTest`, `RelayResistorTest`, `TerminalBlockDiodeTest`
