# FormatAlignLeft

## Declaration

```ats
function FormatAlignLeft(Data: string; Length: integer; Fill: string): string;
```

## Call pattern

```ats
FormatAlignLeft('Data', Length, 'Fill');
```

## Description

Returns the string "Data" left aligned with the minimum length "Length", filled with "Fill".

## Metadata

- Category: Formatting
- Code: 263430
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
Output = FormatAlignLeft('1', 3, '.');
UIWriteNormal(Output);
```

## See also

`FormatAlignCenter`, `FormatAlignRight`
