# FormatIntToHex

## Declaration

```ats
function FormatIntToHex(Value: integer; MinLength: integer): string;
```

## Call pattern

```ats
FormatIntToHex(Value, MinLength);
```

## Description

Returns the number "Value" as a hexadecimal number with a minimum of "MinLength" digits.

## Metadata

- Category: Formatting
- Code: 263433
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `integer`
- `MinLength`: `integer`

## Example

```ats
Output = FormatIntToHex(31, 4);
UIWriteNormal(Output);
```

## See also

`FormatHexToInt`
