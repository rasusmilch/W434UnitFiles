# NWRemoveAllSwitches

## Declaration

```ats
function NWRemoveAllSwitches(): void;
```

## Call pattern

```ats
NWRemoveAllSwitches();
```

## Description

Removes all switches from the network.

## Metadata

- Category: Network Access
- Code: 266008
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
NWAddSwitch('Temporary switch 1', "Pin1", "Pin2", OPEN);
NWAddSwitch('Temporary switch 2', "Pin3", "Pin4", CLOSED);
SwitchTest('Temporary switch 1', "Pin1", "Pin2");
SwitchTest('Temporary switch 2', "Pin3", "Pin4");
NWRemoveAllSwitches();
```

## See also

`NWAddSwitch`, `NWRemoveAllCapacitors`, `NWRemoveAllDiodes`, `NWRemoveAllResistors`, `NWRemoveAllRLCCombinations`, `NWRemoveAllWires`, `NWRemoveSwitch`
