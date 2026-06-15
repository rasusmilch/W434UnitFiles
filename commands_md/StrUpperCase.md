# StrUpperCase

## Declaration

```ats
function StrUpperCase(Text: string): string;
```

## Call pattern

```ats
StrUpperCase('Text');
```

## Description

Returns the text "Text" in capitals.

## Metadata

- Category: String Processing
- Code: 262411
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
UpperCase = StrUpperCase('hello world');
UIWriteNormal(UpperCase);
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrContains`, `StrReplace`
