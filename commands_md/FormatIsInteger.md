# FormatIsInteger

## Declaration

```ats
function FormatIsInteger(Value: string): boolean;
```

## Call pattern

```ats
FormatIsInteger('Value');
```

## Description

Returns TRUE if "Value" contains an integer value, otherwise FALSE.

## Metadata

- Category: Formatting
- Code: 263439
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `string`

## Example

```ats
if (FormatIsInteger('1'))
begin
   UIWriteNormal('Integer');
end
else
begin
   UIWriteNormal('No integer');
end;
```

## See also

`FormatIsReal`
