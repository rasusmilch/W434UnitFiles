# BitOr

## Declaration

```ats
function BitOr(Value1: integer; Value2: integer): integer;
```

## Call pattern

```ats
BitOr(Value1, Value2);
```

## Description

Returns the result of a bit wise OR operation of "Value1" and "Value2".

## Metadata

- Category: Bitwise Operations
- Code: 262913
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
Value = BitOr(1, 2);
UIWriteNormal(Value);
```

## See also

`BitAnd`, `BitNot`, `BitXOr`
