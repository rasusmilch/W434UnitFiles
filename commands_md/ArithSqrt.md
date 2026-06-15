# ArithSqrt

## Declaration

```ats
function ArithSqrt(Value: real): real;
```

## Call pattern

```ats
ArithSqrt(Value);
```

## Description

Returns the square root of "Value".

## Metadata

- Category: Arithmetical Operations
- Code: 262664
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
SquareRoot = ArithSqrt(4);
UIWriteNormal(SquareRoot);
```
