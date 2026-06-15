# ArithTrunc

## Declaration

```ats
function ArithTrunc(Value: real): integer;
```

## Call pattern

```ats
ArithTrunc(Value);
```

## Description

Returns "Value" without decimal places.

## Metadata

- Category: Arithmetical Operations
- Code: 262656
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Value = 1.111;
Truncated = ArithTrunc(Value);
UIWriteNormal(Truncated);
```

## See also

`ArithRound`
