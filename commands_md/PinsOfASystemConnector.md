# PinsOfASystemConnector

## Declaration

```ats
function PinsOfASystemConnector(Connector: integer; var StartAddress: integer): integer;
```

## Call pattern

```ats
PinsOfASystemConnector(Connector, StartAddress);
```

## Description

Returns the number of pins of a system connector.
The address of the first test pin of the connector is returned in StartAddress.

## Metadata

- Category: Pin Access
- Code: 268565
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Connector`: `integer`
- `var StartAddress`: `integer`

## Example

```ats
StartAddress = 0;
PinCount = PinsOfASystemConnector(1, StartAddress);
```
