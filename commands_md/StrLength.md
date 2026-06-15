# StrLength

## Declaration

```ats
function StrLength(Data: string): integer;
```

## Call pattern

```ats
StrLength('Data');
```

## Description

Returns the number of characters of the string "Data".

## Metadata

- Category: String Processing
- Code: 262409
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data`: `string`

## Example

```ats
Length = StrLength('Hello world');
UIWriteNormal(Length);
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
