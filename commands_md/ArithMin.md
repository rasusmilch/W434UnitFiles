# ArithMin

## Declaration

```ats
function ArithMin(Value1: real; Value2: real): real;
```

## Call pattern

```ats
ArithMin(Value1, Value2);
```

## Description

Returns the minimum of "Value1" and "Value2".

## Metadata

- Category: Arithmetical Operations
- Code: 262662
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value1`: `real`
- `Value2`: `real`

## Return value

The return value is Value1 if Value1 < Value2, otherwise Value2.

## Example

```ats
Minimum = ArithMin(1, 3);
```

## See also

`ArithMax`
