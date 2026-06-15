# ArithSin

## Declaration

```ats
function ArithSin(Value: real): real;
```

## Call pattern

```ats
ArithSin(Value);
```

## Description

Returns the sine of the angle in "Value". The angle must be passed as radian.

## Metadata

- Category: Arithmetical Operations
- Code: 262665
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
Sin = ArithSin(Rad);
UIWriteNormal(Sin);
```

## See also

`ArithCos`, `ArithTan`
