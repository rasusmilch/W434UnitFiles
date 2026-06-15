# ArithPower

## Declaration

```ats
function ArithPower(Base: real; Exponent: real): real;
```

## Call pattern

```ats
ArithPower(Base, Exponent);
```

## Description

Returns the base to the exponent.

## Metadata

- Category: Arithmetical Operations
- Code: 262668
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Base`: `real`
- `Exponent`: `real`

## Example

```ats
Power = ArithPower(10, 2);
UIWriteNormal(Power);
```
