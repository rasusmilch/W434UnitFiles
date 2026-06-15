# StrLowerCase

## Declaration

```ats
function StrLowerCase(Text: string): string;
```

## Call pattern

```ats
StrLowerCase('Text');
```

## Description

Returns the text "Text" in lower case letters.

## Metadata

- Category: String Processing
- Code: 262410
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Text`: `string`

## Example

```ats
LowerCase = StrLowerCase('HELLO WORLD');
UIWriteNormal(LowerCase);
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
