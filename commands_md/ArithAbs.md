# ArithAbs

## Declaration

```ats
function ArithAbs(Value: real): real;
```

## Call pattern

```ats
ArithAbs(Value);
```

## Description

Calculates the absolute value of the passed value.

## Metadata

- Category: Arithmetical Operations
- Code: 262670
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Value = -2;
AbsValue = ArithAbs(Value);
UIWriteNormal(AbsValue);
```
