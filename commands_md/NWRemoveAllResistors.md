# NWRemoveAllResistors

## Declaration

```ats
function NWRemoveAllResistors(): void;
```

## Call pattern

```ats
NWRemoveAllResistors();
```

## Description

Removes all resistors from the network.

## Metadata

- Category: Network Access
- Code: 266002
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
NWAddResistor('Temporary resistor 1', "Pin1", "Pin2", 100Ohm, 10Ohm, 10Ohm);
NWAddResistor('Temporary resistor 2', "Pin3", "Pin4", 100Ohm, 10Ohm, 10Ohm);
ResistorTest('Temporary resistor 1', "Pin1", "Pin2");
ResistorTest('Temporary resistor 2', "Pin3", "Pin4");
NWRemoveAllResistors();
```

## See also

`NWAddResistor`, `NWRemoveAllCapacitors`, `NWRemoveAllDiodes`, `NWRemoveAllRLCCombinations`, `NWRemoveAllSwitches`, `NWRemoveAllWires`, `NWRemoveResistor`
