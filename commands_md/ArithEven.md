# ArithEven

## Declaration

```ats
function ArithEven(Value: integer): boolean;
```

## Call pattern

```ats
ArithEven(Value);
```

## Description

Checks whether the passed value is even.

## Metadata

- Category: Arithmetical Operations
- Code: 262660
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Value`: `integer`

## Return value

Returns TRUE if "Value" is even, otherwise FALSE.

## Example

```ats
if (ArithEven(2))
begin
   UIWriteNormal('Even');
end
else
begin
   UIWriteNormal('Odd');
end;
```

## See also

`ArithOdd`
