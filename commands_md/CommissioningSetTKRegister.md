# CommissioningSetTKRegister

## Declaration

```ats
function CommissioningSetTKRegister(IP: string; Rack: integer; CardAddress: integer; Register:integer; Modus:integer; State: integer): boolean;
```

## Call pattern

```ats
CommissioningSetTKRegister(<IP>,<Rack>,<CardAddress>,<Register>,<Modus>,<State>);
```

## Description

Befehl zum setzen einzelner Register auf der Treiberkarte.

## Metadata

- Category: Commissioning
- Code: 272144
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `IP`: `string`
- `Rack`: `integer`
- `CardAddress`: `integer`
- `Register`: `integer`
- `Modus`: `integer`
- `State`: `integer`
