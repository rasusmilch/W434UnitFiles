# StrCompare

## Declaration

```ats
function StrCompare(Data1: string; Data2: string): integer;
```

## Call pattern

```ats
StrCompare('Data1', 'Data2');
```

## Description

Compares string "String1" with string "String2".

## Metadata

- Category: String Processing
- Code: 262405
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data1`: `string`
- `Data2`: `string`

## Return value

The return value is greater than 0 if "String1" is greater than "String2".

The return value is less than 0 if "String1" is less than "String2".

The return value is 0 if "String1" equals "String2".

## Example

```ats
Value = StrCompare('hello', 'hello');
UIWriteNormal(Value);
```

## See also

`StrPosition`, `StrAdd`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
