# NWRemoveAllCapacitors

## Declaration

```ats
function NWRemoveAllCapacitors(): void;
```

## Call pattern

```ats
NWRemoveAllCapacitors();
```

## Description

Removes all capacitors from the network.

## Metadata

- Category: Network Access
- Code: 266004
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
NWAddCapacitor('Temporary capacitor 1', "1", "2", 100uF, 20uF, 30uF, 10V);
NWAddCapacitor('Temporary capacitor 2', "3", "4", 200uF, 10uF, 20uF, 30V);
CapacitorTest('Temporary capacitor 1', "1", "2");
CapacitorTest('Temporary capacitor 2', "3", "4");
NWRemoveAllCapacitors();
```

## See also

`NWAddCapacitor`, `NWRemoveAllDiodes`, `NWRemoveAllResistors`, `NWRemoveAllRLCCombinations`, `NWRemoveAllWires`, `NWRemoveCapacitor`
