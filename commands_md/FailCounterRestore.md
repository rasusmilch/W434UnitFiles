# FailCounterRestore

## Declaration

```ats
function FailCounterRestore(): void;
```

## Call pattern

```ats
FailCounterRestore();
```

## Description

Restores the values of all failcounters.

## Metadata

- Category: Failcounter
- Code: 267265
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Example

```ats
UIWriteNormal(StrAdd('Errors position 1: ', FailCounterGet(FAILCOUNTER_Main)));
FailCounterStore();
FailCounterCount(FAILCOUNTER_Main);
UIWriteNormal(StrAdd('Errors position 2: ', FailCounterGet(FAILCOUNTER_Main)));
FailCounterRestore();
UIWriteNormal(StrAdd('Errors position 3: ', FailCounterGet(FAILCOUNTER_Main)));

```

## See also

`FailCounterCount`, `FailCounterGet`, `FailCounterStore`
