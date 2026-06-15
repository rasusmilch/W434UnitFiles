# BitAnd

## Declaration

```ats
function BitAnd(Value1: integer; Value2: integer): integer;
```

## Call pattern

```ats
BitAnd(Value1, Value2);
```

## Description

Returns the result of a bit wise AND operation of "Value1" and "Value2".

## Metadata

- Category: Bitwise Operations
- Code: 262912
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
Value = BitAnd(3, 1);
UIWriteNormal(Value);
```

## See also

`BitNot`, `BitOr`, `BitXOr`
