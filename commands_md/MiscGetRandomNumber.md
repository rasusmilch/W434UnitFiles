# MiscGetRandomNumber

## Declaration

```ats
function MiscGetRandomNumber(Range: integer): integer;
```

## Call pattern

```ats
MiscGetRandomNumber(<Range>);
```

## Description

Returns a random integer number Z in the range 0 <= Z < Range

## Metadata

- Category: Miscellaneous
- Code: 266521
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Range`: `integer`

## Example

```ats
Number = MiscGetRandomNumber(100);
```
