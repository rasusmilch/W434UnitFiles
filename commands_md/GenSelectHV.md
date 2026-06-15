# GenSelectHV

## Declaration

```ats
function GenSelectHV(ExtInt: integer): boolean;
```

## Call pattern

```ats
GenSelectHV(INTERNAL|EXTERNAL);
```

## Description

Switch between HVG and external HV generator

## Metadata

- Category: Generators
- Code: 270084
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `ExtInt`: `integer` — Allowed values: INTERNAL, EXTERNAL

## Example

```ats
GenSelectHV(EXTERNAL);
```
