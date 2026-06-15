# StrTrim

## Declaration

```ats
function StrTrim(Data: string): string;
```

## Call pattern

```ats
StrTrim('Data');
```

## Description

Removes all whitespaces and special characters from the beginning and the end of "Data" and returns the result.

## Metadata

- Category: String Processing
- Code: 262406
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data`: `string`

## Example

```ats
Trimmed = StrTrim('   Hello world   ');
UIWriteNormal(Trimmed);
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
