# FormatAlignCenter

## Declaration

```ats
function FormatAlignCenter(Data: string; Length: integer): string;
```

## Call pattern

```ats
FormatAlignCenter('Data', Length);
```

## Description

Returns the string "Data" centered with the minimum length "Length", filled with whitespaces.

## Metadata

- Category: Formatting
- Code: 263432
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data`: `string`
- `Length`: `integer`

## Example

```ats
Output = FormatAlignCenter('CAPTION', 20);
UIWriteNormal(Output);
```

## See also

`FormatAlignLeft`, `FormatAlignRight`
