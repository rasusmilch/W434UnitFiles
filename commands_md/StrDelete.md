# StrDelete

## Declaration

```ats
function StrDelete(Data: string; Index: integer; Count: integer): string;
```

## Call pattern

```ats
StrDelete('Data', Index, Count);
```

## Description

Returns the string "Data" without "Count" characters from position "Index".

## Metadata

- Category: String Processing
- Code: 262403
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Data`: `string`
- `Index`: `integer`
- `Count`: `integer`

## Example

```ats
OnlyWorld = StrDelete('Hello world', 1, 6);
UIWriteNormal(OnlyWorld);
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrCopy`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
