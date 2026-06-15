# TerminalBlockSwitchTest

## Declaration

```ats
function TerminalBlockSwitchTest(PinPrefix: string; SwitchIndex: integer = TERMINAL_BLOCK_AllSwitches): void; tests terminal_block_switches;
```

## Call pattern

```ats
TerminalBlockSwitchTest('Pin prefix', SwitchIndex);
```

## Metadata

- Category: Meta components
- Code: 271622
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string`
- `SwitchIndex`: `integer = TERMINAL_BLOCK_AllSwitches`

## Example

```ats
TerminalBlockSwitchTest('XSQ73');
```

## Example notes

Tests the contacts of the specified terminal block.

The switches will be tested with automatically created SwitchTest commands.

## See also

`RelayContactTest`, `SwitchTest`, `TerminalBlockConnectionTest`, `TerminalBlockDiodeTest`, `TerminalBlockResistorTest`
