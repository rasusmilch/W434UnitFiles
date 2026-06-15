# FormatAlignRight

## Declaration

```ats
function FormatAlignRight(Data: string; Length: integer; Fill: string): string;
```

## Call pattern

```ats
FormatAlignRight('Data', Lenght, 'Fill');
```

## Description

Returns the string "Data" right aligned with the minimum length "Length", filled with "Fill".

## Metadata

- Category: Formatting
- Code: 263431
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data`: `string`
- `Length`: `integer`
- `Fill`: `string`

## Example

```ats
Output = FormatAlignRight('1', 3, '0');
UIWriteNormal(Output);
```

## See also

`FormatAlignCenter`, `FormatAlignLeft`
