# ParamCheckForInterchangedWires

## Declaration

```ats
function ParamCheckForInterchangedWires(OnOff: boolean): void;
```

## Call pattern

```ats
ParamCheckForInterchangedWires(ON|OFF);
```

## Description

Activates or deactivates the check for interchanged wires for the commands WireTest and ConnectionTest.

## Metadata

- Category: Parameters
- Code: 266248
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `OnOff`: `boolean` — Allowed values: ON, OFF

## Example

```ats
ParamCheckForInterchangedWires(ON);
```

## See also

`ConnectionTest`, `WireTest`
