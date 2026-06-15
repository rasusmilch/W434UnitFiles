# TwistedPairRunCompensation

## Declaration

```ats
function TwistedPairRunCompensation(AdapterName: string = 'Default'): boolean;
```

## Call pattern

```ats
TwistedPairRunCompensation();
```

## Description

Is used for compensation of adaption cables of twisted pair UUTs.

The adapter cables mus be connected to each other during this procedure.

## Metadata

- Category: Twisted Pair Test
- Code: 4354
- Visible in alphabetical index: no
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `AdapterName`: `string = 'Default'`

## Example

```ats
TwistedPairRunCompensation('Default');
```

## See also

`TwistedPairTest`, `TwistedPairTestFrequencies`
