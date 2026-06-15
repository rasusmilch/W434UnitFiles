# ArithDiv

## Declaration

```ats
function ArithDiv(Value1: integer; Value2: integer): integer;
```

## Call pattern

```ats
ArithDiv(Value1, Value2);
```

## Description

Executes an integer division. "Value1" is divided by "Value2" and returns the integer part of the result.

## Metadata

- Category: Arithmetical Operations
- Code: 262658
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value1`: `integer`
- `Value2`: `integer`

## Example

```ats
Value = ArithDiv(10, 3);
UIWriteNormal(Value);
```

## See also

`ArithMod`
