# BitNot

## Declaration

```ats
function BitNot(Value: integer): integer;
```

## Call pattern

```ats
BitNot(Value);
```

## Description

Returns the bit wise negated value of "Value1".

## Metadata

- Category: Bitwise Operations
- Code: 262914
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `integer`

## Example

```ats
Value = BitNot($FFFFFFFF);
UIWriteNormal(Value);
```

## See also

`BitAnd`, `BitOr`, `BitXOr`
