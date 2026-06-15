# NetworkTest

## Declaration

```ats
function NetworkTest(NetworkName: string; Topology: integer): void; tests wires;
```

## Call pattern

```ats
NetworkTest('NetworkName', TOPOLOGY_?);
```

## Description

Tests all connections of the network "NetworkName".

If TOPOLOGY_Star or TOPOLOGY_Chain is passed for "Topology" the wires of the network will be tested with the ConnectionTest command.

If TOPOLOGY_Netlist is passed for "Topology" the wires of the network will be tested with the WireTest command.

The results of the single steps will count to the result of the whole test.

## Metadata

- Category: Electrical testing
- Code: 515
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `NetworkName`: `string`
- `Topology`: `integer` — Allowed values: TOPOLOGY_Netlist, TOPOLOGY_Star, TOPOLOGY_Chain

## Example

```ats
NetworkTest('Network1', TOPOLOGY_Netlist);
```

## Example notes

Tests all wires with then name Network1 as defined in the netlist.

## See also

`ConnectionTest`, `IsConnected`, `ParamAutostart`, `ParamCheckForInterchangedWires`, `ParamContinuity`, `ParamStopOnFail`, `TestWires`, `WireTest`
