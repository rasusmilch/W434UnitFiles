# FormatIntToChar

## Declaration

```ats
function FormatIntToChar(Value: integer): string;
```

## Call pattern

```ats
FormatIntToChar(Value);
```

## Description

Returns the character of the ASCII code "Value".

## Metadata

- Category: Formatting
- Code: 263437
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `integer`

## Example

```ats
Char = FormatIntToChar(65);
UIWriteNormal(Char);
```

## See also

`FormatCharToInt`
