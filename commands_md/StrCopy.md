# StrCopy

## Declaration

```ats
function StrCopy(Source: string; Index: integer; Count: integer): string;
```

## Call pattern

```ats
StrCopy('Data', Index, Count);
```

## Description

Copies "Count" characters from position "Index" out of the string "Source" and returns this substring.

## Metadata

- Category: String Processing
- Code: 262402
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Source`: `string`
- `Index`: `integer`
- `Count`: `integer`

## Example

```ats
OnlyHello = StrCopy('Hello world', 1, 5);
UIWriteNormal(OnlyHello);
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrDelete`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
