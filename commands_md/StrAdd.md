# StrAdd

## Declaration

```ats
function StrAdd(Data1: string; Data2: string): string;
```

## Call pattern

```ats
StrAdd('Data1', 'Data2');
```

## Description

Adds two strings.

## Metadata

- Category: String Processing
- Code: 262400
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data1`: `string`
- `Data2`: `string`

## Example

```ats
Hello = StrAdd('Hello ', 'world');
UIWriteNormal(Hello);
```

## See also

`StrPosition`, `StrCompare`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
