# FailCounterCount

## Declaration

```ats
function FailCounterCount(Counter: integer): void;
```

## Call pattern

```ats
FailCounterCount(FAILCOUNTER_?);
```

## Description

Increments the failcounter "Counter" and the main-failcounter.

## Metadata

- Category: Failcounter
- Code: 267266
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Counter`: `integer` — Allowed values: FAILCOUNTER_Main, FAILCOUNTER_Continuity, FAILCOUNTER_IsolationLV, FAILCOUNTER_IsolationHV, FAILCOUNTER_DielectricBreakdown, FAILCOUNTER_ElectricalComponents, FAILCOUNTER_OpticalComponents, FAILCOUNTER_CANBus, FAILCOUNTER_VoltageAndCurrent, FAILCOUNTER_LV, FAILCOUNTER_TwistedPair, FAILCOUNTER_Others

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

`FailCounterGet`, `FailCounterRestore`, `FailCounterStore`
