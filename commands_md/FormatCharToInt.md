# FormatCharToInt

## Declaration

```ats
function FormatCharToInt(Char: string): integer;
```

## Call pattern

```ats
FormatCharToInt('Char');
```

## Description

Returns the ASCII code of the character "Char".

## Metadata

- Category: Formatting
- Code: 263436
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Char`: `string`

## Example

```ats
Code = FormatCharToInt('A');
UIWriteNormal(Code);
```

## See also

`FormatIntToChar`
