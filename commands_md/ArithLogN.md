# ArithLogN

## Declaration

```ats
function ArithLogN(Base: real; Value: real): real;
```

## Call pattern

```ats
ArithLogN(Base, Value);
```

## Description

Returns the logarithm to the base.

## Metadata

- Category: Arithmetical Operations
- Code: 262669
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Base`: `real`
- `Value`: `real`

## Example

```ats
Logarithm = ArithLogN(2, 64);
UIWriteNormal(Logarithm)
```
