# GenPowerSupplyExternal

## Declaration

```ats
function GenPowerSupplyExternal(StimBus: integer; On: boolean): boolean;
```

## Call pattern

```ats
GenPowerSupplyExternal(STIMBUS_?, ON|OFF);
```

## Description

Connect or disconnect U2 or U3 with external power supply

## Metadata

- Category: Generators
- Code: 270085
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `StimBus`: `integer` — Allowed values: STIMBUS_U2, STIMBUS_U3
- `On`: `boolean` — Allowed values: ON, OFF

## Example

```ats
GenPowerSupplyExternal(STIMBUS_U2, TRUE);
```
