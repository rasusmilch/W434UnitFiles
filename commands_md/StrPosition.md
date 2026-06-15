# StrPosition

## Declaration

```ats
function StrPosition(SubData: string; Data: string): integer;
```

## Call pattern

```ats
StrPosition('SubData', 'Data');
```

## Description

Returns the position of the first occurance of a string within an other string.

## Metadata

- Category: String Processing
- Code: 262401
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `SubData`: `string`
- `Data`: `string`

## Example

```ats
WorldPosition = StrPosition('world', 'Hello world');
UIWriteNormal(WorldPosition);
```

## See also

`StrAdd`, `StrCompare`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`, `StrReplace`
