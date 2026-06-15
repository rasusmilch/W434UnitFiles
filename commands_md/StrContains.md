# StrContains

## Declaration

```ats
function StrContains(SubData: string; Data: string; CaseSensitive: boolean = TRUE): boolean;
```

## Call pattern

```ats
StrContains('SubData', 'Data', TRUE|FALSE);
```

## Description

The function checks whether one string contains an other.
The asterisk * can be used as a wildcard.
Other characters can be (nor "must be") in places where the asterisk is used.
No other characters are allowed wher no asterisk is used.

CaseSensitive sepcifies whether the function distinguishes between small and capital letters or not.

## Metadata

- Category: String Processing
- Code: 262413
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Project selection program, Test initialization program, Test start program, Test, Report generation program, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `SubData`: `string`
- `Data`: `string`
- `CaseSensitive`: `boolean = TRUE` — Allowed values: TRUE, FALSE

## Return value

TRUE, if Data contains SudData, otherwise FALSE

## Example

```ats
UIWriteNormal(StrAdd('BCD        not in   ABCD (0): ', StrContains('BCD', 'ABCD')));
UIWriteNormal(StrAdd('ABC        not in   ABCD (0): ', StrContains('ABC', 'ABCD')));
UIWriteNormal(StrAdd('A*C        not in   ABCD (0): ', StrContains('A*C', 'ABCD')));
UIWriteNormal(StrAdd('B*D        not in   ABCD (0): ', StrContains('B*D', 'ABCD')));
UIWriteNormal(StrAdd('A*B*C      not in   ABCD (0): ', StrContains('A*B*C', 'ABCD')));
UIWriteNormal('');
UIWriteNormal(StrAdd('*CD*           in   ABCD (1): ', StrContains('*CD*', 'ABCD')));
UIWriteNormal(StrAdd('ABCD           in   ABCD (1): ', StrContains('ABCD', 'ABCD')));
UIWriteNormal(StrAdd('*B*C*          in   ABCD (1): ', StrContains('*B*C*', 'ABCD')));
UIWriteNormal(StrAdd('A*C*           in   ABCD (1): ', StrContains('A*C*', 'ABCD')));
UIWriteNormal(StrAdd('A*D            in   ABCD (1): ', StrContains('A*D', 'ABCD')));
UIWriteNormal(StrAdd('A*B*C*D        in   ABCD (1): ', StrContains('A*B*C*D', 'ABCD')));
UIWriteNormal('');
UIWriteNormal('Case sensitive');
UIWriteNormal(StrAdd('*BC*       not in   abcd (0): ', StrContains('*BC*', 'abcd')));
UIWriteNormal(StrAdd('A*C*       not in   abcd (0): ', StrContains('A*C*', 'abcd')));
UIWriteNormal(StrAdd('A*D        not in   abcd (0): ', StrContains('A*D', 'abcd')));
UIWriteNormal('');
UIWriteNormal('Not case sensitive');
UIWriteNormal(StrAdd('*BC*           in   abcd (1): ', StrContains('*BC*', 'abcd', FALSE)));
UIWriteNormal(StrAdd('A*C*           in   abcd (1): ', StrContains('A*C*', 'abcd', FALSE)));
UIWriteNormal(StrAdd('A*D            in   abcd (1): ', StrContains('A*D', 'abcd', FALSE)));
```

## See also

`StrPosition`, `StrAdd`, `StrCompare`, `StrCopy`, `StrDelete`, `StrInsert`, `StrLength`, `StrLowerCase`, `StrReplace`, `StrTrim`, `StrTrimLeft`, `StrTrimRight`, `StrUpperCase`
