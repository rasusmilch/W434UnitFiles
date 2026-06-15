# ArithCos

## Declaration

```ats
function ArithCos(Value: real): real;
```

## Call pattern

```ats
ArithCos(Value);
```

## Description

Returns the cosine of the angle in "Value". The angle must be passed as radian.

## Metadata

- Category: Arithmetical Operations
- Code: 262666
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `real`

## Example

```ats
Angle = 45;
Rad = (Angle * 3.1415) / 180;
Cos = ArithCos(Rad);
UIWriteNormal(Cos);
```

## See also

`ArithSin`, `ArithTan`
