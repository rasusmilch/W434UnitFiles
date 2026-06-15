# StrReplace

## Declaration

```ats
function StrReplace(Original: string; OldPattern: string; NewPattern: string; ReplaceAll: boolean = TRUE; IgnoreCase: boolean = TRUE): string;
```

## Call pattern

```ats
StrReplace('<Original>', '<Old>', '<New>', TRUE|FALSE, TRUE|FALSE);
```

## Description

Replaces in "Original" the pattern in "OldPattern" by the pattern in "NewPattern".

## Metadata

- Category: String Processing
- Code: 262412
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `Original`: `string`
- `OldPattern`: `string`
- `NewPattern`: `string`
- `ReplaceAll`: `boolean = TRUE` — If TRUE all occurrences of "OldPattern" are replaced, otherwise only the first.; Allowed values: TRUE, FALSE
- `IgnoreCase`: `boolean = TRUE` — If TRUE the search is not case sensitive, otherwise it is.; Allowed values: TRUE, FALSE

## Example

```ats
Original = 'From two to two to two two';
Changed = StrReplace(Original, 'two', 'one', TRUE);
UIWriteNormal(Changed);
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`, `StrContains`
