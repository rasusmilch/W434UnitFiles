# GenVoltageOff

## Declaration

```ats
function GenVoltageOff(StimBus: integer): boolean;
```

## Call pattern

```ats
GenVoltageOff(STIMBUS_?);
```

## Description

Switch off voltage on stimbus

## Metadata

- Category: Generators
- Code: 270081
- Visible in alphabetical index: yes
- Deprecated: no
- Usable in: Test initialization program, Test start program, Test, Test end program
- Count result: no
- Archive allowed: no

## Parameters

- `StimBus`: `integer` — Allowed values: STIMBUS_Force, STIMBUS_U2, STIMBUS_U3

## Return value

Possible values:

TRUE, FALSE

## Example

```ats
Iresult = GenVoltageOn(STIMBUS_U2, 20V, 100mA);

if (Iresult == TRUE)
begin
   UIInfoDialog('U2 on');
end;
if (Iresult == FALSE)
begin
   UIInfoDialog('U2 Voltage < 20');
end;
if (Iresult == EXTVOLTAGE)
begin
   UIInfoDialog('U2 External voltage');
end;

GenVoltageOff(STIMBUS_U2);
UIInfoDialog('U2 off');
```

## See also

`GenCurrentOff`, `GenCurrentOn`, `GenVoltageOn`
