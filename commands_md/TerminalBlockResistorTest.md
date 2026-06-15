# TerminalBlockResistorTest

## Declaration

```ats
function TerminalBlockResistorTest(PinPrefix: string; ResistorIndex: integer = TERMINAL_BLOCK_AllResistors): void; tests terminal_block_resistors;
```

## Call pattern

```ats
TerminalBlockResistorTest('Pin prefix', ResistorIndex);
```

## Description

Tests the resistors of the specified terminal block.

The resistors will be tested with automatically created ResistorTest commands.

## Metadata

- Category: Meta components
- Code: 271623
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string`
- `ResistorIndex`: `integer = TERMINAL_BLOCK_AllResistors`

## Example

```ats
TerminalBlockResistorTest('XSQ73');
```

## See also

`RelayResistorTest`, `ResistorTest`, `TerminalBlockConnectionTest`, `TerminalBlockDiodeTest`
