# ArithOdd

## Declaration

```ats
function ArithOdd(Value: integer): boolean;
```

## Call pattern

```ats
ArithOdd(Value);
```

## Description

Checks whether the passed value is odd.

## Metadata

- Category: Arithmetical Operations
- Code: 262661
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `integer`

## Return value

Returns TRUE if "Value" is odd, otherwise FALSE.

## Example

```ats
if (ArithOdd(1))
begin
   UIWriteNormal('Odd');
end
else
begin
   UIWriteNormal('Even');
end;
```

## See also

`ArithEven`
