# GenCurrentOff

## Declaration

```ats
function GenCurrentOff(StimBus: integer): boolean;
```

## Call pattern

```ats
GenCurrentOff(STIMBUS_?);
```

## Description

Switch off current on stimbus

## Metadata

- Category: Generators
- Code: 270083
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
Iresult = GenCurrentOn(STIMBUS_U2, 100mA, 20V);

if (Iresult == TRUE)
begin
   UIInfoDialog('U2 on');
end;
if (Iresult == FALSE)
begin
   UIInfoDialog('U2 current < 100mA');
end;
if (Iresult == EXTVOLTAGE)
begin
   UIInfoDialog('U2 ExtVoltage');
end;

GenCurrentOff(STIMBUS_U2);
UIInfoDialog('U2 off');
```

## See also

`GenCurrentOn`, `GenVoltageOff`, `GenVoltageOn`
