# ArithRound

## Declaration

```ats
function ArithRound(Value: real; DecimalPlaces: integer=0): integer;
```

## Call pattern

```ats
ArithRound(Value, DecimalPlaces);
```

## Description

Returns "Value" rounded.

## Metadata

- Category: Arithmetical Operations
- Code: 262657
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`
- `DecimalPlaces`: `integer=0`

## Example

```ats
Value = 1.116;
Rounded = ArithRound(Value, 2);
UIWriteNormal(Rounded);
```

## See also

`ArithTrunc`
