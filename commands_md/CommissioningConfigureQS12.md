# CommissioningConfigureQS12

## Declaration

```ats
function CommissioningConfigureQS12(IP:string; CardAddress: integer; Configuration: integer): boolean;
```

## Call pattern

```ats
CommissioningConfigureQS12(<IP>, <CardAddress>,<Configuration>);
```

## Description

QS12 wird nicht in der Matrixkonfiguration angezeigt

Setzt die internen Pullup / Pulldown Widerst�nde

0 Ausgang hat 5V

1 Ausgang hat 0V

Es gibt 4 B�cke zu je 8 Ausg�nge

$1 Ausg�nge 1-8

$2 Ausg�nge 9-16

$4 Ausg�nge 17-24

$8 Ausg�nge 25-32



## Metadata

- Category: Commissioning
- Code: 272147
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `IP`: `string`
- `CardAddress`: `integer`
- `Configuration`: `integer`
