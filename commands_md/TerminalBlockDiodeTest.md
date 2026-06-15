# TerminalBlockDiodeTest

## Declaration

```ats
function TerminalBlockDiodeTest(PinPrefix: string; DiodeIndex: integer = TERMINAL_BLOCK_AllDiodes): void; tests terminal_block_diodes;
```

## Call pattern

```ats
TerminalBlockDiodeTest('Pin prefix', DiodeIndex);
```

## Description

Tests the diodes of the specified terminal block.

The diodes will be tested with automatically created DiodeTest commands.

## Metadata

- Category: Meta components
- Code: 271624
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string`
- `DiodeIndex`: `integer = TERMINAL_BLOCK_AllDiodes`

## Example

```ats
TerminalBlockDiodeTest('XSQ73');
```

## See also

`DiodeTest`, `RelayDiodeTest`, `TerminalBlockConnectionTest`, `TerminalBlockResistorTest`
