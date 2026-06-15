# RelayConnectionTest

## Declaration

```ats
function RelayConnectionTest(PinPrefix: string; ConnectionIndex: integer = RELAY_AllConnections): void;  tests relay_connections;
```

## Call pattern

```ats
RelayConnectionTest('Pin prefix', ConnectionIndex);
```

## Description

Tests the connections of the specified relay.

The connections will be tested with automatically created WireTest commands.

## Metadata

- Category: Meta components
- Code: 271619
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `PinPrefix`: `string`
- `ConnectionIndex`: `integer = RELAY_AllConnections`

## Example

```ats
RelayConnectionTest('REL QC248');
```
