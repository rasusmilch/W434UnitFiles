# GenSetJacksEnabled

## Declaration

```ats
function GenSetJacksEnabled(Enable: boolean): void;
```

## Call pattern

```ats
GenSetJacksEnabled(ON|OFF);
```

## Description

The function enables (and disables) the jacks which will then be in parallel to the generator.
This does not work for th HVG if your test syste, is equipped with a HV safety unit.

## Metadata

- Category: Generators
- Code: 270097
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test
- Count result: no
- Archive allowed: no

## Parameters

- `Enable`: `boolean` — Allowed values: ON, OFF

## Example

```ats
GenSetJacksEnabled(ON);
ConnectionTest('Connection', "Pin1", "Pin2");
GenSetJacksEnabled(OFF);
```
