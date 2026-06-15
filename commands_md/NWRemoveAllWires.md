# NWRemoveAllWires

## Declaration

```ats
function NWRemoveAllWires(): void;
```

## Call pattern

```ats
NWRemoveAllWires();
```

## Description

Removes all wires from the network.

## Metadata

- Category: Network Access
- Code: 266003
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
NWAddWire('Wire1', "1", "2", [COLOR_Red]);
NWAddWire('Wire2', "3", "4", [COLOR_Blue]);
TestResult = WireTest('Wire1', "1", "2");
TestResult = WireTest('Wire2', "3", "4");
NWRemoveAllWires();
```

## See also

`NWAddWire`, `NWRemoveAllCapacitors`, `NWRemoveAllDiodes`, `NWRemoveAllResistors`, `NWRemoveAllRLCCombinations`, `NWRemoveWire`
