# MiscGetTestSystemBoxNumbers

## Declaration

```ats
function MiscGetTestSystemBoxNumbers(Numbers: tcreatearray): integer;
```

## Call pattern

```ats
MiscGetTestSystemBoxNumbers(Numbers);
```

## Description

Returns the numbers of all boxes of the test system in a list.
The return value of the function is the box-number count.

## Metadata

- Category: Miscellaneous
- Code: 266520
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Numbers`: `tcreatearray`

## Example

```ats
Count = MiscGetTestSystemBoxNumbers(Numbers);
for Index = 1 to Count do
begin
   UIWriteNormal(Numbers[index]);
end;
```
