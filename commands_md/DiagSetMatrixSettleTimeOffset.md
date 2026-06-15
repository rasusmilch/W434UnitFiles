# DiagSetMatrixSettleTimeOffset

## Declaration

```ats
function DiagSetMatrixSettleTimeOffset(Offset: ttime): void;
```

## Call pattern

```ats
DiagSetMatrixSettleTimeOffset(<Offset>ms);
```

## Description

Increases the relay settle time of the testpoint cards by the specified value.

The allowed maximum is 250 ms

## Metadata

- Category: Diagnostics
- Code: 269316
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Offset`: `ttime`

## Example

```ats
DiagSetMatrixSettleTimeOffset(10ms);
```

## See also

`DiagGetAdapterConnectorCode`
