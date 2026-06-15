# TerminalBlockConnectionTest

## Declaration

```ats
function TerminalBlockConnectionTest(PinPrefix: string; ConnectionIndex: integer = TERMINAL_BLOCK_AllConnections): void; tests terminal_block_connections;
```

## Call pattern

```ats
TerminalBlockConnectionTest('Pin prefix', ConnectionIndex);
```

## Description

Tests the connections of the specified terminal block.

The connections will be tested with automatically created WireTest commands.

## Metadata

- Category: Meta components
- Code: 271616
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string` — Pin prefix of the terminal block
- `ConnectionIndex`: `integer = TERMINAL_BLOCK_AllConnections` — Index of the connection to be tested. Use TERMINAL_BLOCK_AllConnections to test all connections of the terminal block.; Allowed values: TERMINAL_BLOCK_AllConnections

## Example

```ats
TerminalBlockConnectionTest('XSQ73');
```

## See also

`WireTest`
