# ArithMod

## Declaration

```ats
function ArithMod(Value1: integer; Value2: integer): integer;
```

## Call pattern

```ats
ArithMod(Value1, Value2);
```

## Description

Returns the rest of the division of the numbers "Value1" and "Value2".

## Metadata

- Category: Arithmetical Operations
- Code: 262659
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
Value = ArithMod(10, 3);
UIWriteNormal(Value);
```

## See also

`ArithDiv`
