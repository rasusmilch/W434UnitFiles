# FormatIsReal

## Declaration

```ats
function FormatIsReal(Value: string): boolean;
```

## Call pattern

```ats
FormatIsReal('Value');
```

## Description

Returns TRUE if "Value" contains a floatingpoint value, otherwise FALSE.

## Metadata

- Category: Formatting
- Code: 263440
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `string`

## Example

```ats
if (FormatIsReal('1.3'))
begin
   UIWriteNormal('Real');
end
else
begin
   UIWriteNormal('No real');
end;
```

## See also

`FormatIsInteger`
