# NWRemoveAllDiodes

## Declaration

```ats
function NWRemoveAllDiodes(): void;
```

## Call pattern

```ats
NWRemoveAllDiodes();
```

## Description

Removes all diodes from the network.

## Metadata

- Category: Network Access
- Code: 266005
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
NWAddDiode('Temporary diode 1', "Pin1", "Pin2", 0.5V, 1.3V, 5V, 10mA);
NWAddDiode('Temporary diode 2', "Pin3", "Pin4", 0.5V, 1.3V, 5V, 10mA);
DiodeTest('Temporary diode 1', "Pin1", "Pin2");
DiodeTest('Temporary diode 2', "Pin3", "Pin4");
NWRemoveAllDiodes();
```

## See also

`NWAddDiode`, `NWRemoveAllCapacitors`, `NWRemoveAllResistors`, `NWRemoveAllRLCCombinations`, `NWRemoveAllWires`, `NWRemoveDiode`
