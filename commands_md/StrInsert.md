# StrInsert

## Declaration

```ats
function StrInsert(Source: string; Target: string; Index: integer): string;
```

## Call pattern

```ats
StrInsert('Source', 'Target', Index);
```

## Description

Inserts the string "Source" at position "Index" into the string "Target" and returns the complete string.

## Metadata

- Category: String Processing
- Code: 262404
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Source`: `string`
- `Target`: `string`
- `Index`: `integer`

## Example

```ats
WithSpace = StrInsert(' ', 'Helloworld', 6);
UIWriteNormal(WithSpace);
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrCopy`, `StrDelete`, `StrLength`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
