# FailCounterStore

## Declaration

```ats
function FailCounterStore(): void;
```

## Call pattern

```ats
FailCounterStore();
```

## Description

Stores the values of all failcounters.

## Metadata

- Category: Failcounter
- Code: 267264
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

`FailCounterCount`, `FailCounterGet`, `FailCounterRestore`
