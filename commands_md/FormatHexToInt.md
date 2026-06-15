# FormatHexToInt

## Declaration

```ats
function FormatHexToInt(Data: string): integer;
```

## Call pattern

```ats
FormatHexToInt('Data');
```

## Description

Returns the hexadecimal value "Value" as a number.

## Metadata

- Category: Formatting
- Code: 263434
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data`: `string`

## Example

```ats
Value = FormatHexToInt('$1F');
UIWriteNormal(Value);
```

## See also

`FormatIntToHex`
