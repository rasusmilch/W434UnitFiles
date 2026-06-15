# BitXOr

## Declaration

```ats
function BitXOr(Value1: integer; Value2: integer): integer;
```

## Call pattern

```ats
BitXOr(Value, Value2);
```

## Description

Returns the result of a bit wise XOR operation of "Value1" and "Value2".

## Metadata

- Category: Bitwise Operations
- Code: 262915
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
Value = BitXOr(2, 3);
UIWriteNormal(Value);
```

## See also

`BitAnd`, `BitNot`, `BitOr`
